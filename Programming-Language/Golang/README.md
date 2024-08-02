## Install
1. 用当前系统常用的包管理器
2. 按照[Manual](https://go.dev/doc/install)下载

## Config

`go help env`查看什么是Go环境变量

+ 关于Go环境，建议讲对应变量设置在环境变量中（`export`语句放在rc文件里），而不是通过`go env -w`语句设置。

+ Go环境变量：`GO111MODULE`，应该默认为`on`，如果不是，请设置。
+ Go环境变量：`GOPROXY`，代理，通常是需要设置的。
    + 国内官方：`https://goproxy.io,direct`

## Go Command

`go help`

## Go Project Structure

[Standard Go Project Layout](https://github.com/golang-standards/project-layout/blob/master/README_zh.md)

## Go Style

+ [Uber Go Style Guide](https://github.com/xxjwxc/uber_go_guide_cn?tab=readme-ov-file)
    + 配置：[VSCode](../../Missing-Semester/VSCode.md#Golang)
        + 推荐使用`goimports`，更熟悉`gofmt`，实际上，`goimports`是`gofmt`的扩展。
        + 推荐使用`golangci-hint`，虽然Go已经把代码规范写在编译器里了，但是这个可能有更严格的代码规范，比如类似警告变错误这种。
    + `nil`是一个有效的`[]Slice`

### 名称命名规范

+ Go在语法层面通过名称首字母的大小写控制来控制是否**导出**

+ 项目名：小写，使用中划线划分单词
+ 文件名：小写，使用下划线划分单词
+ module名：使用反向域名，规范同项目名
+ package名/目录名：小写不使用下划线，package名和目录相同
+ 其他（接口名/结构体名/函数名/变量名）：使用驼峰命名法作为基本规范
    + 常量：全大写使用下划线

## 槽点

1. 面向接口编程+包内名称共享+名称在包内不分先后——影响代码可读性：当我看到一个接口时，我不知道哪些结构体实现了它；当我看到一个结构体实现了很多方法时，我不知道它是为了实现哪些接口。
2. `interface{}`，一个`map[string]interface{}`或者函数返回`interface{}`就直接相当于动态类型了，我怎么知道这里的值是什么东西？
3. 相似名称过多。比如`net/http`中，包对外方法、结构体`ServeMux`都有方法`HandleFunc`，还有一个类型也是`HandleFunc`。
