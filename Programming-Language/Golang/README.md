## Install

## Command

```bash
go --help
```

## Config

command
```bash
go help env
go env
```

建议使用放在rc文件的`export`命令设置go环境变量，而非使用`go env -w`的flag

重要的go环境变量
```
GO111MODULE  # 默认为on, 如果不是, 请设置
GOPROXY      # 代理, 国内官方为https://goproxy.io,direct, 如果在公司中, 使用公司内部的

GOROOT  # go的安装目录, 默认设置
GOPATH  # go1.11引入module, 不再需要; 
        # go1.16该环境变量被正式废弃;
        # 目前的意义是通过go install下载的二进制文件的保存位置
```

# Effective

在我个人的实践中，意识到go的语法有这样的特点

+ 语法会要求命名
    + 包名与目录名相关
    + 名称首字母大小写影响可见性

再结合go比较适合的业务场景——中间件和部分后端

所以go项目应该有比较严格的规范

+ 语法简单，抽象有限

这意味着某种需求只有有限的实现方式

所以适合针对可能的应用场景定义好相关的库，业务实现使用这些库即可

综上所属，通过最佳实践可以对一个没有接触过go的程序员迅速形成生产力

这里引入 [Go Style](https://google.github.io/styleguide/go/) 的三个分级，Guide，Decision，Best Practice，我最初以为他们的区别是影响的纬度从抽象到具体，但实际上是Entry的可变性，Guide是最不可能变化的，Best Practice是可能随着版本变化而变化的。在这种情况下，我觉得，应该将每个Entry都作为必须的。

这样才能规范项目质量，让未来者更快的接手项目。

所以这个章节就描述这样的主题，比如硬规范的东西，比如常见的问题与解决方案，比如最佳实践。在这里罗列。

+ https://go.dev/doc/effective_go
+ https://google.github.io/styleguide/go/
+ https://github.com/uber-go/guide

### 项目结构和名称命名

+ Go在语法层面通过名称首字母的大小写控制来控制是否**导出**

+ 项目名：小写，使用中划线划分单词
+ 文件名：小写，使用下划线划分单词
+ module名：使用反向域名，规范同项目名
+ package名/目录名：小写不使用下划线，package名和目录相同
+ 其他（接口名/结构体名/函数名/变量名）：使用驼峰命名法作为基本规范
    + 常量：全大写使用下划线

+ 项目结构：[Standard Go Project Layout](https://github.com/golang-standards/project-layout/blob/master/README_zh.md)

### CLI
https://github.com/spf13/cobra

### Config
https://github.com/spf13/viper

### 限流

#### 漏桶

+ 定义：https://en.wikipedia.org/wiki/Leaky_bucket

形象的，有两个参数，水桶的大小和水桶的漏水速度。可以想象，如果访问的请求量很低，比水桶漏水的速度都低，此时请求（相当于）可以（不被限制地）访问；当访问量逐渐增大，让桶中积累水的时候，则只能按照水桶的流水速度恒定的被处理；让访问量继续增大，在水桶中的水已经充满开始外溢了，则请求直接被拒绝。

特点，服务处理请求的速度是存在一个被划定的上限的。超过上限的请求都必须等待甚至被拒绝。

+ 实现：https://github.com/uber-go/ratelimit

#### 令牌桶

+ 定义：https://en.wikipedia.org/wiki/Token_bucket

形象的，有两个参数，令牌桶的大小和令牌桶新增令牌的速度。每个请求只有令牌桶中存在令牌才能访问。可以想象，当访问速度大于令牌新增速度时，令牌桶内的令牌会逐渐减少，直到令牌桶中的令牌为空，此时请求可以访问的速度和令牌生成速度相同。同样的，如果请求速度比较小，令牌桶中的令牌也不会无限积累，有一个上线。

特点，令牌桶算法能限制的最大流量并不是令牌生成的速度，如果令牌桶中积累了足够的令牌，此时大流量过来时，在一定量的范围内，速度依然可以很高。

与漏桶算法的比较：加入这里的令牌桶是不存在的，只有令牌生成速度，两个算法是一样的（如果不考虑多余流量的处理）。但是令牌桶的出现，让其在大流量来时，可以在一定范围内依然很大流量的处理，知道流量耗尽回归到漏桶的状态。而漏桶是有一个锁死的上限的。

+ 实现：https://github.com/juju/ratelimit

#### 其他TODO

+ https://github.com/ulule/limiter

### 其他TODO

TODO：
+ https://marksuper.xyz/2022/08/26/groupcache/
+ https://marksuper.xyz/2022/10/13/xxl-job/
+ https://marksuper.xyz/2021/10/15/error_group/
+ https://marksuper.xyz/2023/01/23/tunny/
+ https://marksuper.xyz/2023/12/23/ant/
+ local cache

### 性能调优与注意事项

+ GOMAXPROCS（go max procs）：go中goroutine的队列数量，最好和CPU核数一致。
    + 目前这个版本通常不需要求，可以由服务器通过环境变量设制

+ Ballast（压舱石）：建议设置为最大内存资源的一半。和GC相关，避免频繁GC。
    + 在go1.19之前：申请一块大内存，因为GC是会有一个目标GC的内存，此时活跃内存就更多了。而且这块内存不会真是分配内存。
    + 在go1。19之后：则添加了GOMEMLIMIT（go mem limit），即可以设置触发的阈值
+ 性能分析：Go-Monitor

TODO: GC和内存碎片

## tools

### Json-to-Go-struct
https://mholt.github.io/json-to-go/

# Roast

1. 面向接口编程+包内名称共享+名称在包内不分先后——影响代码可读性：当我看到一个接口时，我不知道哪些结构体实现了它；当我看到一个结构体实现了很多方法时，我不知道它是为了实现哪些接口。
    >现代编辑环境可以一定程度解决这个问题。
2. `interface{}`，一个`map[string]interface{}`或者函数返回`interface{}`就直接相当于动态类型了，我怎么知道这里的值是什么东西？
    >这个也能一定程度接受，因为其他的代码想要使用这个值必须知道其类型，这里只是对读代码有阻碍，不过出现错误只能在运行时感知呀。
3. 相似名称过多。比如`net/http`中，包对外方法、结构体`ServeMux`都有方法`HandleFunc`，还有一个类型也是`HandleFunc`。
    >不知道能不能通过最佳实践解决
4. 构造结构体时类似C而非使用类似C++的构造函数，会出现若干参数我没有设置也不会报错，这在多人合作时，假如结构体的定义者增加了字段，但是结构体的使用者不修改也能编译，则容易出现bug。
    >golang相关的lint应该可以解决这个问题，即假如某些字段没有使用则会提示/报错。但是目前感觉不好用，不能保证流程的完全，个人认为这种情况还是容易出现的。
