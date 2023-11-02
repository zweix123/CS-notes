```python
class ClassName:
	def __init__(self, status: int, **kwargs) -> None:
		for key, value in kwargs.items():
			setattr(self, key, value)
```

+ 代码风格：`Pythonic`
+ 相关工具：
	+ `ipython`
	+ `jupyter`
+ 脚本：在Linux中，在脚本代码开头添加
	```python
	#! /usr/bin/python3
	#-*- coding: utf-8 -*-
	```
	并给脚本代码添加可执行权限，可以像可执行文件一样使用脚本

# Use

Python2和Python3是没有向后兼容的，这里造成了一些混乱，比如某些语境下`python`指的就是最新版的Python，但是有些语境下则是默认Python2、只有`python3`才指的是Python3。  
所以建议使用命令`python3`，如果没有则将（是Python3）的`python` copy 一个`python3`，还有诸如`pip`这样的命令，也建议加上`python3 -m pip`的前缀
>对于诸如`poetry`或者`thefuck`这样的应用则不用这样，因为他们都是由pip下载的，如果在piip时指的python版本，那么他们的版本肯定是对的。

# Tools

## pip

### 代理

+ 参考资料：
	+ [一个把来龙去脉解释清楚的文章](https://codeantenna.com/a/pAOz55u5Px)

我个人在win上的Python通过Scoop下载，在Linux上我用的Ubuntu，自带Python，所以一直没有遇到关于代理的问题，直到我在win数据中心上搭建服务需要手动安装Python时，

目前的解决方案是：
```bash
pip config set global.proxy http://127.0.0.1:7890
```
在服务器我使用的代理工具是`Clash for Windows`，配置文件照猫画虎的。

### 软件源

+ 命令：
	+ 临时换源：`pip install module_name -i ...`
	+ 永久换源：
		```bash
		pip config --global set global.index-url .../simple/
		pip config --global set install.trusted-host ...
		```
		+ 取消换源（或者直接修改配置pip的ini）：
			```bash
			pip config unset global.index-url
			pip config unset install.trusted-host
			````

+ 常用源：
```
https://pypi.tuna.tsinghua.edu.cn/simple  # 清华源
https://mirrors.aliyun.com/pypi/simple/  # 阿里源
http://mirrors.cloud.tencent.com/pypi/simple  # 腾讯源
http://pypi.douban.com/simple/  # 豆瓣源
```

## poetry
一款相当现代的Python虚拟环境管理工具

+ Install：
	```bash
	python3 -m pip install poetry  # 之后可直接在命令行使用命令poetry
	```

+ Update：
	```bash
	poetry self update
	```

+ Config：
	+ 配置文件位置：覆盖默认配置
		+ win：`C:\用户\$用户名\AppDatat\Roaming\pypoetry\config.toml`
	+ 相关命令：
		+ `poetry config --list`：查看配置
		+ `poetry config 配置参数 值`：更改配置
		+ `poetry config 配置参数 --unset`：删除配置（使用默认配置）
	+ 我的配置：
		```bash
		poetry config virtualenvs.in-project true  # 在项目下创建虚拟环境，这样VSCode也能找到对应库
		```

+ Use：	
	+ 初始化：
		+ 1. 创建项目并初始化：`poetry new 项目名`
		+ 2. 在已有项目中初始化：`poetry init`

		会在项目中创建`pyproject.toml`文件和`poetry.lock`文件（在修改项目依赖后）
		+ 两者都有项目依赖的信息，但是toml中的依赖是最低版本，但是依赖也有依赖，lock文件保存依赖的递归依赖的信息

	+ 使用不同版本的Python：`poetry env use 版本`
		>2.7之前的应该不可以
	
	+ 库管理：
		+ 添加库：`python3 -m poetry add 库名`
		+ 删除库：`python3 -m poetry remove 库名`

		Poetry管理虚拟环境的底层工具是Pyenv和Virtualenv，其中后者负责虚拟环境，有时poetry的依赖管理算法不能处理库的依赖关系，但是使用Virtualenv本身的功能可以，但是这样的修改不会被Poetry管理，具体的，直接在虚拟环境中使用`pip`进行依赖库的`install`。
		+ 其他问题，很多项目提供`requirements.txt`文件，让我们使用`python3 -m pip install -r requirements.txt`，那这样的方法在虚拟环境中确实可以安装好依赖，但是这些依赖不会记录在配置文件中。
			+ poetry是兼容它们的：`pip freeze > requirements.txt`即可依照我们的虚拟环境依赖生成这样的txt文件
			+ 它们是不兼容poetry：通过这样的方法不会修改poetry的配置文件，我们需要其他方法将该文件的内容正确的放入到配置文件，使用更现代的方式管理依赖
				```bash
				poetry add `cat requirements.txt`  # linux
				poetry add $(type requirements.txt)  # win
				```

				但是这样的方法经常失效，到这种情况只能使用虚拟环境中的`pip`管理了。

	+ 程序运行：
		+ 1. `poetry run python 程序`
		+ 2. 激活环境`poetry shell`，进入虚拟环境命令行即可使用`python 程序`（虚拟环境中除了python外还有pip，管理的库也会被poetry管理）

+ MISC：
	+ 部署：在项目目录下使用命令`poetry install`即可将项目中的虚拟环境配置到本地
	+ 问题：如果报错`AssertionError`，可能的原因是项目和添加的包重名