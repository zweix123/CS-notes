
# Breaking-the-x86-ISA

+ ref：
	+ [video](https://www.youtube.com/watch?v=KrksBdWcZgQ)
		+ [homepage](https://www.blackhat.com/us-17/briefings.html#breaking-the-x86-instruction-set)
			+ [paper](https://www.blackhat.com/docs/us-17/thursday/us-17-Domas-Breaking-The-x86-Instruction-Set-wp.pdf)：官网链接的文论不全，全文是6页，它只有3页，不知道为啥。
			+ [slide](https://www.blackhat.com/docs/us-17/thursday/us-17-Domas-Breaking-The-x86-ISA.pdf)

+ 背景：
+ 目的：

## Searching the Instruction Set: tunneling

+ Pre：
	+ 困难：x86的指令是不定长的，范围是1到15字节
+ 简单方案：
	+ 随机：时间不可接受，随机采样覆盖率低
	+ 依赖文档：需要先验知识，无法发现未知指令



1. 15个字节的buffer
2. 从一个长度开始，递增该长度buffer中的低字节
3. 检测当前指令，如果**指令长度变化**或者**异常**

## Resolving Instruction Lengths: injector

+ 方法：
	+ disassembling：但是不能处理未记载指令
	+ trag flag：观察指令之前前后的instruction pointer，但是不能处理抛出异常的指令
+ 要求：
	+ injector需要可以识别不同的mode下的指令

+ 页错误分析：

	对于需要检测的指令（15字节），将其其中1个字节放在一个页（执行页）中，然后将剩余的14个字节放在下一个页（非执行页）

	如果页错误出现在指令fetch中，则触发`#PF`异常，页的边界也出现在`CR2`寄存器中，表明有部分页在下一个页中

	如果发现没有，则移动一个字节

	还有一点，如果该指令不存在，则抛出的是`#UD`异常

	而privileged指令则会抛出`#GP`

	+ 既然我们选择页错误作为检测方式，那么怎么保证程序的正常进行呢（维持执行一致性）？比如其他功能，持久化
		+ 保持在ring3，应该是用户态
		+ 要hook所有可能异常，当出现时，将存储异常的寄存器换成“已知且正常”的
		+ 比如写指令到injector的地址空间中 -> 将所有的寄存器初始化为0并映射空指针到injector内存中
		+ 将一个页映射到地址0
			+ 因为这样非特权指令也可以正常执行，进而区分
			+ 但是仍然不保险，有些指令仍然可能修改
				+ 所以和一个手动的黑名单
		+ 测试后怎么恢复，面对分支指令，通过设置trap flag，在指令测试（执行）之前设置，它允许执行指令之后抛出单步异常

## 指令判断: sifter

+ sifter：
	+ 使用反汇编器估算指令长度
	+ 与injector的结果进行比较
	+ 有差异说明存在错误
	+ 如果injector发现指令存在，但是反汇编器说没有，那么这是一个没有文档的指令
	+ 那么对于虚拟机管理程序和硬件错误呢？这些会导致injector判断的长度不一样，进入被标记为错误，需要手动划分