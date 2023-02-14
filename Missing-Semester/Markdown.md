我个人使用Markdown的原因是，对于word，它的功能非常之多，对应着的，想要自如的使用这些功能需要很高的学习成本，实际上在大部分场景下并不需要这些功能，Markdown其实就是提供一些“受限”的功能，功能受限、意味着学习成本更低。除此之外Markdown还可以一对一转换成HTML，将笔记转换成网页更有利于其传播。

# 语法
无论是Markdown的语法还是Markdown的方言还是LaTeX简单语法还是Markdown内置的graph语法千万不要记笔记，全面浏览、之后多用、随用随查是最好的。

# Editor

+ 考虑角度：
	+ 编辑模式：Markdown的主要编辑模式有即时渲染，即对应的格式不显示源码，直接是渲染后的效果；或者是分屏浏览，一边的源码、一边是渲染后的结果
	+ Markdown方言：有些Markdown编辑器还提供“Markdown方言”。比如Typora的`[TCO]`生成目录、Obsidian的内部链接`[[]]`，这些确实扩大了Markdown的功能，但是如果这些功能并不是所有编辑器都提供的话，意味着我们的笔记没有更强的鲁棒性，比如我的笔记有些功能如果不能在Github上渲染，那么在给其他人看的时候就影响体验
	+ 一款软件还要考虑其对平台的支持和收费情况。
	+ 笔记能否源码导出。
	+ 笔记能否多机管理。
	+ 个人习惯

每种编辑器各有优缺点，我的选择是按照自己的习惯选择的，下面描述一下心路历程，请读者结合各编辑器特点自行选择

+ Typora：即时渲染能力极强，在其加持下，甚至感觉不到Markdown语法；可以管理项目、可以查看小标题（两者只能同时看到一个）；维护本地文件，上云需要其他手段；收费使用。
+ 有道云笔记：免费，自动上云；编辑模式有即时渲染和双屏，体感一般。文件不能源码导出。
+ VSCode结合插件（Markdown Preview Enhanced、Markdown All in One）：只能双屏编辑，但是VSCode编辑能力极强；似乎不能看小标题；维护本地文件，上云需要其他手段。
+ Obsidian：即使渲染能力略逊于Typora，可以同时查看项目和小标题，维护本地项目，可通过插件上云，免费且全平台支持，具有丰富的插件！
+ Notion：不了解。

最后我选择主要使用Obsidian，单文件使用VSCode

## Obsidian

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

+ 使用：
	+ [win下安装和插件推荐](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/win10%E5%BC%80%E5%8F%91%E6%9C%BA%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97.md#4%E7%AC%94%E8%AE%B0%E8%BD%AF%E4%BB%B6obsidian)
	+ [linux下安装](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/Linux%E6%9C%BA%E5%99%A8%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97.md#obsidian)

+ Obsidian缺点（至少对我来说）：
	+ 既然选择以项目为中，为什么不能提供右键打开当前目录的选项？

# 导出

## 导出成PDF

## 导出成HTML