## Install
按照[manual](https://go.dev/doc/install)下载即可
+ 这里不建议将`$PATH`的修改放在`profile`中，如果对shell比较了解，推荐放在对应的`rc`文件中（虽然这样只修改终端），我个人使用`zsh`
	```
	vim ~/.zshrc
	export PATH=$PATH:/usr/local/go/bin  # manual中的
	export PATH=$PATH:$(go env GOPATH)/bin  # 见下我关于依赖管理问题的讨论
	```
### config
```bash
go env -w GOPROXY=https://goproxy.io,direct  # 设置软件源
```

### 依赖管理问题
早期Golang通过`GOPATH`管理，现在逐渐使用Go Modules管理

---
+ 命令`go env`可查看关于Golang的环境变量，上面config中的GOPROXY就在其中
---
+ GOPATH默认是`$HOME/go`
+ GO111MODULE默认为空，相当于`on`
---
+ 命令`go mod init ...`初始化项目，生成`go.mod`文件
---
+ `go get ...`用于修改go.mod（修改依赖）
+ `go install ...`用于构建和安装二进制文件
	+ 下载的二进制文件就在GOPATH路径下的`bin`目录下  
		这时就可以解释为什么要将GOPATH/bin设置为环境变量，只有这样下载的二进制文件才能作为一个命令使用
---
+ `go mod tidy`可以依照项目中依赖的使用情况自动更新go.mod，所以这里推荐使用这句命令，即使各大开发框架的install是get
---
除了上面的go.mod文件，还有一个`go.sum`文件，其中的是依赖的校验信息

## Command
[资料](https://docs.kilvn.com/go_command_tutorial/)

## project file struct
>[资料](https://github.com/golang-standards/project-layout/blob/master/README_zh.md)

## IDE
VSCode [Manual](https://learn.microsoft.com/zh-cn/azure/developer/go/configure-visual-studio-code)
+ how to debug: [tutor](https://www.digitalocean.com/community/tutorials/debugging-go-code-with-visual-studio-code)