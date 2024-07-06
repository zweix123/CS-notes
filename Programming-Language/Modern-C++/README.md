
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




# 资源管理

+ 堆：是内存管理器向操作系统申请的，所以内部也需要管理，但是C++编码的过程中并没有体感，但是其实仍然有内存碎片的可能，不过面对内存泄漏问题已经焦头烂额了。
+ POD类型：简单类型  
	对于有构造函数和析构函数的非POD类型，在栈上的内存分配同样有效，只有具体代码由编译器选择
	+ 栈展开，当异常发生时，会调用栈中的非POD类型的析构函数
+ 值语义：C/C++中所有的变量缺省值都是值语义的，即可以通过`.`或者`->`访问（而其他的变量都是指向堆的，即使只能通过`.`访问）

## RAII

对象有时不能放在栈上，比如对象很大，或者对象的大小不能在编译阶段确定，或者说对象是函数返回值，但是不能值返回（这样的场景这个对象应该存在哪里？函数返回对应的栈就释放了）

功能上不仅能用来释放内存，还能关闭文件、释放锁、或者其他重要的系统资源等等。

+ new和delete
	+ new的过程：申请空间，构建，这个过程出现异常则释放空间
	+ delete是可以delete空指针的，里面会检测。

+ 动态内存Ref：[Dynamic memory management](https://en.cppreference.com/w/cpp/memory)
	+ raw ptr: new&delete
		+ [new](https://en.cppreference.com/w/cpp/keyword/new)和[delete](https://en.cppreference.com/w/cpp/keyword/delete)：正如ref所说，这两个关键字既是expression又是function

	+ smart pointers：
		+ [unique_ptr](https://en.cppreference.com/w/cpp/memory/unique_ptr)
		+ [shared_ptr](https://en.cppreference.com/w/cpp/memory/shared_ptr)
		+ [weak_ptr](https://en.cppreference.com/w/cpp/memory/weak_ptr) 

+ 智能指针的简单实现：
	+ `auto_ptr`（C++17废除），因为拷贝语义实际运行的是移动
	+ `unique_ptr`：只能进行移动，禁用拷贝
	+ `shared_ptr`：

+ shared_ptr的Control Block：
	>热知识，shared_ptr的大小是裸指针的两倍。

	+ shared_ptr的大小是裸指针的两倍，其中一个相当于裸指针，另外一个指针指向Control Block
	+ Control Block即起到引用计数的功能，关于计数的变换使用**原子变量**（所以这部分是多线程安全的，但是shared_ptr整体不是线程安全的）
	+ 还有关于weak_ptr的相关信息，即这块内存表示的裸指针有多少weak_ptr也在维护，如果有weak_ptr，即使shared_ptr都销毁了也应该保留。
	+ 性能相关，这里首先堆内存的使用有一定损耗，另外控制块内部有虚函数的调用（不过通常只有析构这一次），也有对应的损耗。

+ unique_ptr与所有权语义exclusive ownership

+ `unique_ptr`的自定义删除器：
	>热知识，unique_ptr的大小在不定义自定义删除器时时空消耗是和裸指针一样的

	但是unique_ptr并没有Control Block，所以它的删除器相关代码需要放置在实例内部，如果其状态过多，可能需要申请堆内存，届时会有性能损耗

+ Effective Modern C++ Item21，使用make系标准函数而不是使用裸指针去构造只能指针。
	+ 一般情况下标准函数决定可以满足需求了，除了自定义删除器和关于初始化括号的歧义场景
	+ 结合shared_ptr的控制块，如果不小心多次使用裸指针去构造多个shared_ptr，这些控制块可不是同一个。
		+ 那如果我直接将`new`语句作为shared_ptr的构造参数呢？   
			在函数调用时可能出错，因为函数调用要先构造实参，而这个过程是不保序的，而上面的构造过程分成了两个部分，`new`和构造，这两步未必是连续的，如果中间的步骤异常了，则最开始new的空间就泄露了。
	+ 需要`push_back(this)`场景，如果你想这么做，比如将你的类从`std::enable_shared_from_this`去继承，该类有成员函数`shared_from_this()`来代替`this`
	+ 还是结合控制块，make可以直接申请类型大小和控制块大小的堆空间，然后再分别构造，而使用裸指针，就说明这里肯定是分两步了。

+ weak_ptr使用场景：
	+ 工厂设计模式中，如果是根据ID构建，且这个构建昂贵且频繁，就可以把对应的实例缓存起来，但是工厂方法通常使用unique_ptr做返回值，这可没法缓存。
	+ 观察者设计模式，subject需要持有observer的指针，但是它并不关心observer的生成周期。
	+ 循环引用


## inline
[ref](https://en.cppreference.com/w/cpp/language/inline)

+ 内联函数
+ 内联变量（C++17）
	+ `const`缺省不内联, `constexpr`缺省内联

## const
[ref: cv qualifier](https://en.cppreference.com/w/cpp/language/cv)

+ const类并不是并发安全的，因为内部可能有成员使用`mutable`
+ 螺旋修饰规则：
	+ [first](https://c-faq.com/decl/spiral.anderson.html)
	+ [叔叔](https://zclll.com/index.php/cpp/182.html)


## 名称空间
>1. 实体：变量、函数、结构、枚举、类以及类和结构的成员。
>2. 名称：实体的标识符。

+ 传统的C++名称空间：
	1. 声明区域(declaration region)：可以进行声明的区域
	2. 潜在作用域(potential scope)：从声明点开始，到其声明区域结尾。  
		作用域(scope)：数据对的对程序的可见区域。

		这里潜在作用域较于普通的作用域是区别是什么？比如同名变量的隐藏

	C++关于局部变量和全局变量的规则定义了一种名称空间层次、不同声明区域声明名称相互独立。

+ 现代的C++名称空间：定义并命名一个声明空间——名称空间：提供声明名声的区域，不同区域的同名名称不冲突，运行其他部分使用该名称空间的对象。

+ 名称空间的分类：
	+ 全局名称空间：文件级声明区域，所有名称默认的作用域
	+ 自定义名称空间：
		+ 类作用域。

+ 定义：
	```cpp
	namespace 名称空间名 {
		该名称空间内的实体
	};
	```

	+ 名称空间内的声明和定义规则同全局的相同
	+ 名称空间可定义嵌套，但不能定义于代码块（默认名称空间为链接性外部，块内名称不能是外链接性）
	+ 名称空间是open的

+ 访问：
	1. 作用域解析运算符`::`，格式：`名称空间名::实体标识符`，作为总体使用
		>未限定的名称(unquealified name)：未被装饰的名称  
		>限定的名称(qualified name)：包含名称空间的名称

	2. `using`声明：格式：`using 名称空间名::实体名;` ：将实体名暴露在当前的名称空间中，即可使用未被限定的名称使用
		+ 冲突和覆盖：编译报错，无法导入

	3. `using`编译指令：格式：`using namespace 名称空间名;`：将名称空间内的所有实体名暴露在当前名称空间中
		+ 冲突和覆盖：单独使用::强调

+ 其他特性：
	+ 定义可嵌套，对应的访问是嵌套使用作用域解析运算符，在内嵌的名称空间也可以使用using，而其作用可在内外层传递
	+ 为名称空间创建别名：`namespaces 新名 = 旧名;`
	+ 匿名名称空间
	+ C++标准库放在名称空间std中
