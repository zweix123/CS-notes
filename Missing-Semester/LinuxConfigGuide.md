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

[我的教程](Missing-Semester/CLI/ssh.md)

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

[我的笔记](./CLI/vim.md)

### tmux
>终端复用器

+ 功能：
  + 多个终端
  + 断开SSH而不影响命令执行

[我的笔记](./CLI/tmux.md)

### git

+ 配置：[我的教程](./CLI/git.md#config)
+ 使用：[我的教程](./CLI/git.md#usage)

### zsh

我的终端方案：zsh+oh-my-zsh

+ 前置条件：
    1. 下载并配置Git

#### 1.下载zsh并更换默认shell
>macOS不需要

Manual：[https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH)，一行命令即可

比如在Ubuntu上是
```bash
sudo apt install -y zsh
```

更新默认shell：`chsh -s $(which zsh)`
>实际上这边建议不要着急修改，在克隆oh-my-zsh会提示是否修改默认shell

#### 2.下载oh-my-posh并安装插件

Manual：[https://github.com/ohmyzsh/ohmyzsh/wiki](https://github.com/ohmyzsh/ohmyzsh/wiki)

```bash
sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

使用国内源：
```bash
git clone https://gitee.com/mirrors/oh-my-zsh ~/.oh-my-zsh
```

| 插件名                     | 功能                                               | 下载                                                                                                                                      | 国内源下载                                                                                                                                    |
| ----------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| z                       | 提供了一个快速跳转到你之前访问过的目录的功能，使用命令`z`                   | 默认安装                                                                                                                                    |                                                                                                                                          |
| git                     | 集成了 git 命令的自动补全和高亮显示                             | 默认安装                                                                                                                                    |                                                                                                                                          |
| history                 | 增强了 zsh 的历史命令功能                                  |                                                                                                                                         |                                                                                                                                          |
| zsh-completions         | 提供了额外的命令补全脚本                                     | `git clone https://github.com/zsh-users/zsh-completions ~/.oh-my-zsh/custom/plugins/zsh-completions`                                    |                                                                                                                                          |
| colored-man-pages       | 将 man 命令的输出以彩色显示                                 | 默认安装                                                                                                                                    |                                                                                                                                          |
| command-not-found       | 尝试执行一个不存在的命令时，尝试找到正确的命令或者提供安装缺失命令的方法             | 默认安装                                                                                                                                    |                                                                                                                                          |
| zsh-autosuggestions     | 输入命令时自动显示可能的命令建议，以暗色的形式，按当前键入的命令作为前缀匹配，使用方向键右键补全 | `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`             | `git clone https://gitee.com/phpxxo/zsh-autosuggestions.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`              |
| zsh-syntax-highlighting | 高亮显示你输入的命令中的语法错误                                 | `git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting` | `git clone https://gitee.com/Annihilater/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting` |

#### 3.导入配置

导入[我的配置](https://github.com/zweix123/unix-config)，在README中有使用方法

## 5.导入软件配置

导入[我的配置](https://github.com/zweix123/unix-config)，在README中有使用方法

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
