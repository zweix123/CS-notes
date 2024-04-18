# Quick Start

## What
>什么是命令行？

就是黑框框，如果你现在的是Windows的机器，使用快捷键`Win + r`然后键入`cmd`并回车，弹出的就是命令行；如果你现在使用的是MacOS的机器，使用快捷键`Command + space`打开聚焦搜索，然后键入`terminal`并回车，弹出的就是命令行。

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

## How
>怎么使用命令行？

+ 打开一个命令行程序
	+ Windows：快捷键`Ctrl + r`键入`cmd`或者`powershell`，个人更建议`powershell7`，原因和如果下载使用这里不讨论
	+ Linux：Excuse me?
	+ macOS：快捷讲吗`Command + space`打开聚餐搜索，键入`terminal`
+ 使用这个命令行程序
	+ [新手指南： Linux 新手应该知道的 26 个命令](https://linux.cn/article-6160-1.html)
	+ [The Art Of Command Line简体中文](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md)

# Config

## Windows

### 前置知识

值得强调的，在win11中Windows Terminal（下面会提到）是默认安装的，快捷键`win + r`键入`wt`即打开一个软件，它的样子是属于Windows Terminal的，但是"内核"使用的cmd这个Shell，同样这个”内核“是可以替换的，我们下面会将其替换成Powershell7。

+ 为什么要配置命令行？
	+ 功能上
		+ win上的命令行并不优秀（至少cmd是这样的），比如查看当前目录文件的命令`ls`，cmd是不支持的
		+ 有些扩展功能比如历史命令补全是非常好用、非常提高生产力的，很有必要添加这种功能
	+ 样式上
		+ 真的会好看很多

+ 配置思路：（这里提供全局的观念，下面会有具体配置步骤）
	+ 功能上：
		+ 更换Shell为`PowerShell7`（注意这不是Windows PowerShell），它支持Linux的相关命令
			>ps7（PowerShell7的简称）有很多独特的功能，比如独特的命令、独特的管道

		+ 使用程序oh-my-posh提供功能上的增强，主要是历史命令补全
		+ 使用Windows Terminal提供类似Tmux的功能
	+ 样式上：（这方面是审美和使用习惯，我会提供我的配置，您可以再做定制）
		+ 信息的输出，比如用户名、主机名、当前路径、Git状态，甚至时间、电量，这里使用oh-my-posh对这些信息进行排布和染色，即主题
		+ 底层的配置，比如字体、字体大小、颜色定义，这里通过Windows Terminal

		>关于颜色，颜色是个连续的概念，但是命令行程序只需要几种颜色，这里由”终端“确定某种颜色比如Red到底是什么样的（在这里颜色变成离散的概念），然后上层程序比如Shell通过设置好的Red进行染色，比如将用户名染色成Red。除了Shell之外比如Vim同样是在命令行上运行的程序，所以这里的对Red的设定也会影响到它。

+ 我的[配置](https://github.com/zweix123/posh-config)，项目README中有使用方法（需要在下载完下面三个软件后再导入配置）

### PowerShell7

+ 安装：[Manual](https://learn.microsoft.com/zh-cn/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.3)（官方推荐winget）
+ 更新：reinstall
+ 使用：快捷键`win + r`键入`pwsh`打开一个命令行程序
+ pwsh在打开后会运行`$PROFILE`这个脚本（直接在命令行中输入这个命令即可查看脚本位置）
	+ 所以可以把这个文件当做Linux中Bash的`.bashrc`文件

+ Powershell7的ls对输出的目录的美化需要下载额外模块：（下载比较慢）
	```powershell
	Install-Module PSColor
	```

+ 更新：当有新版本的pwsh时在打开命令行时会出现提示，比较烦，更新即可。
	```powershell
	winget update Microsoft.PowerShell
	```

### oh-my-posh

+ 安装：[Manual](https://ohmyposh.dev/docs/installation/windows)（官方推荐使用winget）
+ 使用：还记得pwsh在打开后运行一个脚本嘛？我们只要把调用oh-my-posh的相关命令放在那里就可以用了，这里比较重要的是**主题**的选择

### Windows Terminal

>win10需要下载，win11自带

+ 安装：使用国内网在Microsoft Store直接搜索下载（[Manual](https://github.com/microsoft/terminal#installing-and-running-windows-terminal)推荐）
+ 使用：
	+ 快捷键`win + r`键入`wt`打开一个Windows Terminal
		>报错：报错VCRUNTIME140_1.dll缺失：在C盘搜寻文件，将其复制到`C:\Windows\System\`即可

	+ 在文件资源管理器中右键在终端打开

+ 配置（涉及字体种类、字体大小、字体粗细、窗口大小、窗口打开位置、打开后模式、快捷键、配色方案等等）
	+ 下载字体（[下载链接](https://github.com/ryanoasis/nerd-fonts/releases/download/v2.3.3/Meslo.zip)）这里用的是Manual推荐的`MesloLGM NF`字体，通过链接下载并解压发现并没有对应名称的文件夹，而是一种`.ttf`文件  
		打开观察（主要关注安装按钮和字体命令字段（关于字体文件名中的部分含义：`Regular`常规、`Italic`斜体、`Bold`加粗  ））
		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/字体打开.png" style="zoom:50%;" div align=center />  
		我们把字体名称`MesloLGM NF`的所有形态都下载  

	+ 更多配色见[Windows Terminal Themes](https://windowsterminalthemes.dev/)

## Unix: Linux and macOS

+ shell通识：
	+ `echo $SHELL`查看使用shell
	+ `cat /etc/shells`查看机器有的shell程序
	+ `chsh -s shell绝对路径`设置默认shell
		>[关于chsh](https://wangchujiang.com/linux-command/c/chsh.html)

---

主要通过zsh和oh-my-zsh，前者是和bash一样的一个shell，但是它有更强的拓展性，但是想通过配置利用这些扩展性比较复杂，oh-my-zsh相当于一种辅助配置工具

1. 下载`zsh`：[Manual](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH)，一行命令即可  
	```bash
	sudo apt install -y zsh
	```
	更新默认shell：`chsh -s $(which zsh)`
	>实际上这边建议不要着急修改，在clone oh-my-zsh会提示是否修改默认shell

2. 下载oh-my-posh：[Manual](https://github.com/ohmyzsh/ohmyzsh/wiki)
	```bash
	sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
	```
	>这里提供国内镜像源：`https://gitee.com/mirrors/oh-my-zsh`，clone到本地修改名字为`.oh-my-zsh`即可
	
	>我在使用VMware workstation时出现错误，通过这两个博客解决（[一个](https://blog.csdn.net/m0_56681539/article/details/127912811)、[另一个](https://blog.csdn.net/u014454538/article/details/123563034)）

+ 命令：
	+ 刷新配置效果：`source ~/.zshrc`

+ `~/.zshrc`：oh-my-zsh配置文件
	+ 语法：
		+ `ZSH_THERE="random"`：配置主题，这里使用随机主题
		+ `plugins=(插件1 插件2 ... 插件n)`：配置插件，插件名之间空格隔开

+ `~/.oh-my-posh`：oh-my-zsh配置
	+ `~/.oh-my-zsh/plugins/`插件目录：每个目录即为一个插件名，目录下的`.sh`文件可查看其逻辑
		>不过下面的两个插件并没有安装在这里

+ 插件推荐：
	>插件的能否下载依照Github的可连接程度，注意本机clone下载后scp到服务器的方法中，如果本机和服务器的OS不同的情况下，可能由于编码原因报错

	+ `git`：默认安装，手动配置，为git命令提供缩写，可在插件目录下的sh文件查看
	+ `z`：默认安装，手动配置，目录快速跳转（后不再使用）
		+ history：`~/.z`
		+ 命令：`z 目录`
	+ `zsh-syntax-highlighting`：手动安装，手动配置，语法高亮
		```bash
		git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
		```
		下面提供国内镜像
		```bash
		git clone https://gitee.com/Annihilater/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
		```		

	+ `zsh-autosuggestions`：手动安装，手动配置，命令历史补全

		```bash
		git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
		```
		>这里的网址就是没有`.git`，Manual中就没有  

		下面提供国内镜像
		```bash
		git clone https://gitee.com/phpxxo/zsh-autosuggestions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
		```
	+ `zsh-completions`：更好的Tab补全？似乎不太需要。
	+ `command-not-found`：无需下载
