[我的VSCode&Cursor的配置](https://github.com/zweix123/unix-config/blob/master/IDE/settings.json)：基本配置以及本文涉及的插件的配置，都在这个配置中，且有脚本可以直接应用到本机。

关于主力编辑器的选择，对我个人而言，如果一个新的工作流被验证效率优于当前，我可以不顾学习成本去迁移，比如输入法迁移到双拼。对于VSCode和Vim的选择，我相信vim的上限是优于VSCode的，但是基于GUI修饰键的操作在各个软件都成了事实标准。不能保证所有常用软件都支持vim模式。出于对统一美感的追求，最终还是选择VSCode，但vim终究还是我们的老前辈，对于某些vim下很好的操作模式积极寻找VSCode等价操作。关于VSCode和jetbrains的选择，我个人依然使用VSCode原因是我个人对命令行操作比较熟练，且有多语言编程需求，VSCode的"All In One"属性比较吸引我，但是我承认jetbrains家软件的优秀，日常关注其更好的点寻找VSCode的等价效果。

+ 怎么打开VSCode？我的方式：在终端cd到对应路径，然后`code .`
    + 没有`code`命令？使用VSCode命令`Shell Command: Install 'code' command in PATH`，什么是VSCode命令，见下一条。
+ Command Center：即UI顶部的输入框，默认是项目下文件检索，通过添加前缀实现各种功能，下面是我常用的
    + Search files by name：默认`Ctrl/Comand + p`，相当于fd
	+ Go to Line:  默认`Ctrl/Command + g`，相当于vim的`数字 + g`
	+ Go to Symbol：默认`Ctrl/Command + Shift + O`（英文字母O）
	+ Show and Run Cmd：默认`Ctrl/Command + Shift + P`，本文的“命令”即为了这里的命令
+ 常用通用命令：
    + 快捷键相关：`Perferences: Open Keyboard Shortcuts`
        + 在macOS中，不同输入法下的快捷键不同，要分别设置
    + 选中文本进行大小写转换：`Transform to Lowercase`/`Transform to Uppercase`
    + 代码块折叠：`Fold All`/`Unfold All`，还能按层级`Fold Level ...`

+ Settings：VSCode的配置分三个层级：默认 -> 用户 -> 工作区，同一项配置后者覆盖前者：快捷键`Ctrl + ,`或者命令`open settings`

	聊到配置就要聊到`.vscode`目录，这里聊一下该目录下和插件无关的文件

	+ `settings.json`：即上面提到工作区范围的配置文件。

## 基本文本操作
> 各种编辑软件都支持的文本操作的事实标准

|                                    | Windows                 | macOS                      |
| ---------------------------------- | ----------------------- | -------------------------- |
| Insert                             | Insert                  | 无                         |
| Delete                             | Delete                  | Command + backspace        |
| Home                               | Home                    | Command + left             |
| End                                | End                     | Command + right            |
| Top                                | Ctrl + Home             | Command + up               |
| Button                             | Ctrl + End              | Command + down             |
| 全选，保存，撤退，剪切，复制，粘贴 | Ctrl+a，s，z，x，c，v   | Command+a，s，z，x，c，v   |
| 选中                               | 按住Shift使用方向键     | 按住Shift使用方向键        |
| 整行移动                           | 按住Alt使用方向键上下键 | 按住Option使用方向键上下键 |
| 按word单位移动                     | 按住Ctrl使用方向键      | 按住Option使用方向键       |
| 按word单位删除                     | 按住Ctrl使用backspace   | 按住Option使用backspace    |

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
    + win：`Ctrl+~`和`Ctrl+num`
    + mac：`Ctrl+·`和`Command+num`：看起来有点反直觉，但是mac的`Comamnd+·`是系统级快捷键

    首先使用上面的快捷键可以在终端和不同窗口之前选择，其次单独使用终端相关的则是打开/关闭，关闭自然就会到workspace了。

    进一步，使用`Ctrl/Command + Shift + j`则是将Terminal的全屏和取消全屏

+ 格式化：Shift+Alt/Option+f，效果依赖插件，大部分项目设置为format on save

+ 名称跳转：
    + Ctrl/Commad+鼠标左键点击
    + Go Back：
        + win：Alt/Option+方向键Right（一般来说应该是方向键左键Left，但是在win上我会将Caps改成方向键右键用于加速命令行补全）
        + mac：F3（个人习惯，在mac上没有follow win是因为Command+左右是Home/End，Option+左右是单词移动，Ctrl不不能+左右作为快捷键）

## 配置同步

设置同步：UI左下角齿轮图标中的`Settings Sync is On`，自动同步。
+ 规则：云上配置、端的配置，当一个端打开VSCode时，其配置将会被云上配置覆盖；当端修改配置时，会上传到云上。
    + 但我遇到这样的场景：针对插件，当活跃的一端删除时，删除后，另一段打开，并不会删除，返回删除的端再打开会下载回来。

## 字体与外观

+ 主题：插件`One Dark Pro`（`One Dark Pro Darker`）
+ 图标：插件`vscode-icons`
+ 字体：插件`FiraCode font - Professional Font for Developers`
    + 编辑器字体
    + 终端字体

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

## Git

| 我的需求                           | 解决方式                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 查看当前的修改（by文件，可对比）              | VSCode自带的Source Control（就是侧边栏分支图标）                                                                                                                                                                                                                                                                                                                                               |
| `.gitignore`编辑增强               | gitignore插件（现在VSCode已经自带这个功能了）                                                                                                                                                                                                                                                                                                                                                   |
| blame（单行blame，文件层面blame）       | 这其实是一个值得讨论的问题，JB家的blame功能是在编辑器左边开一个窗口，仔细想一下，这个VSCode其实是原生不支持的，这样的一个窗口在VSCode下不是一等公民。下面讨论一些插件的解法。<br>+ Git Blame：在下面状态栏开一个位置表示光标在的位置上次修改的username<br>+ Annotator：它的行为是仿照JB家的，但是上面说的，VSCode原生不能支持这样的形式，所以它是单独开一个页面，在这里划分两个窗口分别显示blame内容和代码内容，因为不原生支持，在这里，源文件内容的显示修改很差<br>+ gitlens：它和Annotator在原理上是一样的，但是它优化的更好，显示效果基本相当于原生的了。<br>我目前只用Git Blame，因为Annotator效果不好，然后我个人觉得gitlens太重了 |
| 图形化提交历史                        | Interactive Git Log插件：真不错，画风很喜欢，而且很干净                                                                                                                                                                                                                                                                                                                                            |
| 查看某一次提交修改的所有文件并且可以查看某一个文件的对比修改 | Interactive Git Log插件                                                                                                                                                                                                                                                                                                                                                            |
|                                |                                                                                                                                                                                                                                                                                                                                                                                  |

+ gitlens：
    + Gitlens > Current Line: Enabled
    + Gitlens > Code Lens Endabled

    以上两个关闭，不然大文件卡，我blame看的也是状态栏

+ Go to next change

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
+ 使用`#%%`可类似Jupyter分块，而Jupyter状态下有很多快捷键

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

+ 插件与部分配置：[微软教程->按照与配置Golang插件](https://learn.microsoft.com/zh-cn/azure/developer/go/configure-visual-studio-code)、[安装之后VSCode可以提供的能力](https://code.visualstudio.com/docs/languages/go)和[debug tutor](https://www.digitalocean.com/community/tutorials/debugging-go-code-with-visual-studio-code)

```bash
> go version                                                   
go version go1.22.12 darwin/arm64

> go install golang.org/x/tools/gopls@v0.16.2
> go install github.com/golangci/golangci-lint/cmd/golangci-lint@v1.60.2
```

## Shell

+ format: 
    + shell-format
        + dep: shfmt comamnd

## Web

+ Auto Rename Tag：补全
+ Live Server：启动服务渲染页面
+ ~~Thunder client：HTTP Client，类似postman~~

## Markdown

+ Markdown：[我的MarkDown笔记](./Markdown.md)
    + Markdown All in One：Yes，All in One
        >Markdown的渲染还有插件Markdown Preview Enhanced，据说更好看，我没有使用

### Mind-Map

我在最开始是使用思维导图记笔记的，直到现在我也觉得树形结构是比流式结构更好的笔记结构，此时随机选择了[Xmind8](https://xmind.cn/download/xmind8/)（是8而不是最新版，这个可能不是最好看的，但是我觉得是操作最合理高效的）。随机笔记规模的扩大就有了渲染性能和文件管理的问题，这个时候使用Markdown；此时思维导图这个形式只是偶尔使用，最后发现没必要在为这偶尔使用的需求留着一个软件了，换到[markmap](https://markmap.js.org/)框架（有VSCode插件Markmap）

### Slide

>我书写本文的发心是如何制作像[南大蒋炎岩老师那样的](http://jyywiki.cn/OS/2022/slides/1.slides.html#/)运行于Web的幻灯片，而不是微软的能量点，后又接触到PDF全屏播放的效果也类似幻灯片，如果可以导出成PDF那也可以作为一种幻灯片

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


## LaTeX
+ Ref：
    + [知乎 · 槿灵兮 · 【LaTeX】针对萌新自学者的入门教程](https://zhuanlan.zhihu.com/p/521649367?utm_source=zhihu)
    + [LaTeX 入门与进阶](https://latex.lierhua.top/zh/)

+ 插件：
    + LaTeX Workshop
    + BibTeX formatter


+ 在线：比较有名的一款是overleaf，我个人使用的是[texpage](https://www.texpage.com/)，原因在于某些模板在overleaf如果有中文则格式不符合预期，后面本地环境跑起来之后一直使用本地。下面详细讲本地。

==Tex Live by Scoop and VSCode in Windows==

+ 编译工具：软件包Tex Live，包含一款LaTeX编辑器XeLaTeX，而且我使用Scoop进行安装（[我的Scoop教程](./WindowsConfigGuide.md#6包管理器scoop)）
	>LaTeX的编译工具有很多，宛如古神的低语，我个人将下面这个跑的通的方案作为黑盒，慢慢了解全貌。

	```powershell
	scoop bucket add scoopet https://github.com/ivaquero/scoopet
	scoop install texlive  # 需要较长时间
	```

	+ 设置环境变量，这应该是Scoop的问题，它设置的相关环境变量不全，在我的机器上，还需要将`...\Scoop\apps\texlive\current\bin\windows`手动设置环境变量，在该路径下才是Tex Live软件包中各种可执行文件的路径，设置后可以通过`xelatex --version`检测。
	+ LaTeX的包管理器是tlmgr，其依赖脚本perl，tlmgr已经包含在Tex Live软件包中，而tlmgr也内置了perl，不需要单独下载（其他教程可能会说单独下载），问题出现在perl在Windows中可能出现报错

		```
		Locale 'Chinese (Simplified)_China.936' is unsupported, and may crash the interpreter.
		```

		其原因是Windows非常经典的编码问题，关于这个问题在[Windows编码问题](./WindowsConfigGuide.md#win-code)

	+ 包管理tlmgr配置：

		```powershell
		tlmgr update --self  # 升级自身
		tlmgr update --all  # 升级所有包
		tlmgr list --only-installed  # 列出已安装包
		```

	+ 常见包安装

		```powershell
		tlmgr install ctex ctexrep latexmk  # 中文支持
		tlmgr install mhchem chemfig circuitikz  # 化学 & 电子
		tlmgr install multirow ifoddpage relsize titlesec  # 排版
		tlmgr install epstopdf subfigure appendix  # 图表
		tlmgr install ulem xcolor environ letltxmacro enumitem stringenc trimspaces soul algorithm2e genmisc  # 字符 & 字体
		tlmgr install cleveref titling placeins minted tocloft biblatex biber  # 其他, 主要是我校毕业论文模板的依赖包
		tlmgr install latexindent  # 格式化工具
		```

		面对一个模板的报错，可以尝试从是否缺乏某个依赖包的角度考虑（通过看log）

+ 编辑环境：个人使用VSCode，插件推荐和配置如下：

	+ 核心插件：LaTeX Workshop
		+ 我个人使用的配置在[这里](https://github.com/zweix123/zstu-graduation-thesis-latex-template/blob/master/.vscode/settings.json)，其他教程通常将该配置作为全局配置，出于最小化全局状态原则，我个人使用将配置放在项目下。
		+ 使用：一个项目就是一个模板和文章，在任意`.tex`保存时即可触发插件生成pdf。

+ 其他：
	+ [`.gitignore`](https://github.com/zweix123/zstu-graduation-thesis-latex-template/blob/master/.gitignore)

## Copilot

我也不知道为啥我有资质，因为VSCode和Github都是微软家的，用起来好方便啊！

+ 插件：
    + Github Copilot
        + Github Copilot Chat

## 其他

+ Project Manager：VSCode是围绕项目的，该插件会出现在Explorer上面，用于在不同项目之前跳转。
+ Better Comments：注释增强，TODO的高亮之类的。
+ AutoCorrect：中文拼接与格式检测。
+ Compare Folder：文件夹之间的比较。
+ Wakatime：统计编程情况。
+ Bookmarks：by项目的创建标签，快速导航。
+ 


==垃圾，狗都不用==

~~更新自工作，我并不喜欢JetBrains家的编辑器，毕竟当你有了锤子，你看谁都是钉子，而JB家的一个语言一个软件的哲学不太喜欢。而且它的内存占用太高，真的卡。但是同事很喜欢，也许是因为这是业务岗，同事们之前都是做Java的（现在是Golang），可能Java确实IDEA是最好的。在这样的情况下，我明显感觉自己在同事的屏幕看代码有困难（可能是因为主题），于是希望自己的VSCode和IDEA更像，希望可以提高效率。~~ 
1. ~~图标：JetBrains Icon Theme~~
2. ~~主题：JetBrains Darcula Theme~~
3. ~~字体：~~
    + ~~[下载链接](https://www.jetbrains.com/lp/mono/)~~
    + ~~/JetBrainsMono/fonts/ttf，所有字体，手动点击下载~~
    + ~~在font改成`JetBrains Mono, Fira Code`~~


还在考察中的：
+ indent-rainbow
+ dendron
+ Live Server