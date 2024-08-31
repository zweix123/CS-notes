SSH是**网络协议**，通过**非对称加密**的方式**远程登录**到服务器

+ 非对称加密：由公钥和私钥组成。公钥由私钥生成，公钥不能反推私钥。公钥自己持有，公钥可以公开。通过公钥进行加密的数据只有持有私钥的才能解密。私钥可以创建数字签名，通过公钥可以验证有效性。这也是SSH的基础。以上这些由数学定理保证。

    >下面也会将私钥称之为密钥，我个人在同时提到公钥和私钥时使用私钥，在单独提到密钥时使用密钥 : )

+ 配置目录：用户目录下`.ssh`目录
    + Windows：`C:\User\${用户名}\.ssh\`
    + Unix（Linux & macOS）：`/home/${用户名}/.ssh/`
+ 目录结构：
	```bash
	├── authorized_keys  # 服务端存放客户端公钥, 按行划分
	├── config           # 客户端配置
	├── id_rsa           # 私钥(一定不要公开)
	├── id_rsa.pub       # 公钥(可以公开, 比如放在服务器上、GitHub上)
	└── known_hosts      # 记录本机SSH过的机器, 不用手动管理
	```

+ 配置文件`config`格式：
    ```config
    Host 别名
        HostName 服务器地址  # IP地址或者域名, 如果是云服务器记得使用公网地址
        User 登录的用户  # 在服务器上的用户, 而不是本机的用户
        Port 端口  # 不必须, 默认22
    ```

    必须使用`Tab`缩进，多个服务器别名使用空行分开

+ 基本用法——连接服务器：
    + 直接连接：`ssh 用户名@IP地址或者域名`
    + 通过别名：`ssh 服务器别名`

    命令执行后需要输入密码，（按下面）配置之后则可以免密登录

## Config

SSH的配置需要在客户端和服务端都配置

1. 生成公钥私钥并创建相关文件：鉴于SSH的广泛应用，本机和服务器都可以执行下面的命令

    >当本机连接服务器时，本机是客户端，服务器是服务端；当服务器连接GitHub时，服务器是客户端，GitHub的服务器是服务端。

    ```bash
    ssh-keygen && touch ~/.ssh/authorized_keys ~/.ssh/config  # 之后一路回车/输入y
    ```

2. 将密钥放在服务端上：

    + 服务器：将公钥放在服务器的`authorized_keys`文件中即可实现免密登录

        1. 方法一：手动复制
        2. 方法二：本机使用命令——`ssh-copy-id 服务器别名`

    + GitHub：将公钥放在GitHub用户的Setting的SSH keys中即可通过SSH Link向自己的项目中pull/push

        + 位置描述：Setting -> SSH and GPG keys -> New SSH key -> 拷贝公钥
        + 检测方法：
            ```ssh
            ssh -T git@github.com
            ```

3. 配置服务器别名（方法见上文）

## 文件传输

+ `scp`：`scp source destination`，dest描述为：`别名:path`
	+ 多文件：`scp source1 source2 destination`
	+ 复制文件夹：添加选项`-r`
	+ 指定端口：添加参数`-P`
+ `sshpass`：就是把`scp`的`password`从stdin input变成argument
+ `ftp`：可以先登陆到服务器上，然后在通过`get`和`mget`传文件
