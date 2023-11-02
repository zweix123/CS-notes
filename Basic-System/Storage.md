+ Term: Page
	+ Hardware Page(usually 4KB)
	+ OS Page(usually 4KB)
	+ Database Page(512B - 16KB)
		+ 512B可能是便携式设备
		+ 16KB则是取下层存储最小单位的整数倍

	A hardware page is the largest block of data that the storage device can guarantee failsafe writes

## Storage Hierarchy

从上到下，越来越慢、越来越大、越来越便宜（、越来越不容易损坏）

+ CPU Registers：寄存器
+ CPU Caches：（多级）缓存
+ DRAM：内存Memory

Volatile（Byte-Addressable字节地址Random Access随机访问）  

+ Non-volatile Memory：非易失内存
	>很新很贵，未广泛使用

Non-Volatile（Block-Addressable块地址Sequential Access顺序访问）  

+ SSD：固态硬盘
+ Fast Network Storage：使用传输介质极快的局域网的存储介质
+ HDD：机械硬盘
+ Network Storage
+ Tape Archives：磁带硬盘

从一次缓存的一次访问时间是0.5ns，（DRAM要100ns，SSD要150.000ns，HDD要1e7ns）到磁带硬盘的一次访问时间是1e9ns，有如此大数量级倍数的差异，相当于从0.5秒到（100秒，1.7天，16.5周）31.7年。

+ 一般来讲，顺序访问较于随机访问快得多。

## Cache

+ Reference：
	+ [给我树苗的《Cache的基础知识》](https://zhuanlan.zhihu.com/p/632189718)

## 分支预测

+ Reference：
	+ [johnnysswlab的《How branches influence the performance of your code and what can you do about it?》](https://johnnysswlab.com/how-branches-influence-the-performance-of-your-code-and-what-can-you-do-about-it/)

+ Pre：现在CPU一般都有一下几个功能：
	+ Pipeline流水线
	+ Out of order execution乱序执行
	+ Branch prediction分支预测
	+ Speculative execution推测执行

	分支预测主要是为了服务流水线，不然怎么流水出多分支的指令？

+ 在没有分支预测的CPU上，也会提前处理分支后的指令，如果错误了，就重新

+ Vectorization：一下处理多个数据。不论是算还是存
