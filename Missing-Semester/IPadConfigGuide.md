>STFW: Search the Friendly Web 

# 1.网络

1. 美区账号：STFW
2. 学会如何付款购买软件：STFW
3. 软件：我个人使用OneClick
	>因为我没有学会如何付款

4. 你还需要一个魔法，请问下身边的朋友。

# 2.终端iSH

首先它使使用完整的Linux内核，实际上，如果你想在它上面做更大的开发也是可以的。我主要需要通过它安装Git

+ 下载：直接App Store下载即可。
+ 配置：类似Linux，参见[Linux配置指南](Missing-Semester/LinuxConfigGuide)
	+ 配置SSH
	+ 下载并配置Git

	注意发行版版本
	```
	localhost:~# cat /etc/os-release 
	NAME="Alpine Linux"
	ID=alpine
	VERSION_ID=3.14.3
	PRETTY_NAME="Alpine Linux v3.14"
	HOME_URL="https://alpinelinux.org/"
	BUG_REPORT_URL="https://bugs.alpinelinux.org/"
	```

	包管理器为`apk`，即`apk add`

# Obsidian

+ 下载：App Store
+ 配置：相关教程都可以在Obsidian官方英文论坛中找到，仅仅论坛中的教程即可，不用去其他社区，反而混淆视听。

	这里说一下重点和教程没提到的

	+ 将iSH挂载到IPad文件系统中`mount`的参数`-t`使用`ios-unsafe`而非`ios`，不然Git相关操作特别慢。
	+ 在Obsidian需要配置插件（较于PC），主要是用户名和邮箱。

	还有一些问题，在[IPad中的Obsidian-Git插件没有完整的功能](https://github.com/denolehov/obsidian-git/issues/459)，具体的，目前的情况是不能在不离开Obsidia的情况下完成所有同步操作。

	我个人在PC也是大部分通过命令行同步，虽然不爽，但是可以接受。
