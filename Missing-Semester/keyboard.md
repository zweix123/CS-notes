+ 对Windows用户来说，Mac的Command键是什么？
    >来自Windows老用户的疑问。

    在CLI时代，修饰键使用Ctrl，在GUI时代，又多了很多快捷键，如何设计？Windows选择直接复用Ctrl，而Mac则选择添加新的修饰键，即Command。

    所以

    被人熟知的Ctrl+c是复制，Ctrl+v是粘贴，则在Mac中分别是Command+c和Command+v
    >有人可能觉得Ctrl+cv最直觉，这是可能是因为Windows的市场占有率太大了。

    macOS这样处理的好处是在CLI时代的快捷键依然保留，比如在命令行中Ctrl+a是Home，Ctrl+e是End。同样的操作可能在Windows中可能无法实现。
    >这里macOS中也有坏处，就是Home、End或者其等价操作在终端用不了，必须用使用Ctrl做修饰键的。

+ 键盘选择与配置：
    + 外接键盘使用84键盘且必须有`Home`、`End`、`Insert`、`Delete`，因为Windows在CLI和GUI中混用`Ctrl`导致`Ctrl + c/v`并不能在任何环境都适用，只有`Ctrl + Insert`作为复制、`Shfit + Insert`作为粘贴，才能在各种环境（win、terminal、vim、ssh to linux、ssh to linux and vim、ssh to linux and tmux）都适用。通过改建基本可以兼容两平台。
        >实际上MacBook自带键盘真挺好的。

    + 切换输入法：`Ctrl + space` and `Control + space`，其中MacBook上左下角修饰键顺序为`Fn` -> `Control` -> `Option` -> `Command`，鉴于`Control`的使用频率远远大于`Fn`，使用设置交换两者位置。
    + 关于`Cap Lock`：个人输入大写通常通过`Shift`，几乎不用`Cap Lock`，但它的位置又非常的好，业界有很多对其按照个人习惯改键的方案，我是将其改成“方向键右键”（非常逆天）
        + Windows：通过修改注册表修改
        + Mac：MacBook键盘不能修改，外接键盘通过改建软件（VIA）修改
        + VSCode：在Windows中将`Go back`改成`Alt+right`（逆天）实现单手光标跳转；在macOS由于自带键盘无法修改还是使用默认的`Ctrl+减号`
    
+ 触控板

    |      | Windows  | macOS    |
    | ---- | -------- | -------- |
    | 左键 | 单指轻点 | 单指重点 |
    | 右键 | 双指轻点 | 双指重点 |

    各有好处，轻点确实更舒服，但是容易误触。

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
    + Windows使用Delete，macOS使用Command + backspace
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

+ VSCode命令行相关：命令`code`，打开VSCode，`code .`则是在当前目录打开VSCode
+ Command Center：即UI顶部的输入框，默认项目下文件检索，通过添加前缀实现各种功能，下面是我常用的
	+ Go to Line:  默认`Ctrl/Command + G`，相当于vim的`数字 + g`
	+ Go to Symbol：默认`Ctrl/Command + Shift + O`
	+ Show and Run Cmd：默认`Ctrl/Command + Shift + P`，下文说的命令即为了这里的命令，这里聊一些常用命令
		+ `shortcuts`：快捷键设置页面
		+ 选中文本大学写转换：`upper`、`lower`
		+ 代码块折叠：`fold`和`unfold`，可以按层级折叠

+ 查找：`Ctrl/Command+f`（当前文件）和`Ctrl/Command + Shift + f`（当前项目）
+ 多光标：
    + Alt/Option+鼠标点击
    + 选中文本->`Command+d`：相同文本多光标
        + 如果对全文全部相同文本都出现光标：`Command+F2`
    + Option+Command+方向键上下

+ `Ctrl + ~`/`Ctrl + num`光标切换terminal于workspace
    + `Ctrl + j`显示/关闭Terminal，`Ctrl + Shift + j`则是Terminal全屏/取消全屏
+ `Ctrl + b`：打开/关闭左边栏
+ `Ctrl + Shift b`：光标跳转/返回到资源管理器

+ 格式化：`Shift + Alt + f`，效果依赖插件，大部分项目设置为`format on save`

+ 名称跳转：
    + `Ctrl + 鼠标左键点击`
    + `Alt + 方向键左键`返回到上次光标位置：但是这个快捷键需要两个手，一般都是我正在跳转准备调回来，拿到我还要右手离开鼠标么？而我为了补全zsh的历史命令补全将Caps设置为方向键右键，于是将这个快捷键设置为`Alt + 方向键右键`实现单手操作

+ 常用命令：
	+ 格式化：手动，快捷键`Shift + Alt + f`，效果依赖于插件
	+ 命令`Fold All`可以指定层级
