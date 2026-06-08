终端作为程序员学习工作中接触最多的东西，在本笔记项目中，有多次重复的笔记，让人疑惑（让我本人也疑惑），在这里梳理统一下。相关话题可以分成以下几类：

- Missing-Semester类：
    - 对命令行使用的扫盲 -> 放在本文章中

+ 知识笔记：
    + Linux相关知识 ->  放在Linux相关文件中
    + Bash语法 -> 放在语言相关文件中
    + 常见命令的详细笔记 -> 放在CLI目录下

+ 生产力配置：
    + 终端模拟器推荐（by 操作系统） ->  放在各系统配置文档中
    + 终端环境配置教程（by 操作系统） -> 放在各系统配置文档中
    + 新生态命令推荐 -> 放在本文章中

# Quick Start

## What
>什么是命令行？

就是黑框框，如果你现在的是Windows的机器，使用快捷键`Win + r`然后键入`cmd`并回车，弹出的就是命令行；如果你现在使用的是macOS的机器，使用快捷键`Command + space`打开聚焦搜索，然后键入`terminal`并回车，弹出的就是命令行。

+ 名词解析，你可能听过关于这个话题下的很多名词：工作台、命令行、终端、Shell、cmd、bash
	+ 工作台：请不要使用这个名词
	+ 命令行：通常是最大范围的语义
	+ 终端：很多时候和命令行语义重叠，有时特指某些软件，比如Windows下的Windows Terminal或者macOS下的Terminal
	+ Shell：在狭义的操作系统定义中，操作系统就是Shell和内核；在只有Command-Line interface(CLI)而没有Graphical User Interface(GUI)图形用户接口时，打开机器看到的就是Shell，是人操作机器的入口。而在GUI中，打开机器看到的是GUI，此时黑框框是GUI中的一个程序（比如上面的Windows Terminal或者Terminal），Shell即这个程序内部真正执行键入的命令的程序。有多种Shell，比如在Windows上有cmd、windows powershell、powershell7，在Unix中有bash、zsh、fish
		+ 注意有些场景也没必要严格区分“GUI中的软件”和“执行命令的程序”，比如`cmd`会弹出窗口，里面按照`cmd`的语法执行，或许可以理解为Shell在GUI中自带一个Terminal
		+ 另一个角度是Shell是一个解释器，键入的是按照其语法写的代码，交由其执行（自然也能直接解释执行某个文件）
	+ cmd和bash：已在上一条解释，是一种Shell

## Why
>为什么要使用命令行？

我个人是因为很喜欢手指在键盘上舞动的哒哒生，而编码其实思考的占比是较多的，但是通过命令行使用命令和计算机交互则是非常快速（不需要思考的），所以我很喜欢使用终端。

## How
>怎么使用命令行？

+ 打开一个命令行程序
	+ Windows：快捷键`Ctrl + r`键入`cmd`或者`powershell`，个人更建议`powershell7`，原因和如果下载使用这里不讨论
	+ Linux：Excuse me?
	+ macOS：快捷讲吗`Command + space`打开聚餐搜索，键入`terminal`
+ 使用这个命令行程序
	+ [新手指南： Linux 新手应该知道的 26 个命令](https://linux.cn/article-6160-1.html)
	+ [The Art Of Command Line简体中文](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md)

# 快速开始

0. [智慧的提问](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md)+网络问题
1. 什么是命令行？它和图形化的计算机操作方式比有什么特点？Anyway，反正你必须要使用命令行，等你用了就知道了。
2. 去哪里找一个可以用的命令行？
	+ Windows：`Ctrl + r`然后键入`cmd`，此时弹出的黑框框就是命令行，但不建议使用，建议使用[Powershell7](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4)（区分于Windows自带的Windows Powershell），推荐直接在`cmd`执行`winget install --id Microsoft.Powershell --source winget`下载。之后`Ctrl + r`键入`pwsh`打开的黑框框即是Powershell7，虽然和Linux原生的终端仍然有差别，不过就学习而言，个人体会差别不大，但仍然推荐使用Linux。
	+ Linux：如果你使用的是无桌面的模式，则你已经在命令行中了；否则快捷键`Ctrl + T`打开命令行
	+ Mac：`Command + space`打开聚焦搜索，键入`terminual`打开命令行
3. 区分一些名词：
	+ Shell：
		+ 狭义的操作系统 = 操作系统内核 + Shell，所以Shell是和操作系统进行交互的工具。
		+ Shell是一种“编程语言”，是脚本语言，可以按照期语法何其进行”交互式编程“，也能将命令作为代码放进文件中然后一起在Shell中运行。

		上面提到cmd、Windows Powershell、Powershell7都是Shell，Bash，Zsh，Fish也都是Shell。

	+ Terminal：Shell是一个抽象的概念，即执行命令本身和操作系统进行交互的。那么我们作为计算机的用户，通过什么将命令给到Shell呢？这个概念划分出来意义本来不大，比如我在任何地方打开一个命令行，肯定是终端和Shell一起打开，Shell自带一个终端（或者反过来）。但是在Windows中，有一个Windows Ternimal的软件，它需要绑定某个Shell才能使用，所以这里区分一下
	+ 命令行：在这里作为Shell和Terminal的合称

4. 快速开始一些简单常用的命令：[新手指南： Linux 新手应该知道的 26 个命令](https://linux.cn/article-6160-1.html)，如果你时间多一点的话，可以看看[The Art Of Command Line简体中文](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md)

5. 好，你可以退出本教程了。
6. 下面会在场景中讨论相关命令，相互之间没有递进关系。

# Command Recommend

ranger strace time

df, dust, free, du, ssh `ssh`：[我的教程](./ssh.md), top

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

# 附录

https://utcc.utoronto.ca/~cks/space/blog/programming/BashGoodSetEReports
https://scottspence.com/posts/speeding-up-my-zsh-shell
https://tratt.net/laurie/blog/2025/better_shell_history_search.html
