## Install
按照[Manual](https://go.dev/doc/install)操作即可。

## Config
无

### Go的依赖管理

## Command

+ Ref：
    + [GO 命令教程](https://docs.kilvn.com/go_command_tutorial/)

## Go项目文件结构

+ Ref：
    + [Standard Go Project Layout](https://github.com/golang-standards/project-layout/blob/master/README_zh.md)

## 槽点

1. 面向接口编程+包内名称共享+名称在包内不分先后——影响代码可读性：当我看到一个接口时，我不知道哪些结构体实现了它；当我看到一个结构体实现了很多方法时，我不知道它是为了实现哪些接口。
2. `interface{}`，一个`map[string]interface{}`直接相当于动态类型了，我怎么知道这里的值是什么东西？
3. 相似名称过多（我不知道是什么原因导致的），库里面的命名，比如有多个结构体，它们可能有同名的方法，或者一个名为xxx的结构体有一个名为xxx的方法！又或者有很多和其他名字很类似的”中间类型“，真的很难读啊。