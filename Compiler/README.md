
## 几个问题

+ 编译器和解释器：一般来说，以这样的方式区分：
	+ 编译器：将代码作为输入，将机器码作为输出；机器码有输入和输出
	+ 



+ 编译器和解释器：一般来说，通过这样的方式区分，
	+ 编译器是将代码作为输入，机器代码作为输出，然后机器代码有自己的输入和输出
	+ 解释器是将代码和输入一起作为输入，将计算结果作为输出

	但个人认为这样区分编译器或者解释器意义不大，实际上，在解释器中也有“编译”的部分，比如将代码作为输入，将中间代码或者字节码作为输出。然后将字节码和输入一起作为解释器剩下部分的输入。

	故下面不再区分，以编译器作为覆盖以上概念的具有最大意义的概念。

+ 程序语言与编译器




+ References：
	+ [Crafting interpreters](http://www.craftinginterpreters.com/)：全开源，我愿称之为学习编译原理最好的第一本书；[代码](https://github.com/munificent/craftinginterpreters) | [翻译](https://readonly.link/books/https://raw.githubusercontent.com/GuoYaxiang/craftinginterpreters_zh/main/book.json)
	+ [Essentials of Compilation](https://github.com/IUCompilerCourse)

 

+ 编译相关书籍布局：
	+ 通常将编译组织为一系列阶段，然后每个章节描述一个阶段
	+ 增量方法，在每一章都构建一个完整的编译器，然后逐渐丰富功能