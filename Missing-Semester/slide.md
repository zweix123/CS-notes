Updata in 2023.01.13，我会考虑开发一款类似的框架，敬请期待


>本文讨论的是制作像[南大蒋炎岩老师那样的](http://jyywiki.cn/OS/2022/slides/1.slides#/)运行于Web的幻灯片，而不是微软的力量点

|                                     |                   简介                   |           优点           |       缺点       |
|:-----------------------------------:|:----------------------------------------:|:------------------------:|:----------------:|
|              Reveal.js              |            网页幻灯片演示框架            |         效果最好         |    学习难度大    |
|              reveal-md              | reveal的前端，使用前端知识和Markdown方言 |   接近reveal，可转ppt    |                  |
|               slidev                |     软件，使用前端知识和Mardown方言      |         功能完善         |   无垂直幻灯片   |
| VSCode插件Markdown Preview Enhanced |        使用前端知识和Markdown方言        | VSCode具有极强的编辑能力 |                  |
|           Obsidan核心插件           |       使用唯一的Markdown方言`---`        |                          | 只有“水平”幻灯片 |
|  Obsidian第三方插件Advanced Slides  |              对标Reveal.js               |                          |   没有官方支持^[1 [网址](https://forum.obsidian.md/t/advanced-slides-create-markdown-based-reveal-js-presentations-in-obsidian/28243/200)]   |
>我猜测蒋炎岩老师的方案是reveal-md

我选的的方案是VSCode编辑+reveal-md库（注意VSCode插件和reveal-md的Markdown方言并不同，这里不是利用VSCode的渲染插件，而是利用其编辑功能）

# 资料
+ [Manual](https://github.com/webpro/reveal-md)：一切尽在Manual中
+ 我的reveal-md项目模板（[github地址](https://github.com/zweix123/code-tutor)）

# Build

+ VSCode插件：
	+ Markdown Preview Enhanced：即上面讨论的插件，用于局部渲染查看
	+ Markdown All in One：Manual语法补全
+ reveal-md：  
	```
npm install -g reveal-md
	```

# Use

```bash
reveal-md slides.md -w --theme white --highlight-theme github
```

# Grammer

## Markdown方言

+ `\n---\n`水平幻灯片
	`\n----\n`水平幻灯片

+ 代码特定行高亮：
	```
	\`\`\`c++ [1 | 2-3 | 4]
	int main() {
		int a = 1, b = 2;
		cout << a + b << endl;
	}
	\`\`\`
	```

+ 其他属性  
	背景
	```
	<!-- .slide: data-background="./image1.png" -->
	```
	逐条演示：[教程](https://blog.csdn.net/qq_45682183/article/details/127032676)

+ 其他语法同Mardown
