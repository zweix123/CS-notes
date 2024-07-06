## Install
按照[Manual](https://go.dev/doc/install)操作即可。

## Config

```bash
go env -w GO111MODULE=on
go env -w GOSUMDB=off
```

```bash
go env -w GOPROXY=???
```

### Go的依赖管理

## Command

+ Ref：
    + [GO 命令教程](https://docs.kilvn.com/go_command_tutorial/)

## Go项目文件结构

+ Ref：
    + [Standard Go Project Layout](https://github.com/golang-standards/project-layout/blob/master/README_zh.md)

## 槽点

1. 面向接口编程+包内名称共享+名称在包内不分先后——影响代码可读性：当我看到一个接口时，我不知道哪些结构体实现了它；当我看到一个结构体实现了很多方法时，我不知道它是为了实现哪些接口。
2. `interface{}`，一个`map[string]interface{}`或者函数返回`interface{}`就直接相当于动态类型了，我怎么知道这里的值是什么东西？
3. 相似名称过多。比如`net/http`中，包对外方法、结构体`ServeMux`都有方法`HandleFunc`，还有一个类型也是`HandleFunc`。
