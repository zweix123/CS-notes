# LinuxConfigGuide
>Linux有众多发行版、机器也分云服务器、虚拟机和物理机，该指南并没有限制某种机器，对独属于某种机器的问题会单独说明，请读者选择对您有帮助的部分

## 0.机器检查

+ `ping`检查网络：
	+ IPv6：`ping mirrors.tuna.tsinghua.edu.cn -c 4`
	+ IPv4：`ping www.baidu.com -c 4`
	+ 外网：`ping www.youtube.com -c 4`

## 1.创建用户

>建议为机器创建非root用户，后续使用在非root用户中

```bash
adduser 用户名 # 创建用户
# 需要填写密码、重复密码以及其他信息，其他信息无脑回车即可，最后Y确认
usermod -aG sudo 用户名 # 给用户分配sudo权限
# 用户在第一次使用sudo时要求输入root用户密码
passwd 用户名 # 修改用户密码, 这种方法也可以修改root用户

# hostname 主机名  # 可修改主机名, 需要重启终端才可以查看修改
```

## 2.配置SSH

>[这](./SSH.md)是我的SSH小教程：

1. 配置：
	```bash
	ssh-keygen && touch ~/.ssh/authorized_keys ~/.ssh/config  # 之后一路回车+y
	```

2. **将公钥放置到GitHub上**  
	+ 测试：
		```
		ssh -T git@github.com
		```

## 3.修改软件源

+ 源位置：`/etc/apt/sources.list`

1. 备份：
	```bash
	sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup
	```

2. 按照系统版本选择合适的源：
	>查看系统版本的命令
	>```bash
	>lsb_release -a
	>```

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

### 文本编辑器

Linux下的文本编辑器非常之多，上面使用vi就是一种，选择看个人喜好  
且也是一种可玩性很好的软件，所以[单拿出来](Linux/vi.md)，记录有配置和用法

### 终端复用器

tmux

+ 使用：我的[笔记](Linux/tmux.md)

### Git

+ 配置：我的[教程](./Git.md#config)
+ 使用：我的[笔记](./Git.md)

### zsh

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

相关问题见[我的教程](./WindowsConfigGuide.md#虚拟机vmware-workstation-pro)
