+ 该笔记部分插图使用各种书籍、课程或其他资料，如果涉及到任何版权行为，请联系我，我将删除内容。
+ 文中所有内容，与本人现在，之前或者将来的雇佣公司无关，本人保留自省的权力，即你看到的内容不一定代表本人最新的认知和观点。

### 笔记的意义

1. 在初学时
   + 在学习时记下笔记有助于记忆
   + 在整理时重构笔记有助于搭建知识体系
     随着进一步学习，我们对同一知识的理解发生变化，会动态的调整笔记（重构知识体系的过程）

2. 在实践时  
   通过笔记快速的回忆起学习时的理解或者查找对应的知识点

但随着时间的推移，笔记的作用减少了

+ 常用的、重要的知识点内化于心
+ 零碎的、细节性的知识现用现查

此时笔记更像是”当年攻城略地时的纪念品“

### Plan of 2023

<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/word of cs.png"/>

### Obsidian推荐

### tool

项目下的tool目录为使用Python开发的一系列博客处理工具，目前只开发用于Powershell7的版本
我的Python版本为3.11.1，用到python的虚拟环境标准库venv，目录结构如下：
```
project
   |----.vscode/
   |----install.ps1  # 安装虚拟环境
   |----uninstall.ps1  # 卸载安装虚拟环境
   |----cnt_word.py  # 统计博客字数
   |----perl_md.py  # 批量修改博客图床路径
```

使用时通过命令`.\Scripts\activate`进入虚拟环境
推出虚拟环境：`deactivate`

#### cnt_work.py

命令格式：`python3 cnt_word.py [不要统计的目录]`

+ 比如：我们的笔记目录下有一个`.git`目录是git配置，`source`目录保存图片，`tool`目录是博客工具，这些目录是不要统计的，所以命令是这样的
  ```powershell
  python3 cnt_word.py .git source tool
  ```