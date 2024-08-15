# 一、简单说明

SSH的使用场景是连接服务器，Git则是版本管理工具，当结合Git仓库托管服务，可用于团队协作或者其他。而`git clone ssh url`使用SSH作为非对称加密，此处涉及SSH配置，故两者的配置通常的一同的，故放在同一文档管理。

## 1.1 SSH

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

## 1.2 Git

Git是一种版本管理工具，

+ 配置文件位置：
	+ win：`C:\User\$User\.gitconfig`
	+ unix：`/home/${User}/.gitconfig`

## 1.3 GitHub

GitHub是一个代码托管平台。

# 二、Config

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

## 2.2 Git

第一时间配置：
```bash
git config --global user.name xxx  # 设置全局用户名
git config --global user.email xxx@xxx  # 设置全局邮箱地址
```
+ 注意这里的flag——`--global`，假如想配置单个项目的用户信息，可以在Git项目下使用去掉该flag的命令配置，相关配置维护在项目根目录的`.git/config`中

必选设置
```bash
# 设置语言, 不然语言显示的是乱码(Win and Mac)
git config --global core.quotepath false
git config --global gui.encoding utf-8
git config --global i18n.commit.encoding utf-8
git config --global i18n.logoutputencoding utf-8

# 禁用不同操作系统换行符的自动转换(win: CRLF, linux: LF)
git config --global core.autocrlf false
```

可选设置
```bash
git config --global core.editor vim  # your favorite editor
git config --global color.ui true
```

其他设置
```bash
# 我还遇到过网络问题，报错形如Failed to connect to github.com port 443 after xxx ms: Couldn't connect to server, 通过下面的方法解决，如果没遇到可不执行
git config --global http.proxy http://127.0.0.1:7890 
git config --global https.proxy http://127.0.0.1:7890
# 查看
git config --global http.proxy
git config --global https.proxy
# 取消
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 2.3 GitHub

0. SSH相关配置：在`~/.ssh/config`添加
    ```
    Host github.com
        Hostname ssh.github.com
        Port 443
    ```

1. 上传密钥：<a href="#密钥">上文</a>

# 三、Usage
## 3.1 SSH

+ ssh本来的功能就是连接服务器：<a href="#连接服务器">上文</a>

## 3.2 scp&sshpass&ftp

+ `scp`：`scp source destination`，dest描述为：`别名:path`
	+ 多文件：`scp source1 source2 destination`
	+ 复制文件夹：添加选项`-r`
	+ 指定端口：添加参数`-P`
+ `sshpass`：就是把`scp`的`password`从stdin input变成argument
+ `ftp`：可以先登陆到服务器上，然后在通过`get`和`mget`传文件

## 3.3 Git


+ Init: 进入项目目录下：
	```bash
	git init
	```
	+ 信息维护在项目目录下的隐藏文件夹`.git`中
>下面提到的修改包括创建、删除和修改

工作区和暂存区
+ `git status`：查看工作区状态，维护文件是否修改、是否提交到暂存区
+ `git add file`：将`file`文件（的修改）添加到暂存区
	>add命令不仅有将文件的修改放入暂存区，还有将新的文件放入git的索引中

	`git add .`：添加所有
+ `git reset .`：撤销上一次提交暂存区的操作
+ `git restore --stated file`：将file（的修改）从暂存区撤出，但是仍然在索引区
+ `git rm --cached file`：将file从索引中删除——不再管理
	>然后将该文件放在`.gitignore`中保证不再维护。
+ `git restore file`：将file的修改撤回到暂存区的版本——这里是暂存区和工作区、不是版本库和工作区
	+ `git restore .`：注意暂存区中最开始的时候应该和版本库当前分支前是一样的，如果被所有文件都撤回到暂存区版本，相当于取消这次的修改
		>但是注意到只有add的file才能管理，也就是说我这次修改不仅修改了内容还创建了文件，此时如果想取消这次修改对于创建的文件只能手动删除
+ `git diff <file>`：查看工作区的file相对于缓存区都修改了那些内容
+ `git commit -m "remarks"`：将暂存区的内容提交到当前分支  
	`git commit`将进入文本编辑器，`Ctrl + C` -> `Y`提交
---
版本库
+ 版本号：哈希值的前六位，下面支出可查看的命令
+ `git log`：查看当前分支的所有版本
	+ 参数`--pretty=online`
+ `git reflog`：查看HEAD指针的移动历史（包括回滚动作）
+ `git reset --hard HEAD^`/`git reset --hard HEAD~`：将工作区的代码回滚到上一个版本
	+ `git reset --hard HEAD^^`：回滚两次、以此类推
	+ `git reset --hard HEAD~100`：往上回滚100个版本
	+ `git reset --hard 版本号`：回滚到特定版本

	可以同于合并最近的几个commit

+ 关于分支：
    >关于命令`git checkout`，它既能用于切换分支，又能恢复工作树，不是很直觉，推荐使用`git switch`和`git resotre`

	+ `git branch [branch]`创建分支
	+ `git checkout [branch]`切换分支
	`git checkout -b [branch]`创建并切换分支
	+ `git branch`：查看分支
	+ `git merge [branch]`：将分支合并到当前分支上

+ merge:
	+ 进入合入的分支，如果`xxx`是需要合进来的分支，则命令为`git cherry-pick xxx`

## 3.4 GitHub

+ Init：创建一个新项目时有足够的提示
+ `git push`：推送，将本地版本库放到云端
+ `git pull`：拉回，将云端版本库放到本地
+ `git clone ...`：将某个项目down到本地
	+ `GitHub`提供了不同的clone url，个人项目使用ssh，即通过之前绑定的公钥来修改

+ 指定分支克隆：
	```bash
	git clone --branch <branchname> <remote-repo-url>
	git clone -b <branchname> <remote-repo-url>
	```

### 3.4.1 Page

考虑这样的场景，我的项目的有些成果可以静态网页的形式展示，缩短路径让客户最快的看到我们产品的效果。但是大费周章的在服务器搭建一个Web服务也不合适，因为大概率服务器属于你的时间要远小于项目属于你的时间。这时GitHub Pages就派生用场了。下面给出一个方案。

打开项目 -> Settings -> Pages(在右边) -> (在Branch下选择)master + docs -> Save -> 然后把一个index.html放到项目的docs目录下即可通过`https://用户名.github.io/项目名/`访问
