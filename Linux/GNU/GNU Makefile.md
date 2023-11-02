命令`make`使用，命令检测当前目录下的`Makefile`文件。

## Config

+ `ccache`：顾名思义，一个大型项目的每次修改调试都需要重新编译，实际上只需要重新编译小部分，但是默认全部重新编译，该软件可以识别只编译修改过的
	+ config：rc：`export PATH=/usr/lib/ccache:$PATH`，要放在前面，此时`which gcc`为`/usr/lib/ccache/gcc`

# Use

## Args

+ `make`命令是单线程的，我们可以通过`lscpu`查看机器cpu数量，然后通过添加参数`-j?`来多CPU并行编译，其中`?`为数字
+ `-n`：只输出命令而不执行
+ `-B`：强制更新，make会检测文件是否变化嘛，该参数无论是否变化都构建

## Grammer

基本组成
```makefile
目标: 依赖
	（生成目标的）规则  # 注意这里的空白是Tab
```

比如
```makefile
a.out: a.c
	gcc a.c
```

每次make，会检测依赖是否变化，只有变化才执行规则生成目标  
依赖是递归的，如果依赖是其他语句的目标，会递归检测执行

+ 变量，Makefile中可以定义变量
	+ 定义：`变量名 = 变量内容`
	+ 使用：`$(变量)`
	+ 操作：
		+ 拼接：`+=`
		+ 函数：
			```makefile
			$(shell ...)  # 命令输出字符串
			```
	+ `$@`规则的目标  
		`$^`规则的依赖
	+ 隐含规则：
		+ 如果目标是.o，那么依赖会寻找同名.c

+ 伪目标：
	```makefile
	.PHONY: clean
	clean: 
		rm ...
	```

	```makefile
	make clean
	```