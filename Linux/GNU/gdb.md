>GDB即GNU Debugger

+ Reference
	+ [QuickStart](https://www.cprogramming.com/gdb.html)

+ 不要忘了`help`

+ 启动：
	1. 编译：`gcc -g main.c -o main.out`，参数`-g`
	2. 调试：`gdb main.out`
	3. 打断点：`break`(`b`)
		+ `b main`
		+ `b file:line`
	4. 运行：`run`(`r`)

	+ 有参数的程序：`gdb --args main.exe 参数`
		+ `show args`查看参数

+ 查看代码：
	+ `list`(`l`)：输出即将运行的语句的附近的代码
	+ `layout src`：试试就知道了
		+ `Ctrl + l`
	+ `f`：查看即将要运行的语句
	+ `bt`：打印栈

+ 控制：
	+ 执行语句不进入函数：`next`(`n`)
	+ 执行语句进入函数：`step`(`s`)
	+ 执行到当前函数末尾：`finishhh`(`fin`)

+ 调试：
	+ `print`(`p`)查看值

+ misc:
	```bash
	starti  # 执行程序第一条语句
	```
