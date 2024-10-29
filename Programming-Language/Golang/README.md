Go不需要框架，它本身就是框架

## Install

STFM

## Command

### go test

+ flag `-v`：即 verbose
+ args `-run=XXX`：通过正则执行特定case
+ flag `-race`：竟态竞争检测，最佳实践必加
+ args `-parallel`：Go在test时会尝试并行执行测试，该参数用于限制最多并行多少个
+ args `-shuffle`：随机化测试，参数作为随机化种子（按理说测试case之间不应该有依赖呀）
+ flag `-cover`：启动覆盖率

## Config

建议使用放在rc文件的`export`命令设置go环境变量，而非使用`go env -w`的flag

一些重要的go环境变量如下
```
GO111MODULE  # 默认为on, 如果不是, 请设置
GOPROXY      # 代理, 国内官方为https://goproxy.io,direct, 如果在公司中, 使用公司内部的

GOROOT  # go的安装目录, 默认设置
GOPATH  # go1.11引入module, 不再需要; 
        # go1.16该环境变量被正式废弃;
        # 目前的意义是通过go install下载的二进制文件的保存位置
```

# Effective

+ Go的特点：
    + Go在语法中限制代码实现，比如包名要求和目录名相关，名称首字母大小写影响可见性，保存时格式化。
    + Go的语法非常简单，程序员能做的抽象有限。意味着某种需求只有有限的实现方式。
    + Go适合的业务场景有中间件和部分后端。

对于Go的这些特点，通过“最佳实践”可以让一个没有接触过Go的程序员循序形成生产力。

+ Ref：
    1. [谷歌推荐的Effective Go](https://go.dev/doc/effective_go)
    2. [谷歌官方的规范](https://google.github.io/styleguide/go/)
    3. [uber的最佳实践](https://github.com/uber-go/guide)
    4. ["最差实践"](https://100go.co/)
    5. [beihai · 构建可持续迭代的 Golang 应用](https://wingsxdu.com/posts/golang/clean-go/)

### 项目结构

+ Ref：
    + [官方](https://go.dev/doc/modules/layout)
    + [社区](https://github.com/golang-standards/project-layout/)

### 名称命名

+ 项目名：小写，使用中划线划分单词
+ mod名：使用反向域名，其他规范同项目名
+ package名：小写，单个单词，不使用下划线或者驼峰
    + 包名和其所在的目录名相同
+ 其他使用驼峰命名法作为基本规范（包括常量）
+ 其他：
    + [名称自解释/递归解释](https://google.github.io/styleguide/go/best-practices#function-and-method-names)

## 语法细节

+ 数组是值，切片是指针
+ 类型转换可以是复合类型
+ [nil调用函数](https://golang3.eddycjy.com/posts/nil-func/)
    + 对于为`nil`的Slice和Map（不是Slice指针和Map指针），可读不可写
    + 对于map中没有的键，获取并不会panic，会是被负值成值的零值，所以`map[key]bool`天然就是一个set
        + 同样的，对于`delete(map..., key)`，中key不在map也是安全的
+ `new(T)`与`&T{}`等价，而不是与`T{}`，使用`T{}`的优先级大于`make(...)`再大于`new()`
    + 所以最佳实践上
        + 无论是内置类型还是自定义类型，创建指针都是使用`&T{}`而非`new`
        + 对于内置类型，实例使用`make`
        + 对于自定义类型，实例使用`T{}`

## 其他准则

+ 假如不知道一个名称是否导出，则不导出

## 业务场景

+ 命令行：[cobra](https://github.com/spf13/cobra)
+ 配置：[viper](https://github.com/spf13/viper)
+ 限流：
    + 漏桶：[uber-go/ratelimit](https://github.com/uber-go/ratelimit)
    + 令牌桶：[juju/ratelimit](https://github.com/juju/ratelimit)
    + 其他：[ulule/limiter](https://github.com/ulule/limiter)

+ Local Cache：
    + pre：
        + built-in：map、sync.Map
        + go1.5以后，当map里的key和value都不包含指针时则GC扫描忽略
    + 需求：
        + 低时延
        + 高并发
        + 容量大
        + 不持久化
        + 接口简单

| 链接                                                      | 有无GC | 是否支持过期时间         | 接口         | 其他                                               |
| --------------------------------------------------------- | ------ | ------------------------ | ------------ | -------------------------------------------------- |
| [bigcache](https://github.com/allegro/bigcache)           | 无GC   | 是，但一个实例只能有一个 | 复杂，见其他 | 接口复杂（hash冲突不兼容+没有更新接口+手动序列化） |
| [fastcache](https://github.com/VictoriaMetrics/fastcache) | 无GC   | 否                       | 简单         | 比bigcache快                                       |
| [freecache](https://github.com/coocood/freecache)         |        | 是                       | 简单         | 存储空间预先分配（开始多+后面不增）                |
| [go-cache](https://github.com/patrickmn/go-cache)         |        | 是                       | 简单         | 结构简单，推荐万级小key                            |
| [groupcache](https://github.com/golang/groupcache)        |        |                          |              | 轻量memcached，不在当前选型范围中                  |

+ 并发：
    + 无依赖：协程池：

        + 需求：
            + 限制并发量
            + 控制生命周期

        1. [sync.errgroup](https://github.com/golang/sync/tree/master/errgroup)（官方）
            1. https://marksuper.xyz/2021/10/15/error_group/
        2. [tunny](https://github.com/Jeffail/tunny)
            1. https://darjun.github.io/2021/06/10/godailylib/tunny/
        3. [ants](https://github.com/panjf2000/ants)
            1. https://marksuper.xyz/2023/12/23/ant/

    + 有依赖：任务处理器/任务编排

        1. [machinery](https://github.com/RichardKnop/machinery)

    + 重试

## 性能

也算是常见八股吧，不仅八股中重要，在实际工作中也重要

+ 性能分析：Go-Monitor

### 调度

+ GOMAXPROCS（go max procs）：go中goroutine的队列数量，最好和CPU核数一致。
    + 目前这个版本通常不需要求，可以由服务器通过环境变量设制

https://povilasv.me/go-scheduler/

### 内存分配

https://medium.com/eureka-engineering/understanding-allocations-in-go-stack-heap-memory-9a2631b5035d
https://medium.com/@ankur_anand/a-visual-guide-to-golang-memory-allocator-from-ground-up-e132258453ed
### 堆栈

https://medium.com/eureka-engineering/understanding-allocations-in-go-stack-heap-memory-9a2631b5035d

### GC

+ Ballast（压舱石）：建议设置为最大内存资源的一半。和GC相关，避免频繁GC。
    + 在go1.19之前：申请一块大内存，因为GC是会有一个目标GC的内存，此时活跃内存就更多了。而且这块内存不会真是分配内存。
    + 在go1。19之后：则添加了GOMEMLIMIT（go mem limit），即可以设置触发的阈值

## Tool

+ Json生成可序列化的Go结构体：[Json-to-Go-struct](https://mholt.github.io/json-to-go/)
+ go visualize call graph: ondrajz/go-callvis -- 当前版本在1.22之后会出问题, 而维护者不太活跃 --> Egor3f/go-callvis(解决: [pr](https://github.com/ondrajz/go-callvis/pull/177/files), 只删除了代码) -- 原项目有一些不太好的实现 --> zweix123/go-callvis(从ondrajz的fork)

# Roast

1. 面向接口编程+包内名称共享+名称在包内不分先后——影响代码可读性：当我看到一个接口时，我不知道哪些结构体实现了它；当我看到一个结构体实现了很多方法时，我不知道它是为了实现哪些接口。
    >现代编辑环境可以一定程度解决这个问题。
2. `interface{}`，一个`map[string]interface{}`或者函数返回`interface{}`就直接相当于动态类型了，我怎么知道这里的值是什么东西？
    >这个也能一定程度接受，因为其他的代码想要使用这个值必须知道其类型，这里只是对读代码有阻碍，不过出现错误只能在运行时感知呀。
3. 相似名称过多。比如`net/http`中，包对外方法、结构体`ServeMux`都有方法`HandleFunc`，还有一个类型也是`HandleFunc`。
    >不知道能不能通过最佳实践解决
4. 构造结构体时类似C而非使用类似C++的构造函数，会出现若干参数我没有设置也不会报错，这在多人合作时，假如结构体的定义者增加了字段，但是结构体的使用者不修改也能编译，则容易出现bug。
    >golang相关的lint应该可以解决这个问题，即假如某些字段没有使用则会提示/报错。但是目前感觉不好用，不能保证流程的完全，个人认为这种情况还是容易出现的。

## 其他

### go shebang trick
```go
//usr/bin/env go run $0 $@; exit
```
