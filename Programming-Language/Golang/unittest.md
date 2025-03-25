+ Ref：
    + [稀土掘金 · ag9920 · 解析 Golang 测试专栏](https://juejin.cn/column/7133408018649055269)
    + https://philipotoole.com/how-is-rqlite-tested/
    + https://martinfowler.com/articles/practical-test-pyramid.html
    + https://research.swtch.com/testing

使用猴子补丁 [gomonkey](https://github.com/agiledragon/gomonkey) 对不便于测试的函数或方法进行 monkey patch；
使用断言库 [testify](https://github.com/stretchr/testify) 对测试结果进行断言，以保证测试用例的正确性；

# 一、我们真的足够了解test这个内置库么？

## TestMain

```go
func TestMain(m *testing.M) {
	// 前置操作
	os.Exit(m.Run())
	// 后置操作
}
```

+ 用于设置执行测试时的前置和后置操作
+ 该函数是包纬度的，会执行包纬度所有的单测

## go cmd

+ 一些有用的flag或者args
    + flag `-v`：即verbose
    + args `-run`：通过正则执行指定的case
    + flag `-race`：竟态竞争检测，最佳实践必加
    + flag `-cover`：启动覆盖率检测工具，最佳实践必加
        + 相关报告以标准输出的形式产出，假如希望这部分信息单独出来可以使用参数`-coverprofile=coverage.out`，对得到out文件还可以以网页的形式展示`go tool cover -html=coverage.out`，*在网页中还能展示哪些代码没有被覆盖到*。该命令是直接打开浏览器，也能输出为html：`go tool cover -html=coverage.out -o coverage.html`
    + args `-parallel`：go test会尝试并行执行测试，该参数用于限制并行执行的case的数量上限
    + args `-shuffle`：随机化测试（即一个单测文件的测试case并非依次执行），参数作为随机化种子（案例说测试case之间不应该存在依赖）

所以下面两个命令是好用的组合技

```bash
go test -v -cover -race ./...  # 执行当前路径下所有的golang包中的参数, 并打印输出, 检测覆盖率, 检查竟态竞争.
go test -v -cover -race -run XXX  # 参数同上, 只是执行某一个/类的case
```


# 二、还有那些几乎成事实标准的库呢？testify和goconvey

# 三、测试驱动开发和表驱动测试
> Table-Driven Test


# 四、发挥单测的全部能力！Test Double！

+ SUT（System Under Test）待测试系统

> 让我们先梳理一下来自[xUnit Test Patterns: Refactoring Test Code, Gerard Meszaros](https://www.amazon.com/xUnit-Test-Patterns-Refactoring-Code/dp/0131495054)的一些术语

+ Test Double，测试替身（是的，这里的double不是浮点数），一个通用的术语（因为这方面有很多容易混淆的概念），表示任何的用于测试目的而代替真实对象的模拟对象（any kind of pretend object used in place of a real object for testing purposes）
然后我们可能会看到五种test double
1. Dummy：对象被传递但从来没有被使用，仅用于填充占位（placeholder）
> Dummy objects are passed around but never actually used. Usually they are just used to fill parameter lists.
2. Fake：对象有实际的实现，但是通常会有捷径，使它们不适合生产环境。比如内存数据库，在代码中会实际链接数据库服务，但是测试中连接已经存在于内存的数据，其接口和其行为与服务一致或者基本一致。
> Fake objects actually have working implementations, but usually take some shortcut which makes them not suitable for production (an in memory database is a good example).
3. Stubs：对测试过程中的调用返回固定的结果。
> Stubs provide canned answers to calls made during the test, usually not responding at all to anything outside what's programmed in for the test.
4. Spies：它就是Stubs，但是除了返回信息之外，还会存储一些信息用于验证
> Spies are stubs that also record some information based on how they were called. One form of this might be an email service that records how many messages it was sent.
5. Mocks：
> Mocks are what we are talking about here: objects pre-programmed with expectations which form a specification of the calls they are expected to receive.



## 单元测试
1.单元测试的场景有哪些
2.各场景的代码实践演示
3.如何与测试各环节联动