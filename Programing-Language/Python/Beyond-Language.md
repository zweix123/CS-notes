想在这里聊一下在使用Python开发软件的过程中语言之外的知识点。具体的，我们讨论一个语言时，语法仅仅是很小的一部分，它的生态也很重要：如何管理依赖，如何构建，如何发布；相关测试框架、相关格式化软件、相关Lint软件；被普遍使用的工程架构、代码风格，有没有什么奇技淫巧。

>同样发心的资料应该不少，这里会陆续挂一些链接，不是作为推荐，仅仅作为标记。
>+ [脚手架](https://github.com/waynerv/cookiecutter-pypackage)

+ Python2和Python3：Python3对Python2不是后向兼容的，只建议Python3，但是仍有正在运行的Python2代码，这造成了一些混乱，比如某些语境下`python`指的就是最新版的Python（Python3），但是有些语境则指的是Python2，只有`python3`才是Python3，在这里，Python表示Python3

+ 鉴于我个人的开发经历，具体讨论的操作系统只有Windows和Ubuntu。
	+ Ubuntu预装Python，许多系统工具和组件依赖Python，请不要试图删除默认的Python

+ 代码风格：Pythonic，鉴于Python的抽象程度之高，Pythonic不仅是代码风格上的强迫，它能指示我们写出性能更高的Python代码。
+ 项目结构：并没有官方的推荐的项目结构，符合普遍接受的项目结构即可。

+ 从[IPython](https://ipython.org/)到[Jupyter](https://jupyter.org/)

+ PyPi和TestPyPi：TODO
+ black and mypy: TODO
+ VSCode Settings: TODO

# Install

你可能需要让自己的库适用于更低版本的Python3，此时可能需要在机器中维护不同版本的Python3解释器。

在Linux上有（据说）非常好用的工具`pyenv`，它在Windows上也有对应的版本`pyenv-win`，但我个人并未使用，而是使用包管理器，在Windows上使用`scoop`，在Ubuntu上使用`apt`。
```bash
scoop install python
# 以下两行命令需要先执行
# scoop bucket add versions
scoop install python36
scoop install python310

sudo apt install python3.6
sudo apt install python3.10
```

>[我的Scoop笔记](../../Missing-Semester/WindowsConfigGuide.md#6%E5%8C%85%E7%AE%A1%E7%90%86%E5%99%A8scoop)

Scoop只维护大版本的Python3，而`python`表示最新版的Python；两种方式下载解释器的可执行文件名称不同，Scoop为`python310`的形式，`apt`是`python3.10`的形式。我们可以通过指定小版本的命令来执行不同的版本。

Python在下载第三方库时，有些库会提供可执行文件，这些文件在这里，Windows上在`Python路径/Script/`，Ubuntu上在`~/.local/bin/`下，如果不同的版本都安装了同样的库，那么对应的命令代表的是哪个版本的Python下载的呢？

在Scoop中，通过命令`scoop reset 命令`的方式将某个版本的相关路径设置在系统路径的前面，比如`scoop reset python10`，它是将相关系统路径都放在前面，不仅`python`这个名称对应的版本会设置为`python10`，其下的库的对应的可执行文件所在的目录也会调整。

在`apt`下则没有好的办法。

我个人为了避免混淆，在执行库的可执行命令时通常使用前缀Python的`-m`选项，下面会聊。

+ 特别的，在Scoop中，我通常使用`scoop install python`维护全局使用的库，比如`dryads`、`black`、`mypy`，因为它通常的最新的Python版本，而其他小版本则仅仅用来给虚拟环境的不同版本提供解释器（下面会聊）。

# Use

+ 脚本语言的Shebang，在Unix系统中，在代码的开头添加
	```python
	#! 一个Python解释器的路径
	#-*- coding: utf-8 -*-
	```

+ 让我们看看Python的help option：
	+ `-m`：run library module as a script (terminates option list)，这样我们就通过Python命令显式的指定哪个版本Python下载的库的可执行文件了，比如
		```bash
		python3.6 -m pip install ...  # 使用python3.6的pip下载第三方库
		python310 -m poetry ....     # 使用python3.10的poetry进行虚拟环境管理
		```

		这里涉及的两个库都会在下面讲

## pip

Python官方推荐的、默认安装的依赖管理工具，常用操作如下

```bash
pip install xxx    # 第三方库下载
pip uninstall xxx  # 第三方库卸载
pip --help         # [沟通]
```

+ pip有一个问题，就是下载的库的版本的全局的，为一个项目下载的库会被其他的项目访问到，如果有两个项目的需要的依赖版本不同，就会出现问题，所以，我们需要虚拟环境，每个虚拟环境中的依赖是独立的、互不影响的。

## poetry

一款现代的Python虚拟环境管理工具

+ install：`pip install poetry`
+ config：
	+ 我的配置：
		```bash
		poetry config virtualenvs.in-project true  # 默认依赖环境放在单独的目录下，使用该配置将虚拟环境放在项目目录下
		```

+ use：
	+ init：`poetry init`在当前项目中初始化

		会在项目中创建`pyproject.toml`和`poetry.lock`文件用来记录依赖版本

	+ 进入虚拟环境：`poetry shell`

	+ 库管理：
		```bash
		poetry add 库名
		poetry remove 库名
		```


	+ 安装：对于一个新下载的使用poetry管理虚拟环境的项目，通过`poetry install`部署项目虚拟环境

	+ 虚拟环境使用和全局环境不同的Python：`poetry env use [解释器路径]`

		>注意，poetry虚拟环境用的是virtualenv，而它已经放弃对Python3.6的支持，所以poetry也是这样的。[issue](https://github.com/python-poetry/poetry/issues/8185)


	+ 一些坑点：在`pyproject.toml`中描述Python版本的格式为：
		```
		[tool.poetry.dependencies]
		python = "^3.12"
		```

		但是可能遇到这种错误
		```
		The current project's supported Python range (>=3.12,<4.0) is not compatible with some of the required packages Python requirement:
		  - pyside6 requires Python <3.13,>=3.8, so it will not be satisfied for Python >=3.13,<4.0
		```

		你可能会感到疑惑，我设置的版本大于3.12，且实际的虚拟环境的版本就是3.12，这个数字明明符合库要求的`[3.8, 3.13)`

		但是实际上，它比较的是区间`[3.8. 3.13)`和`[3.12, +∞)`，我们发现这两个区间有对称差集，所以出了问题。

		把配置中改成类似
		```
		[tool.poetry.dependencies]
		python = ">=3.10, <3.13"
		```

		就行

		值得注意的是，我们发现来自依赖库的报错肯定是这个库本身要求安装的Python版本，如果这是一个你的库，那么像上面那样设置也会导致别人也遇到同样的限制，而使用`^`则宽泛的多