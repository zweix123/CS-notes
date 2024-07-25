## What is the Command key for Windows?
>来自Windows老用户的疑问。

在CLI时代，修饰键使用Ctrl，在GUI时代，又多了很多快捷键，如何设计？Windows选择直接复用Ctrl（实际上还是添加了Windows键的，但是就像霸王龙的前肢），而Mac则选择添加新的修饰键，即Command。

所以

被人熟知的Ctrl+c是复制，Ctrl+v是粘贴，则在Mac中分别是Command+c和Command+v
>有人可能觉得Ctrl+cv最直觉，这可能是因为Windows的市场占有率太大了。

macOS这样处理的好处是在CLI时代的快捷键依然保留，比如在命令行中Ctrl+a是Home，Ctrl+e是End。同样的操作在Windows中可能无法实现。
>这里macOS中也有坏处，就是Home、End或者其等价操作在终端用不了，必须用使用Ctrl做修饰键的。

## 个人外接键盘喜好

由于在Windows中，只有`Ctrl+Insert`/`Shift+Insert`才能在任何环境（Windows GUI，Windows Terminla，Vim，SSH to Linux，SSH to Linux and Vim，SSH to Linux and Tmux）都适用，且我确实使用数字键盘次数很少。故选择必须有`Home`、`End`、`Insert`、`Delete`的84键盘，且该键盘必须支持Windows和Mac两个平台。
>实际上我用拯救者的全键盘和MacBook的键盘也挺开心的【捂脸】

# 配置

+ 通用配置：
    + 输入法使用默认输入法软件
    + 输入法只保留ABC和拼音
    + 输入法默认使用英文
    + 拼音设置为双拼且不自动扩展到全拼，双拼布局使用微软
    + 输入法切换只使用Ctrl/Control + Space

+ Windows：
    + 全半角和中英标点的切换设置为无
    + 翻页只有+/-
+ macOS：
    + 按下地球键时“不执行任何操作”：Fn/地球键只体现Fn
    + 将F1、F2等键用作标准功能键：需要按下Fn才能使用F键的功能
    + “所有输入法”：
        + 关闭使用大写锁定键切换“ABC”输入法
        + 关闭自动纠正拼写
        + 关闭自动大写字母的首字母
        + 关闭连按两下空格插入句号

## 改键

+ Windows笔记本自带键盘：通过注册表将`Caps Lock`键改成方向键右键`rigth`
+ MacBook自带键盘：交换左下角`Fn`和`Control`的位置，这是因为`Control`的使用频率远远大于`Fn`
    + 实际上我也希望修改它的`Caps Lock`为方向键右键`right`但是没有优雅（简约）的方案
+ 外界键盘：利用改键软件将`Caps Lock`键改成方向键右键`rigth`

将`Caps Lock`键改成方向键右键`rigth`的作用
>个人大写输入使用`Shift`，几乎不用`Caps Lock`，而其位置又非常的好，市面上有很多关于其改键方案。

1. oh-my-zsh/oh-my-posh的历史命令补全是方向键右键，但是右手移动过去比较慢，正好输入命令中`Tab`比较常用，`Caps Lock`在它下面，可以用同一个手指按。用来加速历史命令补全
2. 在VSCode中跳转通常是按住`Ctrl`/`Command`然后鼠标左键点击名称，但是跳转过去之后怎么回来呢？我将快捷键设置成`Alt+Right`，就能实现单手`Go Back`（否则默认快捷键需要两个手）。当然这是在Windows和Linux，在macOS上没有好的方案。
    + 该方案放弃，使用`F4`，这样全平台通用。

# 快捷键

## 软件

|      | Windows | macOS       |
| ---- | ------- | ----------- |
| 软件切换 | Alt+tab | Command+tab |
| 软件全屏 | Win+up  | 双击软件边框（乐）   |
| 关闭窗口 | Ctrl+w  | Command+w   |
| 关闭软件 | Alt+F4  | Command+q   |

## 终端

|      | Windows | macOS    |
| ---- | ------- | -------- |
| Home | Home    | Ctrl + a |
| End  | End     | Ctrl + e |

## 编辑器

+ 全选，保存，撤退，剪切，复制，粘贴，Windows和macOS分别以Ctrl和Command为修饰键，后接a，s，z，x，c，v。
+ 选中：按住Shift使用方向键。
+ 功能键：
    + Windows使用Insert，macOS用不到Insert
    + Windows使用Delete，macOS使用Command + backspace，其实在编辑器中是删除到行首，在编辑器外是Delete，好用。
    + Windows使用Home，macOS使用Command + left
    + Windows使用End，macOS使用Command + right

    还有

    |        | Windows    | macOS        |
    | ------ | ---------- | ------------ |
    | Top    | Ctrl+Home  | Command+up   |
    | Button | Command+up | Command+down |

|           | Windows           | macOS               |
| --------- | ----------------- | ------------------- |
| 按word单位移动 | 按住Ctrl使用方向键       | 按住Option使用方向键       |
| 按word单位删除 | 按住Ctrl使用backspace | 按住Option使用backspace |
>这里macOS更智能，Windows不能识别中文中的一个word

### VSCode

+ 特别的
    + 在mac上，打开short key的页面，不同的输入法是不同的。所以对于某些快捷键，需要在每种输入法下分别设置下。

+ VSCode命令行相关：命令`code`，打开VSCode，`code .`则是在当前目录打开VSCode
+ Command Center：即UI顶部的输入框，默认项目下文件检索，通过添加前缀实现各种功能，下面是我常用的
    + Go to find：默认`Ctrl/Comand + p`，相当于fd
	+ Go to Line:  默认`Ctrl/Command + g`，相当于vim的`数字 + g`
	+ Go to Symbol：默认`Ctrl/Command + Shift + O`
	+ Show and Run Cmd：默认`Ctrl/Command + Shift + P`，下文说的命令即为了这里的命令，这里聊一些常用命令
		+ `shortcuts`：快捷键设置页面
		+ 选中文本大学写转换：`upper`、`lower`
		+ 代码块折叠：`fold`和`unfold`，可以按层级折叠

+ 查找：`Ctrl/Command+f`（当前文件）和`Ctrl/Command + Shift + f`（当前项目）（相当于rg）
+ 多光标：
    + Alt/Option+鼠标点击
    + 选中文本->`Command+d`/`Ctrl+Alt+d`：相同文本多光标
        + 如果希望全文全部相同文本都选中（并出现光标）：`Command`/`Ctrl`+`F2`
    + `Ctrl + Alt`/`Option + Command`->方向键上下

+ 光标在terminal与workspace切换，以及在workspace中的不同窗口切换：
    + win：`Ctrl+~`和`Ctrl+num`
    + mac：`Ctrl+·`和`Command+num`：看起来有点反直觉，但是mac不能`Comamnd+·`的快捷键

    首先使用上面的快捷键可以在终端和不同窗口之前选择，其次单独使用终端相关的则是打开/关闭，关闭自然就会到workspace了。

    进一步，使用`Ctrl/Command + Shift + j`则是将Terminal的全屏和取消全屏

+ 格式化：`Shift`+`Alt`/`Option`+`f`，效果依赖插件，大部分项目设置为`format on save`

+ 名称跳转：
    + `Ctrl`/`Commad`+`鼠标左键点击`
    + Go Back：
        + win：`Alt`/`Option`+`方向键Right`
        + mac：`Ctrl+``
