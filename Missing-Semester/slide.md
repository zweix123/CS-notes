>我书写本文的发心是如何制作像[南大蒋炎岩老师那样的](http://jyywiki.cn/OS/2022/slides/1.slides#/)运行于Web的幻灯片，而不是微软的能量点，后又接触到PDF全屏播放的效果也类似幻灯片，如果可以导出成PDF那也可以作为一种幻灯片

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