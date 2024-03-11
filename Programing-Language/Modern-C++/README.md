
+ 使用`nullptr`而不是`0`或者`NULL`，因为`0`除了可以表示空指针还表示整数，而`NULL`的具体含义和实现有关。  
	这不仅影响函数重载决议，还影响类型推导。
	+ 如果非得使用`0`或者`NULL`就要注意避免重载指针和整型

+ 断言：
	+ [assert](https://en.cppreference.com/w/cpp/language/aggregate_initialization)：运行期断言
	+ [static_assert](https://en.cppreference.com/w/cpp/language/static_assert)：编译器断言

+ [concepts](https://en.cppreference.com/w/cpp/language/constraints)
+ Pimpl（pointer to implementation）惯用法
	+ 不完整类型
	+ 初学者错误，析构错误，是因为默认析构在使用static_assert查看是否是不完整类型，我们需要让类的函数知道这个类型，所以在.cpp中，不完成类型的完整定义要在其他函数的实现前，即使使用default，也应该放在.cpp 中

## 初始化方式问题

目前C++有三种初始化方法
```cpp
int a = 42;
int a(42);
int a{42};
int a = {42};  // 和花括号方案等效, 不讨论
```
+ 不区分等号，花括号和等号花括号，通常情况下它们等价于花括号
+ C++的uniform initialzation统一初始化即为使用花括号进行初始化

| 场景           | 小括号 | 等号      | 花括号         |
| ------------ | --- | ------- | ----------- |
| 非静态数据成员默认初始化 | 不可以 | C++11可以 | 可以          |
| 不可拷贝对象       | 可以  | 不可以     | 可以          |
| 变窄转换检测       | 不会  | 不会      | 会（不通过则不会编译） |


+ narrowing conversion变窄转换：括号表达式的值不能保证被初始化的对象的类型表示。
+ 规定“可以被解析为一个声明的东西必须被解析为声明”，导致使用无参构造函数的定义被认为是函数生成`Weight w();`，而使用`Weight w{};`则没有这个歧义。
+ 问题：`std::initializer_list`
	+ 如果类有一个构造函数的参数是`initializer_list`，如果使用花括号初始化，编译器会想方设法匹配该构造函数
	+ `std::vector`就有参数为`initializer_list`的构造函数，所以`std::vector<int>(10, 10)`是一个有10个值为10的vector，而`std::vector<int>`则得到的是vector`[10, 10]`

## `std::vector<bool>`的返回代理

```cpp
std::vector<bool> vec = {false, false, false};
auto first = vec[0];
first = true;
assert(vec[0] == false);  // failed
```

## `constexpr`关键字

+ 与`const`的比较：`const`的语义是不可变，`constexpr`的语义是编译期可计算且不可变，即`const`的值可以在运行时计算并初始化，之后不可修改，但`constexpr`的值必须在编译期计算。

# 杂项

## 默认参数是编译期信息而非运行期
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