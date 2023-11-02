我个人对Markdown的理解是把它当作Word的一种“受限”的实现，因为Word在提供丰富功能的同时以带来了极高的学习成本，依照奥卡姆剃刀原理，Markdown简单易用、功能小但足够。而且Markdown到HTML的转换非常自然容易。

- [语法学习](#语法学习)
- [Editor](#editor)
	- [Obsidian](#obsidian)
- [导出](#导出)
	- [导出成PDF](#导出成pdf)
	- [导出成HTML](#导出成html)
- [奇技淫巧](#奇技淫巧)
	- [用Markdown写论文](#用markdown写论文)
	- [用Markdown写幻灯片](#用markdown写幻灯片)

# 语法学习
个人建议Markdown语法/Markdown方言/LaTeX简单语法/Markdown内置graph语法都不需要刻意记忆：全面浏览、随用随查最好。

# Editor

+ 考虑角度：
	+ 编辑模式：Markdown的主要编辑模式有
		+ 即时渲染，即对应的格式不显示源码，直接是渲染后的效果  
		+ 分屏浏览，一边的源码、一边是渲染后的结果
	+ Markdown方言：有些Markdown编辑器还提供“Markdown方言”。比如Typora的`[TCO]`生成目录、Obsidian的内部链接`[[]]`，这些确实扩大了Markdown的功能，但是如果这些功能并不是所有编辑器都提供的话，意味着我们的笔记在迁移时要付出更大的成本，我个人选择都不使用，只使用最严格的语法。
	+ 是否多平台支持
	+ 能否源码导出
	+ 能否多机同步
	+ 个人习惯
	+ 是否付费

每种编辑器各有优缺点，我的选择是按照自己的习惯选择的，下面描述一下心路历程，请读者结合各编辑器特点自行选择

+ Typora：即时渲染能力极强，在其加持下，甚至感觉不到Markdown语法；可以管理项目、可以查看小标题（两者只能同时看到一个）；维护本地文件，上云需要其他手段；收费使用。
+ 有道云笔记：免费，自动上云；编辑模式有即时渲染和双屏，体感一般。文件不能源码导出。
+ VSCode结合插件(Markdown Preview Enhanced、Markdown All in One)：只能双屏编辑，但是VSCode编辑能力极强；能看大纲；维护本地文件，上云需要其他手段。
+ Obsidian：即时渲染能力略逊于Typora，可同时查看目录和大纲，维护本地项目，可通过插件上云，免费且全平台支持，插件丰富。
+ Notion：不了解。

最后我选择是用Obsidian维护笔记项目，其他Markdown文件使用VSCode作为副驾驶
>没有选择VSCode做主力的原因是，想象一下，项目结构、源码、渲染结果、大纲同时出现屏幕上得多挤，所以还是得要即时渲染。

## Obsidian
Obsidian之于Typora，就像VSCode之于Jetbrains：后者在提供功能的同时也带来了“抽象成本”。  
下面讨论我从Typora转向Obsidian的心路历程

+ Typora的即时渲染做的很好，对Makedown本身的语法补全非常到位，而这方面Obsidian略有差距
	+ Makedown：基本语法补全基本一致
	+ Table：Obsidian需要插件，对快捷键自定义化更高但也意味着更高的心智负担，且体验不如Typora
	+ LaTeX：语法更严格
		+ Tikz：Obsidian可以通过插件支持而Typora不支持
	+ \`\`\`graph：Obsidian更好看
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
	+ 如果用Git维护内容和格式（`.obsidian/`），这个文件`.obsidian/workspace.json`变化频繁，很容易冲突，后来我直接把它gitignore了

# 导出

## 导出成PDF

## 导出成HTML

# 奇技淫巧

## 用Markdown写论文

## 用Markdown写幻灯片

见我的[讨论](./slide.md)