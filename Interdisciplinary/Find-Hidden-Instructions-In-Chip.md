
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


we use a buffer of 15 0 bytes as the starting
candidate. The instruction is executed, and its length (in bytes)
is observed. The byte at the end of the instruction is then
incremented. For example, in the case of the 15 byte zero
buffer, the instruction will be observed to be two bytes long