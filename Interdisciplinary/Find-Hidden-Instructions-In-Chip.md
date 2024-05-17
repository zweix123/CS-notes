# Breaking-the-x86-ISA

+ ref：
	+ [video](https://www.youtube.com/watch?v=KrksBdWcZgQ)
		+ [homepage](https://www.blackhat.com/us-17/briefings.html#breaking-the-x86-instruction-set)
			+ [paper](https://www.blackhat.com/docs/us-17/thursday/us-17-Domas-Breaking-The-x86-Instruction-Set-wp.pdf)：官网链接的论文不全，全文是6页，它只有3页，不知道为啥。完整的要在Github上找，见下。
			+ [slide](https://www.blackhat.com/docs/us-17/thursday/us-17-Domas-Breaking-The-x86-ISA.pdf)
	+ [sandsifter](https://github.com/xoreaxeaxeax/sandsifter)：项目中有完整的论文

+ 背景：
+ 目的：找到处理器中的
	+ 隐藏指令
	+ 软件错误
	+ Hypervisor Flaw
	+ 硬件勘误

## tunneling指令搜索

+ pre：
	+ 难点：x86的指令是不定长的，范围是1到15字节，枚举量大。
+ bg：
	+ 简单方案：
		+ 遍历：时间不可接受
		+ 随机：采样覆盖率低
		+ 依赖文档：需要先验知识且无法发现未知指令

+ 15个字节的buffer
1. 从一个字节长度开始迭代，递增该区间最低字节中的值。
2. check，如果**指令长度**和当前不一致，则延长一个字节长度，继续从当前的最低位迭代。
3. 如果一个字节迭代到255，则长度减少一个字节。

## injector指令长度判断

+ pre：
	+ 方法：
		+ disassembling：但是不能处理未记载指令
		+ trag flag：观察指令执行前后的instruction pointer，但是不能处理抛出异常的指令
	+ 要求：
		+ 可以识别不用mode下的指令

页错误分析：对于需要检测的指令（15字节），将其其中1个字节放在一个页（执行页），剩余14个字节放在下一页（是非执行页）
+ 如果在fetch中错误，会触发`#PF`异常，页的边界也出现在`CR2`寄存器中，此时表明有部分指令在下一页，移动1个字节，直到正常
+ 如果指令不存在，则抛出`#UD`异常
+ 如果指令的privileged不对，则抛出`#GP`异常

其他

+ 程序一致性，既然使用页错误作为检测方式，怎么保证程序本身的正常执行呢？
	+ 要求：
		+ 保持在ring3，即用户态
		+ hook所有异常，当异常出现时，处理完后将异常寄存器置为“已知且正常”
	+ 做法：
		+ 将所有的寄存器初始化为0并映射空指针到injector内存中
		+ 将一个页映射到0
			+ 非特权指令也能正常执行，进而区分
			+ 仍然不保险，手动维护一个黑名单
		+ check后恢复，面对分支指令，通过设置trap flag，在指令测试（指令）之前设置，其运行指令后抛出单步异常

## sifter指令分析
>上面的方法将搜索空间从 ${10}^{36}$ 变成了 `1e8`，下面的问题就是对筛选出来的指令进行分类

使用已有的反汇编器（Capstone），比较反汇编器的结果的长度和injector的结果。
1. 如果长度不同则是软件错误
2. 如果injector认为指令存在而反汇编器认为不存在则是一个未知指令
3. 剩下的手动分析。

## 结果

作者将代码在一下处理器执行：Intel Core i7-4650U, Intel Quark SoC X1000, Intel Pentium, AMD Geode NX1500, AMD C-50, VIA Nano U3500, VIA C7-M, Transmeta TM5700, and another.