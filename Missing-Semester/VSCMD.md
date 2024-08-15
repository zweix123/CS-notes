VSCMD = VSCode Markdown
# 标记语言

## Markdown

+ Why：为什么需要Markdown

	对于文字处理，首先想到的是微软的Word，但是对于笔记的场景中，它首当其冲的一个问题是——"冗余"，它有相当多的功能，而我们只需要很少的部分，那么多余的部分都是造成负担。Markdown则是更轻量的一个系统。

+ What：什么是Markdown

	在Word中，"内容"和"排版"是不分离的，即对于部分内容，控制对应格式。这是复杂的原因之一。有将其分离的排版或者系统。

	+ 基于标记的排版系统：LaTeX、Typest
	+ 标记语言：HTML、Markdown

	具体的，针对记笔记的几个核心需求，标题、分段、列表、表格、图片，它以非常简单的语法给予支持。

	除此之外，现代的网站都是用HTML写的，而Markdown向HTML的转换非常自然，所以Markdown也是很多博客的首选。

+ How：怎么学Markdown：不用学，没几个语法。

Word是没有语法的概念，功能都集合在软件中。Markdown是一种语言，渲染它需要具体的软件。下面聊聊Markdown编辑器。

## LaTeX

+ Ref：
	+ [知乎 · 槿灵兮 · 【LaTeX】针对萌新自学者的入门教程](https://zhuanlan.zhihu.com/p/521649367?utm_source=zhihu)
	+ [LaTeX 入门与进阶](https://latex.lierhua.top/zh/)

+ 你一定需要[Zotero](Missing-Semester/Zotero.md)

# 编写软件

+ 考虑角度：
	+ 编辑模式：Markdown的主要编辑模式有
		+ 即时渲染，即对应的格式不显示源码，直接是渲染后的效果  
		+ 分屏浏览，一边的源码、一边是渲染后的结果
	+ Markdown方言：有些Markdown编辑器还提供“Markdown方言”。比如Typora的`[TCO]`生成目录、Obsidian的内部链接`[[]]`，这些确实扩大了Markdown的功能，但是如果这些功能并不是所有编辑器都提供的话，意味着我们的笔记在迁移时要付出更大的成本，我个人选择都不使用，只使用最严格的语法。
	+ 是否多平台支持
	+ 能否源码导出
	+ 能否可多机同步
	+ 个人习惯
	+ 是否付费

每种编辑器各有优缺点，我的选择是按照自己的习惯选择的，下面描述一下心路历程，请读者结合各编辑器特点自行选择

+ Typora：即时渲染能力效果非常好，在其加持下，甚至感觉不到Markdown语法；可以管理项目、可以查看小标题；维护本地文件，上云需要其他手段；收费使用。性能在字数达到一定程度后很卡。
+ 有道云笔记：免费，自动上云；编辑模式有即时渲染和双屏，体感一般。文件不能源码导出。
+ VSCode结合插件：只能双屏编辑，但是VSCode编辑能力极强；能看大纲；维护本地文件，上云需要其他手段。
+ Obsidian：即时渲染效果略逊于Typora，可同时查看目录和大纲，维护本地项目，可通过插件上云，免费且全平台支持，插件丰富。性能目前还未遇到性能问题。
+ Notion：不了解。

最后我选择是用Obsidian维护笔记项目，其他Markdown文件使用VSCode作为副驾驶
>没有选择VSCode做主力的原因是，想象一下，项目结构、源码、渲染结果、大纲同时出现屏幕上得多挤，所以还是得要即时渲染。

## Typora

Obsidian之于Typora，就像VSCode之于Jetbrains：后者在提供功能的同时也带来了“抽象成本”。 
## Obsidian

下面讨论我从Typora转向Obsidian的心路历程

+ Typora的即时渲染做的很好，对Makedown本身的语法补全非常到位，而这方面Obsidian略有差距
	+ Makedown：基本语法补全基本一致
	+ Table：Obsidian需要插件，对快捷键自定义化更高但也意味着更高的心智负担，且体验不如Typora
	+ LaTeX：语法更严格
		+ Tikz：Obsidian可以通过插件支持而Typora不支持
	+ 代码graph：Obsidian更好看
	+ 代码块：
		+ 列表：Typora在改变代码块的列表从时自动对齐代码，Obdian在不使用插件时不行
	+ 使用模式：Typora更多的是单文件（其实也能维护目录），而Obsidian则是完全以项目为中心

+ Obsidian优势：
	+ 更完善的文档、更活跃的社区
	+ 全平台且开源
	+ LaTeX通过插件可支持LaTeX的Tikz
	+ 使用插件可比较方便的通过Github实现多机同步
	+ 双链，想象一下，笔记可以像IDE的`Ctrl + Click`一样跳转（我本人不用，因为这算是Markdown方言）
	+ 体感上感觉性能Obsidian比Typora强
	+ Obsidian可以实现同时查看目录和大纲
	+ Obsidian可能自动维护项目内的内链，比如我想笔记项目，内部肯定有相互引用，这时如果修改某个文件名，对其相关的链接也会自动修改

+ Obsidian缺点（至少对我来说）：
	+ 性能很怪，当一个文章的链接（就是普通的外链）很多时，即时渲染会出现bug（方向键无效，不能渲染）
	+ 既然选择以项目为中心，为什么不能提供右键打开当前目录的选项？后面也能理解了，谁tm有那么多笔记项目？
	+ 一个插件往往提供大量的功能，同时提供了对这些功能的快捷键自定义，需要打磨出自己一套操作，可选项太多了很容易冲突。

+ 插件推荐
    + Obsidian Git：多机同步必备，取消所有快捷键，因为核心功能主要有三个（如果熟悉Git的话）：add + commit、push、pull。而Obsidian也有类似VSCode的命令行模式（快捷键`Ctrl + p`或者`Command + p`），输出前缀`git`即有上面提到的几个选项，甚至在PC上，我都是命令行手动管理。
    + Advanced Tabled：Markdown表格相关补全，它存在大量的自定义，抽象程度低就意味着复杂，索性它提供了图形化的操作，鉴于表格用的本来就不多。我干脆没有设计快捷键。

## VSCode

# 应用场景

## LaTeX

+ 在线：比较有名的一款是overleaf，我个人使用的是[texpage](https://www.texpage.com/)，原因在于某些模板在overleaf如果有中文则格式不符合预期，后面本地环境跑起来之后一直使用本地。下面详细讲本地。

==Tex Live by Scoop and VSCode in Windows==

+ 编译工具：软件包Tex Live，包含一款LaTeX编辑器XeLaTeX，而且我使用Scoop进行安装（[我的Scoop教程](./WindowsConfigGuide.md#6包管理器scoop)）
	>LaTeX的编译工具有很多，宛如古神的低语，我个人将下面这个跑的通的方案作为黑盒，慢慢了解全貌。

	```powershell
	scoop bucket add scoopet https://github.com/ivaquero/scoopet
	scoop install texlive  # 需要较长时间
	```

	+ 设置环境变量，这应该是Scoop的问题，它设置的相关环境变量不全，在我的机器上，还需要将`...\Scoop\apps\texlive\current\bin\windows`手动设置环境变量，在该路径下才是Tex Live软件包中各种可执行文件的路径，设置后可以通过`xelatex --version`检测。
	+ LaTeX的包管理器是tlmgr，其依赖脚本perl，tlmgr已经包含在Tex Live软件包中，而tlmgr也内置了perl，不需要单独下载（其他教程可能会说单独下载），问题出现在perl在Windows中可能出现报错

		```
		Locale 'Chinese (Simplified)_China.936' is unsupported, and may crash the interpreter.
		```

		其原因是Windows非常经典的编码问题，关于这个问题在[Windows编码问题](./WindowsConfigGuide.md#win-code)

	+ 包管理tlmgr配置：

		```powershell
		tlmgr update --self  # 升级自身
		tlmgr update --all  # 升级所有包
		tlmgr list --only-installed  # 列出已安装包
		```

	+ 常见包安装

		```powershell
		tlmgr install ctex ctexrep latexmk  # 中文支持
		tlmgr install mhchem chemfig circuitikz  # 化学 & 电子
		tlmgr install multirow ifoddpage relsize titlesec  # 排版
		tlmgr install epstopdf subfigure appendix  # 图表
		tlmgr install ulem xcolor environ letltxmacro enumitem stringenc trimspaces soul algorithm2e genmisc  # 字符 & 字体
		tlmgr install cleveref titling placeins minted tocloft biblatex biber  # 其他, 主要是我校毕业论文模板的依赖包
		tlmgr install latexindent  # 格式化工具
		```

		面对一个模板的报错，可以尝试从是否缺乏某个依赖包的角度考虑（通过看log）

+ 编辑环境：个人使用VSCode，插件推荐和配置如下：

	+ 核心插件：LaTeX Workshop
		+ 我个人使用的配置在[这里](https://github.com/zweix123/zstu-graduation-thesis-latex-template/blob/master/.vscode/settings.json)，其他教程通常将该配置作为全局配置，出于最小化全局状态原则，我个人使用将配置放在项目下。
		+ 使用：一个项目就是一个模板和文章，在任意`.tex`保存时即可触发插件生成pdf。

+ 其他：
	+ [`.gitignore`](https://github.com/zweix123/zstu-graduation-thesis-latex-template/blob/master/.gitignore)


## Mind-Map

我在最开始是使用思维导图记笔记的，直到现在我也觉得树形结构是比流式结构更好的笔记结构，此时随机选择了[Xmind8](https://xmind.cn/download/xmind8/)（是8而不是最新版，这个可能不是最好看的，但是我觉得是操作最合理高效的）。随机笔记规模的扩大就有了渲染性能和文件管理的问题，这个时候使用Markdown；此时思维导图这个形式只是偶尔使用，最后发现没必要在为这偶尔使用的需求留着一个软件了，换到[markmap](https://markmap.js.org/)框架（有VSCode插件Markmap）

## Slide

>我书写本文的发心是如何制作像[南大蒋炎岩老师那样的](http://jyywiki.cn/OS/2022/slides/1.slides.html#/)运行于Web的幻灯片，而不是微软的能量点，后又接触到PDF全屏播放的效果也类似幻灯片，如果可以导出成PDF那也可以作为一种幻灯片

+ 目前幻灯片种类有三种：
	+ 图形化的幻灯片，以微软的能量点为代表
	+ 基于Web的幻灯片，以[Reveal.js](https://revealjs.com/)为大爹
	+ 必须导出成pdf使用的幻灯片，基本指LaTeX包[Beamer](https://www.overleaf.com/learn/latex/Beamer)

这里
+ 微软的能量点，相对来说更被大众熟知，PPT几乎成了幻灯片的代名词，我没有选择它的原因可以从Markdown的设计出发，能量点提供了大量的功能，这意味着想掌握这些功能需要更高的学习成本，实际上我们大部分场景根本用不到这么多功能，能不能调节下抽象程度。
+ Bearmer：感兴趣的同学可以了解下，相信你一定看过由它制作的幻灯片，但是LaTeX谁爱用谁用。
+ Web幻灯片：  
	下面的讨论对标Reveal.js，基于Web，兼容Markdwon，支持水平和垂直幻灯片，支持代码特定行高亮，其他
	+ Reveal.js，学习难度大
	+ reveal-md：Reveal.js的前端，该有的功能都有，但是想要调教出一个非常适合自己的主题仍然困难
	+ [Slidev](https://sli.dev/)：对主题的定制较于reveal-md更好（大概），但是不支持水平幻灯片
	+ 其他：
		+ VSCode插件Markdown Perview Enhanced提供Markdown方言实现幻灯片：功能单一
		+ Obsidian自带幻灯片插件提供通过`---`划分幻灯片：功能仅此而已
		+ Obsidian第三方插件Advanced Slides据说对标Reveal.js，但是没有官方支持（[这里](https://forum.obsidian.md/t/advanced-slides-create-markdown-based-reveal-js-presentations-in-obsidian/28243/200)）
---
我们发现并没有一款完美的框架，于是我准备自己开发，具体看[项目](https://github.com/zweix123/jyyslide-md)。  

+ 使用**简单**Markdown方言，设计过程严格按照奥卡姆剃刀，尽可能保证功能和语法的简单。
+ 基于Web，兼容Markdwon，支持水平和垂直幻灯片，不支持代码特定行高亮，支持依次出现，支持渐变动画。
+ **蒋炎岩风格**，实际上，本框架完全可以制作和蒋老师一摸一样的。
