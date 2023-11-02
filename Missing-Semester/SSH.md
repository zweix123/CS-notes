+ 功能：
	+ 连接服务器
	+ 使用代码托管平台

+ 配置目录：`C:\User\$用户名\.ssh\`（Windows）、`~/.ssh/`（Linux）
	```
	├── authorized_keys
	├── config
	├── id_rsa
	├── id_rsa.pub
	├── known_hosts
	└── known_hosts.old
	```

	+ `id_rsa`和`id_rsa.pub`：使用RSA加密算法的公钥和秘钥。
		+ 生成命令：`ssh-keygen`，之后一路回车

		+ 应用：
			+ 将公钥内容放在服务器的`authorized_keys`中即可实现免密登录
				1. 方法一：手动copy，多个秘钥用回车隔开
				2. 方法二：本机使用命令添加公钥：`ssh-copy-id 服务器别名`
			+ 将公钥内容放在Github用户的Setting的SSH keys中即可向该用户的项目中push  
				`Setting -> SSH and GPG keys -> New SSH key -> 拷贝公钥`
	 + `config`：为云服务机配置别名
		```
		# 格式
		Host 别名
			HostName 云服务器公网地址
			User 登录用户
			Port 端口  # 不必须
		```
		必须Tab缩进，多个服务器别名用空行分开
  
	 + `authorized_keys`：如上所述
	 + `known_hosts`和`know_hosts.old`：记录本机ssh到的机器（包括云服务机和Github）

## SCP
命令格式：`scp source destination`：将`source`路径下的文件复制到`destination`中

+ 多文件：`scp source1 source2 destination`
+ 复制文件夹：`scp -r ... ...`
+ 指定端口：`scp -P 端口号 ... ...`

> 其中参数`-r`和`-P`尽可能放在两组地址之前

+ source和destination是逻辑关系，不是本机和服务器的关系
	+ 本机：正常使用
	+ 服务器：`服务器别名:...`
		+ `服务器别名:/home/acs/...`
		+ `服务器别名:家目录下的文件`：服务器的家目录不用起始`~`