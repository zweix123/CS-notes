## RoadMap

```
                                Julian Stecklina's baresifter
                        |-------------> bare-machine
                        |
                      tunnel        Catherine Easdon
       |--Search-->    and -----------> check
       |         page-error-analysis
       |                |----- -------> Li X
Domas's Sandsifter      |    optimization: prefix instruction
       |                |
       |                |-------------> JiaTong
       |                           instruction format
       |
       |          register            Catherine Easdon
       |-Analysis-> and --------------> Clock Cycle
                 Side channel
                        |-------------> JiaTong
                                         Port    
```

# Breaking-the-x86-ISA
>Domas

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

+ 准备15个字节长度的buffer，并初始化为全0
	```
	00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	```
+ 从第一个字节开始迭代
	```
	 @
	01 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	```
+ 检查当前buffer中作为指令本身的长度
	```
	 @
	01 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	--
	```
+ 当前指令长度和迭代区间范围一致，继续迭代
	```
	 @
	02 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	03 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	04 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	--
	```
+ 直到长度变化（这里以长度变化多于1个字节为例）
	```
	 @
	04 00 00 00 00 00 00 00 00 00 00 00 00 00 00
	--------
	```
+ 则使用当前长度的最低字节开始迭代
	```
	 @  @  @
	04 00 01 00 00 00 00 00 00 00 00 00 00 00 00
	--------
	```
+ 继续
	```
	 @  @  @
	04 00 02 00 00 00 00 00 00 00 00 00 00 00 00
	04 00 03 00 00 00 00 00 00 00 00 00 00 00 00
	04 00 04 00 00 00 00 00 00 00 00 00 00 00 00
	--------
	```
+ 当迭代位迭代完毕时，迭代更上一层
	```
	 @  @  @
	04 00 fe 00 00 00 00 00 00 00 00 00 00 00 00
	04 00 ff 00 00 00 00 00 00 00 00 00 00 00 00
	 @  @
	04 01 00 00 00 00 00 00 00 00 00 00 00 00 00
	04 02 00 00 00 00 00 00 00 00 00 00 00 00 00
	--------
	```

	注意此时迭代区间和指令长度不同
+ 如此往复

## injector指令长度判断
上面搜索算法中的关键在于如何判断buffer中的字节序列中表达指令部分的长度。

>在代码实现中，搜索包含判断长度，整个程序叫做injector，而不出判断长度部分叫做injector。

+ pre：
	+ 方法：
		+ disassembling：但是不能处理未记载指令
		+ trag flag：观察指令执行前后的instruction pointer，但是不能处理抛出异常的指令
	+ 要求：
		+ 可以识别不用mode下的指令

**页错误分析**：对于需要检测的指令（15字节），将其中1个字节放在一个页（执行页），剩余14个字节放在下一页（是非执行页）
+ 如果在fetch中错误，会触发`#PF`异常，页的边界也出现在`CR2`寄存器中，此时表明有部分指令在下一页，移动1个字节，直到正常
+ 如果指令不存在，则抛出`#UD`异常
+ 如果指令的privileged不对，则抛出`#GP`异常

### 其他问题

+ 程序涉及到页，怎么保证程序injector本身不崩溃呢？
	1. 保持在ring3，即用户态，上面算法显示不影响，依然可以处理权限更高的指令
	2. hook所有的异常，比如Linux下的段错误这种，当异常出现时，处理完指令后将异常寄存器设置为已知正常的
	3. 在处理指令前将所有通用寄存器设置为0
	4. 在处理指令前设置trap flag，保证其运行后抛出单步异常

## sifter指令分析

>上面的搜索方法将搜索空间从 ${10}^{36}$ 降低到 `1e8`，剩下的问题就是怎么判断搜索的指令是有问题的。

使用已有反汇编器（Sandsifter）使用Capstone，比较反汇编器的结果（它是按照Manual的）和injector的结果
1. 如果长度不同则是软件错误
2. 如果injector认为指令存在但反汇编器认为不存在则是一个未知指令
3. 剩下的手动分析

## 结果

作者将代码在以下处理器执行：Intel Core i7-4650U, Intel Quark SoC X1000, Intel Pentium, AMD Geode NX1500, AMD C-50, VIA Nano U3500, VIA C7-M, Transmeta TM5700, and another.

# Hardware Backdoors in x86 CPUs
>Domas
Domas

# X86架构处理器隐藏指令检测与功能分析

+ ref：
	+ 知网检索即可
