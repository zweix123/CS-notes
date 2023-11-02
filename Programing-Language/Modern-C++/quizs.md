## 1

```cpp
#include <iostream>

class Base {
    public:
        int a = 1;
        virtual void print(int n = 2) {
            std::cout << "Base: " << a + n << '\n';
        }
};

class Derive: public Base {
    public:
        int b = 3;
        virtual void print(int n = 10) {
            std::cout << "Derive: " << b + n << '\n';
        }
};

int main() {
    Base* p = new Derive[10];
    p[7].print();
    // Derive: 5

    Derive* p2 = new Derive;
    p2 -> print();
    // Derive: 13

    return 0;
}
```
这是为什么呢？
因为默认参数是Compile time的信息，所以具体取什么值看static type。

## Effective Modern C++ tag dispatch技术
模板元编程的标准构建模块

对于下面的场景

```cpp
std::multiset<std::string> names;       //全局数据结构

template<typename T>                    //志记信息，将name添加到数据结构
void logAndAdd(T&& name)
{
	auto now = std::chrono::system_clokc::now();
	log(now, "logAndAdd");
	names.emplace(std::forward<T>(name));
}
std::string nameFromIdx(int idx);   //返回idx对应的名字

void logAndAdd(int idx)             //新的重载
{
	auto now = std::chrono::system_clock::now();
	log(now, "logAndAdd");
	names.emplace(nameFromIdx(idx));
}
```

这是有大问题的，如果我传入一个`long long`，我期望调用的是from id呀，但是这个更匹配通用引用。

来看一下魔法

```cpp
template<typename T>
void logAndAdd(T&& name)
{
	logAndAddImpl(
		std::forward<T>(name),
		std::is_integral<typename std::remove_reference<T>::type>()
	);
}
```
这里甚至不能用`std::is_integral<T>()`，因为可能传入`int&`，这个不会被判定为interger

```cpp
template<typename T>                            //非整型实参：添加到全局数据结构中
void logAndAddImpl(T&& name, std::false_type)	//译者注：高亮std::false_type
{
	auto now = std::chrono::system_clock::now();
	log(now, "logAndAdd");
	names.emplace(std::forward<T>(name));
}
std::string nameFromIdx(int idx);           //与条款26一样，整型实参：查找名字并用它调用logAndAdd
void logAndAddImpl(int idx, std::true_type) //译者注：高亮std::true_type
{
  logAndAdd(nameFromIdx(idx)); 
}
```

但是这个只能有两个分支

`std::enable_if`可以给你提供一种强制编译器执行行为的方法。

## Effective Modern C++ Item38 不同线程句柄的析构行为

我们看到
+ `std::thread`的析构如果检测到线程的joinable会直接终止程序，讨论进行`join`或者`detach`都有对应问题
+ 未延迟（non-deferred）`std::future`和`std::thread`，但是它在析构方面似乎没啥问题。

实际上，future可以看做是通信信号的一端，被调用者将计算结果写入通信信号（通常是`std::promise`对象）  
那么这个promise存储在哪里呢？肯定不能在被调用者，因为它已经结束了，也不能放在future中，因为future可能变成shared_future。所以这个东西不会存储类调用者和被调用者的任何一个地方，放在一个额外的地方。即

共享状态（shared state）
+ 基于堆的对象
+ 标准并未支出其类型、接口和实现