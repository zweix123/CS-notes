>本文讨论的是像[南大蒋炎岩老师那样](http://jyywiki.cn/OS/2022/slides/1.slides#/)运行于Web的幻灯片，而不是微软的能量点

|               abstraction               |     简介      |            难度            |   效果   |           特点           |                                                                  缺点                                                                  |
|:---------------------------------------:|:-------------:|:--------------------------:|:--------:|:------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------:|
|                Reveal.js                |     框架      |                            | 同蒋老师 |         效果极佳         |                                                           需要较多的前端知识                                                           |
|                reveal-md                | reveal的前端  |      使用Markdown方言      | 近reveal |         可转ppt          |                                                                                                                                        |
|                 slidev                  |     软件      |   前端知识和Mardown方言    |          |         功能完善         |                                                              无垂直幻灯片                                                              |
| VSCode插件<br>Markdown Preview Enhanced |               | Markdown方言（不同于上面） | 中规中矩 | VSCode具有极强的编辑能力 |                                                                                                                                        |
|             Obsidan核心插件             |               |                            | 只能分片 |                          |                                                                                                                                        |
|  Obsidian第三方插件<br>Advanced Slides  | 对标Reveal.js |                            |          |                          | 被官方干了^[1 [网址](https://forum.obsidian.md/t/advanced-slides-create-markdown-based-reveal-js-presentations-in-obsidian/28243/200)] |

我选的的方案是VSCode编辑+reveal-md库（注意VSCode插件和reveal-md的Markdown方案并不同，这里不是利用VSCode的渲染插件，而是利用其编辑功能）

# Build

+ VSCode插件：
	+ Markdown Preview Enhanced：即上面讨论的插件，用于局部渲染查看
	+ Markdown All in One：语法补全
+ reveal-md（[Manual](https://github.com/webpro/reveal-md)）：一切尽在Manual中
	```bash
	npm install -g reveal-md
	```

# Use
```bash
reveal-md slides.md -w --theme white --gighlight-theme github
```
# Grammer

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

+ 其他语法同Mardown

---


+ 其他属性
	```
	<!-- .slide: data-background="./image1.png" -->
	```