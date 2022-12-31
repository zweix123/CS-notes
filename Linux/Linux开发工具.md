# 终端复用器tmux

+ 功能：

  1. 分屏

  2. 允许断开ssh连接后，继续运行进程

     > `top`：查看进程（任务管理器）

     服务器中的进程如果断开连接则停止

+ 结构：树形：一个tmux可包含多个session，每个session可包含多个window，每个window可包含多个pane

  其中pane是最小单位，每个pane都会打开一个shell对话框

1. `tmux`：新建一个session，包含一个window，window中包含一个pane，pane里打开了一个shell对话框

2. `按下Ctrl + a后手指松开，然后按%`：将当前pane左右平分成两个pane

   `按下Ctrl + a后手指松开，然后按"`：将当前pane左右平分成两个pane

   + `鼠标点击`选择pane/`按下Ctrl + a后手指松开，使用方向键`选择pane
   + 鼠标拖动pane之间的分割线，可以调整分割线的位置/`按下Ctrl + a的同时使用方向键`调整分割线。
   + `按下Ctrl + a后手指松开，然后按z`：将当前pane全屏/取消全屏

3. `Ctrl + d`：关闭当前pane，如果当前window的所有pane均已关闭，则自动关闭window，如果当前session的所有window均已关闭，则自动关闭session

4. `按下Ctrl + a后手指松开，然后按d`：挂起当前session

   `tmux a`/`tmux attch`：返回挂起的session

5. `按下Ctrl + a后手指松开，然后按s`：选择其他session

   + 方向键——上，选择上一项 session/window/pane
   + 方向键——下，选择下一项 session/window/pane
   + 方向键——右，展开当前项 session/window
   + 方向键——做，闭合当前项 session/window

6. `按下Ctrl + a后手指松开，然后按c`：在当前session中创建一个新的window

7. `按下Ctrl + a后手指松开，然后按w`：选择其他window

   + 方向键——上，选择上一项 session/window/pane
   + 方向键——下，选择下一项 session/window/pane
   + 方向键——右，展开当前项 session/window
   + 方向键——做，闭合当前项 session/window

8. 复制粘贴：

   + tmux内复制粘贴：

     + `Ctrl + a`后松开手指，然后按`[`进入复制模式，之后鼠标选中的文本进入**tmux**的粘贴板。
     + `Ctrl + a`后松开手指，然后按`]`，将tmux粘贴板中的文本粘贴出来

   + tmux和其他软件复制粘贴：

     选中：按`shift`键同时鼠标选中

     之后复制粘贴同Shell

# 文本编辑器vim

每次用vim编辑文件时，会自动创建一个`.filename.swp`的临时文件，此时如果打开某个文件时，该文件的swp文件已存在，则会报错，可以找到正在打开该文件的程序，并退出或者直接删掉该swp文件即可。

+ 功能：

  1. 命令行模式下的文本编辑器
  2. 根据文本扩展名自动判别编程语言。支持代码缩进、代码高亮等功能
  3. 使用方式：`vim filename`
     + 如果已有该文件，则打开它
     + 如果没有该文件，则打开一个新的文件，并命名为`filename`

+ 模式：

  1. 一般命令模式（默认）：可进行复制、粘贴、删除。

  2. 编辑模式：

     在一般命令模式里按`i`，进入编辑模式

     `按下ESC`退出编辑模式，返回到编辑模式

  3. 命令行模式：在一般命令模式按下`:`、`/`、`?`三个字母中的任意一个，进入命令行模式，命令行在最下面，

     ​                       可进行查找、替换、保存、退出、配置编辑器等

+ 命令：

  1. `i`：进入编辑模式

  2. `ESC`：进入一般命令模式

  3. `h`或`左箭头键`：光标向左移动一个字符

     `j`或`向下箭头`：光标向下移动一个字符

     `k`或`向上箭头`：光标向上移动一个字符

     `l`或`向右箭头`：光标向右移动一个字符

  4. `数字+空格`：光标向右移动数字大小个字母

     `数字+回车`：光标向下移动数字大小个行

  5. `0`或`功能键[Home]`：光标移动到本行开头

  6. `$`或`功能键[End]`：光标移动到本行末尾

  7. `G`：光标移动到最后一行

     `:数字`/`数字G`：光标移动到第n行

     `gg`：光标移动到第一行，相当于`1G`

  8. 查找：

     + `/word`：向光标之下寻找第一个值为word的字符串
     + `?word`：向光标之上寻找第一个值为word的字符串
     + `n`：重复前一个查找操作
     + `N`：反向重复前一个查找操作

  9. 替换：

     + `:数字1,数字2s/word1/word2/g`：在数字1和数字2行之间的word1替换成word2

       `:1,$s/word1/word2/g`：全文替换

       `:1,$s/word1/word2/gc`：全文替换，并且在替换前询问用户

  + `:noh`：取消高亮

  10. `v`：选中文本

      `d`（剪切）：删除选中的文本

      `dd`（剪切）：删除当前行

      `y`：复制选中的文本

      `yy`：复制当前行

      `p`：将复制的数据在光标的下一位置粘贴

  11. `u`：撤销

      `Ctrl + r`：取消撤销

  12. `shift + >`：将选中的文本整体向右缩进一次

      `shift + <`：将选中的文本整体向左缩进一次

  13. `:w`保存（`:w 文件名`）

      `:w!`强制保存

      `:q`退出

      `:q!`：强制退出

      `:wq`保存并退出

  14. `:set paste`设置成粘贴模式，取消代码自动缩进

      `:set nopaste`取消粘贴模式，开启代码自动缩进

      `:set nu`显示行号

      `:set nonu`隐藏行号

  15. 连招`gg=G`：将全文代码格式化

  16. `Ctrl + q`：当vim卡死时，可以取消当前正在执行的命令

+ 常见异常/异常处理：

  >  每次用vim编辑文件时，会自动创建一个.filename.swp的临时文件。
  
  + 如果打开某个文件时，该文件的swp文件已存在，则会报错。此时解决办法有两种
    1. 找到正在打开该文件的程序，并退出
    2. 直接删掉该swp文件即可

# 版本管理工具git

> git是版本管理工具，github是代码托管平台。

+ 工作区：仓库的目录。工作区是独立于各个分支的。
+ 暂存区：数据暂时存放的区域，类似于工作区写入版本库前的缓存区。暂存区是独立于各个分支的。
+ 版本库：存放所有已经提交到本地仓库的代码版本
+ 版本结构：树结构，树中每个节点代表一个代码版本。

1. 初始化：

   ```bash
   git config --global user.name xxx  # 设置全局用户名
   git config --global user.email xxx@xxx  # 设置全局邮箱地址
   ```

   信息记录在`~/.gitconfig`文件中

   > 这部通常是在github上创建好项目后，它会知道具体参数
   >
   
2. 把文件夹创建成一个仓库：进入目录，然后`git init`即把当前目录配置成git仓库，信息记录在隐藏`.git`文件夹中

   > 其中有个HEAD为版本树上的一个结点指针

+ 通过`get status`：查看仓库当前状态

1. 当前本地目录相当于工作区

2. `git add XXX`：将XXX文件添加到暂存区（也是加到仓库索引目录）

   + `git add .`：将所有待加入暂存区的文件加入暂存区
   + 对于”删除文件“这种操作，同样可以将”对应“文件再加入缓存区，此时加入的是对这个文件的删除操作
   + `git reset .`：撤销上一次提交暂存区的操作
   
   + `git resotore --stated <file>`：将暂存区的文件从暂存区撤出：还要管理
   
   + `git rm --cached XX`：将文件从仓库索引目录中删除——不再管理
   
   + `git restore <file>`：将文件的修改撤回到暂存区的版本
   + `git diff XX`：查看XX文件相对于缓存区修改了哪些内容
   
3. `git commit -m "备注信息或者说节点名"`：将暂存区的内容提交到当前分支（情况暂存区）
   + 如果暂存区只有部分仓库所有目录中的部分文件，commit后就只修改这部分

+ `git log`：查看当前分支的所有版本
  + 参数`--pretty=online`一行显示

+ `git reflog`：查看HEAD指针的移动历史（包括被回滚的版本）

1. `git reset --hard HEAD^`或`git reset --hard HEAD~`：将代码库（工作区）回滚到上一个版本

   + `git reset --hard HEAD^^`：往上回滚两次，以此类推

   + `git reset --hard HEAD~100`：往上回滚100个版本

   + `git reset --hard 版本号`：回滚到某一特定版本

     > 版本号：`git log`和`git reflog`均可查看版本的版本号：哈希值的前六位

+ 上云origin：

  > 平台基本回给出提示命令

  0. 在托管平台上的偏好设置中添加SSH密钥为自己的ssh公钥

  1. `git remote add origin git@git.acwing.com:zweix/homework.git`：将本地仓库关联到远程仓库

  2. `git push`：将当前分支推送到远程仓库

     `git push origin branch_name`：将本地的某个分支推送到远程仓库

     > 如果是第一次push需要添加`-u`参数

  3. 克隆：`git clone 在托管平台上找到clone按钮`

+ 分支：默认创建主分支`master`

  + `git branch branch_name`：创建新分支
  + `git checkout branch_name`：切换到`branch_name`分支
    + `git checkout -b branch_name`：创建并切换到`branch_name`这个分支
  + `git branch`：查看所有分支和当前所处分支
  + `git merge branch_name`：将分支`branch_name`合并到当前分支上

  ---

  + `git push --set-upstream origin branch_name`：设置本地的`branch_name`分支对应远程仓库的`branch_name`分支

    > `--set-upstream`参数可不需要

  + `git branch --set-upstream-to=origin/branch_name1 branch_name2`：将远程的`branch_name1`分支与本地的`branch_name2`分支对应

  ---

  + `git branch -d branch_name`：删除本地仓库的`branch_name`分支
  + `git push -d origin branch_name`：删除远程仓库的`branch_name`分支

  ---

  + `git pull`：将远程仓库的当前分支与本地仓库的当前分支合并
  + `git pull origin branch_name`：将远程仓库的`branch_name`分支与本地仓库的当前分支合并

  ---

  + `git checkout -t origin/branch_name`：将远程的`branch_name`分支拉取到本地

+ `stash`：存储没有持久化的修改
  
  + `git stash`：将工作区和暂存区中尚未提交的修改存入栈中
  + `git stash apply`：将栈顶存储的修改恢复到当前分支，但不删除栈顶元素
  + `git stash drop`：删除栈顶存储的修改
  + `git stash pop`：将栈顶存储的修改恢复到当前分支，同时删除栈顶元素
  + `git stash list`：查看栈中所有

# 容器[docker](https://docs.docker.com/desktop/)

+ > Tip：如果apt-get下载软件速度较慢，可以参考[清华大学开源软件镜像站](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)中的内容，修改软件源。
>
  > 1. `vim /etc/apt/sources.list`：把软件园首页的代码copy进去
> 2. 然后`apt-get update`即可
  > 3. 之后的下载自动利用镜像站中的软件源

+ 将当前用户添加到docker用户组，为了避免每次使用docker命令都需要加上sudo权限，可以将当前用户加入安装中自动创建的docker用户组(可以参考官方文档)：`sudo usermod -aG docker $USER`执行完此操作后，需要退出服务器，再重新登录回来，才可以省去sudo权限。

  > docker很多命令需要sudo

+ 每个docker可以管理多个image镜像，每个image都可以生成多个container容器（这些容器里的环境都是一样的），每个容器都相当于一个完整的云服务器

+ 镜像（images）：

  + `docker images`：列出本地所有镜像

  + 从docker官网拉去一个镜像：`docker pull ubuntu:20.04`：拉取一个镜像

    > 镜像有两部分构成：`type:version`

  + `docker image rm ubuntu:20.04` \ `docker rmi ubuntu:20.04`：删除镜像ubuntu:20.04

  + 迁移镜像：

    1. 压缩：`docker save -o ubuntu_20_04.tar ubuntu:20.04`：将镜像ubuntu:20.04导出到本地文件ubuntu_20_04.tar中

       > 该文件通常权限是不可读，要手动加一个可读权限`chmod +r ubuntu_20_04`

    2. 迁移到其他服务器：`docker load -i ubuntu_20_04.tar`：将镜像ubuntu:20.04从本地文件ubuntu_20_04.tar中加载出来

       将该压缩文件传到对应的服务器即可下载

+ 容器（container）：

  + `docker ps -a`：查看本地的所有容器

    + `docker ps`：查看各容器状态

  + `docker [container] create -it ubuntu:20.04`：利用镜像ubuntu:20.04创建一个容器。

    `docker [container] commit CONTAINER IMAGE_NAME:TAG`：创建某个`container`的镜像

  + `docker [container] start CONTAINER`：启动容器
    `docker [container] stop CONTAINER`：停止容器
    `docker [container] restart CONTAINER`：重启容器
    `docker [contaienr] run -itd ubuntu:20.04`：创建并启动一个容器

    > 这里的参数`-itd`：如果没有d是创建、启动并进入

    `docker [container] attach CONTAINER`：进入容器

    + 先按`Ctrl-p`，再按`Ctrl-q`可以挂起容器

      > `Ctrl + d`是直接关掉容器

    `docker [container] rm CONTAINER`：删除容器（需要容器停止）

    + `docker container prune`：删除所有已停止的容器

  + `docker [container] exec CONTAINER COMMAND`：在容器中执行命令

  + 迁移容器：并没有迁移容器，而是浅出容器的镜像

    + `docker export -o xxx.tar CONTAINER`：将容器CONTAINER导出到本地文件xxx.tar中

    + `docker import xxx.tar image_name:tag`：将本地文件xxx.tar导入成镜像，并将镜像命名为image_name:tag

    > docker export/import与docker save/load的区别：
    >
    > + export/import会丢弃历史记录和元数据信息，仅保存容器当时的快照状态
    > + save/load会保存完整记录，体积更大

  + `docker top CONTAINER`：查看某个容器内的所有进程
    `docker stats`：查看所有容器的统计信息，包括CPU、内存、存储、网络等信息
    `docker cp xxx CONTAINER:xxx` 或 `docker cp CONTAINER:xxx xxx`：在本地和容器间复制文件
    `docker rename CONTAINER1 CONTAINER2`：重命名容器
    `docker update CONTAINER --memory 500MB`：修改容器限制
