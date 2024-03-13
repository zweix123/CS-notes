# Win机器开发机配置指南
>[姊妹篇：Linux开发机配置指南](./LinuxConfigGuide.md)

+ 精华：
	+ [命令行](#5.命令行)：为Windows配置一个相当优雅的命令行环境，让你在win中有近似unix的命令行体验
	+ [包管理器Scoop](#6.包管理器scoop)：十分建议您千万不要错过这样一款包管理器，它极大的改善了我的开发环境

# 前言
本教程有一定门槛，不强求，只给有缘人。

>作此文章的发心：
>1. 作为重置系统的记录，在下次重置或者初始化一个win机器时提供可供参考的记录。
>2. 观察到有人对计算机的软件和文件的管理相当粗放，我想在这里提供一个我使用win机器的习惯和经验。
>3. 部分软件的配置确实值得记录，如果网上已经有足够优秀的教程，我会提供链接；否则，我会尽量按照Manual提供一个有全局观的教程。
>4. 软件推荐

+ 须知：
	+ STFW：有些名词会导致递归学习没有解释，有些问题教程颇多，这里只提供索引，请读者"Search The Friendly Web"。
	+ STFM：软件的下载通常有大量教程，但是软件更新迭代很快，不同环境、不同软件版本，流程就很可能不一样，我尽量依照Manual。
	+ 具体配置更多的是符合我个人的习惯，朋友们可以在此基础上进行定制。

+ 环境：我的Windows机器的规格是：`Windows 10 专业版`和`Windows 11 专业版`，我尝试让指南在两者是兼容的。

+ 关于数据的管理：  
	我并没有将软件和文档分成两个盘，实际上我在学生时代创造的值得存储的数据不到30G，所以我直接在D盘创建一个专门的目录并在其下管理我的数据，这样的好处是在进行数据备份和转移时，只需要维护这个目录即可。

+ 关于软件的管理：尽量安装在非C盘的盘，因为C盘是系统盘，如果满了影响系统的正常运行，而现在非C盘也都是固态硬盘、没有速度问题
	>软件倾向于默认安装在C盘的原因：
	>+ 以前C盘是固态硬盘，其他盘则未必，故将软件安装在C盘可以更快
	>+ 软件作者不能保证用户一定具有除了C盘以外的某块盘。  

	+ 通过安装包安装软件时通常会有对应的步骤提示（或者是一个拉起的选项卡）选择路径
	+ 诸如WeChat、QQ、TIM或者是软件管家这样的软件通常涉及到文件的存储，需要在“设置”中手动修改
	+ 有些安装包直接安装软件并在桌面创建快捷方式，可以通过查看快捷方式的指向来确定其存储位置，但不建议直接横移文件夹修改

+ 后记：
	+ 既然所有的盘都是固态盘，我重新划分盘空间，只留一个C盘

## 0.初始设置

+ 第一次开机：win10会以对话式的方法进行初始化配置，仔细阅读其描述按照自己的理解选择即可。
	>其中有个选项是“是否连接WiFi”，如果是新电脑，连接后通常不能进行退换（我不保证属实，我不知道原理，本文不是一个新机检查的教程）

	+ 用户名尽量使用ASCII字符
	+ 系统可能会默认下载一些软件，比如视频或音乐软件，这些通常下载在C盘，我都是卸载然后如果需要再重新安装
	+ 简约风格，扫描一下桌面把不需要的东西去掉。

+ 导入备份：数据目录

+ 语言配置（个人习惯）：
	+ 输入法：默认
	+ 拼音设置：双拼且不自动扩展到全拼
	+ 中英切换：只保留`Ctrl + Space`
	+ 全半角和中英标点的切换设置为无
	+ 翻页只有+/-
	+ 设置默认英文

+ 文件的查看：
	+ 打开文件扩展名
	+ 打开隐藏的项目

+ 电源设置（笔记本）：
	>睡眠：风扇转：此时电脑仍供电给内存，CPU以较低频率运行  
	>休眠：风扇不转，信息保留：计算机将内存中的内容写入进磁盘中，并断电。下次开机时可以恢复到之前的工作状态。  
	>关机：信息不保留 
	
 |          | 电池   | 通电   |
 | -------- | ------ | ------ |
 | 电源按钮 | 休眠   | 休眠   |
 | 关盖     | 不使用 | 不使用 |

+ 关于在Windows上编程时出现的语言问题，解决方案：控制面板 -> 时钟和区域 -> 区域 -> 管理 -> 更改系统区域设置 -> 打开Beta版
	+ 默认是没有开的，此时比如使用C++的`std::cout`输出中文是乱码，但是打开后，对于其他的在win上的在未打开时进行压缩的压缩包，在我们机器上进行解压会有乱码。

+ 不能进入`C:\Program Files\WindowsApps`目录：[solution](https://jingyan.baidu.com/article/1876c852de26a0c80b1376c5.html)

+ 升级到专业版或企业版，这样的场景比如连接到win的服务器就需要使用win的remote功能，这种功能家庭版没有，如何升级请STFW
	+ Reference
		+ https://blog.csdn.net/qq_32682301/article/details/116003700

# 必装软件

## 1.浏览器Chrome或Edge

我一直使用Chrome，由于工作原因在部分机器上需要使用Edge，不过Microsoft Edge浏览器也改为Chromium内核，可直接同步数据。

Chrome是六大浏览器之一，插件丰富，登陆谷歌账号同步信息和配置。

+ Edge在win上默认每个选项卡是一个窗口，很反直觉，解决方案如下：
	+ win10：`设置` -> `系统` -> `多任务处理` -> `Alt + Tab`，打开就知道了。
	+ win11：`设置` -> `系统` -> `多任务处理` -> "对齐或按Alt + Tab时显示应用中的标签页"改为"不显示选项卡"。

+ Chrome默认安装C盘：不处理，软件位置右键快捷方式查看位置
+ 谷歌需要人工验证：使用插件Header Editor（[教程](https://blog.azurezeng.com/recaptcha-use-in-china/)）
	```
	https://azurezeng.github.io/static/HE-GoogleRedirect.json
	```
+ 插件推荐：
	+ YouTube双语字幕
		+ 字幕位置有点碍眼
	+ 默认翻译、划词翻译（全文翻译收费）和沉浸式翻译（开源）：默认翻译用于最普遍的全文翻译，划词翻译用于PDF翻译，沉浸式翻译用于网站单段翻译和逐段全文翻译
	+ 油猴脚本
		+ 这里推荐一款我开发的关于哔哩哔哩的脚本，[地址](https://github.com/zweix123/BilibiliProgressBar)
	+ crxMouse Chrome手势：后退、前进、顶部、底部，对文件图片链接的打开
	+ Vimium：Vim用户的福音，嘎嘎好用。
	+ epub阅读器

## 2.解压缩7z
一款简单的解压缩软件

+ win11似乎不需要额外的解压缩软件

## 3.科学上网Clash
懂得都懂
>记得软件安装包和梯子的备份

+ 配置：
	+ 开机自启动
	+ `F2`作为开关System Proxy的快捷键

## 4.笔记软件Obsidian

该软件跨平台，我在Windows、Linux甚至IOS（IPad）上使用它。所以这里记录其仅关于Windows的东西（下载），其他的（为什么选择它以及其他操作）放在另外的位置

+ 安装：Obsidian默认安装C盘：不处理，软件位置右键快捷方式查看。

	该软件是围绕项目的，一个项目的相关配置放在项目目录下的`.obsidian`目录中。而这部分配置文件放在对应的项目下，所以不占C盘空间。

## 5.命令行

### 前置知识

+ 什么是命令行？  
	命令行、终端、工作台、Shell在很多语境下都是语义重叠的  
	+ 命令行通常是最大范围的语义
	+ 终端很多时候和命令行重叠，有时特指Window Terminal或者Terminal，下面会指关于颜色的部分
	+ 工作台：请不用使用这个名词
	+ Shell有时单指执行命令的程序，linux中bash是一种shell，win中的cmd是一种shell

+ win中怎么打开一个命令行？
	+ 快捷键`win + r`键入`cmd`弹出一个窗口即为一个命令行程序，其中的Shell是cmd
	+ 键入`powershell`弹出一个shell使用windows powershell的命令行程序

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

### 5.1.PowerShell7

+ 安装：[Manual](https://learn.microsoft.com/zh-cn/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.3)（官方推荐winget）
+ 更新：reinstall
+ 使用：快捷键`win + r`键入`pwsh`打开一个命令行程序
+ pwsh在打开后会运行`$PROFILE`这个脚本（直接在命令行中输入这个命令即可查看脚本位置）
	+ 所以可以把这个文件当做Linux中Bash的`.bashrc`文件

+ Powershell7的ls对输出的目录的美化需要下载额外模块：（下载比较慢）
	```powershell
	Install-Module PSColor
	```

### 5.2.oh-my-posh

+ 安装：[Manual](https://ohmyposh.dev/docs/installation/windows)（官方推荐使用winget）
+ 使用：还记得pwsh在打开后运行一个脚本嘛？我们只要把调用oh-my-posh的相关命令放在那里就可以用了，这里比较重要的是**主题**的选择

### 5.3.Windows Terminal

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

## 6.包管理器Scoop

**Scoop非常强大，几乎任何你想下载的命令行程序或者依赖软件都可以去search一下，几乎都有！**  
比如C/C++（`gcc`、`g++`、`gdb`、`make`、`cmake`）、Python（Python和某些库的依赖）、Golang、Java、LaTeX还有各种软件。

首先考虑第一性原理的问题，我们为什么需要这样的包管理器？  
在Windows中正常使用软件通常的流程是去官网下载对应机器和系统的安装包，运行安装包安装，安装过程中会选择诸如下载路径之类的设置。在开发过程中常用的比如Git或者Python这种，下载过程中还要设置更多的选项。同时想要通过命令行使用它们还要将其设置为“环境变量”。但是在实际使用的过程中，基本只会在命令行中或者以命令的形式使用，那么下载过程中下载的诸如添加桌面快捷键、添加右键菜单栏这样的功能是画蛇添足、没有必要的。
>其实win下还有其他包管理器比如winget和chocolatey，上面终端相关就是用winget下载的，看个人习惯

+ Scoop的优点就是能统一且清楚的管理下载的软件并自动为其配置环境变量
+ Scoop的“缺点”：
	+ 不能自动配置win注册表
	+ 不能自动添加右键菜单栏  

	这里为什么加双引号呢？因为Windows是一个图形化的操作系统，命令行很高效、图形化也有独特的魅力。上面的缺点有很多问题，比如Scoop可以下载VSCode，但是不能自动设置使用VSCode默认打开`.py`文件、`.c`文件，而且不会自动添加到右键菜单栏，想用VSCode打开一个文件夹的场景大概率不是用命令行去`code`（虽然我后面确实都是用命令行打开），而是图形化的找到这个文件然后右键打开；再比如`7zip`，在图形化界面下的使用流程肯定是右键压缩包解压而不是使用命令；但是这些都是在对标之前的下载流程，我们选择Scoop的原因恰恰是它不会这样，所以善用Scoop这些不是缺点。

+ 你几乎可以用Scoop管理你使用的所有语言的编译器/解释器。

+ Reference：
	+ [项目](https://github.com/ScoopInstaller/scoop)
	+ [官网](https://scoop.sh/#/)
	+ [文档](https://github.com/ScoopInstaller/Scoop/wiki)

+ 安装：
	```powershell
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser # 设置PowerShell执行策略
	irm get.scoop.sh -outfile 'install.ps1'                              # 下载安装脚本
	.\install.ps1 -ScoopDir 'D:\Scoop'                                   # 执行安装, --ScoopDir参数指定Scoop安装路径
	```

+ 文件结构：
	```
	Scoop
	  | ---apps      # 下载的软件安装位置
	  | ---buckets   # 桶(可以理解为软件源)
	  | ---cache     # 下载的安装包
	  | ---persist   # 用户数据
	  `----shims     # 命令位置
	```

+ 配置：
	+ 安装sudo：`scoop install sudo`
	+ 利用`aria2`来加速下载，**极大**的提高安装成功率
		```powershell
		scoop install aria2  # 安装
		scoop config aria2-enabled false  # 如果使用代理可能需要这样的配置
		# 线程相关
		
		scoop config aria2-retry-wait 4
		scoop config aria2-split 16
		scoop config aria2-max-connection-per-server 16
		scoop config aria2-min-split-size 4M
		```
	+ 添加仓库（软件源）

		```
		scoop bucket add extras   # 官方维护的extras bucket  # 需要先下载git(在教程的下面)
		scoop bucket add versions # 软件多版本 
		scoop bucket add nirsoft
		scoop bucket add dorado https://github.com/h404bi/dorado
		scoop bucket add Ash258 'https://github.com/Ash258/Scoop-Ash258.git'
		scoop bucket add nerd-fonts
		```

	+ 检查：检查当前配置是否有问题：
		```bash
		scoop checkup
		```

+ 相关命令：  
	```powershell  
	scoop --help  # 查看帮助
	scoop list    # 查看已经下载的软件
	
	scoop search 命令     # 查看有无命令
	scoop install 命令    # 下载命令
	scoop uninstall 命令  # 删除命令
	
	scoop update  # 更新scoop、软件源和各个软件
	
	scoop bucket add 桶名 [桶地址]  # 添加桶	
	```

+ 软件多版本：一般可以通过指定文件名为`文件名@版本号`的方式下载特定版本
	+ Python：`scoop install python310`
	+ 版本切换：使用命令`scoop reset [app]@[version]`

+ 其他：
	+ 关于软件`unxutils`：这里有很多Linux常用命令，用来补齐Windows和Linux命令不同的问题，但是我没有安装，首先Powershell7本身就有很多和Linux一致的命令，部分会单独安装。而这里不仅有基本的命令，还有`zsh`这样的命令， 至少给我带来的一个问题是在VSCode使用CMake插件会造成输出乱码已经部分情况不能编译。所以卸载了这个。

### 7.Git

+ 安装：`scoop install git`
+ 配置：[我的教程](./Git.md#config)
+ 配置SSH：[我的教程](./SSH.md)
+ Github配置：`Setting -> SSH and GPG keys -> New SSH key -> 拷贝公钥`（配置公钥用于自己通过SSH链接去`push`）

## 8.编辑器:VSCode
VSCode本身是编辑器，在插件的支持下扩展出丰富的功能（<strike>极具可玩性</strike>）

+ install：STFW
+ uninstall：
	+ 软件安装位置
	+ `C:\Users\$用户名\.vscode\`：全局配置
	+ `C:\Users\$用户名\AppData\Roaming\Code\`：缓存

+ configs：内容多且散，且无关平台，我将其放在这个[教程](../Missing-Semester/VSCode.md)

# 工具软件

## 基于命令行的编辑器

VSCode本是一个轻量型的编辑器，轻量型意味着可以快速的打开，但随着我们给它装了大量的插件，它开始变得臃肿，此时如果有轻度的编辑，再使用它就不再流畅了（无论是命令行打开还是图形化打开），我们需要一个更轻量型的编辑器。  
得益于强大的包管理器Scoop和我调教好的终端，我们可以有近似Linux的命令行体验，所以我选择vi系列作为这个轻度编辑器。
>这部分对我个人来说也是必须的，但未必适用于其他开发者，VSCode足以在可接受的成本内满足要求，所以没有将该软件放在必装软件中

+ 安装：亲爹Scoop
+ 配置和使用：我的[文章](../Linux/Editor.md)
	>实际上vim是一个可玩性很高的编辑器，这里引用的文章不仅有vim的基本用法，可能还会有我倒腾vim的记录。

## 图片悬停Snipaste
优秀的截图软件，很好用，开源，解压即用。

+ `F1`截屏
+ 截屏后`Ctrl + T`可将截屏悬浮在屏幕上
+ `F3`可以将剪切板的内容转化成图片悬浮在屏幕上

## 启动器
类似Mac上的Alfred，先Mark下

## 思维导图

我在最开始是使用思维导图记笔记的，直到现在我也觉得树形结构是比流式结构更好的笔记结构，此时随机选择了[Xmind8](https://xmind.cn/download/xmind8/)（是8而不是最新版，这个可能不是最好看的，但是我觉得是操作最合理高效的）。随机笔记规模的扩大就有了渲染性能和文件管理的问题，这个时候使用Markdown；此时思维导图这个形式只是偶尔使用，最后发现没必要在为这偶尔使用的需求留着一个软件了，换到[markmap](https://markmap.js.org/)框架（有VSCode插件）

## 幻灯片jyyslide-md
见我的[讨论](./slide.md)

## 论文LaTeX
见我的[讨论](./LaTeX.md)

## UML图PlantUML
见我的[教程](./misc/UML.md)

## 虚拟机VMware Workstation Pro

+ 我的使用方式：主要是为我在win机器上提供一个linux环境，所以我使用的场景一般是打开后就放在后台，然后通过SSH或者VSCode的remote（本质也是SSH）连过去，我们发现上面的场景几乎不需要VMware Workstation的图形化界面，索性VMWare为我们提供了命令行的操作形式
	```bash
	vmrun start D:\VMware\VM\Ubuntu64\Ubuntu64.vmx nogui  # 没有图形化的运行
	vmrun list  # 查看是否运行
	# 怎么关闭呢? ssh进去然后sudo poweroff
	```

+ SSH到本机的VMware虚拟机中：
	>Reference：[教程](https://cloud.tencent.com/developer/article/1679861#:~:text=windows%E5%AE%BF%E4%B8%BB%E6%9C%BA%E5%A6%82%E4%BD%95SSH%E8%BF%9E%E6%8E%A5VMware%E7%9A%84Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%201%201%E3%80%81%E5%AE%89%E8%A3%85%E5%A5%BDUbuntu%E8%99%9A%E6%8B%9F%E6%9C%BA%202,2%E3%80%81%E5%BB%BA%E7%AB%8BIP%E6%98%A0%E5%B0%84%203%203%E3%80%81%E9%85%8D%E7%BD%AE%E8%99%9A%E6%8B%9F%E6%9C%BASSH%204%204%E3%80%81%E9%85%8D%E7%BD%AE%E8%99%9A%E6%8B%9F%E6%9C%BA%E9%98%B2%E7%81%AB%E5%A2%99)

	这个方法我只设置过一次，之后创建新的虚拟机（我一般只有一个虚拟机），只需要修改本机config的目标IP地址，就可以正常使用，但是虚拟机的IP是变化了的，不知道是什么魔法？

	1. check本机和虚拟机的IP
	2. `编辑` -> `虚拟网络编辑器` -> `VMnet8` -> `更改设置` -> `VMnet8` -> `NAT设置` -> `添加`（端口转发） -> `按要求填写`
	3. 
		```bash
		sudo apt install -y openssh-client
		sudo apt install -y openssh-server
		sudo /etc/init.d/ssh restart         # 启动
		```
	+ 即可连接
+ 文件互传：VMware Workstation有相关扩展工具，我个人使用命令`scp`
+ <span id="lan">虚拟机使用本机的魔法</span>：本质是两个机器在一个局域网下，而Clash的Allow Lan模式可以让局域网中的其他机器使用自己的魔法，其他类似场景也可以。
	1. 网络条件保证，即保证在具体网，这里指的是保证本机可以SSH到虚拟机上。
	+ 不能通过ping去检测，ping使用的ICMP，它的打开与有无魔法无关
		+ 如果想实现linux ping win，可以`windows安全中心->防火墙和网络保护->高级设置->入站规则->四条ICMP回显打开`。
	2. 在win上用`ipconfig`找到自己的IPv4地址，替换到下面的位置。
	3. 设置linux方的proxy
		```bash
		export http_proxy=win_ip_v4_address:7890
		export https_proxy=win_ip_v4_address:7890
		```

		注意`export`命令的生效范围只在当前窗口，可以将其放在rc文件中

	+ 其他linux和proxy相关的命令
		```bash
		# 查看
		env|grep -i proxy
		# 取消
		unset http_proxy
		unset https_proxy
		```

	即便如此依然可能遇到什么`git clone`错误的问题，STFW吧。

## 硬件扩展
见我的[讨论](../misc/Multi-computer%20Cooperation.md)
