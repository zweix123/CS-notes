+ Go的源码文件：
	+ 命令源码文件：作为可执行程序的入口
	+ 库源码文件：集中放置各种待被使用的程序实体
	+ 测试源码文件：对功能和性能进行测试





## Go的命令
>[资料](https://docs.kilvn.com/go_command_tutorial/)

+ `build`：用于编译我们指定的源码文件或代码包以及它们的依赖包（检查性编译而不输出文件）
	```bash
	go build # 编译当前目录所对应的代码包
	go build [path]
	```


## Go项目的结构
>[资料](https://github.com/golang-standards/project-layout/blob/master/README_zh.md)



## Go项目的复现

```bash

go mod tidy  # 下载依赖库

```