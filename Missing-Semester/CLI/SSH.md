
+ 非对称加密：私钥生成公钥，公钥不能反推私钥，只有私钥可以匹配公钥
    + 作为SSH的客户端，即我们本地的机器，拥有私钥；将对应的公钥放在SSH的服务端上（比如云服务器，比如Github），这样当我们向服务端连接的时候，对方可以识别我们的身份。

+ 配置目录路径：
    + Windows：`C:\User\$用户名\.ssh\`
    + Unix(Linux&macOS)：`/home/${用户名}/.ssh/`

+ 配置目录内容：
	```bash
	├── authorized_keys  # 服务端存储客户端公钥的文件, 按行划分
	├── config           # 客户端SSH配置
	├── id_rsa           # 私钥, 一定不要公开
	├── id_rsa.pub       # 公钥, 放在服务端的就是这个
	└── known_hosts      # 记录本机ssh到的机器（包括云服务机和Github）, 不用管理
	```

+ <span id="config"></span>配置文件`config`格式：
    ```
    # 格式
    Host 别名
        HostName 云服务器公网地址
        User 登录用户
        Port 端口  # 不必须    
    ```

    必须Tab缩进，多个服务器别名用空行分开

+ <span id="连接服务器"></span>连接服务器：
    + 直接连接：`ssh 用户名@IP地址`
    + 通过别名：`ssh 服务器别名`

    命令执行之后需要输入密码，加入将客户端密钥放在服务器上的`authorized_keys`文件后，则不需要输入密码


## 2.1 SSH

### 2.1.1 Server

1. 生成密钥和相关文件：
    ```
    ssh-keygen && touch ~/.ssh/authorized_keys ~/.ssh/config  # 之后一路回车+y
    ```

### 2.1.2 Client

1. 生成密钥和相关文件：

    ```
    ssh-keygen && touch ~/.ssh/authorized_keys ~/.ssh/config  # 之后一路回车+y
    ```

2. 将密钥放在服务端上：
    1. 将公钥内容放在服务器的`authorized_keys`中即可实现免密登录
        - 方法一：手动copy，多个秘钥用回车隔开
        - 方法二：本机使用命令添加公钥：`ssh-copy-id 服务器别名`
    2. <span id="密钥"></span>将公钥内容放在Github用户的Setting的SSH keys中即可向该用户的项目中push：`Setting -> SSH and GPG keys -> New SSH key -> 拷贝公钥`
        - 测试方法：`sh -T git@github.com`

3. 配置服务器别名：<a href="#config">上文</a>
