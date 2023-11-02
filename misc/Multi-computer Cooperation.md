下面的推荐尽可能支持多平台和多端。

## 摄像头扩展iVam
>因为拯救者R7000P没有摄像头

电脑和手机分别安装通过数据线连接可将手机作为笔记本摄像头

## 多系统桌面键鼠共享
[barrier](https://github.com/debauchee/barrier)

选择这个软件的原因是我的要求要平台，这里指出一些其他键鼠共享软件https://sspai.com/post/72143


+ 说明：
	+ 在win进入“用户账号控制页面”或者Ubuntu进入"活动"页面时不能使用
	+ 多系统文件拖拽不支持
	+ Bug：包括**内存泄露**和复制粘贴功能的失灵

<hr>

+ 善用日志，软件不能正常运行的ERROR都在里面
	+ 该软件issue极多（不能说是好事还是坏事），你遇到的问题很可能别人也遇到过（至少我的两次都是）
+ 对于服务端，确保防火墙打开端口`24800`
+ 无论是服务端还是客户端，在设置中关闭SSL  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/blog/设置入口.png" width=“100px”><img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/blog/SSL选项.png" style="zoom:81%">
+ 确保你的键盘没有打开Scroll Lock

### 下载
+ Windows10：github上的release有`.exe`的安装包
+ Linux(Ubuntu)：使用`snap install barrier`

### 使用

该软件的架构是在同一局域网内，分服务端和客户端
我使用的教程：[整体使用](https://goinglinux.com/articles/UsingSynergyOnLinuxAndWindows_en.htm)

#### 服务端
1. 设置（窗口）：  
	<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/blog/设置服务端.png" width="255px"><img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/blog/设置机器相对位置.png" width="500px">

2. 运行：点击运行

#### 客户端

1. 设置（服务端IP）：  
	![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/blog/客户端设置.png)

2. 运行：点击运行

## 移动端投屏
[scrcpy](https://github.com/Genymobile/scrcpy)  

[一个不错的教程](https://liarrdev.github.io/post/Scrcpy/)

### Install

+ win：[scoop](https://github.com/Genymobile/scrcpy#windows)

### Config

+ Android：
	1. 进入开发者模式
	2. 打开“USB调试”
	+ 华为：打开‘仅充电“模式下运行ADB调试”’

### Usage
>该项目分两个部分
>+ `adb`
>+ `scrcpy`

+ 确保已经配置好了移动端手机
	```bash
	adb devices  # 检测是否连接成功
	```

+ 运行：
	```bash
	scrcpy
	```
	+ Args:
		```bash
		–turn-screen-off (-S) # 关闭物理设备屏幕
		–stay-awake (-w) # 不锁屏
		-Sw # 上面两条的和
		–fullscreen (-f) #全屏
		```

+ 我的常用快新建：
	+ 左键
	+ 滚轮
	+ 右键返回
	+ 双击黑边消除黑边

+ issue
	+ [中文输入](https://github.com/Genymobile/scrcpy/issues/1055)：
		+ 我的机器：win10+华为 nove 7
		+ 我的方案：QQ输入法，PC换英文，移动端换全键双拼
			+ QQ输入法优点
				+ 轻松的换到双拼
				+ 对按Shift选择文本流畅

## 文件文本传输
什么花里胡哨的都不如微信QQ

## Twomon SE
据说这个能让pad做扩展屏？我还没有pad，先mark下

## 副屏扩展spacedesk
上面是键鼠共享，系统、算力都是各自的，但是这个是指定其他设备作为副屏

## win向ipad键鼠共享：向日葵app