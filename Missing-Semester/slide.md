>本文讨论的是制作像[南大蒋炎岩老师那样的](http://jyywiki.cn/OS/2022/slides/1.slides#/)运行于Web的幻灯片，而不是微软的力量点

+ Reveal.js：一款Web幻灯片演示框架，功能最全、学习难度最大
	+ reveal-md：一款Reveal.js的前端，使用Markdown方言实现接近Reveal.js的效果
+ + Slidev：一款软件用于制作Web幻灯片
+ VSCode插件Markdown Perview Enhanced提供Markdown方言实现幻灯片
+ Obsidian自带幻灯片插件提供通过`---`划分幻灯片（仅此而已）
+ Obsidian第三方插件Advanced Slides据说对标Reveal.js，但是没有官方支持^[1 [网址](https://forum.obsidian.md/t/advanced-slides-create-markdown-based-reveal-js-presentations-in-obsidian/28243/200)]

这里所提到的Markdown方案各家类似但不同

reveal相关支持垂直幻灯片和代码特定行高亮  
slidev不支持垂直幻灯片但是支持代码特定行高亮

---

我开发了一款相当于Reveal.js的前端框架，主要是使用我的Markdown方言将Markdown文件转换成一个html文件，其幻灯片风格是蒋老师那种（实际上格式代码就是cppy的老师），具体见项目[仓库](https://github.com/zweix123/jyyslide-md)