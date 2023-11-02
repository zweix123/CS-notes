# LinuxConfigGuide
>Linux有众多发行版、机器也分云服务器、虚拟机和物理机，该指南并没有限制某种机器，对独属于某种机器的问题会单独说明，请读者选择对您有帮助的部分

[姊妹篇：Win机器开发机配置指南](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/WindowsConfigGuide.md)

+ 指南中涉及的软件配置[地址](https://github.com/zweix123/linux-config)，在README中提供详细的使用方法和说明，请在完成下面步骤后再使用这份配置。

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
	sudo apt upgrade # 让新的包的信息更新所有软件  # 时间较长  # 我通常不用  # 尽量不要用!
	```

## 4.下载刚需软件
>Linux下通常有包管理器，下面的软件没有说明下载方式的软件一般都可以通过包管理器下载

下面是Ubuntu的汇总脚本，个人使用，用户根目录使用，需要交互
```bash
sudo apt install -y vim
sudo apt install -y tmux
sudo apt install -y git

git config --global user.name zweix
git config --global user.email 1979803044@qq.com

git config --global core.editor vim  # your favorite editor
git config --global color.ui true

sudo apt install -y zsh
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

mkdir Configs
cd Configs
git clone git@github.com:zweix123/linux-config.git
cd linux-config
bash ./backup.sh
bash ./install.sh
```

### 文本编辑器

Linux下的文本编辑器非常之多，上面使用vi就是一种，选择看个人喜好  
且也是一种可玩性很好的软件，所以[单拿出来](https://github.com/zweix123/CS-notes/blob/master/Linux/Editor.md)，记录有配置和用法

### 终端复用器

tmux

+ 使用：我的[笔记](https://github.com/zweix123/CS-notes/blob/master/Linux/Tmux.md)

### Git

+ 配置：我的[教程](./Git.md#config)
+ 使用：我的[笔记](https://github.com/zweix123/CS-notes/blob/master/Missing-Semester/Git.md)

### zsh

+ shell通识：
	+ `echo $SHELL`查看使用shell
	+ `cat /etc/shells`查看机器有的shell程序
	+ `chsh -s shell绝对路径`设置默认shell
		>[关于chsh](https://wangchujiang.com/linux-command/c/chsh.html)

---

主要通过zsh和oh-my-zsh，前者是和bash一样的一个shell，但是它有更强的拓展性，但是想通过配置利用这些扩展性比较复杂，oh-my-zsh相当于一种辅助配置工具

1. 下载`zsh`：[Manual](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH)，一行命令即可  
	```bash
	sudo apt install -y zsh
	```
	更新默认shell：`chsh -s $(which zsh)`
	>实际上这边建议不要着急修改，在clone oh-my-zsh会提示是否修改默认shell

2. 下载oh-my-posh：[Manual](https://github.com/ohmyzsh/ohmyzsh/wiki)
	```bash
	sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
	```
	>这里提供国内镜像源：`https://gitee.com/mirrors/oh-my-zsh`，clone到本地修改名字为`.oh-my-zsh`即可
	
	>我在使用VMware workstation时出现错误，通过这两个博客解决（[一个](https://blog.csdn.net/m0_56681539/article/details/127912811)、[另一个](https://blog.csdn.net/u014454538/article/details/123563034)）

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
	+ `z`：默认安装，手动配置，目录快速跳转（后不再使用）
		+ history：`~/.z`
		+ 命令：`z 目录`
	+ `zsh-syntax-highlighting`：手动安装，手动配置，语法高亮
		```bash
		git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
		```
		下面提供国内镜像
		```bash
		git clone https://gitee.com/Annihilater/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
		```		

	+ `zsh-autosuggestions`：手动安装，手动配置，命令历史补全

		```bash
		git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
		```
		>这里的网址就是没有`.git`，Manual中就没有  

		下面提供国内镜像
		```bash
		git clone https://gitee.com/phpxxo/zsh-autosuggestions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
		```
	+ `zsh-completions`：更好的Tab补全？似乎不太需要。
	+ `command-not-found`：无需下载

## 5.导入软件配置

导入[我的配置](https://github.com/zweix123/linux-config)

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

+ config：内容多且散，而且无关平台，我将其放在这个[教程](https://github.com/zweix123/CS-notes/blob/master/blog/VSCode.md)

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

# 云服务器

# 虚拟机

+ SSH到本机的VMware虚拟机中：
	>Reference：[教程](https://cloud.tencent.com/developer/article/1679861#:~:text=windows%E5%AE%BF%E4%B8%BB%E6%9C%BA%E5%A6%82%E4%BD%95SSH%E8%BF%9E%E6%8E%A5VMware%E7%9A%84Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%201%201%E3%80%81%E5%AE%89%E8%A3%85%E5%A5%BDUbuntu%E8%99%9A%E6%8B%9F%E6%9C%BA%202,2%E3%80%81%E5%BB%BA%E7%AB%8BIP%E6%98%A0%E5%B0%84%203%203%E3%80%81%E9%85%8D%E7%BD%AE%E8%99%9A%E6%8B%9F%E6%9C%BASSH%204%204%E3%80%81%E9%85%8D%E7%BD%AE%E8%99%9A%E6%8B%9F%E6%9C%BA%E9%98%B2%E7%81%AB%E5%A2%99)

	这个方法我只设置过一次，之后创建新的虚拟机（我一般只有一个虚拟机），只需要修改本机config的目标IP地址，就可以正常使用，但是虚拟机的IP是变化了的，不知道是什么魔法？

	1. check本机和虚拟机的IP
	2. `编辑` -> `虚拟网络编辑器` -> `VMnet8` -> `更改设置` -> `VMnet8` -> `NAT设置` -> `添加`（端口转发） -> `按要求填写`
	3. 
		```bash
		sudo apt install -y openssh-client
		sudo apt install -y openssh-server
		sudo /etc/init.d/ssh restart         # 启动
		```
	+ 即可连接