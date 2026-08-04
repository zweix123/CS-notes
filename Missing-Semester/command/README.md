终端作为程序员学习工作中接触最多的东西，在本笔记项目中，有多次重复的笔记，让我疑惑，在这里统一梳理下。
相关话题可以分成以下几类：

- Missing-Semester类：
  - 对命令行使用的扫盲 -> 放在[单独文件](../misc/Terminal-Quick-Start.md)中

- 知识笔记：
  - Shell使用技巧 -> 放在[Linux相关文件](./linux.md)中
  - Linux相关知识 -> 放在[Linux相关文件](./linux.md)中
  - Bash语法 -> 放在[语言相关文件](../../Programming-Language/Bash.md)中
  - 重点命令的详细笔记 -> 放在[command目录](./)下

- 生产力配置：
  - 终端模拟器推荐（by 操作系统） -> 放在各系统配置文档中
  - 终端环境配置教程（by 操作系统） -> 放在各系统配置文档中
  - 常见命令下载配置（by 操作系统） -> 放在本文章中（以表格的形式）
  - 新质生产力命令推荐 -> 放在本文章中

|                 | Windows       | Linux | Mac                            | 命令功能                         |
| --------------- | ------------- | ----- | ------------------------------ | -------------------------------- |
| 包管理器        | <!-- TODO --> | -     | brew                           | 其余命令尽量使用包管理器安装     |
| man             |               | 内置  | 内置                           | 查看命令功能（有AI这个也没用了） |
| tldr            |               |       |                                | modern man（有AI这个也没用了）   |
| find            |               | 内置  | 内置                           | 文件搜索                         |
| **fd**          |               | 内置  | `brew install fd`              | modern fd                        |
| grep            |               | 内置  | 内置                           | 内容检索                         |
| **rg(ripgrep)** |               | 内置  | `brew install ripgrep`         | modern grep                      |
| git             |               | 内置  | 内置                           | 版本管理                         |
| uv              |               |       | `brew install uv`              | Python 版本管理 & 环境管理       |
| python          |               |       | `uv python install`            | Python 解释器                    |
| pip             |               |       |                                | Python 包管理器                  |
| fnm             |               |       | `brew install fnm`（需要配置） | Js&Ts 版本管理                   |
| node            |               |       | `fnm install 22 && fnm use 22` | Js&Ts 解释器                     |
| npm             |               |       | 与node打包下载                 | Js&Ts （原生）包管理器           |
| pnpm            |               |       | `npm install -g pnpm`          | modern Js&Ts 包管理器            |

# 附录

- 命令推荐类：
  - [实用命令行工具推荐](https://yanxingliu.github.io/posts/2026/04/useful-cli-tools/)
  - [XuehaiPan/Dev-Setup](https://github.com/XuehaiPan/Dev-Setup)：下载并配置所有推荐工具的包

* [Speeding Up My ZSH Shell](https://scottspence.com/posts/speeding-up-my-zsh-shell)：zsh启动速度prof
* [Better Shell History Search](https://tratt.net/laurie/blog/2025/better_shell_history_search.html)：更好的历史命令搜索
