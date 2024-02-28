+ 冯诺伊曼结构：
	>John von Neumann

	+ flow：
		1. **fetch** instruction from memory
		2. **decodes** it
		3. **executes** it
		4. move to next instruction

# ISA
>Instruction Set Architecture指令集架构

+ ISA分类以及典型的ISA及其分类
	+ Complex Instruction Set Computer, CISC复杂指令集
		+ x86-64
	+ Reduced Instruction Set Computer, RISC精简指令集
		+ ARM：ARMv8支持64位虚拟地址（之前最多支持32位），其支持两种执行模式
			+ AArch32：为向前兼容
			+ AArch64
		+ RISC-V

+ 典型ISA简介：
	+ x86-64
	+ AArch64：
		+ 每条指令长度固定4字节，指令类型包含：数据搬运、寄存器计算、内存读写、跳转、过程调用、特权

## 特权级
>内核态（对比用户态）

+ 切换时机：
	+ 特权调用指令
	+ exception
	+ interrupt

+ 由CPU和OS协同完成
	1. CPU保存状态，通常保存到寄存器中
		+ Program Counter, PC
		+ Stack Pointer, SP
		+ 切换原因

	2. CPU读取Exception Vector Table（寄存器保存其基地址），根据原因调用OS设置的Handler
	3. 处理完成，OS恢复程序上下文执行指令返回

+ 典型ISA：
	+ AArch64：将特权级称为Exception Level, EL异常级别
		+ EL0：用户态
		+ EL1：内核态
		+ EL2：用于系统虚拟化场景使用
		+ EL3：与安全特性TrustZone有关，分成Normal World普通世界和Secure World安全世界。

# Storage

+ 存储层次结构：从上到下，越来越慢、越来越大（越来越便宜）（、越来越不易损坏）
	1. CPU Register
	2. CPU Caches
	3. DRAM：Memory

	+ Volatile：Byte-Addressable Random Access

	4. Non-Volatile Memory：非易失性内存
		>很新很贵，未广泛使用

	+ Non-Volatile：Block-Addressable Sequential Access

	5. SSD（固态硬盘）
	6. Fast Network Storage：比如使用传输介质很快的局域网
	7. HDD（机械硬盘）
	8. Network Storage
	9. Tape Archives（磁带）

## Cache

+ References：
	+ [给我树苗的《Cache的基础知识》](https://zhuanlan.zhihu.com/p/632189718)

在局部性原理的基础上，为解决CPU处理速度和内存访问速度之间的矛盾以及存储介质价格和性能之间的矛盾，于是有了缓存。



+ 局部性原理：空间局部性和时间局部性

+ 程序的指令部分和数据部分一般分别存放在两片不同的Cache中，即I-Cache指令缓存和D-Cache数据缓存
	```
	> lscpu | grep cache 
	L1d cache:                       256 KiB
	L1i cache:                       256 KiB
	L2 cache:                        2 MiB
	L3 cache:                        16 MiB
	```

相联方式不同，直接相联、全相联、Set Associative组相联，其中组相联是前两者的这种，兼顾性能和价格，最常见

+ Set/Index组、Way路、Line行
+ 物理地址表示：Tag（对应Way）、Index（对应组）、Offset（对应行）

这里的组是在地址中的密集表示，比如8bit表示256个组，而Tag则是一个较宽的字节，在对应组中的若干个路中到对应的。相当于缓冲是一个`std::array<std::map<Way, Bytes>>`


# 分支预测

+ References：
	+ [johnnysswlab的《How branches influence the performance of your code and what can you do about it?》](https://johnnysswlab.com/how-branches-influence-the-performance-of-your-code-and-what-can-you-do-about-it/)

+ Pre：现在CPU一般都有一下几个功能：
	+ Pipeline流水线
	+ Out of order execution乱序执行
	+ Branch prediction分支预测
	+ Speculative execution推测执行

	分支预测主要是为了服务流水线，不然怎么流水出多分支的指令？

+ 在没有分支预测的CPU上，也会提前处理分支后的指令，如果错误了，就重新

+ Vectorization：一下处理多个数据。不论是算还是存
