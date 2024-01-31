我试图写一个关于Linux操作的科普文章，面向计算机新生或者AP刚退役选手。
我不想做命令的罗列，我希望在其中嵌入关于Unix哲学、“一切皆文件”思想、操作系统的设计等相关系统知识，并推荐一些旧命令的现代版。

+ 首先还是需要一些命令的罗列的
	+ [新手指南： Linux 新手应该知道的 26 个命令](https://linux.cn/article-6160-1.html)
	+ [The Art Of Command Line简体中文](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md)

+ Shell快捷键：
	+ `Ctrl + C`：中断或杀死当前正在运行的程序或进程，向程序发送一个中断信号（SIGINT），强制它停止运行并返回命令行提示符
	+ `Ctrl + \`：强制退出或终止当前正在运行的程序或进程。向程序发送一个退出信号（SIGQUIT），强制它立即终止并返回命令行提示符
	+ `Ctrl + D`：输入结束或退出当前会话（也称为“断开连接”）。当您在终端窗口中输入时，按下Ctrl+D会告诉终端程序将输入的内容发送给正在等待输入的程序，并指示您已完成输入。如果您在空行中按下Ctrl+D，那么终端会将此解释为您要结束会话并返回到命令行提示符。


+ 文件描述符：Linux程序运行时默认打开3个文件，通过文件描述符区分
	+ 0号文件：默认输入（默认当前终端
	+ 1号文件：默认输出（默认当前终端
	+ 2号文件：默认错误（默认当前终端

+ 文件权限
	一共10位：  
		第一位表示当前是目录`d`还是普通文件`-`  
		剩下9位3位一组  
			三个组分别是当前用户权限、组内用户权限和其他用户权限；  
			组内三位分别表示是否可读、是否可写、是否可执行，由数字0~7表示。  
	![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Linux/Linux文件信息.png)


+ 重定向

	| 命令              | 说明                                          |
	| ----------------- | --------------------------------------------- |
	| `command > file`  | 将stdout重定向到file中                        |
	| `command < file`  | 将stdin重定向到file中                         |
	| `command >> file` | 将stdout以追加方式重定向到file中              |
	| `command n> file` | 将文件描述符n重定向到file中<br> `2>`错误输出 |
	| `command n>> file`                   | 将文件描述符n以追加方式重定向到file中<br>样例同上                                              |

+ 管道：将前一个命令的`stdout`重定向给下一个命令的`stdin`
	+ 只能处理`stdout`，会忽略`stderr`
	+ 要求管道右边的命令必须能接受`stdin`
	+ 可串联

+ `xargs`命令：结合管道将一个命令的stdout作为下一个命令的argues

## 一切皆文件——特殊的目录

## /proc

我遇到这样的事情，一个命令每个按我想的那样标准输出，怎么排查呢？首先确定它真的标准输出（即标准输出的文件描述符是指向我认为的那个文件）

1. `ps aux | grep "命令"`或者`ps -ef | grep "命令"`找到对应的进程的PID
2. `ll \proc\pid\fd`

所以`\proc`目录下放着的就是各个进程的所有信息，包括`top`这样的命令的信息都是来自这里。


## 从存储设备到文件系统

+ 存储设备：HDD和SSD
1. 存储设备初始化：
	1. 分区：讲存储设备分为逻辑部分
	2. 格式化：在分区上创建文件系统
2. 挂载：将文件系统与操作系统中的目录进行关联

+ 命令`lsblk`：查看所有的块设备，`NAME`列即为块设备名称，`MOUNTPOINT`即为对应挂载到的目录
+ `df`, `du`（估计）

## 其他

ranger strace time

df, dust, free, du, ssh `ssh`：[我的教程](../Missing-Semester/SSH.md), top

+ `ps aux`：查看所有进程（直接标准输出）
+ `kill -9 pid`：kill 对应pid 的进程
	>本质是向某个进程传递信号：`kill -s SIGTERM pid`

+ `watch -n 0.1 command`：每0.1秒执行一次`command`命令
+ `tree`：展示当前目录的文件结构
+ `md5sum`：计算md5哈希值：
	+ 可从`stdin`读入内容：执行命令 -> 输入内容 -> `Ctrl + z`
	+ 可从命令行参数传入文件名列表

+ `cloc`：统计行数
+ `wc`：统计字数
	+ `wc -lwc`：行数、单词数、字节数

+ `diff`：比较不同
	+ `vimdiff`
+ 按文件名查找文件：`find`
	+ Modern 替代品：`fd`
+ 按文件内容查找文件：`grep`
	+ Modern 替代品：`ag`
