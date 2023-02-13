一款相当现代的Python虚拟环境管理工具

## 下载
```bash
python3 -m pip install poetry  # 之后可直接在命令行使用命令poetry
```
## 更新
```bash
poetry self update
```
## 配置
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
## 使用

+ 初始化：
	+ 1. 创建项目并初始化：`poetry new 项目名`
	+ 2. 在已有项目中初始化：`poetry init`

+ 使用不同版本的Python：`poetry env use 版本`
	>2.7之前的应该不可以

+ 库管理：
	+ 添加库：`python3 -m poetry add 库名`
	+ 删除库：`python3 -m poetry remove 库名`

+ 程序运行：
	+ 1. `poetry run python 程序`
	+ 2. 激活环境`poetry shell`，进入虚拟环境命令行即可使用`python 程序`（虚拟环境中除了python外还有pip，管理的库也会被poetry管理）

## 部署

+ 在项目目录下使用命令`poetry install`即可将项目中的虚拟环境配置到本地