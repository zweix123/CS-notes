## Intro
Docker是一种类似虚拟机的软件，可以管理多个image镜像，每个image可以生成多个container容器，每个容器都相当于一个完整的机器
>类比类和对象

## Install
这个[手册](https://yeasy.gitbook.io/docker_practice/install)比官网好用

## Config
docker很多命令需要sudo，为了避免麻烦，可以将当前用户将入到安装时自动创建的docker用户组中
```bash
sudo usermod -aG docker $USER
```

## Image

+ 镜像的构成：`type:version`
---
+ `docker images`：列出本地所有的镜像
+ `docker pull ubuntu:20.04`：从docker官网上拉取一个镜像
+ `docker image rm ubuntu:20.04`：删除镜像

+ 镜像的迁移：
	1. 压缩：`docker save -o ubuntu_20_04.tar ubuntu:20.04`
		>该文件通常不可读，`chmod +r`
		
	2. 迁移：`docker load -i ubuntu_20_04.tar` 

## container
+ `docker ps -a`：查看本地所有容器
	+ `docker ps`：查看各容器状态

>下面的`[container]`不是arg，而是“可选”的command，大写单词才是arg
+ `docker [container] create -it ubuntu:20.04`：利用镜像创建容器
+ `docker [container] commit CONTAINER IMAGE_NAME:TAG`：利用容器创建镜像

```bash
docker [container] start CONTAINER  # 启动容器
docker [container] stop CONTAINER  # 停止容器
docker [container] restart CONTAINER # 重启容器

docker [container] run -itd ubuntu:20.04  # 从镜像中创建并启动一个容器
docker [container] run -it  ubuntu:20.04  # 从镜像中创建、启动并进入一个容器
# 以上两个命令的不同就是-d参数，有则后台运行
```

```bash
docker exec 容器ID /bin/bash  # 进入容器
```
>`docker [container] attach CONTAINER  # 进入容器`
>这个命令会卡住，还不清楚为什么

+ `Ctrl+p -> Ctrl+q`：挂起容器
+ `Ctrl+d`：关掉容器

```bash
docker [container] rm CONTAINER  # 删除容器（需要容器停止）
docker container prune  # 删除所有已经停止的容器
```

+ `docker [container] exec CONTAINER COMMAND`“”：在容器中执行命令

+ 容器的迁移
	+ `docker export -o xxx.tar CONTAINER`：将容器导出到本地文件xxx.tar中
	+ `docker import xxx.tar image_name:tag`：

>`docker export/import`和`docker save/load`的区别
>+ export/import会丢弃历史记录和元数据信息，仅保存容器当时的快照状态
>+ save/load会保存完整记录，体积更大

+ `docker top CONTAINER`：查看某个容器内的所有进程  
	`docker stats`：查看所有容器的统计信息，包括CPU、内存、存储、网络等信息  
    `docker cp xxx CONTAINER:xxx` 或 `docker cp CONTAINER:xxx xxx`：在本地和容器间复制文件  
    `docker rename CONTAINER1 CONTAINER2`：重命名容器  
    `docker update CONTAINER --memory 500MB`：修改容器限制  

## Case
+ acwing：
	1. 在本地将镜像上传到自己租的云端服务器：`scp /var/lib/acwing/docker/images/docker_lesson_1_0.tar server_name:`
	2. 在云服务器将镜像加载到本地：`docker load -i docker_lesson_1_0.tar`  
		创建并运行docker_lesson:1.0镜像：`docker run -p 20000:22 --name my_docker_server -itd docker_lesson:1.0 `
	3. 进入创建的docker容器：`docker attach my_docker_server`  
		设置密码：`password`
	4. 去云平台控制台中修改安全组配置，放行端口20000
	+ 则可以通过`ssh root@xxx.xxx.xxx.xxx -p 20000`指定端口ssh
	+ 此时配置的docker容器相当于一个完整的云服务器，可以配置其免密登录，注意此时本地的`~/.ssh/config`中要在多加一行`Port 20000`

## Error log
+ 对于报错：
	```
	Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get"http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": dial unix /var/run/docker.sock: connect: permission denied
	```
	可以这样解决：
	```bash
	sudo chmod 666 /var/run/docker.sock
	```
