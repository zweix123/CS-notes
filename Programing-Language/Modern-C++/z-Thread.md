## Header

+ 交替打印
+ 读写锁实现
	+ 阻塞
	+ 非阻塞
+ 并行STL

+ C++标准库并发组件：tasks、futures、threads、mutexes、condition variable
+ 在C++语境下，thread有三种含义：
	>whatever, 总是我们相信现代操作系统中的最小调度单位是线程，或者说这是一个可以被操作系统调度器管理的最小独立指令序列  

	+ 硬件线程，可以大概理解为一个CPU一个。
	+ 软件线程/系统线程：操作系统概念下的线程
	+ 软件线程句柄`std::thread`，也就是说C++代码中的每个`std::thread`实例都可能对应一个操作系统概念下的线程。

+ 面临的问题：
	+ 软件线程是有限的资源，即使代码没问题，但是超过了这个限额，也异常（`std::system_error`）
	+ 除了个数限额，还有资源超额（oversubscription）
		+ 比如线程调度会有上下文切换，这就增加系统的软件线程管理开销
		+ 如果调度前后安排到不同的硬件线程上，会出现缓存相关问题，这个CPU没有缓存，也会影响之后调度的软件线程的缓存

## `std::future`

如果开发者想异步的执行一个函数，通常有两种方式
+ 基于线程：创建`std::thread`去执行
+ 基于任务：传递给`std::async`去执行
	+ 在这个方式中，传递给`std::async`的函数对象称为task任务

Effective Modern C++ Item 35：优先考虑基于任务的编程而非基于线程的编程

+ 优势：
	1. 代码短
	2. fuctue提供get函数，其提供抛出异常的访问，而thread则会直接终止程序`std::terminate`
	3. 线程的调度有很多问题，而`std::async`将线程管理的责任交给标准库的开发者。
		+ 比如如果软件线程超过限额了，那么这个调用可能不会立刻创建新的软件线程。

+ `std::async`启动策略，即`std::launch`，是一个枚举类
	+ `std::launch::async`：必须异步执行，即不同的线程
	+ `std::launch::deferred`：在future上调用`get`或`wait`时才执行，即future被推迟到此刻才执行，此时相当于同步调用
	>`std::async`默认都行，好处是它可以和标准库的线程管理组件承担线程创建和销毁的责任，避免资源超额，以及平衡负载。坏处是无法预测，这里可不是，具体看例子

	```cpp
	using namespace std::literals;  // 用于下面的1s and 100ms
	void f() { std::this_thread::sleep_for(1s); }
	int main() {
		auto fut = std::async(f);
		while (fut.wait_for(100ms) != std::future_status::ready) {}
	}
	```

	这个可能在低负载（单元测试）正常，但是在负载过高时才显现出来。

	解决方式是先Check一下
	```cpp
	if (fut.wait_for(0s) == std::future_status::deferred) {}  // 说明是std::launch::deferred
	```

	> 难道默认的启动策略不是两种情况都可以发生嘛？这个意思怎么变得只可能有一个，maybe两个launch常量里面还有说法吧。

+ 有一系列的场景判断要不要使用默认启动策略，所以一般都显式指定一定要异步
	```cpp
	// C++14
	template<typename F, typename... Ts>
	inline
	auto
	reallyAsync(F&& f, Ts&&... params) {
	    return std::async(std::launch::async,
					      std::forward<F>(f),
					      std::forward<Ts>(params)...);
	}
	```

+  future的缺点是不能设置优先级，这是只能用基于线程的。

## `std::thread`

+ A `std::thread` instance has two state, joinable and unjoinable.
	+ joinable: 正在运行或者可能要运行的异步执行线程，比如一个阻塞或者等待调度的，另外，一个结束的线程也是joinable的
	+ unjoinable: 
		+ 默认构造的std::thread, 没有函数执行，没有对应到底层的软件线程
		+ 已经被移动走的
		+ 已经被join的
		+ 已经被detach的

+ 禁止销毁joinable的std::thread，即如果std::thread是joinable，则程序直接终止，为什么要这么恐怖？  
	+ 比如函数栈中有一个std::thread
		+ join: 创建后的代码因为发生什么直接终止函数并返回，此时如果如果join在语义上不对，已经出现问题还算什么算？
		+ detach: 这个结合具体的语境，可能std::thread中是局部变量的引用，而detach是取消std::thread和软件线程的关系，并不意味着软件线程结束了，所以就造成栈空间没了，线程还在运行。

+ 你说你非得处理一下呢？因为终止太可怕了，detach的UB也太可怕了，我们就选择一个语义不太对的吧。那么我们就需要保证整个调用链上都被RAII管理，而std::thread没有官方RAII容器。我们需要自己定义。
	```cpp
	class ThreadRAII {
	public:
	    enum class DtorAction { join, detach };
	    
	    ThreadRAII(std::thread&& t, DtorAction a) : action(a), t(std::move(t)) {}  // std::thread只能移动
	
	    ~ThreadRAII() {
	        if (t.joinable()) {
	            if (action == DtorAction::join) {
	                t.join();
	            } else {
	                t.detach();
	            }
	        }
	    }
	
	    std::thread& get() { return t; }

		// 这两句也是必须的，因为上面声明了析构函数，理论上移动相关函数被默认删除了
		ThreadRAII(ThreadRAII&&) = default;
		ThreadRAII& operator=(ThreadRAII&&) = default;
	private:
	    DtorAction action;
	    std::thread t;
	};

	```

## `volatile`

+ Reference：
	+ [始终的《谈谈 C/C++ 中的 volatile》](https://liam.page/2018/01/18/volatile-in-C-and-Cpp/)

## 锁

### 互斥锁
[`<mutex>`](https://zh.cppreference.com/w/cpp/thread/mutex)，请查看示例

+ `std::mutex`的定义：
	+ 在类中：
		```c++
		mutable std::mutex m;
		```
		其中`mutable`即为可变的，因为如果类对象是const的，但是锁肯定需要被修改的，这是特殊说明

+ 如何使用：
	```c++
	type function_name(...) {
		std::unique_lock<std::mutex> lck(m);
		...
		lck.unlock();  // 显示解锁
		lck.lock();    // 显示上锁
	}
	```
	对象`lck`在构建时自动上锁，之后可通过方法`lock`或`unlock`显式上下锁。

	+ 在Golang中有这样的写法：
		```go
		var lck sync.Mutex
		func foo() {
			lck.Lock()
			defer lck.Unlock()
		    // ...
		}
		```
		因为在函数中随时可能退出或者抛出异常，正常写法需要在每个地方都进行显式的开锁。  
		`defer`语句即为退出当前代码块（无论是退出还是抛出）时解锁。  
		C++也有类似的
		```c++
		type function_name(...) {
			std::lock_guard<std::mutex> lck(m);
			...
		}
		```
		这样即可实现同样的功能

	lock_guard语法更简单，unique_lock有更自由的功能，相应的有更高的时空消耗。

#### 锁的唤醒
如果我们想因为某种条件上锁，并在某些条件下解锁怎们办呢？  

[`<condition_variable>`](https://zh.cppreference.com/w/cpp/thread/condition_variable)，请查看示例

### 读写锁
对于同一个临界资源，有多个线程要访问，对于只读访问，它似乎不需要加入阻塞，让他们自由的访问临界资源似乎没什么不妥。

[`<shared_mutex>`](https://zh.cppreference.com/w/cpp/thread/shared_mutex)，请查看示例

### 独占性的唤醒
shared_mutex的unique_lock和mutex的lock一样，而condition_variable的第一个参数必须是std::mutex，有无类似的？

[`<condition_variable_any>`](https://zh.cppreference.com/w/cpp/thread/condition_variable_any)，请查看示例

# 协程

+ Reference：
	+ [Asymmetric Transfer](https://lewissbaker.github.io/)

# 内存模型

