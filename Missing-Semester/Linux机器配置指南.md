>Linux有众多发行版、机器也分云服务器、虚拟机和物理机，该指南并没有限制某种机器，请读者选择对您有帮助的部分

+ 备份：
	+ 各软件配置已上云（[地址](https://github.com/zweix123/linux-config)）
	+ `~/.gitconfig`：不再使用，现用现配
	+ `~/ssh/config`：不再使用

[姊妹篇：Win机器配置指南](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/win10%E5%BC%80%E5%8F%91%E6%9C%BA%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97.md)

## 机器检查

+ `ping`检查网络：
	+ IPv6：`ping mirrors.tuna.tsinghua.edu.cn -c 4`
	+ IPv4：`ping www.baidu.com -c 4`

## 初始设置

### 创建用户

>建议为机器创建非root用户，后续使用在非root用户中

```bash
adduser 用户名 # 创建用户
# 需要填写密码、重复密码以及其他信息，其他信息无脑回车即可，最后Y确认
usermod -aG sudo 用户名 # 给用户分配sudo权限
# 用户在第一次使用sudo时要求输入root用户密码
su passwd 用户名 # 修改用户密码, 这种方法也可以修改root用户

# hostname 主机名  # 可修改主机名, 需要重启终端或机器才可以查看修改
```

### 修改源

+ 源位置：`/etc/apt/sources.list`

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
	# sudo apt upgrade # 让新的包的信息更新所有软件
	```

### end

+ 导入配置和备份
+ 配置ssh（[我的教程](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/SSH.md)）

## 刚需软件
Linux通常有包管理器

### vim

### tmux

### git
要求已经配置好了ssh

+ 初始化：类似Windows（[我的win10开发机配置指南](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/win10%E5%BC%80%E5%8F%91%E6%9C%BA%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97.md#5.-Git)）

### shell

+ 通识：
	+ `echo $SHELL`查看使用shell
	+ `cat /etc/shells`查看机器有的shell程序
	+ `chsh -s shell绝对路径`设置默认shell
		>[关于chsh](https://wangchujiang.com/linux-command/c/chsh.html)

#### 强化
[我的配置](https://github.com/zweix123/linux-config)（嘎嘎好用）

主要通过zsh和oh-my-zsh，前者是和bash一样的一个shell，但是它有更强的拓展性，但是想通过配置利用这些扩展性比较复杂，oh-my-zsh相当于一种辅助配置工具

1. 下载`zsh`：[Manual](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH)，一行命令即可  
	更新默认shell：`chsh -s $(which zsh)`
	>实际上这边建议不要着急修改，在clone oh-my-zsh会提示是否修改默认shell

2. 下载oh-my-posh：[Manual](https://github.com/ohmyzsh/ohmyzsh/wiki)
	>这里提供几个国内镜像源：
	>```bash
	>sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh)"
	>sh -c "$(wget -O- https://gitee.com/pocmon/mirrors/raw/master/tools/install.sh)"
	>```

	+ 镜像源好像G掉了，这里说明下
		1. https://blog.csdn.net/m0_56681539/article/details/127912811
		2. https://blog.csdn.net/u014454538/article/details/123563034
		实际上我还关闭了防火墙，然后hosts里有很多其他教程的东西，不知道有没有影响。

+ 命令：
	+ 刷新配置效果：`source ~/.zshrc`

+ `~/.zshrc`：oh-my-zsh配置文件
	+ 语法：
		+ `ZSH_THERE="random"`：配置主题，这里使用随机主题
		+ `plugins=(插件1 插件2 ... 插件n)`：配置插件，插件名之间空格隔开

+ `~/.oh-my-posh`：oh-my-zsh配置
	+ `~/.oh-my-zsh/plugins/`插件目录：每个目录即为一个插件名，目录下的`.sh`文件可查看其逻辑
		>不过下面的两个插件并没有安装在这里

+ 插件推荐：
	>插件的能否下载依照Github的可连接程度，注意本机clone下载后scp到服务器的方法中，如果本机和服务器的OS不同的情况下，可能由于编码原因报错

	+ `git`：默认安装，手动配置，为git命令提供缩写，可在插件目录下的sh文件查看
	+ `z`：默认安装，手动配置，目录快速调转
		+ history：`~/.z`
		+ 命令：`z 目录`
	+ `zsh-syntax-highlighting`：手动安装，手动配置，语法高亮
		```bash
		git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
		```
		
	+ `zsh-autosuggestions`：手动安装，手动配置，命令历史补全
		```bash
		git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
		```
		>这里的网址就是没有`.git`，Manual就没有  

		下面提供国内镜像
		```bash
		git clone https://gitee.com/phpxxo/zsh-autosuggestions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
		```

## 其他软件
需要机器有图形化

### VSCode

+ 下载：官网提供`deb`类型的安装包

+ `deb`类型安装包的简单语法：`dpkg`命令：
	+ `dpkg -i 安装包`：安装
	+ `dpkg -L 软件名`：查看安装位置
	+ `dpkg -r 软件名`：不清除配置卸载
	+ `dpkg -P 软件名`：清除配置卸载

+ 配置和Windows类似（[我的配置](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/win10%E5%BC%80%E5%8F%91%E6%9C%BA%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97.md#7%E7%BC%96%E8%BE%91%E5%99%A8vscode)）

#### 开发Golang
微软[教程](https://learn.microsoft.com/zh-cn/azure/developer/go/configure-visual-studio-code)已经足够亲爹

### Obsidian

+ 安装包类型为`AppImage`，所有东西放在一个文件内，赋予其可执行权限即可运行软件。不过它单纯的是个文件，想要变成有图标的应用程序需要处理

+ 我的管理方式：
	+ `~/AppIamges/`管理AppImage类型
	+ `~/.icons/`管理AppImage应用程序的图标

我们以Obsidian为例走一个这个过程

0. 下载Obsidian的AppImage类型安装包并`mv`到`~/AppImages/obsidian.AppImage`
1. 编辑文件`obsidian.desktop`
	```
	[Desktop Entry]
	Name=obsidian
	Version=1.1.9
	Type=Application
	Exec=/home/$用户名/AppImages/obsidian.AppImage
	Icon=/home/$用户名/.icons/obsidian.png
	Terminal=false
	StartupNotify=true
	```
	照猫画虎修改即可

+ 让软件图标出现在应用程序栏中：将上面的desktop文件mv到`~/.local/share/application/`

## misc

+ 在登录云服务器后终端会先输出一段话，这些在`/etc/update-motd.d/10-help-text`（Ubuntu），这是一个可执行文件，具体请STFW

## ssh到VMware workstation虚拟机
[教程](https://cloud.tencent.com/developer/article/1679861#:~:text=windows%E5%AE%BF%E4%B8%BB%E6%9C%BA%E5%A6%82%E4%BD%95SSH%E8%BF%9E%E6%8E%A5VMware%E7%9A%84Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%201%201%E3%80%81%E5%AE%89%E8%A3%85%E5%A5%BDUbuntu%E8%99%9A%E6%8B%9F%E6%9C%BA%202,2%E3%80%81%E5%BB%BA%E7%AB%8BIP%E6%98%A0%E5%B0%84%203%203%E3%80%81%E9%85%8D%E7%BD%AE%E8%99%9A%E6%8B%9F%E6%9C%BASSH%204%204%E3%80%81%E9%85%8D%E7%BD%AE%E8%99%9A%E6%8B%9F%E6%9C%BA%E9%98%B2%E7%81%AB%E5%A2%99)