## Intro
>Git是一种版本管理工具，GitHub是一个代码托管平台。

+ 相关资料：
	+ [Pro Git book](https://git-scm.com/book/en/v2)
	+ [Git User Manual](https://mirrors.edge.kernel.org/pub/software/scm/git/docs/user-manual.html)
	+ [可视化](http://onlywei.github.io/explain-git-with-d3/)

## Git

+ 工作区worksapce：仓库所在的目录，是独立于各个分支的。
+ 暂存区Stage/索引Index：数据暂时存放的区域，类似于工作区写入版本库前的缓存区，也是独立于各个分支的。
	>个人感觉两个概念略有区别，索引是git所管理的文件，一个管理的文件可以将修改记录在暂存区、也可以选择不记录，但是它仍然被git管理，在索引中
+ 版本库repositorty：存放所有已经提交到本地仓库的代码版本  
	+ 版本结构：树结构，树中每个节点代表一个代码版本
	+ HEAD：指向当前节点的最新节点
![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/git区.png)  
### Config
```bash
git config --global user.name xxx  # 设置全局用户名
git config --global user.email xxx@xxx  # 设置全局邮箱地址

git config --global core.editor vim  # your favorite editor
git config --global color.ui true

# 设置语言, 不然语言显示的是编码
git config --global core.quotepath false
git config --global gui.encoding utf-8
git config --global i18n.commit.encoding utf-8
git config --global i18n.logoutputencoding utf-8

git config --global http.proxy ""  # 如果使用没遇到问题就不用

# 禁用不同操作系统换行符的自动转换(win: CRLF, linux: LF)
git config --global core.autocrlf fals
```
+ 配置文件位置：
	+ win：`C:\User\$User\.gitconfig`
	+ linux：`~/.gitconfig`

### Use
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
	+ `git branch [branch]`创建分支
	+ `git checkout [branch]`切换分支
	`git checkout -b [branch]`创建并切换分支
	+ `git branch`：查看分支
	+ `git merge [branch]`：将分支合并到当前分支上

## Github
>资料：
>+ 《GotGitHub》[电子书地址](http://www.worldhello.net/gotgithub/)

### Config

### Use

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

### Pages

考虑这样的场景，我的项目的有些成果可以静态网页的形式展示，缩短路径让客户最快的看到我们产品的效果。但是大费周章的在服务器搭建一个Web服务也不合适，因为大概率服务器属于你的时间要远小于项目属于你的时间。这时GitHub Pages就派生用场了。下面给出一个方案。

打开项目 -> Settings -> Pages(在右边) -> (在Branch下选择)master + docs -> Save -> 然后把一个index.html放到项目的docs目录下即可通过`https://用户名.github.io/项目名/`访问

## Practice

+ jargon解释
	+ Github，就是Github
	+ repo/Repository，Github上的项目
	+ Public/Private，上传到Github可以设置可见性
	+ Issue：项目相关问题
		+ 项目作者可以要求提问格式
	+ Fork：将项目拷贝一份放到你的repo中
	+ PR/Pull Request，修改项目的请求
	+ Review，审计pr代码
	+ Merge，在这里指pr通过review，合并进项目中

### 为开源项目贡献代码

一个在Github上Public的repo(Repositories)是“开源”，任何人都可以查看代码，也能为项目贡献代码

+ Good First Issue，开发者认为相对简单的issue，适合新手第一次上手项目
+ 建议在PR之间先提Issue，然后PR中即解决这个Issue

流程如下
1. Fork这个项目到你的仓库
	+ 同步Fork：[ref](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)

2. Clone项目到本地，这个项目指的是Fork到你的仓库的项目
3. 创建新的分支，分支名应该尽可能简介且能反映我们的工作
	```bash
	git checkout -b [branch name]
	```

	+ 每次开始一个新的任务都应该开一个新的分支

修改代码

4. 
	```bash
	git add .
	git commit -s
	```

	+ commit的message应该短小精悍，比如
		```
		任务概括
		# 这里要有空格
		1. 一个小部分
		2. 另一个小部分
		```

	+ 参数`-s`表示在提交信息中加入Signed-off-by签名，即作者已经同意以某种方式授权提交代码

5. `git push 远程分支名 你本地分支名`（通常这个命令自然是一样的）

6. 进入Github网页，进入你的项目，会出现Pull Request按钮

之后就会有项目开发者对你的PR进行Review，这时可能需要进行修改

7. 
	```
	git commit -s --amend
	git push -f
	```

	+ commit参数`--amend`表示修改上一次commit，而不是创建一次新的commit
	+ push参数`-f`


### 多分支维护

上面提到，每次开始一个新的任务都应该开一个新的分支进行开发，这在多人开发中是必要的，那么个人开发也有必要嘛？  
我个人觉得有的，因为在开发新的部分时常常发现上一个部分的小bug，这个时候我可能先`git reset HEAD~1`退回到上一个版本，然后把修改的文件`add`然后重新commit，但是这样太笨对吧，如果上次修改了大量的文件，或者两次修改之间有重复的文件，是不能解决的。所有个人项目开新的分支也是有必要的。

+ 新开一个分支：`git branch 新分支名`
	+ 删除分支：`git branch -d 新分支名`
		+ 同步到云端：`git push origin --delete [branch name]`
+ 查看本地分支：`git branch`
	+ 查看本地和云端（github）的分支：`git branch -a`
+ 切换分支：`git checkout 分支名`
+ push：`git push`后看提示
+ 把新分支合入进master：
	1. 切换到master
	2. `git merge [branch name]`

+ clone分支：
	```bash
	正常clone
	git checkout origin/[branch name]
	```

	+ 查看包括云端的分支：`git branch -a`

### 查看过去版本效果的正确姿势

>如果在开发新功能时是开一个分支就不会有下面的问题

事情是这样的，写一个项目，新版本有bug，而且de不出来，而且我还commit了，于是`git reset HEAD~1`回退到上一个版本，这时所有没有commit的文件就是出bug的版本修改的了，到这里还没啥问题，我想怎么看上一个版本的运行效果呢？于是直接`git checkout .`，把这些没有commit的文件的修改全部“取消”了，回车按下去我心里草了，那我白写了？

幸好有这个命令`git reflog`，这个命令可查看HEAD指针的移动情况，我们发现我们`reset`这个动作的，同一行有对应的哈希值，只需要`git reset [前面提到的哈希值]`，就回到最开始了。

+ 这些信息是保存在本地的，不会随着push到云端

### 修改过去版本中的记录
>这是一个危险的行为，不建议模仿

我的一个个人项目诞生于我对git使用很不规范的时期，有很多无用的commit，其中真的影响使用的是，我发现git clone的速度非常的慢，虽然项目中确实有挺多的静态文件，但是直觉上感觉不应该这么的慢。我在之前的某个commit中把大量的测试用图片交了上去，猜测这部分在.git目录中的记录体积很大。考虑如何删除。

1. 创建并进入新分支：` git checkout -b remove-images`
	>`git branch -a `查看分支
	
2. 列出所有commit` git log --oneline`，有每次commit的hash code和message  
	`git show --name-only <commit-hash>`查看某次commit的提交情况  

	通过上面两个命令找到提交大量图片的commit和commit内容
	>`git show --name-only <commit-hash> | grep ".jpg\|.png\|.gif" | vim -` -> `:w tar-images.txt`

3. 使用脚本`git-delete.sh`：
	```bash
	#!/bin/bash
	
	while read filename; do
		# Run git filter-branch command for each filename
		git filter-branch --force --index-filter "git rm --cached --ignore-unmatch $filename" --prune-empty --tag-name-filter cat -- --all
	done < tar-images.txt
	```

	这个脚本会运行很长时间

4. 删除辅助文件，将当前分支推送到github上
	1. `git push -u origin remove-images`将当前分支推送上去（github该项目有两个分支）
	2. `git checkout master` -> `git merge remove-images`准备何如分支（github上显示pr通知，去通过pr）
	3. `git reset --hard remove-images` -> ` git push --delete origin remove-images`删除本地和github上的新分支

果然快很多。

### 将其他repo各分支push到自己的repo中

下面两个情况，当项目的修改到自己的repo后，就不能再联系到学校本来的repo了，我通常是在服务器从学校clone并保留，每次拿到新的分支copy出来，把copy出来的项目去push到自己的repo，开新的实验在备份那里进行更新再copy。

#### xv6
每个实验都是一个分支，我们把某个分支从MIT clone到本地，然后
```
git remote set-url origin 你的项目的SSH链接
git push
```
这个分支就push到自己的repo下

#### CS144

与xv6的不同的是，它的每个实验在上一次实验的基础上，所以每次开新实验都是把新的分支merge到当前的分支，然后继续开发新进来的TODO  
更新好分支后
```
git remote set-url origin 你的项目的SSH链接

git branch -m old_branch_name new_branch_name
git push origin HEAD
```
然后就可以去github设置默认分支了。
然后我们拿到新的分支后
```
git merge origin/上次实验分支名
```

#### CMU15445

哦！15445提供了更优雅的方案，我上面两个方法简直太笨了。  
记得修改action并save

### 子模块

+ 将其他项目作为子模块：
	```bash
	git submodule add <repository-url> <local-path>
	```

+ 克隆时：
	```bash
	git submodule update --init --recursive
	```