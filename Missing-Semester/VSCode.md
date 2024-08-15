关于主力编辑器的选择，对于个人而言，如果一个新的工作流被验证效率优于当前，我可以不顾学习成本去迁移，比如输入法迁移到双拼。对于VSCode和Vim的选择，我相信vim的上限是优于VSCode的，但是基于GUI修饰键的操作在各个软件都有事实标准。不能保证所有常用软件都支持vim模式。出于对统一美感的追求，最终还是选择VSCode，但vim终究还是我们的老前辈，对于某些vim下很好的操作模式积极寻找VSCode等价操作。关于VSCode和jetbrains的选择，我个人依然使用VSCode原因是我个人对命令行操作比较熟练，且有多语言编程需求，VSCode All In One的属性比较吸引我，但是我承认jetbrains家软件的优秀，日常关注其更好的点寻找VSCode的等价效果。

+ 怎么打开VSCode？我的方式：在终端cd到对应路径，然后`code .`
    + 没有`code`命令？使用VSCode命令`Shell Command: Install 'code' command in PATH`，什么是VSCode命令，见下一条。
+ Command Center：即UI顶部的输入框，默认是项目下文件检索，通过添加前缀实现各种功能，下面是我常用的
    + Search files by name：默认`Ctrl/Comand + p`，相当于fd
	+ Go to Line:  默认`Ctrl/Command + g`，相当于vim的`数字 + g`
	+ Go to Symbol：默认`Ctrl/Command + Shift + O`
	+ Show and Run Cmd：默认`Ctrl/Command + Shift + P`，本文的“命令”即为了这里的命令
+ 常用通用命令：
    + 快捷键相关：`Perferences: Open Keyboard Shortcuts`
        + 在macOS中，不同输入法下的快捷键不同，要分别设置
    + 选中文本进行大小写转换：`Transform to Lowercase`/`Transform to Uppercase`
    + 代码块折叠：`Fold All`/`Unfold All`，还能按层级`Fold Level ...`

+ Settings：VSCode的配置分三个层级：默认 -> 用户 -> 工作区，同一项配置后者覆盖前者：快捷键`Ctrl + ,`或者命令`open settings`

	聊到配置就要聊到`.vscode`目录，这里聊一下该目录和插件无关的文件

	+ `settings.json`：即上面提到工作区范围的配置文件，这里聊一下常用的一些配置项，本文其他部分对于各个话题也会提到相关配置项
		+ `explorer.sortOrder`：资源管理器文件排序关键字
	+ `extensions.json`：项目下插件过滤

## 基本文本操作

|                   | Windows           | macOS               |
| ----------------- | ----------------- | ------------------- |
| Insert            | Insert            | 无                   |
| Delete            | Delete            | Command + backspace |
| Home              | Home              | Command + left      |
| End               | End               | Command + right     |
| Top               | Ctrl + Home       | Command + up        |
| Button            | Ctrl + End        | Command + down      |
| 全选，保存，撤退，剪切，复制，粘贴 | Ctrl+a，s，z，x，c，v  | Command+a，s，z，x，c，v |
| 选中                | 按住Shift使用方向键      | 按住Shift使用方向键        |
| 整行移动              | 按住Alt使用方向键上下键     | 按住Option使用方向键上下键    |
| 按word单位移动         | 按住Ctrl使用方向键       | 按住Option使用方向键       |
| 按word单位删除         | 按住Ctrl使用backspace | 按住Option使用backspace |

+ 全选：Ctrl/Command+a
+ 保存：Ctrl/Command+s
+ 撤退：Ctrl/Command+z
+ 剪切：Ctrl/Command+x
+ 复制：Ctrl/Command+c
+ 粘贴：Ctrl/Command+v
+ 查找：Ctrl/Command+f（当前文件）和Ctrl/Command+Shift+f（当前项目）（相当于rg）
+ 多光标：
    + Alt/Option+鼠标点击
    + 选中文本->Command+d/Ctrl+Alt+d：相同文本多光标
        + 如果希望全文全部相同文本都选中（并出现光标）：Command/Ctrl+F2
    + Alt/Option + Ctrl/Command + 方向键上下

+ 光标在terminal与workspace切换，以及在workspace中的不同窗口切换：
    + win：Ctrl+~和Ctrl+num
    + mac：Ctrl+·和Command+num：看起来有点反直觉，但是mac的Comamnd+·是系统级快捷键

    首先使用上面的快捷键可以在终端和不同窗口之前选择，其次单独使用终端相关的则是打开/关闭，关闭自然就会到workspace了。

    进一步，使用Ctrl/Command + Shift + j则是将Terminal的全屏和取消全屏

+ 格式化：Shift+Alt/Option+f，效果依赖插件，大部分项目设置为format on save

+ 名称跳转：
    + Ctrl/Commad+鼠标左键点击
    + Go Back：
        + win：Alt/Option+方向键Right
        + mac：F3

## 配置同步

设置同步：UI左下角齿轮图标中的`Settings Sync is On`，自动同步。
+ 规则：云上配置、端的配置，当一个端打开VSCode时，其配置将会被云上配置覆盖；当端修改配置时，会上传到云上。
    + 但我遇到这样的场景：针对插件，当活跃的一端删除时，删除后，另一段打开，并不会删除，返回删除的端再打开会下载回来。

## 字体与外观

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
		>需要你已经按照[Shell的配置](Missing-Semester/Terminal.md#font-download)下载了对应字体

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

## 远程开发

远程开发：VSCode较于JB家的IDE值得说的优点就是远程开发功能了，我们假设你本机是win，无论是那么当你需要Linux环境（无论时WSL、服务器还是虚拟机）时，都推荐使用SSH（服务器肯定是SSH，WSL我个人没有用过，虚拟机虽然相当于完整机器但是仍然建议通过SSH过去开发），而VSCode的Remote插件可以达到一个很自然的开发流程和体验。
+ Remote - SSH：远程开发必备
    + Remote - SSH: Editing Configuration Files
    + Remote Explorer

## 文件支持

+ JSON：默认提供
+ YAML：
    + YAML
+ TOML：
    + TOML Language Support

## Python


+ 插件：
    + Python Extension Pack
        + autoDocstring - Python Docstring Generator
        + Python
            + Pylance
            + Python Debugger
        + Jinja
        + Django
        + IntelliCode
            + IntelliCode API Usage Examples
        + Python Indent
        + Python Environment Manager
    + 格式化相关：
        + Black Formatter：库black
        + isort：import排序相关，需要配置
    + 类型提示：
        + Mypy Type Checker：库mypy
    + Jupyter
        + Jupyter Keymap
        + Jupyter Notebooks Renderers
        + Jupyter Slide Show
        + Jupyter Cell Tags

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

## C++

+ 插件：
    + C/C++ Extension Pack
        + C/C++
        + C/C++ Themes：没用
        + CMake Tools
    + llvm相关：
        + clangd：好用
    + Better C++ Syntax
    + cmake
        + 上面提到的CMake Tools
        + CMake Language Support
            >还有一个语言支持插件CMake，但是没有这个鲜艳。

            + .NET Install Tool
        + cmake-format

+ 软件安装：
    + Unix：对应包管理器，比如Ubuntu的apt，macOS的brew
    + Win：Scoop

+ 环境依赖：
    + 构建工具：cmake、make
    + 编译工具：
        + gcc
    + 调试工具：
        + gdb

        据说lldb更快，但是我没有使用过

    + 其他（但很重要）
        + 代码提示：clangd：推荐使用[VSCode clangd doc](https://clangd.llvm.org/installation.html)的方法下载
        + 代码格式化：clangd-format

+ 插件：
    + C/C++ Extension Pack（依赖C/C++、C/C++ Themes、**CMake Tools**）
        + 对应的配置文件为`.vscode/c_cpp_properties.json`
        + 该插件并非提示与跳转的主力，下面的clangd才是，两插件有冲突，经验上看，将下面三个属性设置为Disabled
            + `Intelli Sense Engine`
            + `Autocomplete`
            + `Error Squiggles`
    + clangd
    + Clang-Format
    + CMake Tools（已经随C/C++ Extension Pack一起下载）：该插件集成构建、编译、调试和测试
        + 底部状态栏有相应的按钮
        + 左边活动栏有相应的图标

        上面两个位置的状态可定制，详情见选择`cmake.options.statusBarVisibility`

    如果使用lldb进行调试，则需要插件CodeLLDB，但是我没有使用过

+ 前置知识：
    + compile_commands.json：clangd的功能依赖该文件
        + cmake生成
        + bear生成

        通常将该文件放在构建目录下（构建目录通常命名为build），需要额外设置，因为clangd默认从项目根目录找

        关键字`clangd.arguments`，添加`--compile-commands-dir=build`

+ 调试：上面提到，cmake插件基本可以满足所有开发需求，但是有些项目或者单文件，CMake Tools不可用，则返璞归真

    + 前置知识：
        + `.vscode/tasks.json`：构建/编译任务，在这里配置如何编译出可执行文件
        + `.vsocde/launch.json`：启动调试，在这里配置如何如何启动调试器（比如制定可执行文件位置或者执行参数）
        + 文档：
            + 内次变量：[所有的变量](https://code.visualstudio.com/docs/editor/variables-reference)

    下面是示例与说明

一些变量
```
${workspaceFolder}: 项目根目录
${fileDirname}: 当前文件所在路径
```

```json
// tasks.json
{
    "version": "2.0.0", // 指定配置文件的版本, 确保与VSCode调试器兼容, 一般选择2.0.0
    "tasks": [ // 如果构建包含多个任务，则划分成多个元素
        {
            "type": "shell", // VSCode选择哪类执行器, 一般选择shell, 其他的还有process(直接作为一个进程执行命令)
            "label": "任务名称",
            "command": "任务使用的命令",
            "args": [
                "参数1",
                "参数2"
            ],
            "options": {
                "cwd": "${fileDirname}" // 任务执行的目录
                // 还可以添加环境变量等
            },
            "problemMatcher": [ // 用于将任务输出映射到问题的错误和警告的匹配器, 即将输出的错误信息映射到VSCode的问题面板
                "$gcc" // 通常选择这个, 其他的我也不懂
            ],
            "group": {
                "kind": "build", // 有三种选择: build, test, none
                "isDefault": true // 默认
            },
            "detail": "任务说明"
        }
    ],
}
```

```json
// launch.json
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0", // 指定配置文件的版本, 确保与VSCode调试器兼容, 一般选择2.0.0
    "configurations": [ // 多个可选的调试
        {
            "name": "调试名称",
            "type": "cppdbg", // 调试器类型, 还有python, node, go
            "request": "launch", // 请求类型, 有launch(启动新调试会话)和attach()还有run(只执行，不调试)
            "program": "调试可执行文件路径", // 可以使用变量进行拼接
            "args": [], // 可执行文件的参数
            "stopAtEntry": false, // 是否在程序入口处停止
            "cwd": "${fileDirname}", // 程序运行时的工作目录
            "environment": [], // 环境变量
            "externalConsole": false, // 是否使用外部控制台运行程序，false表示在VSCode的集成终端中运行。
            "MIMode": "gdb", // 调试器的机器接口模式, 还有lldb
            "miDebuggerPath": "调试器可执行文件路径",
            "setupCommands": [ // 表示会话开始时, 要执行的调试器命令
                {
                    "description": "描述",
                    "text": "调试器命令",
                    "ignoreFailures": true // 是否忽略命令执行失败
                }
            ],
            "preLaunchTask": "调试前执行的任务的名称, 即label",
        }
    ]
}
```

+ 其他实践
    + cmake有代码`target_compile_options(... "-Werror" ...)`，这里表示把warning当error，这在某些项目中可能出现有很多的warning，但是项目可运行，但是在clangd这里，把warning当error了，如果文件大起来，前的的error太多了，会导致它不在处理后面的代码。而官方的`C/C++`插件似乎不受这影响。我是开发时把这个参数注释掉，修改后记得重新生成compile_commands.json文件。

## Golang

+ Golang：[微软教程](https://learn.microsoft.com/zh-cn/azure/developer/go/configure-visual-studio-code)和[debug tutor](https://www.digitalocean.com/community/tutorials/debugging-go-code-with-visual-studio-code)
    + Go
        + 下载依赖
    + Go Nightly

+ 插件：[别忘了Go和VSCode都是微软家的](https://learn.microsoft.com/zh-cn/azure/developer/go/configure-visual-studio-code)
    + 修改format tool：打开设置页，搜索`Go: Format Tool`，选择
    + 添加hint：添加设置：`"go.lintTool": "golangci-lint"`
+ 当使用Ctrl/Command+鼠标左键进行跳转时，由于Golang的库通常是网络路径，VSCode会将其识别成网络，此时的跳转变成了跳转链接，但是我们实际上是希望文件跳转，则在settings.json（我通常是在项目下）添加
    ```json
    "[go]": {
        "editor.links": false,
    }
    ```

## Web

+ Auto Rename Tag：补全
+ Live Server：启动服务渲染页面
+ Thunder client：HTTP Client，类似postman

## Markdown

+ Markdown：[我的MarkDown笔记](./Markdown.md)
    + Markdown All in One：Yes，All in One
        >Markdown的渲染还有插件Markdown Preview Enhanced，据说更好看，我没有使用

	+ Markmap：使用Markdown生成思维导图

## LaTeX

+ LaTeX：[我的LaTeX笔记](./LaTeX.md)
    + LaTeX Workshop
    + BibTeX formatter

## Git

+ Git：
    + 内置功能
    + gitignore
    + Git Blame
    + 没有使用gitlens，这玩意太臃肿了。

## Copilot

我也不知道为啥我有资质，因为VSCode和Github都是微软家的，用起来好方便啊！

+ 插件：
    + Github Copilot
        + Github Copilot Chat

## 其他

+ Project Manager：VSCode是围绕项目的，该插件会出现在Explorer上面，用于在不同项目之前跳转，虽然我基本不用，将是Explorer图标太靠上了，用Project Manager的图标占位。
+ Better Comments：注释增强，TODO的高亮之类的。
+ AutoCorrect：中文拼接与格式检测
+ Compare Folder：重大升级！非常好用！
+ Wakatime：统计编程情况
