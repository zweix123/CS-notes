- 前置知识：
  - [ssh](Missing-Semester/CLI/ssh.md)

Git 是一个成为事实标准的版本管理工具，GitHub 是一个代码托管平台（除了它还有其他很多很多也能代码托管）

- Git 配置文件位置：

  - 用户的（全局的）：用户目录下的`.gitconfig`文件
    - Windows：`C:\User\${用户名}\.gitconfig`
    - Unix（Linux & macOS）：`/home/${用户名}/.gitconfig`
  - 项目的（局部的）：使用 Git 维护的项目的`.git/`目录下的`config`文件

  对于同一个配置项，项目的覆盖用户的

## Config

### Git

下面通过命令做的配置会体现在上面提到的配置文件中

基本的：

```bash
git config --global user.name xxx  # 设置全局用户名
git config --global user.email xxx@xxx  # 设置全局邮箱地址
```

对于`--global`这个 flag，表示对应配置记录在用户配置中；假如想配置当个项目的用户信息，则在该项目**根目录路径下**使用不带该 flag 的命令。

必选的（个人建议）：

```bash
# 设置语言, 不然语言显示的是乱码(win and mac)
git config --global core.quotepath false
git config --global gui.encoding utf-8
git config --global i18n.commit.encoding utf-8
git config --global i18n.logoutputencoding utf-8

# 禁用不同操作系统换行符的自动转换(win: CRLF, linux: LF)
git config --global core.autocrlf false

# 又增加了一些新的

git config --global column.ui auto  # 相当于从ls -a变成ls

git config --global branch.sort -committerdate  # git branch 按照修改的时间排序(默认按字典序)

# git config --global tag.sort version:refname  # git tag默认按字段序，但是字典序不一定是tag实际大小排序

# git config --global init.defaultBranch main  # 设置默认分支

# git的默认diff算法是1986的myers diff, 当然它还支持多种: myers, minimal, patience, histogram
git config --global diff.algorithm histogram  # 切换算法
git config --global diff.colorMoved plain  # 更多的颜色
git config --global diff.mnemonicPrefix true  # 替换/a和/b，而表示来源: 即 索引i, 工作目录w, 提交c
git config --global diff.renames true  # 检测文件是否被重命名

# git config --global push.default simple # (default since 2.0)
git config --global push.autoSetupRemote true  # 你将再也看不到git push --set-upstream origin my-branch-name
git config --global push.followTags true  # tag也默认推送

git config --global fetch.prune true
git config --global fetch.pruneTags true
git config --global fetch.all true

# git config --global help.autocorrect prompt  # git会提示错误命令, 这个配置的打开会造成不仅提示, 而且直接提示要不要替代, 我讨厌命令里的[y/N], 所以不使用
# https://blog.gitbutler.com/why-is-git-autocorrect-too-fast-for-formula-one-drivers/

# git config --global commit.verbose true  # git commit会自动添加一些内容, 这个设置会将整个diff放在message里

# git config --global core.excludesfile ~/.gitignore  # 全局git ignore文件, 比较有用, 比如开发环境配置和奇怪的暂时文件, 我不想污染项目的git ignore文件

# 我爱rebase
git config --global rebase.autoSquash true
git config --global rebase.autoStash true
git config --global rebase.updateRefs true

# git config --global pull.rebase true  # 我觉得git pull --rebase也挺好的, 并不想把这个作为默认行为
```

可选的：

```bash
git config --global core.editor vim  # your favorite editor
git config --global color.ui true
```

其他的：

网络问题：

```bash
# 报错：Failed to connect to github.com port 443 after xxx ms: Couldn't connect to server
# 解决：如下
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy http://127.0.0.1:7890
# 查看
git config --global http.proxy
git config --global https.proxy
# 取消
git config --global --unset http.proxy
git config --global --unset https.proxy
```

### GitHub

0. SSH 相关配置：在`~/.ssh/config`添加

   ```
   Host github.com
       Hostname ssh.github.com
       Port 443
   ```

1. 上传密钥：见 SSH 教程

# Usage

- Init: 进入项目目录下：
  `bash
git init
` + 信息维护在项目目录下的隐藏文件夹`.git`中
  > 下面提到的修改包括创建、删除和修改

工作区和暂存区

- `git status`：查看工作区状态，维护文件是否修改、是否提交到暂存区
- `git add file`：将`file`文件（的修改）添加到暂存区

  > add 命令不仅有将文件的修改放入暂存区，还有将新的文件放入 git 的索引中

  `git add .`：添加所有

- `git reset .`：撤销上一次提交暂存区的操作
- `git restore --stated file`：将 file（的修改）从暂存区撤出，但是仍然在索引区
- `git rm --cached file`：将 file 从索引中删除——不再管理
  > 然后将该文件放在`.gitignore`中保证不再维护。
- `git restore file`：将 file 的修改撤回到暂存区的版本——这里是暂存区和工作区、不是版本库和工作区
  - `git restore .`：注意暂存区中最开始的时候应该和版本库当前分支前是一样的，如果被所有文件都撤回到暂存区版本，相当于取消这次的修改
    > 但是注意到只有 add 的 file 才能管理，也就是说我这次修改不仅修改了内容还创建了文件，此时如果想取消这次修改对于创建的文件只能手动删除
- `git diff <file>`：查看工作区的 file 相对于缓存区都修改了那些内容
- `git commit -m "remarks"`：将暂存区的内容提交到当前分支  
  `git commit`将进入文本编辑器，`Ctrl + C` -> `Y`提交

---

版本库

- 版本号：哈希值的前六位，下面支出可查看的命令
- `git log`：查看当前分支的所有版本
  - 参数`--pretty=online`
- `git reflog`：查看 HEAD 指针的移动历史（包括回滚动作）
- `git reset --hard HEAD^`/`git reset --hard HEAD~`：将工作区的代码回滚到上一个版本

  - `git reset --hard HEAD^^`：回滚两次、以此类推
  - `git reset --hard HEAD~100`：往上回滚 100 个版本
  - `git reset --hard 版本号`：回滚到特定版本

  可以同于合并最近的几个 commit

- 关于分支：

  > 关于命令`git checkout`，它既能用于切换分支，又能恢复工作树，不是很直觉，推荐使用`git switch`和`git resotre`

  - `git branch [branch]`创建分支
  - `git checkout [branch]`切换分支
    `git checkout -b [branch]`创建并切换分支
  - `git branch`：查看分支
  - `git merge [branch]`：将分支合并到当前分支上

- merge:

  - 进入合入的分支，如果`xxx`是需要合进来的分支，则命令为`git cherry-pick xxx`

- Init：创建一个新项目时有足够的提示
- `git push`：推送，将本地版本库放到云端
- `git pull`：拉回，将云端版本库放到本地
- `git clone ...`：将某个项目 down 到本地

  - `GitHub`提供了不同的 clone url，个人项目使用 ssh，即通过之前绑定的公钥来修改

+ `git revert`

- 指定分支克隆：
  ```bash
  git clone --branch <branchname> <remote-repo-url>
  git clone -b <branchname> <remote-repo-url>
  ```

考虑这样的场景，我的项目的有些成果可以静态网页的形式展示，缩短路径让客户最快的看到我们产品的效果。但是大费周章的在服务器搭建一个 Web 服务也不合适，因为大概率服务器属于你的时间要远小于项目属于你的时间。这时 GitHub Pages 就派生用场了。下面给出一个方案。

打开项目 -> Settings -> Pages(在右边) -> (在 Branch 下选择)master + docs -> Save -> 然后把一个 index.html 放到项目的 docs 目录下即可通过`https://用户名.github.io/项目名/`访问

- Ref: [Pro Git book](https://git-scm.com/book/en/v2) | [Git User Manual](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/user-manual.html)
- Ref: [《GotGitHub》](http://www.worldhello.net/gotgithub/) | [我的 SSH 笔记](Missing-Semester/CLI/ssh.md)

- 工作区 worksapce：仓库所在的目录，是独立于各个分支的。
- 暂存区 Stage/索引 Index：数据暂时存放的区域，类似于工作区写入版本库前的缓存区，也是独立于各个分支的。
  > 个人感觉两个概念略有区别，索引是 git 所管理的文件，一个管理的文件可以将修改记录在暂存区、也可以选择不记录，但是它仍然被 git 管理，在索引中
- 版本库 repositorty：存放所有已经提交到本地仓库的代码版本

  - 版本结构：树结构，树中每个节点代表一个代码版本 + HEAD：指向当前节点的最新节点
    ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/git区.png)

- 名词解释
  - Github，就是 Github
  - repo/Repository，Github 上的项目
  - Public/Private，上传到 Github 可以设置可见性
  - Issue：项目相关问题
    - 项目作者可以要求提问格式
  - Fork：将项目拷贝一份放到你的 repo 中
  - PR/Pull Request，修改项目的请求
  - Review，审计 pr 代码
  - Merge，在这里指 pr 通过 review，合并进项目中

为开源项目贡献代码

一个在 Github 上 Public 的 repo(Repositories)是“开源”，任何人都可以查看代码，也能为项目贡献代码

- Good First Issue，开发者认为相对简单的 issue，适合新手第一次上手项目
- 建议在 PR 之间先提 Issue，然后 PR 中即解决这个 Issue

流程如下

1. Fork 这个项目到你的仓库

   - 同步 Fork：[ref](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)

2. Clone 项目到本地，这个项目指的是 Fork 到你的仓库的项目
3. 创建新的分支，分支名应该尽可能简介且能反映我们的工作

   ```bash
   git checkout -b [branch name]
   ```

   - 每次开始一个新的任务都应该开一个新的分支

修改代码

4.  ```bash
    git add .
    git commit -s
    ```

    - commit 的 message 应该短小精悍，比如

      ```
      任务概括
      # 这里要有空格
      1. 一个小部分
      2. 另一个小部分
      ```

    - 参数`-s`表示在提交信息中加入 Signed-off-by 签名，即作者已经同意以某种方式授权提交代码

5.  `git push 远程分支名 你本地分支名`（通常这个命令自然是一样的）

6.  进入 Github 网页，进入你的项目，会出现 Pull Request 按钮

之后就会有项目开发者对你的 PR 进行 Review，这时可能需要进行修改

7.  ```
    git commit -s --amend
    git push -f
    ```

    - commit 参数`--amend`表示修改上一次 commit，而不是创建一次新的 commit
    - push 参数`-f`

多分支维护

上面提到，每次开始一个新的任务都应该开一个新的分支进行开发，这在多人开发中是必要的，那么个人开发也有必要嘛？  
我个人觉得有的，因为在开发新的部分时常常发现上一个部分的小 bug，这个时候我可能先`git reset HEAD~1`退回到上一个版本，然后把修改的文件`add`然后重新 commit，但是这样太笨对吧，如果上次修改了大量的文件，或者两次修改之间有重复的文件，是不能解决的。所有个人项目开新的分支也是有必要的。

- 新开一个分支：`git branch 新分支名`
  - 删除分支：`git branch -d 新分支名`
    - 同步到云端：`git push origin --delete [branch name]`
- 查看本地分支：`git branch`
  - 查看本地和云端（github）的分支：`git branch -a`
- 切换分支：`git checkout 分支名`
- push：`git push`后看提示
- 把新分支合入进 master：

  1. 切换到 master
  2. `git merge [branch name]`

- clone 分支：

  ```bash
  正常clone
  git checkout origin/[branch name]
  ```

  - 查看包括云端的分支：`git branch -a`

查看过去版本效果的正确姿势

> 如果在开发新功能时是开一个分支就不会有下面的问题

事情是这样的，写一个项目，新版本有 bug，而且 de 不出来，而且我还 commit 了，于是`git reset HEAD~1`回退到上一个版本，这时所有没有 commit 的文件就是出 bug 的版本修改的了，到这里还没啥问题，我想怎么看上一个版本的运行效果呢？于是直接`git checkout .`，把这些没有 commit 的文件的修改全部“取消”了，回车按下去我心里草了，那我白写了？

幸好有这个命令`git reflog`，这个命令可查看 HEAD 指针的移动情况，我们发现我们`reset`这个动作的，同一行有对应的哈希值，只需要`git reset [前面提到的哈希值]`，就回到最开始了。

- 这些信息是保存在本地的，不会随着 push 到云端

修改过去版本中的记录

> 这是一个危险的行为，不建议模仿

我的一个个人项目诞生于我对 git 使用很不规范的时期，有很多无用的 commit，其中真的影响使用的是，我发现 git clone 的速度非常的慢，虽然项目中确实有挺多的静态文件，但是直觉上感觉不应该这么的慢。我在之前的某个 commit 中把大量的测试用图片交了上去，猜测这部分在.git 目录中的记录体积很大。考虑如何删除。

1. 创建并进入新分支：` git checkout -b remove-images`
   > `git branch -a `查看分支
2. 列出所有 commit` git log --oneline`，有每次 commit 的 hash code 和 message  
   `git show --name-only <commit-hash>`查看某次 commit 的提交情况

   通过上面两个命令找到提交大量图片的 commit 和 commit 内容

   > `git show --name-only <commit-hash> | grep ".jpg\|.png\|.gif" | vim -` -> `:w tar-images.txt`

3. 使用脚本`git-delete.sh`：

   ```bash
   #!/bin/bash

   while read filename; do
       # Run git filter-branch command for each filename
       git filter-branch --force --index-filter "git rm --cached --ignore-unmatch $filename" --prune-empty --tag-name-filter cat -- --all
   done < tar-images.txt
   ```

   这个脚本会运行很长时间

4. 删除辅助文件，将当前分支推送到 github 上
   1. `git push -u origin remove-images`将当前分支推送上去（github 该项目有两个分支）
   2. `git checkout master` -> `git merge remove-images`准备何如分支（github 上显示 pr 通知，去通过 pr）
   3. `git reset --hard remove-images` -> ` git push --delete origin remove-images`删除本地和 github 上的新分支

果然快很多。

将其他 repo 各分支 push 到自己的 repo 中

下面两个情况，当项目的修改到自己的 repo 后，就不能再联系到学校本来的 repo 了，我通常是在服务器从学校 clone 并保留，每次拿到新的分支 copy 出来，把 copy 出来的项目去 push 到自己的 repo，开新的实验在备份那里进行更新再 copy。

xv6
每个实验都是一个分支，我们把某个分支从 MIT clone 到本地，然后

```
git remote set-url origin 你的项目的SSH链接
git push
```

这个分支就 push 到自己的 repo 下

CS144

与 xv6 的不同的是，它的每个实验在上一次实验的基础上，所以每次开新实验都是把新的分支 merge 到当前的分支，然后继续开发新进来的 TODO  
更新好分支后

```
git remote set-url origin 你的项目的SSH链接

git branch -m old_branch_name new_branch_name
git push origin HEAD
```

然后就可以去 github 设置默认分支了。
然后我们拿到新的分支后

```
git merge origin/上次实验分支名
```

CMU15445

哦！15445 提供了更优雅的方案，我上面两个方法简直太笨了。  
记得修改 action 并 save

子模块

- 将其他项目作为子模块：
  ```bash
  git submodule add <repository-url> <local-path>
  ```
- 克隆时：
  ```bash
  git submodule update --init --recursive
  ```

## amazing

```bash
# 查询项目贡献者数量
git log --pretty='%aN' | sort -u | wc -l
# 查询项目commit数量
git log --oneline | wc -l
# 查询项目规模
cloc --git $(git branch --show-current)  # 依赖非原生命令的
find . -name *\.后缀名 -exec wc -l  {} \; | awk '{s+=$1}END{print s}'  # 不依赖非原生命令的

# 开始内卷!
# 查询每个项目贡献者的commit数量并排名
git log --pretty='%aN' | sort | uniq -c | sort -k1 -n -r
# 查询每个项目贡献者的实际代码修改量
git log --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done
# 升级版:
# - 指定时间范围, 通过git log参数: --since=2020-01-01 --until=2025-01-04
git log --since=2020-01-01 --until=2025-01-04 --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done
# - 指定文件夹(包括或排除)
# 排除
git log --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat -- . ":(exclude)要排除的目录" | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done
# 包括
git log --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | grep 要包含的目录 | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -; done

# 你可能没那么内卷, 只关注自己的, 主要还是引入另一种命令的格式
git log --author="用户名" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -;
# 接时间范围、排除路径、指定路径参数如上
```

还能好玩些

```bash
git log --format='%aN' | sort -u | while read name; do echo -en "$name\t"; git log --author="$name" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s,\t removed lines: %s,\t total lines: %s\n", add, subs, loc }' -; done | column -t -s $'\t'
```
