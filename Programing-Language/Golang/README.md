+ source：
	+ [Manual](https://go.dev/)
	+ [Go by Example](https://gobyexample-cn.github.io/)
	+ [Go语言设计与实现](https://draveness.me/golang/)：从名字也能管中窥豹，这不是讲Golang语法和项目的书籍，而是讲它是怎么实现的

+ 一个编译型的语言怎么实现GC的呢？直接把一份go的运行时副本嵌入其中

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
go env -w GO111MODULE=on  # 下面有讨论，按理说应该默认开启
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

+ 参数`-race`竟态检测，检测并发的异常

+ `go build`
	+ 得到汇编代码：`go build -gcflags -S main.go`
	+ 获得优化汇编的过程：`GOSSAFUNC=main go build main.go`，得到一个可交互的网页`ssa.html`

+ `go test`：找到包内文件名为`*.test.go`的文件运行其中的`Test..`函数

## project file struct
>[资料](https://github.com/golang-standards/project-layout/blob/master/README_zh.md)

## IDE
VSCode [Manual](https://learn.microsoft.com/zh-cn/azure/developer/go/configure-visual-studio-code)
+ how to debug: [tutor](https://www.digitalocean.com/community/tutorials/debugging-go-code-with-visual-studio-code)