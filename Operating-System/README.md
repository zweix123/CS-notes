+ Reference：
	+ [ostep](http://www.ostep.org/)，南大蒋岩炎老师称之为操作系统最好的自学书籍
		+ 完全开源，但是各个章节分成多个PDF，[这个脚本](https://github.com/zweix123/arsenal/blob/master/crawler/get_ostep_all_pdf_and_merge.py)的功能是爬取所有章节并拼接成一份PDF
			+ 上面这个脚本是同步，不是那么快，有相对官方的汉化版书籍，我又写了[一个爬虫](https://github.com/zweix123/arsenal/blob/master/crawler/get_zh_ostep_all_pdf_and_merge.py)，这个具有超过的并发
		+ 作者GitHub[链接](https://github.com/remzi-arpacidusseau)

	+ MIT6.S081
		+ [野生讲义翻译](https://mit-public-courses-cn-translatio.gitbook.io/mit6-s081/)

# syscall

## `read`

+ 在syscall `read`中，其中的第三个arg是“期待字节数”
	+ 如果fd是动态的，比如pipe，则会阻塞当前进程，等待pipe中的字节数足够
	+ 只有过程中出现什么问题了，才会error，返回`-1`
	+ 那么什么时候返回小于这个数字呢？可能出现在文件中，但是我们结合动态的情况，read是怎么知道是真的不足而不是暂时不足呢？是通过`EOF`，末尾有EOF则是。反过来我们也可以往（或者自动）fd中放EOF表示输入结束。

## blocking mode and nonblocking mode

对于非阻塞的IO，代码并没有获得期望的数据，只有当前调用的状态，要轮询判断是否完成
1. 重复调用：笨笨
2. select：将调用状态关联到一个数组上，然后轮询数组check状态，数量有限
3. poll：将调用状态关联到一个链表上，然后轮询链表check状态，性能低下
4. epoll：自然回调，当事件完成唤醒

## OCI

https://blog.lizzie.io/linux-containers-in-500-loc.html

# xv6 lab note
>在写xv6 lab时的笔记，包括坑点和随手笔记，估计这样的笔记不可避免的涉及剧透，请酌情观看。

+ VSCode调试xv6符号跳转：`make clean && bear -- make qemu`即可。
+ 系统调用`close`的功能：
	+ 向系统归还可用的文件描述符
	+ 向文件中写入EOF（文件结束）
+ 关于系统调用`dup`，在xv6 book的第一张有`dup(p[0])`就是将管道的读取端和标准输入`0`绑定。dup是在当前的未使用的文件描述符中选择最小的，将其作为参数的“绑定”/"引用"，代码运行至此时最小的是0，所以`0`就和`p[0]`绑定了，不需要显示的接受`dup`的返回值，所以管道会向`p[0]`写东西，这些自然就从文件描述符`0`出来了。
+ lab2的调试按照manual的步骤是运行不起来的，问题描述和解决方案在[so](https://stackoverflow.com/questions/76025743/error-shown-a-problem-internal-to-gdb-has-been-detected-when-doing-xv6)上。
