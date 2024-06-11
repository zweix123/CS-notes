## TLDR

```bash
ssh-keygen  # 执行该命令生成密钥
ssh-copy-id 服务器别名  # 将公钥上传到服务器
```

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

## 文件传输：`scp`、`sshpass` and `ftp`

+ `scp`：`scp source destination`，dest描述为：`别名:path`
	+ 多文件：`scp source1 source2 destination`
	+ 复制文件夹：添加选项`-r`
	+ 指定端口：添加参数`-P`
+ `sshpass`：就是把`scp`的`password`从stdin input变成argument
+ `ftp`：可以先登陆到服务器上，然后在通过`get`和`mget`传文件
