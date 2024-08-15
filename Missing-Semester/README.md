Missing-Semester是MIT的一个计算机课程，学习学校不会教但是非常有用的工具。该目录本意也是该课程的笔记。在中科大“一生一芯”活动中，老师用了一节课的时间强调“工具是第一生产力”。在我个人的实践中，这句话也得到了印证。于是该目录的范围扩展为效率工具与工作流。相信我，它让我变得更强了。

# 第一性原理

1. 摸索一套自己的工作流的投入产出比是极高的，别怕麻烦
2. 严格遵守奥卡姆剃刀原理：“如无必要、勿增实体”
    - 依照需求寻求工具，而非因工具能力而创造需求
    - 不要大而全的工具，而要恰好满足需求的小而精的工具。

# Sum

从大学算起，我个人使用机器的经历是：3年Windows->1年Linux->?年macOS，故后面大概只会更新macOS相关的了。

| OS    | Windows           | Linux           | macOS      | 需求         |
| ----- | ----------------- | --------------- | ---------- | ---------- |
| 浏览器   | Chrome            | Chrome          | Chrome     |            |
| 代理    | Clash for Windows | Clash for Linux | ClashX Pro |            |
| Shell | Powershell7       | zsh             | zsh        |            |
| 终端    | Windows Terminal  | Terminal        | Terminal   |            |
| 包管理器  | Scoop             | 原生              | brew       |            |
| 编程    | VSCode            | VSCode          | VSCode     |            |
| 笔记    | Obsidian          | Obsidian        | Obsidian   | Markdown   |
| 论文    | zotero            | zotero          | zotero     |            |
| 启动器   | Wox               |                 | Spotlight  |            |
| 截图    | PixPin            |                 | PixPin     | 悬停+OCR+长截图 |
|       |                   |                 |            |            |

+ 笔记-Obsidian-Markdown：Obsidian打开的单位是项目而非文件，而我个人成独立的Markdown项目只有这个CS-notes，编程项目通常使用VSCode，而VSCode也能编辑Markdown。故在我的场景下，Obsidian就是专门打开CS-notes的，并结合Git实现存档和多端同步。
+ 截图：
    + 最主要的需求是图片悬停，其次是将粘贴板的文本转换成图片悬停，偶尔会有OCR，极少极少会有长截屏。
    + 有三个选择，Snipaste，PixPin，iShot，Snipaste非常优雅且夸平台，但是后两个需求不能满足，PixPin支持Win和macOS，恰好覆盖需求，UI有点丑，iShot功能最强大但是只支持macOS

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
        + 键鼠：
            + crxMouse Chrome手势：前进后退、顶部底部、链接图片打开
            + Vimium：未使用
        + AI：
            + New Bing Anywhere
    + 油猴脚本
    + 身份验证器：用于双重验证，比如Github
    + 翻译：
        + 默认翻译：简单阅览网页时使用
        + 沉浸式翻译：网站全文翻译且保留原文原样式
    + Zotero：
        + Zotero Connector
    + 信息收集：
        + 主动收集：Cubox，多端统一
        + 被动收集：RSSHub Radar+Feedly Mini，前者为任何网页创建RSS，后者为RSS查看器

### 信息输入

+ Ref：
    + [csdiy·必须工具·日常学习工作流](https://csdiy.wiki/%E5%BF%85%E5%AD%A6%E5%B7%A5%E5%85%B7/workflow/#_10)
        + [少数派·Vacodwave·3000+小时积累的学习工作流](https://sspai.com/post/75969)

+ 痛点：
    + 稳定的周期更新的输出内容分散，通过**RSSHub Radar**（浏览器插件）和**Feedly mini**（浏览器插件）解决
        + [x] Windows(Chrome)
        + macOS(Safari)：不配置，Chrome是独立于系统的，macOS中也有Chrome，以Chrome为主（谷歌账号多端同步）
    + 多个端的收藏分别维护在本地，不能统一，通过**CuBox**（浏览器插件）解决
        + [x] Windows and Chrome
        + [x] macOS and Safari
        + [x] Android
        + [x] iPad and Safari
+ 难点：多端指PC、macOS、Android、IPhone、IPadOS，几乎包含了所有平台，我要求方案可以在以上所有平台有效。

+ 对于Ref的方案中，没有采纳的特性：
    + 多种类型信息转换成markdown或者pdf汇总到obsidian
        + 多种知识肯定会以不同的语言描述，如果仅仅是留存双链而没有经过我自己的消化并不是我想要的。
        + 可能对于论文的场景这样有好处，比如一篇笔记和一篇论文有关，笔记有利于整理框架，

## 代理:Clash系

+ 操作系统：
    + Windows：
    + Linux：
    + macOS：配置不能通过URL直接导入，Windows中的配置文件后缀名是`yml`，macOS中是`yaml`，文件拷贝进来直接改名即可。

+ 配置：
    + 开机自启动
    + 使用`TODO`作为开关快捷键

## 笔记软件:Obsidian

+ 操作系统：
    + Windows：
        + 安装：Obsidian默认安装C盘：不处理，软件位置右键快捷方式查看。
        + 该软件是围绕项目的，一个项目的相关配置放在项目目录下的`.obsidian`目录中。而这部分配置文件放在对应的项目下，所以不占C盘空间。
    + Linux：
    + macOS：

[笔记](./VSCMD.md#obsidian)
