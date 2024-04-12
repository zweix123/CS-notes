+ 首先Apple系的各个产品使用的操作系统是不同的，比如MacBook是macOS，iPhone是iOS，iPad是iPadOS，这也是为什么同是苹果的产品有些软件只能存在部分设备中。
	>这下被鸿蒙遥遥领先了。

+ 然后是对Windows人比较迷惑的`Command`键了，是这样的，`Ctrl`（`Control`）和`Alt`（Apple系是`Option`）在只有终端的时期也是有的。只有Windows的`win`和Apple的`Command`后添加的。原因在于CLI和GUI不同的操作逻辑。Windows是直接使用了`Ctrl`，`win`键是一个比较尴尬的位置。而Apple则是添加一个新的按键`Command`（我觉得这个更合理）。

	真对这个问题（主要是我各种平台的机器都用），我下面展示一个尽可能统一的方案。

	真对键盘最下面一行空格左边的部分，
	+ Windows：Ctrl, Fn, Win, Alt
	+ Mac: Fn/地球键, control, option, command

	改键成

	+ Windows：通过TODO，改成 Ctrl，Fn，Alt，Win
	+ Mac：通过默认提供对修饰键的修改，改成 control，Fn/地球键，option，command

	>相当于每个人都修改一对，公平【狗头】

	逻辑在于，Windows中使用Ctrl还是比较频繁的，不放在左下角使用小拇指够起来太困难了，而在mac中确实要使用Command来进行GUI的操作（全选复制剪切粘贴），放在第三个位置够起来比较费劲。

	有一个小点就是Fn，在Mac中还作为地球键，可以配置额外的功能，这里仅仅作为Fn键使用

	+ 还有一个问题是Cap和切换输入法。我个人使用输入法都是使用Shift，而Cap占着重要的位置怎么利用起来呢？一般情况我将其映射成`Right`方向键用来加速ohmyzsh/ohmyposh的补全（估计只有我一个人这么做吧）。而在Mac中，该键还用来切换输入法。其他系统中我通常Ctrl+Space来切换输入法，这里也可以统一。

## 初始设置

+ 语言配置：
	+ 输入：去掉简体拼音，换成简体双拼
		+ 将双拼输入法改成微软

+ 键盘配置：思路如上，这里记录过程
	+ 关闭Cap本来的功能
		+ 切换输入法：设置-键盘-文字输入-编辑-所有输入法-使用“中/英”切换“ABC”输入法
		+ 切换大小写：设置-键盘-键盘快捷键-修饰键-大写锁定键-无操作
	+ 交换Fn和Control位置：设置-键盘-键盘快捷键-修饰键
	+ 设置切换输入法方式：设置-键盘-键盘快捷键-输入法

## 科学上网

我个人使用的是Clash for Mac —— ClashX，目前似乎也有一些新的、在维护的软件。这里不讨论。

我个人遇到的一些坑点就是，使用的魔法不能直接通过URL导入，然后直接拷贝配置文件，需要修改后缀名之后才能正确使用。

+ 配置：
	+ 开机自启动
	+ `F2`作为开关System Proxy的快捷键

## 命令行

### 包管理器brew

+ 首先下载XCode：
	```bash
	xcode-select --install
	```

+ 然后按照Manual下载[官网](https://brew.sh/zh-cn/)

## 编辑器VSCode

[]()

## 图片悬停Snipaste

公测版

+ 配置
	+ 开启自启动
+ 快捷键：
	+ 截屏：F1（默认）
	+ 悬停粘贴板：F3（默认）
