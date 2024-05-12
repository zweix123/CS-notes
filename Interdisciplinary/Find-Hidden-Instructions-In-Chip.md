
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

+ 页错误分析