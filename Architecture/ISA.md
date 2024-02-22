ISA：Instruction Set Architecture指令集架构

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

## AArch64

每条指令长度固定为4字节，指令类型
+ 数据搬运
+ 寄存器计算
+ 内存读写
+ 跳转
+ 过程调用
+ 特权


+ 特权级，在AArch64的特权级成为Exception Level, EL异常级别
	+ 有四个级别，分别从0到3
		+ EL0：用户态
		+ EL1：内核态，操作系统
		+ EL2：虚拟化场景需要，Virtual Machine Monitor, VVM/Hypervisor虚拟机监控器使用
		+ EL3：与安全特性TrustZone有关
			+ 分为normal world普通世界和secure world安全时间