>concurrency并发，不是coroutine协程，因为GIL的存在，Python的多线程不能真的有多个线程在并行的跑，以至于实际上在并发模型上线程和协程有很多相像之处，所以在一起讨论。

# 线程
>第一个多核CPU IBM的Power4出现在2001，而多线程的概念在上个世纪五六十年代就已经出现了，那么这半个多实际的时间多线程在干嘛呢？

主要是IO瓶颈问题，当前现在协程也行了，而且协程还没有竞争冒险。但是协程有一个无法回避的问题：必须显式的放权，这在大量IO中没有问题，因为每个task都会频繁的放权，但是在计算密集时，调度就成了问题，在协程中显式的放权会有一些问题（影响代码的优雅、对Task的时间消耗难以估计，如果Task调用其他函数则无法在函数中放权。而多线程则可以自动调度。

## threading.Thread

一种写法
```python
class Task(threading.Thread):
	def __init__(self, ...):
		...
		super.__init__()
	def run(self):
		...

t = Task(...)
```
另一种写法
```python
t = Thread(target=一个函数)
```

<hr>

使用：
```python
t.start()  # 放到后台运行，当前线程不阻塞

t.join()  # 阻塞当前线程，等待t的
```

# 协程

+ 目前Python中有关于协程的库：
	+ asyncio
	+ gevent
	+ tornado

## Pre: GIL
>Global Interpreter lock

+ 首先要知道什么是进程和线程
+ 在线程和进程中有racing condition竞争冒险问题，即由于线程之间的相对运行顺序不同导致的结果不同
+ 而Python是如何管理内存的呢？特别是Python解释器的memory managment是怎么释放内存的呢？答案是reference count引用计数机制
+ 这里的源码中有C语言的`--`操作，这可不是atomic的呦，它是读、减、存，会发生竞争冒险
+ 怎么解决竞争冒险问题呢？加锁。Python Object有多个引用计数，设计者直接加了一个全局锁，保证每个bytecode线程安全
这就是GIL
+ 好处：
	+ 简单
	+ 不会死锁
	+ 对于单线程和不能并行的程序，全局锁性能更好，因为“要锁”需要时间，而全局锁的方案锁少
	+ 让Python写C extension更容易
+ 缺点：缺点是显然的，就是没有办法利用多核来增加运算速度，因为只允许有一个线程运行它的bytecode
>Python出现于上世纪九十年代，而多核处理器直到大概2004年才出现，更别说个人电脑上了，所以GIL全是优点

+ 去掉GIL的尝试：
	+ 无法保证在单进程单线程状态下的性能
	+ 无法backward compatibility向后兼容

+ 解决缺点的方案：
	+ multi processing多进程【狗头】
	+ C extension（复杂问题在C方面解决）
	+ 使用没有GIL的Python解释器（Jthon、IronPython）


## 基于Generator协程
>根本没有准备定义，感性理解下吧

+ 在Python的语境下，Coroutine两种语义
	+ 1. coroutine function：以关键字`async def`开头的函数，定义了一个coroutine的”过程“
	+ 2. coroutine object：调用coroutine functino的返回值，类似生成器，调用时不调用函数，而是返回一个coroutine object，不会运行其中代码

+ event loop：感性理解下，类似中枢大脑？
+ `asyncio`：Python标准协程库

+ 怎么运行coroutine function中的代码？
	1. 进入asynchronize模式（正常运行Python代码synchronize模式），让event loop接管程序，通过`asyncio.run(coroutine_object)`
		1. 建立event loop
		2. 将coroutine变成event loop里的task，event loop会自动地找可以执行的task去执行
	2. 把coroutine变成task
		1. 上面讲了一种方法
		2. 使用关键字`await`：`[var] = await coroutine_function`
			1. 将这个coroutine变成task并向event loop注册
			2. 建立依赖，执行await语句的task需要等待await的task执行完后执行
			3. **yield**出去，离开当前task
			+ 当依赖的那个task执行完后，event loop就可以执行调用await语句的task，并把依赖的那个function的返回值作为await语句的返回值

+ 所有控制权的返回都是显示的，event loop不能强行从task拿回控制权，只能等task主动交回
	+ 1. await
	+ 2. 执行完毕

+ `asyncio.sleep(int)`返回返回一个coroutine function

那怎么批量的处理coroutine function呢？  
`asyncio.create_taks(coroutine_function)`：把coroutine变成task并注册到event loop中（相当于await的1），它返回一个task类型的变量，之后通过`await 变量`去执行

`asyncio.gather(若干cotoutine或者task或者future)`返回future类似变量，可以用`await 变量`去建立当前taks对这里所有task的依赖（相当于await的2），并等待所有（相当于await的3）返回时各个task的返回作为一个list返回

### asyncio


## 基于greenlet协程


# 进程
>Python由于GIL的存在无法充分的发挥多核CPU的，想要真的并行，就要通过多进程

https://docs.python.org/zh-cn/3/library/multiprocessing.html