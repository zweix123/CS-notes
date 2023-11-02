+ You can see an estimate of how much different programming languages are used here: https://www.tiobe.com/tiobe-index/

+ 一个语言，分成标准和实现，比如C/C++，有一群人在研究它的标准，同时有一批人在实现它们（的编译器），在不同的实现中有不同的特性，我个人称之为方言，比如实现C++的有GNU、Clang和微软的编译器。当然，比如C++可能研究标准的和实现的是不同的人，但是也有像Python的标准和核心实现几乎是同一拨人，所以严格上来说Python没有标准，而是它的实现称为了事实标准，这也有独特的现象，其他任何一个解释器都干不过CPython，因为它们需要等着CPython的实现去实现自己的编译器，各种库也是优先保证CPython的可行。
+ 代码规范
	+ [Google代码规范](https://zh-google-styleguide.readthedocs.io/en/latest/)
	+ 余子豪：
		+ 不言自明 - 仅看代码就能明白是做什么的(specification)
		+ 不言自证 - 仅看代码就能验证实现是对的(verification)
+ 我来发表一些爆论：世界上的编程语言可谓是不计其数，但是被最广泛使用的是有限的，它们可能有这样那样的问题，一种解决方案就是我们可以创建一个更现代的语言来解决这个问题，但是我觉着面对这样的问题不应该首先想着搞一个新语言。一方面，这完全是工程问题，是动态变化的，新语言同样可能会出现新的问题；另一方面，有大人口基数的语言有巨大的历史惯性，有大量的应用积累，毕竟技术是为了解决需求。所以我觉得应该是是总结并使用一个语言的最佳实践、扬长避短即可。

## 内存模型

+ Reference：
	+ [保罗的酒吧的文章](https://paul.pub/cpp-memory-model/)
	+ [Russ Cox的三篇博客](https://research.swtch.com/mm)：[第一篇翻译](https://colobu.com/2021/06/30/hwmm/) | [第二篇翻译](https://colobu.com/2021/07/11/Programming-Language-Memory-Models/) | 
	+ [Jeff Preshing的《An Introduction to Lock-Free Programming》](https://preshing.com/20120612/an-introduction-to-lock-free-programming/)

+ 内存模型的含义：
	+ 原子操作
	+ 局部顺序：一系列不能乱序的操作
	+ 可见性：对共享变量对其他线程的可见性

+ 为什么需要内存模型：
	+ 编译器优化
	+ CPU乱序执行
	+ Cache不一致
