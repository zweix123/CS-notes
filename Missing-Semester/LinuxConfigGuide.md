# LinuxConfigGuide

>Linux有众多发行版、机器也分云服务器、虚拟机和物理机，该指南并没有限制某种场景，对独属于某种场景的问题会单独说明，请读者选择对您有帮助的部分。

这里的包管理器是Ubuntu的`apt`，如果是其他发行版，要使用对应的包管理器。

+ 查看Linux发行版和版本的命令：
    ```bash
    uname -a
    lsb_release -a
    ```

## 0.机器检查

+ `ping`检查网络：
	+ IPv6：`ping mirrors.tuna.tsinghua.edu.cn -c 4`
	+ IPv4：`ping www.baidu.com -c 4`
	+ 外网：`ping www.youtube.com -c 4`

## 1.创建用户

>建议为机器创建非root用户，后续使用也在非root用户中，如果当前用户已经是非root用户，则不需要创建

```bash
adduser 用户名 # 创建用户
# 需要填写密码、重复密码以及其他信息，其他信息无脑回车即可，最后Y确认
passwd 用户名 # 修改用户密码, 这种方法也可以修改root用户
hostname 用户名  # 修改主机名, 需要重启终端才可以查看修改

# 给用户分配sudo权限
usermod -aG sudo 用户名  # Ubuntu
usermod -aG wheel 用户名  # Centos
```

## 2.配置SSH

+ 配置：[我的教程](./SSH&Git.md#21-ssh)，通常作为服务端和客户端都要配置（作为服务端本机连接，作为客户端连接Github）

## 3.修改软件源

>目前只适合Ubuntu

+ 文件位置：`/etc/apt/sources.list`

1. 备份：
	```bash
	sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
	```

2. 按照系统版本选择合适的源：

	>[清华源](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)、[中科大源](https://mirrors.ustc.edu.cn/repogen/)

	```bash
	sudo vi /etc/apt/sources.list
	```

3. 更新：
	```bash
	sudo apt update # 让系统知道所有包的最新信息
	```

	```bash
	sudo apt upgrade # 让新的包的信息更新所有软件  # 时间较长  # 我通常不用  # 尽量不要用
	```

## 4.下载刚需软件
>Linux下通常有包管理器，下面的软件没有说明下载方式的软件一般都可以通过包管理器下载

### vim
>文本编辑器

[笔记](misc/linux/vim.md)

### tmux
>终端复用器

+ 作用：
  + 多个终端
  + 断开SSH而不影响命令执行

+ 使用：[笔记](misc/linux/tmux.md)

### git

+ 配置：[笔记](./SSH&Git.md#22-git)
+ 使用：[笔记](./SSH&Git.md#33-git)

### zsh

[笔记](Missing-Semester/Terminal.md#unix-linux-and-macos)

## 5.导入软件配置

导入[我的配置](https://github.com/zweix123/unix-config)

## 其他开发环境

### C++

```bash
sudo apt install build-essential  # gcc g++ make
sudo apt install cmake            # cmake

sudo apt install clang-format     # clang-format
```

# 物理机

## 改键

>具体脚本也在我的配置中

+ `Caps`->`right`：用于zsh的历史命令补全
```bash
# xmodmap -pke
# xmodmap -pm
xmodmap -e "remove lock = Caps_Lock"
xmodmap -e "keycode 66 = Right NoSymbol Right"
# 还原：setxkbmap 或者 setxkbmap -option
```

## 软件

### deb
这里以VSCode为例

+ 下载：官网提供`deb`类型的安装包

+ `deb`类型安装包的简单语法：`dpkg`命令：
	+ `dpkg -i 安装包`：安装/升级
	+ `dpkg -L 软件名`：查看安装位置
	+ `dpkg -r 软件名`：不清除配置卸载
	+ `dpkg -P 软件名`：清除配置卸载

+ config：内容多且散，而且无关平台，我将其放在这个[教程](./VSCode.md)

### AppImage
这里以Obsidian为例

Obsidian提供的文件类型是`AppImage`，加上可执行权限（`chmod +x xxx.AppImage`）就可以直接运行。  
我们要想办法把它做成Desktop File桌面文件放在Application Window应用程序窗口，继而放到Application Launcher应用程序启动器中。

+ Desktop File：文件后缀名为`desktop`，通常放在目录`/usr/share/applications`或`~/.local/share/applications`中，放在这里后就会出现在Application Window中
	+ 格式：下面以Obsidian为例（这里的值大小写我不知道是否关键，这种事情我通常避免麻烦都小写）
		```
		[Desktop Entry]
		Name=obsidian
		Type=Application
		Exec=/opt/apps/obsidian.AppImage
		Icon=/usr/share/icons/obsidian.png
		Terminal=false
		StartupNotify=true
		Categories=Development
		```

	+ 这里`/usr/share/icons/`目录通放置图标
	+ 这里`/opt/`目录通常放置第三方软件，我看有个目录叫`apps`叫放进来了。

### misc

+ [解决 Ubuntu22 Alt + Tab 后的滚动错误行为](https://blog.csdn.net/qq_33512762/article/details/128985799)

# 云服务器

# 虚拟机
