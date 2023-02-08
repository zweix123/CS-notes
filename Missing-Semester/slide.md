+ 说在前面：
	+ 本文主要讨论以reveal.js为中心的内容和样式分离的slide，即不是微软的PowerPoint
	+ 本文没有关于node.js的用法，不过我在使用slidev之前也没有用过，照猫画虎即可

+ reveal.js是node.js的一个包，是一个使用HTML制作演讲文稿的框架
+ reveal-md是node.js的一个包，是一个将Makedown文件转换成reveal.js的工具
+ slidev是node.js的一个包，是一个使用Makedown制作演讲文稿的框架
+ Obsidian插件Advanced-Slides，是一个让Obdian支持reveal.js的插件，目前还有bug
	+ 其实Obsidian默认自带一个slide插件，但只提供最基本的功能

最后选择使用slidev（[dov_cn](https://cn.sli.dev/guide/why.html)）

### 安装

+ win10下载node.js的[教程](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/win10%E5%BC%80%E5%8F%91%E6%9C%BA%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97.md#nodejs)

### 使用

>个人没有使用Manual中的手动安全和全局安装，前者还需要自己配置，后者不想让slidev命令污染电脑

1. 初始化一个slidev项目
	```bash
	npm init slidev
	```
	1. 进入命令行交互，设置
		+ 项目名
		+ ~~包名~~
		+ Markdown文件名，默认使用`slidev.md`，建议使用默认名
	2. 选择是否立刻运行：一定选择是
	3. 选择引擎：npm
	4. 设置完成后弹出网址
2. 重启项目（在项目目录下执行）：
	```bash
	npm run dev
	```

#### 部分Manual

+ 默认初始化，一个项目维护一个幻灯片，如果为一门课准备幻灯片肯定是很多了，难道用好几个项目维护嘛？肯定不用，看[Menual](https://cn.sli.dev/guide/install.html#slidev-entry)，如果我在项目下维护一个子目录`slides`，即通过`npm run dev \slides\...md`指定md播放（为什么前缀是`npn run dev`？因为slidev这个包没有下载全局，只能通过npm运行，项目下有文件`package.json`，其中指出命令`dev`相当于`slidev --open`）


### 文法

