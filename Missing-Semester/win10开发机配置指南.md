+ 备份：
	+ 桌面
	+ 数据目录
	+ Chrome配置目录：`C:\Users\$用户名\AppData\Local\Google\Chrome\User Data\Default\`
	+ Clash for Windows配置文件：`C:\Users\$用户名\.config`
	+ wt配置文件：`C:\Users\$用户名\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`  
		+ posh配置：已上云
	+ VSCode配置目录：`C:\Users\$用户名\.vscode\`
	+ Git配置文件：`C:\Users\$用户名\.gitconfig`
	---
	+ Snipaste配置文件：`D:\Snipaste\config.ini`

[姊妹篇：Linux机器配置指南](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/Linux%E6%9C%BA%E5%99%A8%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97.md)

# 前言

>作此博客的发心：
>1. 作为重置系统的记录，在下次重置或者初始化一个win机器时提供可供参考的记录。
>2. 观察到有人对计算机的软件和文件的管理相当粗放，我想在这里提供一个我使用win机器的习惯和经验。
>3. 部分软件的配置确实值得记录，如果网上已经有足够优秀的教程，我会提供链接，否则，我会尽量在理清逻辑的情况下提供教程  
>	>尽可能依照Manual
>4. 后来博客还扩展出我对用过的好用软件的推荐

+ 须知：
	+ STFW：有些名词会导致递归学习且并没有解释，希望读者具有一定的"Search The Friendly Web"的能力
	+ STFM：软件的下载通常有大量教程，但是软件更新迭代很快，不同环境、不同软件版本，流程就很可能不一样，只有Manual中才是最新的

+ 环境：我的Windows机器的规格是：
	```
	版本: Windows 10 家庭中文版
	版本号: 21H2
	操作系统内部版本: 1904.2486
	```

+ 关于数据的管理：  
	我并没有将软件和文档分成两个盘，因为实际上我在学生时代创造的值得存储的数据不到30G，所以我直接在D盘创建一个专门的目录并在其下管理我的数据，这样的好处是在进行数据备份和转移时，只需要维护这个目录即可。

+ 关于软件的管理：
	>软件倾向于安装在C盘的原因：
	>+ 以前C盘是固态硬盘，其他盘则未必，故将软件安装在C盘可以更快
	>+ 软件作者不能保证用户一定具有某个除了C盘以外的某个盘。

	+ 软件尽可能安装在非C盘的盘，现在的非C盘也都是固态硬盘，上面的速度原因无需顾虑
		+ 通过安装包安装软件时通常会有对应的步骤提示（或者是一个拉起的选项卡）选择路径
		+ 诸如WeChat、QQ、TIM或者是软件管家这样的软件通常涉及到文件的存储，需要在“设置”中手动修改
		+ 有些安装包直接安装软件并在桌面创建快捷方式，可以通过查看快捷方式的指向来确定其存储位置，不建议直接横移文件夹修改
			>因为还涉及到注册表等等因素

## 初始设置

+ 第一次开机：win10会以对话式的方法进行初始化配置，仔细阅读其描述按照自己的理解选择即可。
	>其中有个选项是“是否连接WiFi”，如果是新电脑，连接后通常不能进行退换（虽然本篇文章并没有检查新机的教程）

	+ 用户名尽量用英文
	+ 系统可能会默认下载一些软件，比如视频或音乐软件，这些通常下载在C盘，我通常都是卸载然后如果需要再重新安装
	+ 简约风格，扫描一下桌面把不需要的东西去掉。

+ 导入备份：

+ 语言配置：
	+ 输入法：默认
	+ 拼音设置：双拼且不自动扩展到全拼
	+ 中英切换：只保留`Ctrl + Space` （个人习惯）

+ 文件的查看：
	+ 打开文件扩展名
	+ 打开隐藏的项目

+ 电源设置：
	>睡眠：风扇转                      ：此时电脑仍供电给内存，CPU以较低频率运行（微软关于睡眠有详细的模式设置，例如`S0`、`S3`模式等）  
	>休眠：风扇不转，信息保留：计算机将内存中的内容写入进磁盘中，并断电。下次开机时可以恢复到之前的工作状态。  
	>关机：信息不保留 
	
	|                | 电池    | 通电     |
	| --------  | ------ | ------   |
	| 电源按钮 | 休眠    | 休眠     |
	| 关盖        | 不使用 | 不使用 |

---

+ 不能进入`C:\Program Files\WindowsApps`：[教程](https://jingyan.baidu.com/article/1876c852de26a0c80b1376c5.html)

# 必装软件

## 1.浏览器:Chrome
六大浏览器之一，插件丰富
win默认使用Microsoft Edge浏览器现在（2023.2.7）已经改为Chromium内核，可以直接同步Chrome数据（收藏夹、扩展）但是它每个选项卡都是一个窗口，我仅把它作为PDF阅读器使用

+ Chrome默认安装C盘：不处理，软件位置右键快捷方式查看
+ 谷歌需要人工验证：使用插件Header Editor（[教程](https://blog.azurezeng.com/recaptcha-use-in-china/)）
	```
	https://azurezeng.github.io/static/HE-GoogleRedirect.json
	```
+ 插件推荐：
	+ YouTube双语字幕
	+ 划词翻译

## 2.解压缩:7z
一款简单的解压缩软件

## 3.科学上网:Clash
懂得都懂
>记得软件安装包和梯子的备份

## 4.笔记软件:Obsidian
>尽可能在某个学习阶段的开始就确定工作流，不然更换软件或配置的代价是巨大的

+ Obsidian默认安装C盘：不处理，软件位置右键快捷方式查看
	>这个软件的核心其实是配置（项目目录下`.obsidian`文件夹），而配置文件是在对应的项目下的，可以不占C盘空间

Obsidian之于Typora，就像VSCode之于Jetbrains：后者在提供功能的同时也在设置限制。下面讨论我从Typora转向Obsidian的心路历程

+ Typora的即时渲染做的很好，对Makedown本身的语法补全非常到位，而这方面Obsidian有差别且需要配置插件
	+ Makedown：基本语法补全基本一致
	+ Table：Obsidian需要插件
	+ LaTeX：语法有区别，之前笔记失效，还在学习
	+ \`\`\`graph：Obsidian更好看
	+ 代码块：
		+ 列表：Typora在改变代码块的列表从时自动对齐代码，Obdian在不使用插件时不行
	+ 使用模式：Typora更多的是单文件（其实也能维护目录），而Obsidian则是完全以项目为中心

+ Obsidian优势：
	+ 更完善的文档
	+ 全平台且开源
	+ LaTeX通过插件可支持LaTeX的Tikz
	+ 使用插件可通过Github实现多机同步
	+ 链接，想象一下，笔记可以像IDE的`Ctrl + Click`一样跳转
	+ 体感上感觉性能Obsidian比Typora强

+ 为什么没有选择其他的Makedown编辑器？
	+ VSCode：写代码
	+ 有道云笔记：文件使用内部编码
	+ notion：不了解

+ Obsidian缺点（至少对我来说）：
	+ 既然选择以项目为中，为什么不能提供右键打开当前目录的选项？

+ 插件推荐：
	+ Obsidian Git（需要下载Git）多机同步必备
	 >我的配置：  
	    >`Ctrl + Alt + C` -> `commit`、`Ctrl + Alt + H` -> `push`、`Ctrl + Alt + L` -> `pull`  
		>实际上这个插件提供定时自动commit和push，我由于个人习惯没有使用，上面的快捷键是尽量躲避win的ubuntu系统快捷键的结果

	+ Advanced Tabled：Makedown表格的自动补全，使之相当Typora

+ 使用时遇到的问题：
	+ `项目根目录/.obsidian/workspace.json`的修改相当频繁，不及时push和pull比较麻烦

## 5.Windows Terminal
是为诸如cmd和windows powershell这样的命令行程序套一个好看的壳
>命令行基础，`win + R`键入`cmd`打开一个命令行程序

1. 下载：使用国内网在Microsoft Store直接下载即可（Manual推荐）
	>自然默认安装C盘：不处理

2. 使用：快捷键`win + r`键入`wt`打开
	>问题：
	>1. 报错VCRUNTIME140_1.dll缺失：在C盘搜寻文件，将其复制到`C:\Windows\System\`即可

+ 关于wt的设置，网上教程多的修改`setting.json`文件，实际上wt提供图形化的修改方式，是等价的。

### 美化
>推荐下载方式使用winget（因为使用Microsoft Store同样能下载，但是winget方便升级）

1. 安装PowerShell7：[官方教程](https://learn.microsoft.com/zh-cn/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.3)（推荐winget）
	>PowerShell7较于Windows PowerShell已经有了更多的美化功能。
	+ 使用：快捷键`win + r`键入`pwsh`命令
	+ ps7会在打开后运行`$PROFILE`这个脚本

2. 设置字体（[下载地址](https://www.nerdfonts.com/)）：网站内的每种字体都是一个`.zip`文件，里面是一系列的字体，oh-my-posh推荐字体`MesloLGM NF`，我们下载`Meslo`字体并解压，发现里面并没有对应名称的文件夹，这里主要是一种`.ttf`文件，我们双击打开观察，主要关注安装按钮和字体名称字段  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Missing-Semester/字体打开.png" style="zoom:50%;" div align=center />

	关于字体文件名中的部分含义：`Regular`常规、`Italic`斜体、`Bold`加粗  
	我们把字体名称`MesloLGM NF`的所有形态都下载  
	在wt中修改  

3. 安装oh-my-posh：[官方教程](https://ohmyposh.dev/docs/installation/windows)（推荐winget）  
	oh-my-posh本质是一个程序，提供一些命令修改命令行形态，还记得ps7打开会运行一个脚本嘛？我们只需要将设置放入即可美化脚本

+ 这里提供我的[ps7配置和oh-my-posh主题](https://github.com/zweix123/posh-config)
+ 实际上通过`$PROFILE`可以让ps7的功能更加丰富，不过需要更多的ps编程经验，我只使用最基本的美化即可。

### misc

+ 我理解的Powershell7的使用逻辑：它除了有类似shell的命令，还有*模块Medule*的概念（不过还不理解它怎么定义这些模块的），每个模块内部有独特的命令，通过命令`Import-Medule 模块名`可以导入模块（本文并没有讨论如何完备的导入），然后就可以使用模块内的一些命令，比如网上有教程导入oh-my-posh相关模块就可以使用命令`Get-PoshThemes`查看所有主题

+ 如果ssh到linux机器，对vim来说`Ctrl + v`进入列模式比较常用，但会和Windows的`Ctrl + v`冲突：  
	打开Terminal的`Setting.json`，找到这样的字段
	```json
	{
		"command": "paste",
		"keys": "ctrl + v"
	}
	```
	去掉即可

## 6.包管理器:Scoop
在Windows中正常使用软件通常的流程是去官网下载对应机器和系统的安装包，运行安装包安装，安装过程中会选择诸如下载路径之类的设置。在开发过程中常用的比如Git或者Python这种，下载过程中还要设置更多的选项。同时想要通过命令行使用它们还要将其设置为“环境变量”。但是在实际使用的过程中，基本只会在命令行中或者以命令的形式使用，那么下载过程中下载的诸如添加桌面快捷键、添加右键菜单栏这样的功能是画蛇添足的，如果你也这样想，那么Scoop很好用。
>其实win下还有其他包管理器比如winget和chocolatey，上面终端相关就是用winget下载的，看个人习惯

+ Scoop的优点：
	+ 统一且清楚的管理下载的软件
	+ 命令行下载、自动配置环境变量
+ Scoop的缺点：
	+ 不能自动配置win注册表
	+ 不能自动添加右键菜单栏

	这里要多解释下，因为win是一个图形化操作系统，命令行很高效、图形化也有独特的魅力。上面的缺点有很多问题，比如Scoop可以下载VSCode，但是不能自动设置使用VSCode默认打开`.py`文件、`.c`文件，而且不会自动添加到右键菜单栏，想用VSCode打开一个文件夹的场景不可能用命令行去`code`；再比如`7zip`，在图形化界面下的下载流程肯定是右键压缩包解压而不是使用命令。

+ 资源：
	+ [官网](https://scoop.sh/#/)
	+ [文档](https://github.com/ScoopInstaller/Scoop/wiki)

+ 安装：
	```powershell
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser # 设置PowerShell执行策略
	irm get.scoop.sh -outfile 'install.ps1' # 下载安装脚本
	.\install.ps1 -ScoopDir 'D:\Scoop' # 执行安装, --ScoopDir参数指定Scoop安装路径
	```

+ 文件结构：
	```
	Scoop
	  |---apps     # 下载的软件安装位置
	  |---buckets  # 软件源(或者可以这样理解)
	  |---cache    # 下载的安装包
	  |---persist  # 用户数据
	  `---shims    # 命令位置
	```

+ 配置：
	+ 利用`aria2`来加速下载，**极大**的提高安装成功率
		```powershell
		scoop install aria2  # 安装
		# 打开线程
		scoop config aria2-max-connection-per-server 16
		scoop config aria2-split 16
		scoop config aria2-min-split-size 1M 
		```
	+ 添加仓库（软件源），默认只有`main bucket`
		```powershell
		scoop bucket add extras  # 官方维护的extras bucket
		```


+ 相关命令：  
	```powershell  
	scoop --help  # 查看帮助

	scoop --help  # 查看帮助
	
	scoop search 命令     # 查看有无命令
	scoop install 命令    # 下载命令
	scoop uninstall 命令  # 删除命令
	
	scoop update  # 更新scoop、软件源和各个软件
	
	scoop bucket add 桶名 [桶地址]  # 添加桶	
	```


### Git

+ 安装：`scoop install git`

+ 配置：
	+ 配置文件位置：`C:\Users\$用户名\.gitconfig`
	```bash
	git config --global user.email "you@example.com"
	git config --global user.name "Your Name"
	# 其他配置在使用时看git提示
	```

+ ssh配置文件（[我的教程](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/SSH.md)）
	>网上有些例子是通过Scoop下载SSH，难道ssh命令不是win机器默认的嘛？

+ Github配置：`Setting -> SSH and GPG keys -> New SSH key -> 拷贝公钥`（配置公钥用于自己通过ssh链接去push，网上有诸多教程）

### Python3

+ 安装：`scoop install python`

### C/C++

+ 编译：
	+ `scoop install gcc`（`gcc`、`g++`）
	+ `scoop install make`（`GNU Makefile`）
	+ `scoop install cmake`（`Modern CMake`）
+ 调试：`scoop install gdb`（`gdb`）
>是不是已经感受到有个包管理器是多么好用了？

### node.js
+ 安装：`scoop install nodejs`

## 7.编辑器:VSCode

设计类似Obsidian，除了软件本身，更重要的是插件和配置，VSCode的配置分两部分：`C:\Users\$用户名\.vscode\`下的插件和项目目录下的`.vscode\`的配置。

+ 彻底删除VSCode：
	+ 软件安装位置
	+ `C:\Users\$用户名\.vscode\`
	+ `C:\Users\$用户名\AppData\Roaming\Code\`

+ 快捷键习惯：
	+ Ctrl + \`和Ctrl + 1用来代码区和命令行切换

+ 编辑器设置：参考[视频](https://www.bilibili.com/video/BV1YG4y1v7uB/)
	>VSCode打开设置为快捷键`Ctrl + ,`

	+ 主题（背景颜色、字体颜色等等）：插件One Dark Pro和插件Atom One Dark Theme
	+ 文件图标：插件vscode-icons
	+ 字体：
		+ 编辑器字体：打开设置，键入`Editor Font Family`  
			>需要插件`FiraCode font - Professional Font for Developers`

			<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Missing-Semester/编辑器字体.png" style="zoom:60%;" div align=center />
		+ 终端字体：打开设置，键入`Terminal Font Family`  
			<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Missing-Semester/终端字体.png" style="zoom:57.5%;" div align=center />

	+ 关闭受限模式：
		打开设置，键入`workspace.trust`  
		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Missing-Semester/vscode受限模式关闭.png" style="zoom:59%;" div align=center />
	+ 括号连线：打开设置，键入`bracket`，找到对应位置选择true  
		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Missing-Semester/branket.png" style="zoom:60%;" div align=center />
	+ 柔顺：
		打开设置，键入`smooth`，选择下面三个选项  
		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Missing-Semester/smooth.png" style="zoom:79%;" div align=center />  
		打开设置，键入`cursor` ，将下面设置为smooth  
		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Missing-Semester/cursor smooth.png" style="zoom:75%;" div align=center />  
	+ 补全建议：打开设置，键入`preview`，选择下面的选项  
		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Missing-Semester/suggest perview.png" style="zoom:64%;" div align=center />

+ 插件推荐：
	+ `Remote-SSH`：远程开发必备（据说有漏洞，不过我不在乎）
	+ `Error Lens`：报错提示方式，看个人喜好
	+ `Tabnine`：AI 自动补全插件，看个人喜好

### 开发Python
+ 依赖环境：通过Scoop下载Python（Python3）

+ 插件推荐：

+ 开发流程：以项目为中心使用独立的Python运行环境（库）
	1. 使用venv创建虚拟环境
	2. 在虚拟环境中开发

	>python还有其他的环境管理方式（conda和poetry），看个人喜好

### 开发C和C++
+ 教程：
	+ 一个在Linux下的保姆[教程](https://www.bilibili.com/video/BV1YG4y1v7uB)
	+ 一个使用clang的[教程](https://windowsmacos-vscode-c-llvm-clang-clangd-lldb.readthedocs.io/index.html)

+ 依赖环境：通过Scoop下载了gcc、g++、gdb、make和cmake

# 工具软件

## 截图Snipaste
优秀的截图软件，很好用，开源，解压即用。

+ `F1`截屏
+ 截屏后`Ctrl + T`可将截屏悬浮在屏幕上
+ `F3`可以将剪切板的内容转化成图片悬浮在屏幕上

## 思维导图Xmind8
现在的思维导图软件市场并没有一个统一的文件格式，相当于如果我们选择了一个软件几乎不可能迁移到其他软件，我现在的工作流尽可能避免使用思维导图。但是思维导图提供了一个如此独特的树形的组织信息方式，而转为手写的话速度上又很受限。至于选择哪个软件还是小马过河，这里提供Xmind8的特点，请读者自己选择
>**注意**：这里提到的Xmind是8（直接搜索`xmind8`即可），这个软件好像在2022有了更大更新，个人使用新版本不好用
>>而且Xmind8较于最新版还能自定义位置

+ 常用快捷键：`Enter`创建同级节点、`Tab`创建子节点、`Space`编辑当前节点
+ 优点：
	+ 阳间的快捷键
	+ 简约（节点大小紧贴文字）
	+ 可设置成节点任意位置
	+ 大小放缩区间小
+ 缺点：
	+ 节点限制，并不是数量限制，而是过多的节点会非常卡
		>不过这是我早期的巨大文件才出现的情况，后来女朋友用这个记笔记我看规模也很大，但是并没有很卡

## 幻灯片
见我的[教程]()


## iVam
电脑和手机分别安装通过数据线连接可将手机作为笔记本摄像头

## Tencent(WeChat QQ TIM)

+ 下载过程中的自定义路径是隐藏的，仔细寻找，观察“自定义”字眼
+ 这样的软件同样要关注下载文件或者消息记录的保存位置，在设置中修改
	+ TIM的保存路径修改是针对某个账号而不是整个软件的所有用户

如果觉得`QQ`太过臃肿可以试试`Icalingua-plus-plus`，但是是第三方软件，不排除被腾讯警告封号的危险。
