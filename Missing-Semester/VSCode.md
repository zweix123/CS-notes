+ Ref：
	+ [Bilibili · 等疾风 · 【VS Code】四年功力 一刻掌握 速通C++插件/终端美化/工程管理 懒人必备](https://www.bilibili.com/video/BV1YG4y1v7uB/?vd_source=4ee99d4ebd507c7277fa312ed28dbdda)

调教一套适合自己的工作流的收益是不错的，一个程序员的工作流核心就是开发环境——编辑器。

+ 关于主力编辑器的选择：我个人是这样的，如果一个新的工作流被验证效率优于目前使用的工作流，我是可以不顾任何学习成本迁移过去的，比如从输入法从全拼到双拼的转移。
	+ VSCode和vim的选择，我相信上限vim是优于VSCode的，但是基于Ctrl作为leaderkey的操作模式在各个软件都深入人心了，不能保证所有常用的软件都支持vim模式，最后还是选择VSCode。但vim还是我们的老前辈，对于某些vim下很好的操作模式积极寻找VSCode的等价操作。

## Install

官网下载安装包安装

+ 在Mac中，安装包的格式是`dmg`文件，然后点击会要求一个拖动的动作，即在路径`/Applications`下创建对应的`.app`文件（本质是目录），但是VSCode在点击之后直接在当前目录创建，需要手动移入到正确的路径中；所以建议将dmg文件先放在Application下再点击。

## Use

[Keyboard](Missing-Semester/Keyboard.md#VSCode)

## Config

+ Settings：VSCode的配置分三个层级：默认 -> 用户 -> 工作区，同一项配置后者覆盖前者：快捷键`Ctrl + ,`或者命令`open settings`

	聊到配置就要聊到`.vscode`目录，这里聊一下该目录和插件无关的文件

	+ `settings.json`：即上面提到工作区范围的配置文件，这里聊一下常用的一些配置项，本文其他部分对于各个话题也会提到相关配置项
		+ `explorer.sortOrder`：资源管理器文件排序关键字
	+ `extensions.json`：项目下插件过滤

+ 在Mac中，由于是移动`.app`文件到`/Applications`目录下，`PATH`下没有`code`这个命令，需要在Shell的rc文件中添加
  ```bash
  export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
  ```

+ 设置同步：UI左下角齿轮图标中的`Settings Sync is On`，自动同步。
+ 关闭受限模式：打开设置，键入`trust`

	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/vscode受限模式关闭.png" style="zoom:59%;" div align=center />

+ 主题（背景颜色、字体颜色等等）：插件`One Dark Pro`和插件`Atom One Dark Theme`
	>One Dark主题的优点：养眼
	>>我真的使用过很多主题，但是用过One Dark后总感觉其他主题更刺眼，我将还要终端、vim也统一成One Dark风格（无了，没必要，就VSCode的One Dark主题效果最好）

+ 文件图标：插件`vscode-icons`

+ 字体：
	+ 编辑器字体：打开设置，键入`Editor Font Family`  
		>需要插件`FiraCode font - Professional Font for Developers`

		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/编辑器字体.png" style="zoom:60%;" div align=center />

	+ 终端字体：打开设置，键入`Terminal Font Family`  
		>需要你已经按照[Shell的配置](./TerminalConfigGuide.md#font-download)下载了对应字体

		<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/终端字体.png" style="zoom:57.5%;" div align=center />
		
+ 括号连线：打开设置，键入`bracket`，找到对应位置选择true  

	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/branket.png" style="zoom:60%;" div align=center />

+ 柔顺：  
	打开设置，键入`smooth`，选择下面三个选项  

	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/smooth.png" style="zoom:79%;" div align=center />  

	打开设置，键入`cursor` ，将下面设置为smooth  

	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/cursor smooth.png" style="zoom:75%;" div align=center />  

+ 补全建议：打开设置，键入`preview`，选择下面的选项  

	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/suggest perview.png" style="zoom:64%;" div align=center />

+ 行字数提醒：
	```json
	"editor.rulers": [ 80, 120 ],
    // "workbench.colorCustomizations": {
    //     "editorRuler.foreground": "#ff4081"
    // }
	```

## Plugin
>Config步骤中提到的插件不在这里汇总，各个语言开发的插件不在这里汇总。

+ 远程开发
	+ `Remote-SSH`：远程开发必备
	+ `Docker`：Docker开发必备，使用体验和Remote类似

	插件是有本地的远程的概念的，当使用远程开发时，记得一些插件需要在两端都下载。

## Code

+ VSCode较于JB家的IDE值得说的优点就是远程开发功能了，我们假设你本机是win，无论是那么当你需要Linux环境（无论时WSL、服务器还是虚拟机）时，都推荐使用SSH（服务器肯定是SSH，WSL我个人没有用过，虚拟机虽然相当于完整机器但是仍然建议通过SSH过去开发），而VSCode的Remote插件可以达到一个很自然的开发流程和体验。

### Python

+ 依赖环境：
	+ win：通过Scoop下载Python（Python3）
+ 插件推荐：
	+ Python和Python Extension Pack（它们依赖很多插件，会自动下载很多，所以下面只说它不会自动下载的）
	+ Mypy Type Checker：类型检查

+ 配置：
	```json
	{
	    "[python]": {
	        "editor.defaultFormatter": "ms-python.black-formatter",  // 默认格式化工具
	        "editor.formatOnSave": true,  // 保存时格式化
	        "editor.codeActionsOnSave": {
	            "source.organizeImports": true  // 保存时重排import语句
	        },
	    },
	     "mypy-type-checker.args": [  // mypy类型检查
	         "--check-untyped-defs",  // 检查类型时也要检查未标记类型的函数和方法
	    ],
	    // black不能重排import语句，因为这会修改代码的AST，所以重载import语句使用的是isort插件，这里配置表示isort使用black的配置
	    "isort.args": [
	        "--profile",
	        "black"
	    ],
	}
	```

	功能包括代码格式化、`import`语句的重排和去重、静态类型检查

	+ 格式化：使用`black`
		+ 跳过格式化的标记：
			+ 单行：`# fmt: skip`
			+ 多行：`# fmt: off`和`# fmt: on`

	+ 静态检查：需要保存文件
		+ 忽略某行的静态检查：`# type: ignore`
		+ 对于普通类型的静态检查：`# type: 类型`

	+ Import Re-Sort：[VSCode 相关 Manual](https://code.visualstudio.com/docs/python/editing#_sort-imports) | [black 相关 issue](https://github.com/psf/black/issues/333)  
		我个人的理解是关于import语句的重排和去重和black的功能有冲突，在实现上我们发现前者操作会影响代码AST，这似乎和black的架构有关系，我的解决方案体现在配置中

+ 对第三方库的引入补全：[一个回答](https://blog.csdn.net/weixin_38165206/article/details/102903066)

+ 块执行`Python: Run Selection`：选择代码后使用快捷键`Shift + Ehter`会将这部分代码发送到Python Shell中，很容易误触，我取消了这个快捷键
+ 使用`#%%`可类似Jupyter分块，而Jupyter状态下有很多快捷键

+ `Intellicode Api Examples › Python: Enabled`：关闭，暂时不知道为什么TODO

### C/C++

>得益于Scoop，我们在win下也有了好用的包管理器，所以我们在win下的开发体验已经和linux下类似，区别只在需要系统调用或者依赖软件不能跨平台时，所以下面的配置应该是跨平台的。

+ 虽然但是，还是推荐这个视频 [Bilibili · 等疾风 · 【VS Code】四年功力 一刻掌握 速通C++插件/终端美化/工程管理 懒人必备](https://www.bilibili.com/video/BV1YG4y1v7uB/?vd_source=4ee99d4ebd507c7277fa312ed28dbdda)

+ 环境依赖：
	+ 构建工具：`make`、`cmake`
	+ 编译工具：
		+ GNU：`gcc`、`g++`
		+ LLVM：`clangd`、`clangd`、`clang-format`
			+ `clangd`建议使用[VSCode clangd manual](https://clangd.llvm.org/installation.html)的方法下载
	+ 调试工具：
		+ GNU：`gdb`
		+ LLVM：`lldb`

+ 插件：
	+ `g++`：`C/C++`、`C/C++ Extension Pack`
		+ 对应配置文件为`./.vscode/c_cpp_properties.json`
	+ `clang`：`clangd`、`Clang-Format`、`CodeLLDB`

	两插件冲突，这部分使用clangd的，将下面三个属性设置为`Disabled`
	```
	Intelli Sense Engine
	Autocomplete
	Error Squiggles
	```

+ 文件`compile_commands.json`：`clangd`的名称跳转需要通过这个文件，该文件通常由`cmake`生成（在Linux下也有命令`bear`可生成），但是cmake生成的文件通常在构建目录下（通常命名为`build`），需要额外设置，因为`clangd`默认是从项目根目录找。

	关键字`clangd.arguments`，添加`--compile-commands-dir=build`

	+ 还有其他参数
		```json
		"clangd.arguments": [
			// "--query-driver=clang",
			"--completion-style=detailed",  // 提示风格
			"--header-insertion=never",  // 不自动添加头文件
			"--clang-tidy",  // 启用tidy，但是只要项目下有.tidy文件基本都会启用
		],
		// 疑似如果项目没有构建文件时头文件的查找路径, 个人没有使用过
		// "clangd.fallbackFlags": [
		// 	"-I头文件路径"
		// ],
		```
 
+ cmake有代码`target_compile_options(... "-Werror" ...)`，这里表示把warning当error，这在某些项目中可能出现有很多的warning，但是项目可运行，但是在clangd这里，把warning当error了，如果文件大起来，前的的error太多了，会导致它不在处理后面的代码。而官方的`C/C++`插件似乎不受这影响。我是开发时把这个参数注释掉，修改后记得重新生成compile_commands.json文件。

+ cmake tool：该插件集成构建、编译、调试和测试，一般情况仅用该插件即可满足需求，两种用法
	1. 底部状态栏有相关对应的按钮
	2. 左端状态栏有CMake可实现同样的功能（可能不可见，右键找到CMake打勾）

	在该插件某个版本前后，提供对上面两种用法更定制化的选项，详情可见选项`cmake.options.statusBarVisibility`

	+ CMake自动执行，当项目下有CMakeLists.txt文件时，默认状态下，打开VSCode、保存CMakeLists.txt和kit or the configuration preset is changed时都会默认执行，这里取消，通过命令`cmake debug`手动执行。

+ debug：对于特定的项目或者单文件，cmake tool不可用，此时只能返璞归真
	1. `./vscode/tasks.json`：构建/编译任务，在这里配置如何编译出可执行文件
	2. `./vscode/launch.json`：启动调试，在这里配置如何启动调试器

	+ 你可能需要：
		+ VSCode有很多内置的变量，这里有[所有的变量](https://code.visualstudio.com/docs/editor/variables-reference)

### Golang

微软[教程](https://learn.microsoft.com/zh-cn/azure/developer/go/configure-visual-studio-code)已经足够亲爹

+ how to debug: [tutor](https://www.digitalocean.com/community/tutorials/debugging-go-code-with-visual-studio-code)

### Web

+ 插件：
	+ `Auto Rename Tag`：补全
	+ `Live Server`：启动服务渲染页面

## MarkDown

[我的MarkDown笔记](./Markdown.md)

+ 插件：
	+ 渲染：Markdown Preview Enhanced：`Ctrl + k v`
	+ 编辑：Markdown All in One
		+ 提供补全
		+ 生成目录

## LaTeX

[我的LaTeX笔记](./LaTeX.md)