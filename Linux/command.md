+ Reference：
	+ [One Quick Start](https://linux.cn/article-6160-1.html)
	+ 没有《鸟哥的Linux私房菜》

+ Manual：
	+ `man command`
	+ `tldr command`（Too Long, Don't Read）
	+ `--help`

### 最最基本的命令

+ `pwd`：显式当前绝对路径
+ `ls`：list (file and dir)
+ `cd`：change dir
	+ `cd ..`：
+ `cp sourcefile distfile`：copy
+ `rm file`：remove
	+ `rm dir -r`
+ `mv sourcefile distfile`：move or rename
+ `mkdir dir`：make dir
+ `touch file`：create file
+ `cat file`：print file content
+ `chmod`：修改文件权限
	+ `chmod +x XXX`：给XXX添加可执行权限
	+ `chmod -x XXX`：去掉XXX的可执行权限
	+ `chmod 777 XXX`：将XXX的权限改成777
	+ `chmod 777 XXX -R`：递归修改整个文件夹的权限
+ 后台运行：
	+ 命令末尾添加`&`将命令后台运行
	+ `jobs`：查看所有命令
	+ `fg %数字`：将对应后台任务放到前台

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

### 快捷键

+ `Ctrl + u`：请求本行命令
+ `Ctrl + c`/`Ctrl + \`：可以简单的理解强行终止当前命令
+ `Ctrl + r`：检索历史命令，输入历史命令的子串后继续`Ctrl + r`则是继续向上翻找
+ `Tab`：补全命令或文件，双击提示选项
+ 方向键`up`：上一条命令

### 研究

+ `type`：
+ `where`
+ `strace`：检查命令使用的系统调用
+ `time`：给出程序运行时间

## 查看机器信息（和运维）

### 硬件

+ `lscpu`
+ `lsblk`
+ `df -h`：查看硬盘使用情况
	+ 替代品：`dust`
+ `free -h`：查看内存使用情况
+ `du -sh .`：查看当前目录占用的硬盘空间
+ `ping`：网络连接
+ `ssh`：[我的教程](../Missing-Semester/SSH.md)
+ `xrandr`：显示屏

### 软件

+ `uname -a`：查看机器操作系统信息
+ `top`：查看所有进程的信息（Linux的任务管理器）
	+ 打开后，输入`M`：按使用内存排序
	+ 打开后，输入`P`：按使用CPU排序
	+ 打开后，输入`q`：退出

	+ Modern 替代品：`htop`

+ `ps aux`：查看所有进程（直接标准输出）
+ `kill -9 pid`：kill 对应pid 的进程
	>本质是向某个进程传递信号：`kill -s SIGTERM pid`

## 工具（Unix哲学）

+ `watch -n 0.1 command`：每0.1秒执行一次`command`命令
+ `tree`：展示当前目录的文件结构
+ `md5sum`：计算md5哈希值：
	+ 可从`stdin`读入内容：执行命令 -> 输入内容 -> `Ctrl + z`
	+ 可从命令行参数传入文件名列表
+ `tar`：压缩文件
	+ `tar -zcvf xxx.tar.gz /path/to/file/*`：压缩
	+ `tar -zxvf xxx.tar.gz`：解压缩
	+ `tar -jxvf xxx.tar.bz2`：解压tar.bz2

### 统计

+ `cloc`：统计行数
+ `wc`：统计字数
	+ `wc -lwc`：行数、单词数、字节数

### 查找和筛选

+ `diff`：比较不同
	+ `vimdiff`
+ 按文件名查找文件：`find`
	+ Modern 替代品：`fd`
+ 按文件内容查找文件：`grep`
	+ Modern 替代品：`ag`

### 查看

+ `cat`
+ `more`：浏览文件内容：
	+ `回车`：下一行
	+ `空格`：下一页
	+ `b`：上一页
	+ `q`：退出
+ `less`：与more类似，功能更全
	+ `回车`：下一行
	+ `y`：上一行
	+ `Page Down`：下一页  
	+ `Page Up`：上一页
	`q`：退出
+ `head -3 xxx`：展示xxx的前3行内容  
	同时支持从stdin读入内容  
	`cat file | head -10`查看file开头10行内容
+ `tail -3 xxx`：展示xxx末尾3行内容  
	同时支持从stdin读入内容  
	组合机同head

+ `cut`：  
	从stdin中读入多行数据  
    `echo \$PATH | cut -d ':' -f 3,5`：输出PATH用:分割后第3、5列数据  
    `echo \$PATH | cut -d ':' -f 3-5`：输出PATH用:分割后第3-5列数据  
    `echo \$PATH | cut -c 3,5`：输出PATH的第3、5个字符  
    `echo \$PATH | cut -c 3-5`：输出PATH的第3-5个字符

+ `sort`：将每行内容按字典序排序，可从`stdin`内读取多行，可从参数读取文件名列表
