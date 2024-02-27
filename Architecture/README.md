
## 冯诺伊曼结构
>John von Neumann冯·诺伊曼

+ 

	1. **fetch** instruction from memory
	2. **decodes** it
	3. **executes** it
	4. move to next instruction

## ISA
>Instruction Set Architecture指令集架构

+ 典型的ISA及其分类：
	+ Complex Instruction Set Computer, CISC复杂指令集：x86-64
	+ Reduced Instruction Set Computer, RISC精简指令集：ARM
		>ARMv8（支持64位虚拟地址（之前都最多支持32位）），其支持两种执行模式——AArch32和AArch64，前者为向前兼容

+ 特权级：
	+ 用户态到内核态的切换
		1. 特权调用指令
		2. exception异常
		3. interrupt中断

	+ 由CPU和OS协同完成：
		1. CPU保存处理器状态，通常保存到寄存器中：
			+ 指令地址（Program Counter, PC程序计数器）
			+ 原因
			+ Stack Pointer, SP栈指针
		2. CPU读取exception vector table（寄存器中保存其基地址），根据原因调用OS设置的handler
		3. 处理完成，OS回复程序的上下文执行指令返回

### AArch64

每条指令长度固定为4字节，指令类型
+ 数据搬运
+ 寄存器计算
+ 内存读写
+ 跳转
+ 过程调用
+ 特权

---

+ 特权级，在AArch64的特权级成为Exception Level, EL异常级别
	+ 有四个级别，分别从0到3
		+ EL0：用户态
		+ EL1：内核态，操作系统
		+ EL2：虚拟化场景需要，Virtual Machine Monitor, VVM/Hypervisor虚拟机监控器使用
		+ EL3：与安全特性TrustZone有关
			+ 分为normal world普通世界和secure world安全时间

## 存储层次结构

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

### Cache

+ Reference：
	+ [给我树苗的《Cache的基础知识》](https://zhuanlan.zhihu.com/p/632189718)

+ 矛盾：
	+ CPU处理速度和内存访问速度之间的矛盾——于是有了缓存
		+ CPU要访问的数据在Cache有缓存，则为Hit命中，否则是Miss
	+ 存储的价格和性能的矛盾——于是有了多级缓存
		+ CPU的Cache细分为几层：Register -> L1 Cache -> L2 Cache -> L3 Cache -> Memory -> Mass Storage，读写延迟依次增加、实现成本依次降低

+ 局部性原理：空间局部性和时间局部性

+ 程序的指令部分和数据部分一般分别存放在两片不同的Cache中，即I-Cache指令缓存和D-Cache数据缓存
	```
	> lscpu | grep cache 
	L1d cache:                       256 KiB
	L1i cache:                       256 KiB
	L2 cache:                        2 MiB
	L3 cache:                        16 MiB
	```

## 结构

相联方式不同，直接相联、全相联、Set Associative组相联，其中组相联是前两者的这种，兼顾性能和价格，最常见

+ Set/Index组、Way路、Line行
+ 物理地址表示：Tag（对应Way）、Index（对应组）、Offset（对应行）

这里的组是在地址中的密集表示，比如8bit表示256个组，而Tag则是一个较宽的字节，在对应组中的若干个路中到对应的。相当于缓冲是一个`std::array<std::map<Way, Bytes>>`


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
