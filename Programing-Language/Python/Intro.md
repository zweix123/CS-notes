# MISC

## 软件源

+ 临时换源：
	```bash
	#清华源
	pip install markdown -i https://pypi.tuna.tsinghua.edu.cn/simple
	# 阿里源
	pip install markdown -i https://mirrors.aliyun.com/pypi/simple/
	# 腾讯源
	pip install markdown -i http://mirrors.cloud.tencent.com/pypi/simple
	# 豆瓣源
	pip install markdown -i http://pypi.douban.com/simple/
	```
+ 永久换源：
	```bash
	# 清华源
	pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
	# 阿里源
	pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
	# 腾讯源
	pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple
	# 豆瓣源
	pip config set global.index-url http://pypi.douban.com/simple/  
	# 换回默认源  
	pip config unset global.index-url
	```

# 概述

+ Python是解释型语言
  + 如果出现拼写错误不会报错（语法错误），但对程序员会出现逻辑错误，不过编辑器一般都有提示

+ Python Shell——IDLE：Python交互式控制台

  > 本质是Python解释器的交互模式——REPL(read-eval-print loop, 读取、求值、输出的循环)。

+ ipython（b的部分特性）

  + 支持Tab补全（双击Tab进入查找）

  + 支持使用系统命令`!命令`

  + 支持查找和内省

    + `正则表达式?`查找符合正则表达式的
    + `属性/方法名/类名?`内省

  + `_`表示part的代码的编译运行**结果**（`out[]`）

    `_数字`表示对应行的part的代码的编译运行结果（`out[数字]`）

  + 魔术命令：以`%`开头

    + `%run filename.py`

    + `%paste`执行剪切板的内容

    + `%timeit py代码`**评估**代码运行时间（多次运行取平均）

    + `%pdb on/off`对于有bug的代码进行检测，如果检测到bug进入一种调试状态

      ```python
      p 变量  # 打印变量的值
      q  # 退出
      ```

    + `%bookmark 名字 内容`可在其他ipython特性中使用新名字

      `%bookmark -l`

      `%bookmark -d 名字`

  + `jupyter notebook`进入`jupyter`：蓝色命令行模式、绿色编辑模式

    + 命令行下H查看帮助，DD删除，A在上插入、B在下插入、Ctrl + Enter运行
    + 导出为：.md：`jupyter nbconvert --to markdown file.ipynb`

+ Python风格(Pythonic)：一致性：数据模型

  > 数据模型是对Python框架的描述，规范了语言自身构建模块的接口

+ 代码格式设置：[Python改进提案(Python Enhancement Proposal, PEP)（PEP 8）](https://python.org/dev/peps/pep-0008/)

  + 缩进： 使用四个空格

  + 代码行长：不超过79字符

    注释行长：不超过72字符

  + 变量命名规范

    + 只包含字母、数字和下划线
    + 可以字母或下划线打头，数字则不能
    + 不能包含空格，但可用**下划线**来分隔其中的单词
    + 不能使用关键字和函数名
    + 应既简短又具有描述性
    + 慎用小写字母`i`和大写字母`o`，因其易被勿看为数字

  + 函数规范：

    + 给函数指定描述性名称，只使用**小写字母**和**下划线**
    + 在函数定义后采用文档字符串格式简述功能的注释
    + 给形参指定默认值、在函数调用中的关键字实参：等号两边**不要**有空格
    + 如果函数头过长，则在**输入左括号**后回车并缩进**两行**来书写参数
    + 相邻函数用**两个回车**分开

  + 类：驼峰命名法：**每**个单词**首字母大写**，**不**使用下划线

    ​        其 实例名和模块采用**小写**格式，并在单词之前**加上**下划线

    + 使用两个空行分隔类

  + import语句在文件开头，除非有描述整个程序的注释

    先导入**标准**库模块，再导入**自定义**

+ 重构：将代码划分为一系列完成具体工作的例程

+ Linux环境下：要在代码前加上：

  ```python
  #! /usr/bin/env python3
  #-*- coding: utf-8 -*-
  ```

  + 第一行指明解释器，使之可以用过`./文件名`直接运行（当然要加上可执行权限）
  + 第二行指明编码格式