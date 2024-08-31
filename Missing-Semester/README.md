+ 发心：

    在MIT的课程[Missing-Semester](https://missing.csail.mit.edu/)中，没有讲编译原理、操作系统、计算机网络这样的主题，而是讲很少会有课程涉及的、在受教育过程以及职业生涯可能上千小时都会使用的工具，比如命令行、编辑器、版本管理工具等。

    在中科大“一生一芯”活动中，yzh用了[一节课](https://ysyx.oscc.cc/slides/2205/02.html)的时间讲了Linux入门，比如GUI和CLI的对比、命令行工具概述、Unix哲学等。

    本系列文章以此为题，包含各系统配置、重要软件的配置、效率工具的推荐。

+ 原则：

    严格遵守奥卡姆剃刀原理：“如无必要、勿增实体”——依照需求寻找工具，而非因工具能力而创造需求。

+ 结构：

    + 系统纬度：对于新机/新服务器如何配置出生产力的流程
        + [LinuxConfigGuide](./LinuxConfigGuide.md)
        + [WindowsConfigGuide](./WindowsConfigGuide.md)
        + [macOSConfigGuide](./macOSConfigGuide.md)

    + 软件纬度：
        + [VSCode](./VSCode.md)
        + 命令行：包含在各系统配置中（Linux的配置是满血版，macOS也是Unix系统，在oh-my-zsh的配置一样，所以使用Linux的配置；win则是尽力配置出同样的体验）

    + 命令纬度：[CLI介绍](./CLI/README.md) -> 命令行配置（如上） -> [SSH](./CLI/SSH.md) -> [Git](./CLI/Git.md) -> [其他](./CLI/)

大学算起，我个人使用机器的经历是：3年Windows->1年Linux->?年macOS，故后面大概只会更新macOS相关的了。

| OS    | Windows           | Linux           | macOS      | 需求         |
| ----- | ----------------- | --------------- | ---------- | ---------- |
| 浏览器   | Chrome            | Chrome          | Chrome     |            |
| 代理    | Clash for Windows | Clash for Linux | ClashX Pro |            |
| Shell | Powershell7       | zsh             | zsh        |            |
| 终端    | Windows Terminal  | Terminal        | Terminal   |            |
| 包管理器  | Scoop             | 原生              | brew       |            |
| 编程    | VSCode            | VSCode          | VSCode     |            |
| 笔记    | Obsidian          | Obsidian        | Obsidian   | Markdown   |
| 截图    | PixPin            |                 | PixPin     | 悬停+OCR+长截图 |
| 启动器   | Wox               |                 | Spotlight  |            |
| 论文    | zotero            | zotero          | zotero     |            |
|       |                   |                 |            |            |

+ 笔记-Obsidian-Markdown：Obsidian打开的单位是项目而非文件，而我个人成独立的Markdown项目只有这个CS-notes，编程项目通常使用VSCode，而VSCode也能编辑Markdown。故在我的场景下，Obsidian就是专门打开CS-notes的，并结合Git实现存档和多端同步。
+ 截图：最主要的需求是图片悬停，其次是将粘贴板的文本转换成图片悬停，偶尔会有OCR，极少极少会有长截屏；有三个选择，Snipaste，PixPin，iShot，Snipaste非常优雅且跨平台，但是后两个需求不能满足，PixPin支持Win和macOS，恰好覆盖需求，UI有点丑，iShot功能最强大但是只支持macOS。最终选择PixPin。

## 浏览器:Chrome

Chrome是六大浏览器之一，插件丰富，登陆谷歌账号同步信息和配置。

+ 操作系统：
    + Windows：Chrome默认安装C盘，使用默认，可在快捷方式右键查看位置
        + 假如使用Edge，Microsoft Edge也是Chromium内核，可以直接同步。
            + Edge在win上默认每个选项卡是一个窗口，很反直觉，解决方案如下：
                + win10：`设置` -> `系统` -> `多任务处理` -> `Alt + Tab`，打开就知道了。
                + win11：`设置` -> `系统` -> `多任务处理` -> "对齐或按Alt + Tab时显示应用中的标签页"改为"不显示选项卡"。
    + Linux：
    + macOS：

+ 配置与插件：
    + 增强：
        + Header Editor：使用谷歌总需要人工验证，可使用该插件避免，[教程](https://blog.azurezeng.com/recaptcha-use-in-china/)。
        + 标签分组扩展
        + crxMouse Chrome手势：前进后退、顶部底部、链接图片打开
        + Vimium：未使用
    + New Bing Anywhere
    + 油猴脚本
    + 身份验证器：用于双重验证，比如Github
    + 翻译：
        + 默认翻译：简单阅览网页时使用
        + 沉浸式翻译：网站全文翻译且保留原文原样式
    + Zotero：
        + Zotero Connector
    + 信息收集：
        >ref: [csdiy·必须工具·日常学习工作流](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/workflow/#_10) | [少数派·Vacodwave·3000+小时积累的学习工作流](https://sspai.com/post/75969)

        + 主动收集：Cubox，多端统一
        + 被动收集：RSSHub Radar+Feedly Mini，前者为任何网页创建RSS，后者为RSS接收和查看器

## 代理:Clash系

+ 操作系统：
    + Windows：
    + Linux：
    + macOS：配置不能通过URL直接导入，Windows中的配置文件后缀名是`yml`，macOS中是`yaml`，文件拷贝进来直接改名即可。

+ 配置：
    + 开机自启动
    + 使用F2作为开关快捷键

## 编程:终端
## 编程:VSCode
## 笔记:Obsidian

+ 操作系统：
    + Windows：
        + 安装：Obsidian默认安装C盘：不处理，软件位置右键快捷方式查看。
        + 该软件是围绕项目的，一个项目的相关配置放在项目目录下的`.obsidian`目录中。而这部分配置文件放在对应的项目下，所以不占C盘空间。
    + Linux：
    + macOS：

|         | Typora | Obsidian | VSCode |
| ------- | ------ | -------- | ------ |
| 编辑模式    | 即时渲染   | 即时渲染     | 分屏渲染   |
| 渲染效果    | 极好     |          |        |
| 方言      | 无      | 有，双链     |        |
| 跨平台     |        |          |        |
| 源码导出    |        |          |        |
| 多机同步    |        |          |        |
| 付费否     |        |          |        |
| 使用模式    | 单文件/项目 | 项目       | 单文件/项目 |
| Table支持 |        | 可支持Tikz  |        |
| LaTeX支持 |        |          |        |
| 代码画图支持  |        |          |        |
| 性能      | 卡      |          |        |
| 查看大纲    |        |          |        |

+ 插件推荐
    + Obsidian Git：多机同步必备，取消所有快捷键，因为核心功能主要有三个（如果熟悉Git的话）：add + commit、push、pull。而Obsidian也有类似VSCode的命令行模式（快捷键`Ctrl + p`或者`Command + p`），输出前缀`git`即有上面提到的几个选项，甚至在PC上，我都是命令行手动管理。
    + Advanced Tabled：Markdown表格相关补全，它存在大量的自定义，抽象程度低就意味着复杂，索性它提供了图形化的操作，鉴于表格用的本来就不多。我干脆没有设计快捷键。


## 论文:Zotero

+ Install
    + 官网：包含软件和浏览器插件
+ Usage：
    + 论文不像书籍，某个话题下可能有很多篇，Zotero可以用来维护论文文件（操作系统的文件系统也行）
    + 内置多种文献文件类型的阅读器，All in One阅读，比如CAJ（这似乎也不是一定要用它的理由）
        + 通过插件实现划词翻译
    + 有浏览器插件，可以一键导入文献文件（这个是不是有点方便了）
    + 导出文献的BibTeX类型数据文件（这个就很有用了）
    + 其他各种插件
+ config
+ extension：
    + Translate for Zotero：官网下载
    	+ Zotero和Zoreto7的该插件是不兼容的，从github release可能要找比较早的6版本才能用（如果使用Zotero6的话）

## 键盘与改键

由于在Windows中，只有`Ctrl+Insert`/`Shift+Insert`才能在任何环境（Windows GUI，Windows Terminla，Vim，SSH to Linux，SSH to Linux and Vim，SSH to Linux and Tmux）都适用，且我确实使用数字键盘次数很少。故选择必须有`Home`、`End`、`Insert`、`Delete`的84键盘，且该键盘必须支持Windows和Mac两个平台。
+ 外界键盘：利用改键软件将`Caps Lock`键改成方向键右键`rigth`

将`Caps Lock`键改成方向键右键`rigth`的作用
>个人大写输入使用`Shift`，几乎不用`Caps Lock`，而其位置又非常的好，市面上有很多关于其改键方案。

1. oh-my-zsh/oh-my-posh的历史命令补全是方向键右键，但是右手移动过去比较慢，正好输入命令中`Tab`比较常用，`Caps Lock`在它下面，可以用同一个手指按。用来加速历史命令补全
2. 在VSCode中跳转通常是按住`Ctrl`/`Command`然后鼠标左键点击名称，但是跳转过去之后怎么回来呢？我将快捷键设置成`Alt+Right`，就能实现单手`Go Back`（否则默认快捷键需要两个手）。当然这是在Windows和Linux，在macOS上没有好的方案。
    - 该方案目前废弃，选择一个功能键作为`Go Back`，目前使用`F3`

## 其他
这里以关键字罗列一些绝大部分场景都用不到，但是特定情况恰好解决需求的工具

### 工具箱

+ https://github.com/work7z/MDGJX
+ https://www.u.tools/
+ https://tools.fun/index.html
+ https://devtool.tech/
+ https://chuhai.tools/
+ https://smalldev.tools/
+ https://toolfinder.co/
+ https://kuanhsiaokuo.github.io/apple_power_user/overview.html
+ https://github.com/aoaostar/toolbox
+ 独属于macOS的：https://github.com/jaywcjlove/awesome-mac/blob/master/README-zh.md

### Modern Unix Tool
https://github.com/ibraheemdev/modern-unix
https://github.com/johnalanwoods/maintained-modern-unix

### 键鼠操作可视化keyviz
https://github.com/mulaRahul/keyviz

### Windows右键管理ContextMenuManager
https://github.com/BluePointLilac/ContextMenuManager

### GitHub Star管理
https://cn.piliapp.com/
https://github.com/cfour-hi/gitstars
