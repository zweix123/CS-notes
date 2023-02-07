本文主要讨论以reveal.js为中心的内容和样式分离的slide，即不包括微软的PowerPoint

+ reveal.js是node.js的一个包，是一个使用HTML制作演讲文稿的框架
+ reveal-md是node.js的一个包，是一个将Makedown文件转换成reveal.js的工具
+ slidev是node.js的一个包，是一个使用Makedown制作演讲文稿的框架
+ Obsidian插件Advanced-Slides，是一个让Obdian支持reveal.js的插件，目前还有bug
	+ 其实Obsidian默认自带一个slide插件，但是提供的功能太少了。

最后选择使用slidev（[dov_cn](https://cn.sli.dev/guide/why.html)）

0. 安装Scoop
1. 使用Scoop安装node.js（命令`npm`）
	```bash
	scoop install nodejs
	```
+ 不显式安装slidev
2. 初始化一个slidev项目（node.js自动下载slidev）：
	```bash
	npm init slidev
	```
	1. 进入命令行交互，设置
		+ 项目名
		+ ~~包名~~
		+ Markdown文件名（默认slidev.md）建议使用默认名
	1. 设置完成后弹出网址（本地地址开放3030端口）
3. 再次运行项目：进入项目目录
	```bash
	slidev --open
	```
	已经全局安装了slidev，可以将其作为一个命令使用
之后初始化一个slidev项目同样上面的流程