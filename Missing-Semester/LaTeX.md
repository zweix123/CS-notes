+ Ref：
	+ [知乎 · 槿灵兮 · 【LaTeX】针对萌新自学者的入门教程](https://zhuanlan.zhihu.com/p/521649367?utm_source=zhihu)
	+ [LaTeX 入门与进阶](https://latex.lierhua.top/zh/)

## 环境

+ 在线：比较有名的一款是overleaf，我个人使用的是[texpage](https://www.texpage.com/)，原因在于某些模板在overleaf如果有中文则格式不符合预期，后面本地环境跑起来之后一直使用本地。下面详细讲本地。

Tex Live by Scoop and VSCode in Windows

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

		其原因是Windows非常经典的编码问题，解决方案是：控制面板 -> 时钟和区域 -> 区域 -> 管理 -> 更改系统区域设置 -> 打开Beta版。

	>实际上在Windows上如果这个不开，在编码过程肯定也会出现其他问题。

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
