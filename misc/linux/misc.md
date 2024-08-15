## 快速开始

0. 智慧的提问+网络问题
1. 什么是命令行？它和图形化的计算机操作方式比有什么特点？Anyway，反正你必须要使用命令行，等你用了就知道了。
2. 去哪里找一个可以用的命令行？
	+ Windows：`Ctrl + r`然后键入`cmd`，此时弹出的黑框框就是命令行，但不建议使用，建议使用[Powershell7](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4)（区分于Windows自带的Windows Powershell），推荐直接在`cmd`执行`winget install --id Microsoft.Powershell --source winget`下载。之后`Ctrl + r`键入`pwsh`打开的黑框框即是Powershell7，虽然和Linux原生的终端仍然有差别，不过就学习而言，个人体会差别不大，但仍然推荐使用Linux。
	+ Linux：如果你使用的是无桌面的模式，则你已经在命令行中了；否则快捷键`Ctrl + T`打开命令行
	+ Mac：`Command + space`打开聚焦搜索，键入`terminual`打开命令行
3. 区分一些名词：
	+ Shell：
		+ 狭义的操作系统 = 操作系统内核 + Shell，所以Shell是和操作系统进行交互的工具。
		+ Shell是一种“编程语言”，是脚本语言，可以按照期语法何其进行”交互式编程“，也能将命令作为代码放进文件中然后一起在Shell中运行。

		上面提到cmd、Windows Powershell、Powershell7都是Shell，Bash，Zsh，Fish也都是Shell。

	+ Terminal：Shell是一个抽象的概念，即执行命令本身和操作系统进行交互的。那么我们作为计算机的用户，通过什么将命令给到Shell呢？这个概念划分出来意义本来不大，比如我在任何地方打开一个命令行，肯定是终端和Shell一起打开，Shell自带一个终端（或者反过来）。但是在Windows中，有一个Windows Ternimal的软件，它需要绑定某个Shell才能使用，所以这里区分一下
	+ 命令行：在这里作为Shell和Terminal的合称

4. 快速开始一些简单常用的命令：[新手指南： Linux 新手应该知道的 26 个命令](https://linux.cn/article-6160-1.html)，如果你时间多一点的话，可以看看[The Art Of Command Line简体中文](https://github.com/jlevy/the-art-of-command-line/blob/master/README-zh.md)

5. 好，你可以退出本教程了。
6. 下面会在场景中讨论相关命令，相互之间没有递进关系。

# Shell基本操作

+ 控制相关快捷键：
	+ `Ctrl + c`：向当前执行程序发送中断信号SIGINT，强制中断
	+ `Ctrl + \`：向当前执行程序发送退出信号SIGQUIT，强制退出
	+ `Ctrl + d`：退出会话/中断连接

+ 文件权限：一共10位，第一位表示该文件是目录`d`还是文件`-`，剩下9位中3位1组，分别表示当前用户（文件所属用户）权限、组和用户权限和其他用户权限；组内的3位分别表示是否可读`r`、是否可写`w`、是否可执行`x`，可以用数字0到7表示。命令`ls`以及参数`-l`可查看
	![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/linux/Linux文件信息.png)

+ 重定向：
	+ 文件描述符：`0`表标准输入，`1`表标准输出，`2`表标准错误
	+ 重定向操作符：`>`、`<`、`>>`、`n>`、`n>>`
+ 管道：
+ `xargs`：

更多见[Shell 编程](Programming-Language/Bash.md)

## 开发必要软件使用

+ ssh
+ git

# Linux一切皆文件
>你可能需要一个Linux机器，如果你是Windows，可以使用VMware，以无图形化的方式打开，并SSH过去，个人体验很好。
>>当然，怎么SSH又是另外的话题

## `/proc`

进程信息以文件的形式放在该目录下，文件名即为对应进程的PID，获取进程相关信息的命令（比如`top`）（可能）均来自于此。

+ `ps aux`：
	+ USER：各进程对应文件的所属用户就是进程的用户
	+ PID：文件名
	+ COMMAND：进程目录下的`cmdline`文件

+ `netstat`：进程目录下的`fd`文件

## `/dev`：从块设备到文件系统再到挂载点

+ 块设备：存储设备，其对应的文件在`/dev`下，文件名和块设备名相同
	
	使用命令`lsblk`查看
	```bash
	> lsblk
	NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
	loop0         7:0    0     4K  1 loop /snap/bare/5
	loop1         7:1    0  55.7M  1 loop /snap/core18/2812
	loop2         7:2    0  73.9M  1 loop /snap/core22/864
	loop3         7:3    0   219M  1 loop /snap/gnome-3-34-1804/72
	loop4         7:4    0  12.3M  1 loop /snap/snap-store/959
	loop5         7:5    0  40.9M  1 loop /snap/snapd/20290
	loop6         7:6    0  55.7M  1 loop /snap/core18/2796
	loop7         7:7    0  40.4M  1 loop /snap/snapd/20671
	loop8         7:8    0  65.1M  1 loop /snap/gtk-common-themes/1515
	loop9         7:9    0   497M  1 loop /snap/gnome-42-2204/141
	loop10        7:10   0 218.4M  1 loop /snap/gnome-3-34-1804/93
	loop11        7:11   0  74.1M  1 loop /snap/core22/1033
	loop12        7:12   0  91.7M  1 loop /snap/gtk-common-themes/1535
	loop13        7:13   0    51M  1 loop /snap/snap-store/547
	sda           8:0    0 931.5G  0 disk
	nvme0n1     259:0    0 238.5G  0 disk
	├─nvme0n1p1 259:1    0   512M  0 part /boot/efi
	└─nvme0n1p2 259:2    0   238G  0 part /

	```

	第一列即为块设备名，最后一列则是对应的挂载点（后面讲）

	如果添加参数`-f`

	```

	> lsblk -f
	NAME        FSTYPE   LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINT
	loop0       squashfs                                                  0   100% /snap/bare/5
	loop1       squashfs                                                  0   100% /snap/core18/2812
	loop2       squashfs                                                  0   100% /snap/core22/864
	loop3       squashfs                                                  0   100% /snap/gnome-3-34-1804/72
	loop4       squashfs                                                  0   100% /snap/snap-store/959
	loop5       squashfs                                                  0   100% /snap/snapd/20290
	loop6       squashfs                                                  0   100% /snap/core18/2796
	loop7       squashfs                                                  0   100% /snap/snapd/20671
	loop8       squashfs                                                  0   100% /snap/gtk-common-themes/1515
	loop9       squashfs                                                  0   100% /snap/gnome-42-2204/141
	loop10      squashfs                                                  0   100% /snap/gnome-3-34-1804/93
	loop11      squashfs                                                  0   100% /snap/core22/1033
	loop12      squashfs                                                  0   100% /snap/gtk-common-themes/1535
	loop13      squashfs                                                  0   100% /snap/snap-store/547
	sda
	nvme0n1
	├─nvme0n1p1 vfat           FAD9-E464                             504.9M     1% /boot/efi
	└─nvme0n1p2 ext4           e544fee2-1c4a-4e5d-98bd-a501ca498984    137G    36% /
	```

	则在第二列是块设备上的文件系统类型

	+ 如果仅仅想知道当前路径的磁盘占用，可以使用命令`du -sh .`

+ 文件系统：

	如果只关注文件系统（仍然以块设备或块设备分区命名）和挂载点的关系，则可以使用命令`df -h`（`-h`表示humanable），还有参数`-aT`

+ 挂载点：当块设备分区并初始化文件系统后，则可以挂载到某个路径下。因为路径从根目录开始是一个树形结构，所以一个文件系统是该文件树的一个子树上。

### Practice: 划分块设备初始化文件系统并挂载

1. 通过`lsblk`找到一个未分区的块设备，我这里是`sda`
	```
	> lsblk /dev/sda  # 如果不添加参数则是显示所有的块设备
	NAME MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
	sda    8:0    0 931.5G  0 disk
	```

2. 通过`fdisk`对该块设备进行分区，看下面代码注释

	```
	>sudo fdisk /dev/sda  # 需要使用sudo，参数的块设备名是/dev下的文件
	
	Welcome to fdisk (util-linux 2.34).
	Changes will remain in memory only, until you decide to write them.
	Be careful before using the write command.
	
	
	Command (m for help): p  # 命令p是打印当前分区，目前还没有分区
	Disk /dev/sda: 931.53 GiB, 1000204886016 bytes, 1953525168 sectors
	Disk model: ST1000DM010-2EP1
	Units: sectors of 1 * 512 = 512 bytes
	Sector size (logical/physical): 512 bytes / 4096 bytes
	I/O size (minimum/optimal): 4096 bytes / 4096 bytes
	Disklabel type: dos
	Disk identifier: 0x27e86f8a
	
	Command (m for help): n  # 命令n是创建分区
	Partition type
	   p   primary (0 primary, 0 extended, 4 free)
	   e   extended (container for logical partitions)
	Select (default p): p   # 我不清楚主分区和扩展分区的区别，主分区只能创建4个，一般使用主分区即可
	Partition number (1-4, default 1):  # 这里我使用默认
	First sector (2048-1953525167, default 2048):  # 讲磁盘想象成大数组，这里相当于选择分区的起始索引，我使用默认
	Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-1953525167, default 1953525167): +128G  # 该分区大小为128G，别忘了前面的+号

	Created a new partition 1 of type 'Linux' and of size 128 GiB.
	
	Command (m for help): p  # 再次打印，我们发现有了一个新的分区
	Disk /dev/sda: 931.53 GiB, 1000204886016 bytes, 1953525168 sectors
	Disk model: ST1000DM010-2EP1
	Units: sectors of 1 * 512 = 512 bytes
	Sector size (logical/physical): 512 bytes / 4096 bytes
	I/O size (minimum/optimal): 4096 bytes / 4096 bytes
	Disklabel type: dos
	Disk identifier: 0x27e86f8a
	
	Device     Boot Start       End   Sectors  Size Id Type
	/dev/sda1        2048 268437503 268435456  128G 83 Linux
	
	Command (m for help): w  # 确认
	The partition table has been altered.
	Calling ioctl() to re-read partition table.
	Syncing disks.
	```

	此时我们看，该块设备下有了一个新分区
	```
	>lsblk /dev/sda -f
	NAME   FSTYPE LABEL UUID FSAVAIL FSUSE% MOUNTPOINT
	sda
	└─sda1
	```

3. 创建文件系统

	```
	> sudo mkfs.ext4 /dev/sda1
	mke2fs 1.45.5 (07-Jan-2020)
	Creating filesystem with 33554432 4k blocks and 8388608 inodes
	Filesystem UUID: 24e44839-d63d-4eb8-8c8c-4c5a3ae9a8e5
	Superblock backups stored on blocks:
	        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,                                                                                                                                          4096000, 7962624, 11239424, 20480000, 23887872
	
	Allocating group tables: done
	Writing inode tables: done
	Creating journal (262144 blocks):
	done
	Writing superblocks and filesystem accounting information: done	
	```

4. 挂载：
	```
	> sudo mount /dev/sda1 /hdd/hdd1
	```

5. 反过来我们可以查看对应的路径在哪个块设备下：

	```
	> df -h /hdd/hdd1
	Filesystem      Size  Used Avail Use% Mounted on
	/dev/sda1       125G   61M  119G   1% /hdd/hdd1
	```

怎么还原呢？

6. 取消挂载

	```
	sudo umount /hdd/hdd1
	```


	此时在看
	```
	> df -h /hdd/hdd1
	Filesystem      Size  Used Avail Use% Mounted on
	/dev/nvme0n1p2  234G   80G  143G  36% /
	```

	这是因为

	```
	> lsblk /dev/nvme0n1p2
	NAME      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
	nvme0n1p2 259:2    0  238G  0 part /
	```

	很合理

# IO相关

## 磁盘IO

+ `iostat -x 1`

# 其他

ranger strace time

df, dust, free, du, ssh `ssh`：[我的教程](../Missing-Semester/SSH.md), top

+ `ps aux`：查看所有进程（直接标准输出）
+ `kill -9 pid`：kill 对应pid 的进程
	>本质是向某个进程传递信号：`kill -s SIGTERM pid`

+ `watch -n 0.1 command`：每0.1秒执行一次`command`命令
+ `tree`：展示当前目录的文件结构
+ `md5sum`：计算md5哈希值：
	+ 可从`stdin`读入内容：执行命令 -> 输入内容 -> `Ctrl + z`
	+ 可从命令行参数传入文件名列表

+ `cloc`：统计行数
+ `wc`：统计字数
	+ `wc -lwc`：行数、单词数、字节数

+ `diff`：比较不同
	+ `vimdiff`
+ 按文件名查找文件：`find`
	+ Modern 替代品：`fd`
+ 按文件内容查找文件：`grep`
	+ Modern 替代品：`ag`
