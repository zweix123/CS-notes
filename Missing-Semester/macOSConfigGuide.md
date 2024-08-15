## 基本配置

+ [键盘基本配置](Missing-Semester/Keyboard.md#配置)
    + [键盘改键](Missing-Semester/Keyboard.md#改键)
+ 其他设置：
    + 外观：深色
    + 桌面背景：纯色黑色
+ 鼠标：Mos
    + 翻转方向（对触摸板也有效）
    + 转换键设置为Shift
    + 开机自启动
+ 其他基本操作相关软件：
    + KeyboardHolder：记住当前软件使用的输入法，避免切换IM和VSCode时还要换输入法（举个例子）
    + 菜单栏管理：Bartender，状态栏，即左上角的图标，当过多时，macOS的处理是直接不显示x.x，该软件可以看到所有。

### 键盘

+ 通用配置：
    + 输入法使用默认输入法软件
    + 输入法只保留ABC和拼音
    + 输入法默认使用英文
    + 拼音设置为双拼且不自动扩展到全拼，双拼布局使用微软
    + 输入法切换只使用Ctrl/Control + Space

+ macOS：
    + 按下地球键时“不执行任何操作”：Fn/地球键只体现Fn
    + 将F1、F2等键用作标准功能键：需要按下Fn才能使用F键的功能
    + “所有输入法”：
        + 关闭使用大写锁定键切换“ABC”输入法
        + 关闭自动纠正拼写
        + 关闭自动大写字母的首字母
        + 关闭连按两下空格插入句号

+ 改键：Windows笔记本自带键盘：通过注册表将`Caps Lock`键改成方向键右键`rigth`
+ 改键：MacBook自带键盘：交换左下角`Fn`和`Control`的位置，这是因为`Control`的使用频率远远大于`Fn`
    + 实际上我也希望修改它的`Caps Lock`为方向键右键`right`但是没有优雅（简约）的方案
+ 外界键盘：利用改键软件将`Caps Lock`键改成方向键右键`rigth`

将`Caps Lock`键改成方向键右键`rigth`的作用
>个人大写输入使用`Shift`，几乎不用`Caps Lock`，而其位置又非常的好，市面上有很多关于其改键方案。

1. oh-my-zsh/oh-my-posh的历史命令补全是方向键右键，但是右手移动过去比较慢，正好输入命令中`Tab`比较常用，`Caps Lock`在它下面，可以用同一个手指按。用来加速历史命令补全
2. 在VSCode中跳转通常是按住`Ctrl`/`Command`然后鼠标左键点击名称，但是跳转过去之后怎么回来呢？我将快捷键设置成`Alt+Right`，就能实现单手`Go Back`（否则默认快捷键需要两个手）。当然这是在Windows和Linux，在macOS上没有好的方案。
    - 该方案目前废弃，选择一个功能键作为`Go Back`，目前使用`F3`

## 基本战力形成

### 下载浏览器Chrome并登陆谷歌账号

[笔记](./README.md#浏览器chrome)

### 科学上网ClashX

[笔记](./README.md#代理clash系)

### 包管理器brew

1. 首先下载XCode：
    ```bash
    xcode-select --install
    ```

2. 按照[Manual](https://brew.sh/zh-cn/)执行下载命令

### 安装Git->SSH生成密钥->配置Github

1. Git安装: `brew install git`
2. Git配置: [笔记](./Git.md#config)
3. SSH生成密钥: [笔记](./SSH.md#tldr)
4. 将SSH公钥上传到Github上: [笔记](./Git.md#config-1)
5. 克隆CS-notes
### 下载Obsidian
+ 安装：直接安装
+ 其他：[笔记](./Markdown.md)
 
## 其他必装软件

### 命令行配置
[笔记](Missing-Semester/Terminal.md#unix-linux-and-macos)
### 编辑器VSCode

+ 安装：直接安装
+ 配置：配置通过Github账号同步，配置一次后只需要登陆账号即可
  + 全面配置[笔记](./VSCode.md)
