[Wikipedia: De facto standard](https://en.wikipedia.org/wiki/De_facto_standard)

+ 一个现象：某项设计未必是客观最优的方案，要么是一种较优的方案，要么是受限于当时的某些条件。但是其由于各种历史巧合占据了市场。相关配套设施依照它的设计进行设计，而其他同类软件为了某些目的（用户较于成本、利用配套设施）也采用类似的设计。从而形成正循环。

我希望在这里记录这样的东西，即一种最接近道的术。

## 软件配置

1. 所有的软件配置在最底层都是基于**文本**的。即使现在有了各种UI来进行设置，但是存储这些配置的肯定是某个文本文件。而和开发接近的软件一般这个/些文本文件肯定是可达的。
2. 软件配置可以是分层的，比如VSCode的配置就有User Settings和Workspace Settings，而Obsidian里的配置则是围绕项目的（项目根目录的`.obsidian`文件），这也相当于一种Workspace Settings

## 现代编辑器UI设计

+ Menu Bar菜单栏：顶部，左包含`File`、`Help`等等**选项卡**，右包含**最小化**、**全屏**、**关闭** Button按钮（坐井观天了，MacOS不是这样的）
+ Status Bar状态栏：底部
+ Activity bar活动栏：最左侧，上包含插件或者基本功能，下包含账户和设置
+ Side Bar：左Primary Side Bar，右Secondary Side Bar

## What is the Command key for Windows?
>来自Windows老用户的疑问。

在CLI时代，修饰键使用Ctrl，在GUI时代，又多了很多快捷键，如何设计？Windows选择直接复用Ctrl（实际上还是添加了Windows键的，但是就像霸王龙的前肢），而Mac则选择添加新的修饰键，即Command。

所以

被人熟知的Ctrl+c是复制，Ctrl+v是粘贴，则在Mac中分别是Command+c和Command+v
>有人可能觉得Ctrl+cv最直觉，这可能是因为Windows的市场占有率太大了。

macOS这样处理的好处是在CLI时代的快捷键依然保留，比如在命令行中Ctrl+a是Home，Ctrl+e是End。同样的操作在Windows中可能无法实现。
>这里macOS中也有坏处，就是Home、End或者其等价操作在终端用不了，必须用使用Ctrl做修饰键的。
