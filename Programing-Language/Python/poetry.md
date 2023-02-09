## 下载
```bash
python3 -m pip install poetry
```

## 使用

+ 在项目下创建poetry虚拟环境：
	```bash
	python3 -m poetry init
	# 进入命令行交互环境配置项目信息
	```

+ 下面的库管理方式会自动将配置添加到配置文件中

### 一种使用方式

以`python3 -m poetry`为前缀的一系列命令
```bash
python3 -m poetry --help  # 查看细节
```

+ 库管理：
	+ 添加库：`python3 -m poetry add 库名`
	+ 删除库：`python3 -m poetry remove 库名`

+ 运行程序：`python3 -m poetry run python 文件`

### 另一种使用方式

使用命令`python3 -m poetry shell`进入虚拟环境，进入后即可使用普通的python相关命令开发

+ 库管理：`pip`
+ 运行：`python`

## 下载依赖

+ 项目的使用者只需要通过命令`python3 -m poetry install`即将项目中的依赖部署到本地
	>注意这时项目目录中仍然是整洁的，但是这些依赖实实在在的下载到本地，路径会在使用该命令时输出提示。