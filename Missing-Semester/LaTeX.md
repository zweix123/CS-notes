+ 在线：比较有名的一款在线编辑器是overleaf，我个人使用的是[texpage](https://www.texpage.com/)，原因在于某些模板在overleaf上中文显示不正常
+ 本地：
	+ 编译器：LaTeX的编译器有很多，我本人也没完整理清，一个跑的通的方案是使用软件包Tex Live，里面包含一款编译器XeLaTeX，同时我使用Scoop进行安装
		```powershell
		scoop bucket add scoopet https://github.com/ivaquero/scoopet
		scoop install texlive  # 需要时间较长
		# 其他教程可能要求下载perl，它是LaTeX的包管理tlmgr的依赖，但是在texlive中的tlmgr已经内置了perl
		# tlmgr也包含在texlive中了
		# scoop install latexindent  # 暂时不知道功能
		```
		+ 配置：首先是上面提到LaTeX的包管理tlmgr依赖perl，而perl在Windows中可能出现报错
			```powershell
			Locale 'Chinese (Simplified)_China.936' is unsupported, and may crash the interpreter.
			```
			解决方案是在Windows10上使用Beta的编码，具体操作见

		+ 包管理配置
			```
			# 升级自身
			tlmgr update --self
			# 升级所有包
			tlmgr update --all
			# 列出已安装包
			tlmgr list --only-installed
			```
		+ 推荐包
		```
		# 中文支持
		tlmgr install ctex latexmk
		# 化学 & 电子
		tlmgr install mhchem chemfig circuitikz
		# 排版
		tlmgr install multirow ifoddpage relsize titlesec
		# 图表
		tlmgr install epstopdf subfigure appendix
		# 字符 & 字体
		tlmgr install ulem xcolor environ letltxmacro enumitem stringenc trimspaces soul algorithm2e genmisc
		```

	+ 编辑器：个人使用VSCode，插件推荐和配置如下
