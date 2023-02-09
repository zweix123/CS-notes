

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

+ 其他Makedown编辑器：
	+ Typora收费
	+ VSCdoe看个人爱好
	+ 有道云笔记文件不能源文件导出

	其他不了解

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
