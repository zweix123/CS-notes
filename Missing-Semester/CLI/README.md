https://utcc.utoronto.ca/~cks/space/blog/programming/BashGoodSetEReports

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


# Zsh

https://scottspence.com/posts/speeding-up-my-zsh-shell
