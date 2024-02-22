>在写xv6 lab时的笔记，包括坑点和随手笔记，估计这样的笔记不可避免的涉及剧透，请酌情观看。

+ VSCode调试xv6符号跳转：`make clean && bear -- make qemu`即可。
+ 系统调用`close`的功能：
	+ 向系统归还可用的文件描述符
	+ 向文件中写入EOF（文件结束）
+ 关于系统调用`dup`，在xv6 book的第一张有`dup(p[0])`就是将管道的读取端和标准输入`0`绑定。dup是在当前的未使用的文件描述符中选择最小的，将其作为参数的“绑定”/"引用"，代码运行至此时最小的是0，所以`0`就和`p[0]`绑定了，不需要显示的接受`dup`的返回值，所以管道会向`p[0]`写东西，这些自然就从文件描述符`0`出来了。
+ lab2的调试按照manual的步骤是运行不起来的，问题描述和解决方案在[so](https://stackoverflow.com/questions/76025743/error-shown-a-problem-internal-to-gdb-has-been-detected-when-doing-xv6)上。