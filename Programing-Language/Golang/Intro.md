## Install
按照[manual](https://go.dev/doc/install)下载即可
## config
```bash

go env -w GO111MODULE=on 
go env -w GOPROXY=https://goproxy.io,direct

echo "\nexport PATH=\$PATH:\$HOME/go/bin\n" >> ~/.zshrc
```

### go env
可查看关于Golang的环境变量




关于Golang的库管理比较复杂



### GOPATH and go get
Go在09年出现使用GOPATH，这不是包管理器，go get将对应的部件放到GOPATH中。  
Go Modules在Go 1.11出现，使用项目中的`go.mod`文件管理不同项目中的依赖。
>之后两种模式就在冲突

环境变量`GO111MODULE`就是核心，而且不同版本有不同行为。  

无脑`go env -w GO111MODULE=on`就行了，用项目中的`go.mod`和`go install`管理以来（`go mod tidy`就是自动检测项目的依赖并install ）

## Command
[资料](https://docs.kilvn.com/go_command_tutorial/)

### go mod

+ 初始化项目：`go mod init 项目名`
+ 下载项目：`go mod tidy`：下载依赖包

## project file struct

>[资料](https://github.com/golang-standards/project-layout/blob/master/README_zh.md)

