


~~Go不需要框架，它本身就是框架~~

## 吐糟

1. 面向接口编程+包内名称共享+名称在包内不分先后——影响代码可读性：当我看到一个接口时，我不知道哪些结构体实现了它；当我看到一个结构体实现了很多方法时，我不知道它是为了实现哪些接口。
    >现代编辑环境可以一定程度解决这个问题。
2. `interface{}`，一个`map[string]interface{}`或者函数返回`interface{}`就直接相当于动态类型了，我怎么知道这里的值是什么东西？
    >这个也能一定程度接受，因为其他的代码想要使用这个值必须知道其类型，这里只是对读代码有阻碍，不过出现错误只能在运行时感知呀。
3. 相似名称过多。比如`net/http`中，包对外方法、结构体`ServeMux`都有方法`HandleFunc`，还有一个类型也是`HandleFunc`。
    >不知道能不能通过最佳实践解决
4. 构造结构体时类似C而非使用类似C++的构造函数，会出现若干参数我没有设置也不会报错，这在多人合作时，假如结构体的定义者增加了字段，但是结构体的使用者不修改也能编译，则容易出现bug。
    >golang相关的lint应该可以解决这个问题，即假如某些字段没有使用则会提示/报错。但是目前感觉不好用，不能保证流程的完全，个人认为这种情况还是容易出现的。

5. 擦，这么东西怎么能过编译啊！
```go
package main

import (
	"encoding/json"
	"fmt"
)

const s = `{
    "a": 1,
    "b": 2
}`

func main() {
	// 主要区别在m1使用指针, m2没有使用指针
	var m1 map[string]int
	json.Unmarshal([]byte(s), &m1)
	fmt.Println(m1) // map[a:1 b:2]

	var m2 map[string]int
	json.Unmarshal([]byte(s), m2)
	fmt.Println(m2) // map[]
}
```

6. 真神奇啊
```go
package main

import (
	"fmt"
	"reflect"
)

func main() {
	var (
		s1, s2, s3 []string
	)
	s1 = nil
	s2 = []string{}
	s3 = []string(nil)
	fmt.Println(reflect.DeepEqual(s1, s2)) // false
	fmt.Println(reflect.DeepEqual(s1, s3)) // true
	fmt.Println(reflect.DeepEqual(s2, s3)) // false
}
```

7. 逆天，没有默认初始化？还是内置类型默认是“某种指针”？
```go
package main

import "fmt"

func main() {
	var m map[string]int
	m["a"] = 1
	fmt.Println(m)
}
/*
> go run main.go
panic: assignment to entry in nil map

goroutine 1 [running]:
main.main()
        /Users/.../main.go:7 +0x34
exit status 2
*/
```


### 编程最佳实践并非业务最佳实践

1. 枚举


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

```bash
go test -v -cover -race ./...
```

### go build

```bash
go build -gcflags="-m" .
```
内存逃逸分析

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

对于Go的这些特点，通过“最佳实践”可以让一个没有接触过Go的程序员迅速形成生产力。

+ Ref：
    1. [A Tour of Go](https://go.dev/tour/)
    2. [谷歌推荐的Effective Go](https://go.dev/doc/effective_go)
    3. [谷歌官方的规范](https://google.github.io/styleguide/go/)
    4. [uber的最佳实践](https://github.com/uber-go/guide)
    5. ["最差实践"](https://100go.co/)
    6. [beihai · 构建可持续迭代的 Golang 应用](https://wingsxdu.com/posts/golang/clean-go/)
    7. [CoolShell · Go编程模式](https://coolshell.cn/articles/series/go%e7%bc%96%e7%a8%8b%e6%a8%a1%e5%bc%8f)
        + 但是我感觉里面关于范型的讨论已经过时了。
    8. [高性能golang](https://goperf.dev/)：真挺不错的（我看的时候有一个错误，不知道后面修复了没有）
    9. [Go项目设计的“七宗罪”？警惕那些流行的“反模式”](https://tonybai.com/2025/04/21/go-project-design-antipatterns/)

## 项目结构

+ Ref：
    + [官方](https://go.dev/doc/modules/layout)
    + [社区](https://github.com/golang-standards/project-layout/)

## 名称命名

+ 项目名：小写，使用中划线划分单词
+ mod名：使用反向域名，其他规范同项目名
+ package名：小写，单个单词，不使用下划线或者驼峰
    + 包名和其所在的目录名相同
+ 其他使用驼峰命名法作为基本规范（包括常量）
+ 其他：
    + [名称自解释/递归解释](https://google.github.io/styleguide/go/best-practices#function-and-method-names)

## 语法细节

+ 数组是值，切片是指针
    + Full Slice Expression：`s := arr[start:end:cap]`，此时s指向的底层数组与arr的没有关系（不然指向的是同一个区域，appand且没有触发resize可能会相互影响！）
+ 类型转换可以是复合类型
+ [nil调用函数](https://golang3.eddycjy.com/posts/nil-func/)
    + 对于为`nil`的Slice和Map（不是Slice指针和Map指针），可读不可写
    + 对于map中没有的键，获取并不会panic，会是被赋值成值的零值，所以`map[key]bool`天然就是一个set
        + 同样的，对于`delete(map..., key)`，中key不在map也是安全的
+ `new(T)`与`&T{}`等价，而不是与`T{}`；有的构造方式有：`T{}`、`make(...)`和`new()`
    + 无论是内置类型还是自定义类型，创建指针都是使用`&T{}`而非`new`
    + 对于内置类型，实例使用`make`
        + 这里隐含的最佳实践是创建时指定cap，假如实在不能或者就是期望为空，则可以以声明变量而不赋值的形式“初始化”
    + 对于自定义类型，实例使用`T{}`

+ `defer`
    + defer是针对函数的，而不是针对代码块的，常见错误：循环中的defer
    + 多个defer：可以把defer理解为将一个函数放入栈中，对应的，执行也是从栈顶开始的，相当于在函数中越早defer的函数越晚执行。
    + 对协程一定要`defer recover()`，当写成发生panic时，仍然一定会执行所有的defer，假如defer发生panic时，其他defer仍然也依然执行。假如没有recover，则这些panic会影响整个进程，有了recover，就能只影响该协程。同时，recover比如通过defer使用，且必须是第一个defer（按照上面的，保证该defer最后一个执行，handle其他defer的panic）

## 其他准则

+ 假如不知道一个名称是否导出，则不导出

## 业务场景

### 命令行
[cobra](https://github.com/spf13/cobra)

### 配置
[viper](https://github.com/spf13/viper)

### 限流

+ 漏桶：[uber-go/ratelimit](https://github.com/uber-go/ratelimit)
+ 令牌桶：[juju/ratelimit](https://github.com/juju/ratelimit)
+ 其他：[ulule/limiter](https://github.com/ulule/limiter)
+ 标准库：golang.org/x/time/rate

### 本地缓存

+ pre：
    + built-in：map、sync.Map
    + go1.5以后，当map里的key和value都不包含指针时则GC扫描忽略
+ 需求：
    + 低时延
    + 高并发
    + 容量大
    + 不持久化
    + 接口简单

| 链接                                                        | 有无GC | 是否支持过期时间     | 接口     | 其他                           |
| --------------------------------------------------------- | ---- | ------------ | ------ | ---------------------------- |
| [bigcache](https://github.com/allegro/bigcache)           | 无GC  | 是，但一个实例只能有一个 | 复杂，见其他 | 接口复杂（hash冲突不兼容+没有更新接口+手动序列化） |
| [fastcache](https://github.com/VictoriaMetrics/fastcache) | 无GC  | 否            | 简单     | 比bigcache快                   |
| [freecache](https://github.com/coocood/freecache)         |      | 是            | 简单     | 存储空间预先分配（开始多+后面不增）           |
| [go-cache](https://github.com/patrickmn/go-cache)         |      | 是            | 简单     | 结构简单，推荐万级小key                |
| [groupcache](https://github.com/golang/groupcache)        |      |              |        | 轻量memcached，不在当前选型范围中        |

ristretto

### 并发

#### 无依赖：协程池

<a id="batch"></a>

需求引入：

考虑这样的场景，我们有一批参数需要去下游请求，
假如是简单的串行执行，肯定是划不来的，这种IO密集型的场景中我们肯定有大量的时间在等待。
所以需要异步，但是一口气将请求全部都发出去也有新的问题；主要发生在参数的数量过多时，
2. 我们在短时间内创造了大量的协程
3. 对下游的访问量是突增的，可能造成被限流，导致很多可以正常请求得到结果的请求失败。

然后我们再扩展这个场景，假如下游的接口支持批量请求呢？（比如参数从参数变成参数列表）
这种可以将我们的所有参数一口气在一次请求中发送出去么？当参数比较多时大概率不行，因为对每个参数进行处理的时间是客观存在的，当多个参数一起请求时，可能出现长尾效应，即若干个参数的计算时间远远大于本次请求其他参数的平均处理时间，从而导致整个请求超时失败。
仍然要想一些办法。

所以我们的需求可以如下总结：
4. 尽量高的并发
5. 最高并发数有限（即自身服务的协程数，既防止协程的徒增，又防止被下游限流）

我首先的设计是这样的，
将这一批参数首先划分成多个“大批”，然后对每个大批再划分成多个小批（假如下游支持批量查询则小批的大小就是下游建议的每次请求参数个数（因为长尾效应是随着参数的数量越多而越显著的），假如下游每次请求只支持单个参数，则小批的大小是1），每个小批则对应一次请求。
然后对于每个大批，小批之间的请求是并行的，而大批与大批之间的处理，则是串行的。
此时请求的并发量最多就是一个大批的小批个数，同时也在尽量的并发，满足我们的需求。

这里是一种函数式表述
```go
Flatten(
    MapSeries(
        Chunk(input, big_chunk_size) -> []big_chunk,
        Flatten(
            MapParallel(
                Chunk(big_chunk, small_chunk_size) -> []small_chunk,
                F(small_chunk) -> []result,
            ),
        ),
    ),
)
// Flatten是Chunk的逆操作, 相当于
/*
Reduce(
    collection,
    func(agg []T, item Slice, index int) []T {
        return append(agg, item...)
    },
    []T{},
)
*/
```

但是正解不是这样的，我们再来看我们的需求，发现这个不正是一个协程池会做的事情么？我们只需要资源限制好，任务尽量的往里塞，至于任务的调度就交给协程池就可以了。由协程池维护协程数和并发量，对下游的压力自然也就可控了。

+ 业界协程池的实现：
    + [sync.errgroup](https://github.com/golang/sync/tree/master/errgroup)（官方）
        + Ref：
            + https://marksuper.xyz/2021/10/15/error_group/
    + [tunny](https://github.com/Jeffail/tunny)
        + Ref：
            + https://darjun.github.io/2021/06/10/godailylib/tunny/
    + [ants](https://github.com/panjf2000/ants)
        + Ref：
            + https://marksuper.xyz/2023/12/23/ant/

#### 有依赖: 任务编排
[machinery](https://github.com/RichardKnop/machinery)

#### 重试

### 序列化

方法
json
gob
pb
msgp
性能(ns/op)
458.8
113.8(-75%)
52.30(-88%)
35.94(-92%)
内存(B/op)
291
304(+4%)
24(-91%)
32(-89%)
大数据量
方法
json
gob
pb
msgp
性能(ns/op)
26378
111.8(-99.5%)
16610(-37%)
34.44(-99.8%)
内存(B/op)
293602
304(-99.8%)
245776(-16%)
32(-99.9%)

## 开发工具

### json to go

+ Json生成可序列化的Go结构体：[Json-to-Go-struct](https://mholt.github.io/json-to-go/)

### go visualize call graph

+ go visualize call graph: ondrajz/go-callvis -- 当前版本在1.22之后会出问题, 而维护者不太活跃 --> Egor3f/go-callvis(解决: [pr](https://github.com/ondrajz/go-callvis/pull/177/files), 只删除了代码) -- 原项目有一些不太好的实现 --> zweix123/go-callvis(从ondrajz的fork)

## 其他技巧

### go shebang trick
```go
//usr/bin/env go run $0 $@; exit
```



# Source Code

## 并发模型

+ Ref：
    + [知乎 · 小徐先生 · 温故知新——Golang GMP 万字洗髓经](https://zhuanlan.zhihu.com/p/869632834)
    + [Russ Cox · Coroutines for Go](https://research.swtch.com/coro)
+ 

Golang的并发模型——GMP（goroutine-machine-processor）
+ G即goroutine，是Golang对协程的抽象
+ M即machine，是Golang对线程的抽象
+ P即Processor，是Golang中的调度器
    + lrq（local run queue）：通过数组实现循环队列

## 内存管理

Golang的内存管理模块主要继承自TCMalloc（Thread-Caching-Malloc）的设计思路。

+ Ref：
    + [Russ Cox · Memory Models](https://research.swtch.com/mm)
    + [Medium · James Kirk · Understanding Allocations in Go](https://medium.com/eureka-engineering/understanding-allocations-in-go-stack-heap-memory-9a2631b5035d)
    + [Medium · Ankur Anand · A visual guide to Go Memory Allocator from scratch (Golang)](https://medium.com/@ankur_anand/a-visual-guide-to-golang-memory-allocator-from-ground-up-e132258453ed)

## 并发工具

锁和管道

## IO模型

因为Linux的epollo多路复用技术是线程纬度的，所以Golang设计了一套netpoll机制。

## 数据结构

https://research.swtch.com/godata
https://research.swtch.com/interfaces
https://research.swtch.com/godata2
