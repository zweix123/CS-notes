## Install
按照[manual](https://go.dev/doc/install)下载即可
## config
```bash
go env -w GOPROXY=https://goproxy.io,direct  # 设置软件源
```

### go env
可查看关于Golang的环境变量

+ `GOPATH`：`go install`的下载位置（默认为`$HOME/go/bin`）
+ `GO111MODULE`：是否启用Go Modules管理项目依赖（默认启用）

## Command
[资料](https://docs.kilvn.com/go_command_tutorial/)

### go mod

+ 初始化项目：`go mod init 项目名`

### go get, go install

+ go get用于修改go.mod的依赖
+ go install用于构建和安装二进制文件

+ go mod tidy：依照项目中import的实际使用情况调整go.mod

## project file struct
>[资料](https://github.com/golang-standards/project-layout/blob/master/README_zh.md)
