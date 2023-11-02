+ 参考学习资料：
	+ Crafting interpreters：全开源，我愿称之为学习编译原理最好的第一本书
		+ 官网：http://www.craftinginterpreters.com/
		+ Github：https://github.com/munificent/craftinginterpreters
		+ 比较不错的翻译：https://readonly.link/books/https://raw.githubusercontent.com/GuoYaxiang/craftinginterpreters_zh/main/book.json

+ zweix一家之言：编译原理是实践而不是理论，在这样的认知下
	+ 关于编译原理的各种定义，比如语言类型，编译阶段，都可以认为是一种认识事物的角度，在实践时不必"墨守成规"
	+ 关于编译原理的各种名词，比如生成抽象语法树的各种技术，它们真的就是技术，有缺点、有特点、有适用范围，在实践时选择合适的甚至根据已有的去改编也行

# Intro

+ translation program的区分：
	+ Compiler编译器：Program经过compiler输出executable file，执行exe输入Data，输出Output
	+ Interpreter解释器：Program和Data一起同时进入Interpreter，输出Output

	实际上这样的划分不能概括所有情况，比如Python，在CPython中，先将代码转换成字节码，然后对字节码进行解释运行  
	所以下文不再可以区分，除非特殊声明，否则两个基本同义

+ 
	+ 词法分析工具：lex(Unix) <- flex(Linux)：C的扩展，文件扩展名为`l`，通过编译器将其转换成C语言进行编译
	+ 语法分析工具：yacc(Unix) <- bison(Linux)：文件扩展名为`y`

+ 执行代码的方案：
	+ transfer to 机器码
		+ 编译
		+ single-pass compilers：直接在parser中生成code
			+ 会限制语言的设计，比如没有全局数据结构存储全局变量，执行顺序只能可见
			+ 需求来自当年的内存非常稀有，编译器做不到现在这种
	+ transfer to 字节码，解释字节码
		+ virtual machine虚拟机，机器码运行在物理机上，虚拟机类似模拟物理机来运行字节码
		+ Just-in-time, JIT complitation即时编译：执行代码最快的方式就是将其转换成机器码，所以对解释型的语言在运行时转换成机器码
			+ 能分析哪些区域对性能最关键，对热点进行重编译
			+ 缺点肯定是复杂
			+ 优点就是既能有解释型语言的灵活，又能逼近编译型语言的性能
	+ source-to-source complier/transcompiler：把你的语言转换成其他的语言或者其他语言的中介码
	+  tree-walk interpreter：直接在AST中运行
		+ 缺点是慢

## overview

+ 整个编译过程通常分成front end、middle end、back end
	+ 这个middle end似乎有点怪，几乎可以直接理解为中间代码
	+ 为什么如此划分？想一下，如果你想为`x`个语言编写`y`个指令集机器的编译器，则需要写$x \times y$个软件；如果对于每个语言，分别写个软件将它们转换成中间代码，然后在分别写个软件将中间代码转换成各个指令集的硬件代码，这就只需要`x + y`个

<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Compiler/mountain.png" width="70%">


### 前端

1. Scanning/lexing/lexical analysis: txt -> token
2. Parsing/syntactic analysis: token -> parse tree/abstract syntax tree(AST)
3. Static Analysis/Semantic Analysis: 
	+ 比如为identifier和scope进行binding or resolution
	+ 比如type check

### 中端
intermediate representation, IR中介码

4. Optimization:
	+ 比如常量折叠

### 后端

5. Code Generation
	1. 生成机器码
	2. 生成bytecode字节码


## 编程语言设计

+ 关于函数参数：
	+ argument：actual parameter实参，给到函数的值
	+ parameter：formal parameters形参，在函数中的变量

+ 关于OOP语言的设计：
	+ [classes](https://en.wikipedia.org/wiki/Class-based_programming)类：这种方式是最多的
		+ instances实例和类classes
	+ [prototypes](https://en.wikipedia.org/wiki/Prototype-based_programming)原型：比如Golang中的接口就是原型，随着Js而更多的被讨论
	+ [multimethods](https://en.wikipedia.org/wiki/Multiple_dispatch)

+ 关于表达式的side effect副作用

+ 关于控制流的定义：
	+ Conditional条件/Branching control flow分支控制流
	+ Looping control flow循环控制流

+ desugaring脱糖
	>syntactic sugar语法糖，最广泛的是for对于while

	语法糖是有代价的，特别是对于复杂的语言，会让后端更复杂，脱糖就是前端将语法糖转换成更基础的形式

+ 关于语言内存类型：
	+ 基于堆栈
	+ 基于寄存器指令集

	比如lua前期是使用堆栈的模拟器，在5.0转换基于寄存器，快了很多，也复杂了很多

## 编程语言实现

+ 环境：变量与值之间的绑定关系保存的地方。
+ 作用域scope：定义了名称映射到特定实体的一个区域，多个作用域允许相同名称在不同的上下文指向不同的内容。
	+ 静态作用域/词法作用域：局部变量和全局变量，可以通过静态分析得知
	+ 动态作用域：多态

+ 作用域与环境，前者是理论，后者是实现机制
	+ 块作用域结束后里面的变量应该不在
	+ 不是粗暴的删除，因为可能全局也有同名的，所以块作用域应该是shadow遮蔽
	+ 而且还要考虑块作用域引用了全局的变量


# 实现

## 1.lexing词法分析

+ 概念：
	+ lexemes词素: lexing中的每一组具有某些含义的最小序列
	+ Tokens: 将lexemes和*其他数据*放在一起

	比如一个数字`42`，`"42"`这个字符串为一个词素，一个结构体，其中包含数字这个Token类型，这个词素还有其他数据，则是Token
	
	+ token data struct
		+ Token type
		+ Literal value字面量
		+ Location info

### regular language and expression正则语言和表达式
一种实现词法分析的工具

+ 有些语法，比如Python的语法不是regular的，因为它缩进敏感，所以要比较连续行的开头空格数量，regular language无法实现
+ 关于分号和全大写关键字，都已经是时代的眼泪的，关于的分号的处理，可以用换行符尝试替代，但是这样的方法在不同的语言中有[不同的处理方式](https://readonly.link/books/https://raw.githubusercontent.com/GuoYaxiang/craftinginterpreters_zh/main/book.json/-/4.%E6%89%AB%E6%8F%8F.md#design-note-implicit-semicolons)。

### 手动模拟

对于简短的符号，比如一个字符的符号和两个字符串的符号，可以通过switch和lookahead解决，对于不规则的比如数字、字符串、标识符和保留字则通过分类讨论和trie树

## 2.syntactic analysis句法分析

### 形式化语言表达语法

+ [Formal grammar形式化语言](https://en.wikipedia.org/wiki/Formal_grammar)：有一组原子片段，即alphabet，分别对应一组string（由alphabet中的letter组成的sequence）
	+ 那如何写下一个包含无限多有效字符串的语法呢？
		+ derivations派生
		+ productions生成

+ 其实上面我们也已经看到了，有些语法不能用正则语言处理，这个就是同样的处理的工具，当然它的功能更加强大。  
	对照定义，这个工具
	+ 如果用于词法分析中，则单个字符的表就是alphabet，所有的lexeme就是string
	+ 而在句法分析中，则每个token是的letter，然后组合成expression

+ Context-Free Grammars上下文无关语法：形式化语言的一种
	+ 每个生成式有一个head（名称），一个body，从形式上body是一系列符号symbol
	+ 符号有两种：
		+ terminal：字面量，
		+ nonterminal：名称（一个生成式的（即可以是自己））

	我们可以将无限多的字符串打包到一个有限的语法中

这些是概念上的，具体的什么样子的？

+ 巴科斯范式BNF：`name -> symbols;`，终止符是带引号的字符串，非终止符是小写的单词。

	+ 一种扩展语法：
		+ 支持`}`和`()`的组合
		+ 支持`*`、`+`和`?`（正则表达式概念下的）

我们很快遇到问题，对于一个字符串可能有多种生成的方式（意味着多种可能的AST）

+ Precedence优先级
+ Associativity结合性

### 建立抽象语法树
abstract syntax tree, AST抽象语法树

有很多工具

#### 递归下降建立

+ recursive descent递归下降（自顶向下解析器）：将语法规则直接翻译成命令式代码的文本翻译器，每个规则变成一个函数
	+ Terminal：匹配并消费一个token
	+ NonTerminal：调用规则对应的函数
	+ `*` and `+`：loop
	+ `?`：if

+ 检查语法错误：因为代码解析同样出现于静态分析，比如高亮，所以解析器会大量遇到错误的代码
	+ Detect and report the error
	+ Avoid crashing or hanging

	+ Be fast
	+ Report as many distinct errors as there are
	+ Minimize cascaded errors最小化级联错误

+ error recovery：
	+ panic mode：当遇到错误，它进入恐慌模式，要先进行synchronization同步，将当前的状态和下面的token的状态对齐，使后面是对的。

+ 抽象语法树的应用
	+ 直接在AST上运行
	+ 不依赖运行时状态的工作
		+ 没有副作用
		+ 没有控制流

#### 自顶向下算符优先解析建立

这种算法（如果可以称为算法的话），有很多，这里只讨论Pratt Parsing算法
https://matklad.github.io/2020/04/13/simple-but-powerful-pratt-parsing.html

## 3.semantic analysis语义分析
不是必须的，概念性的

## 运行时

### 闭包

+ Lua的实现方式：upvalue

### 垃圾回收

### 反射

# MISC

+ 图灵机：
	>什么样的函数是可计算的？

	艾伦·图灵和阿隆佐·邱奇分别做出了回答，他们各自设计了一个具有最小机器集的微型系统，前者发明图灵机，后者则是lamdba演算

	+ 图灵完备Turing-complete：语言可以实现一个图灵机的模拟器，因为图灵机是可以计算任何可计算函数，那么实现了图灵机的语言也可以。