类型推导：模板、关键字`auto`和`decltype`。

+ 对于转发引用`T&&`，有不同的叫法，这里叫做转发引用

## 模板中的类型推导

以下面的代码为例
```cpp
template<typename T>
void foo(ParamType param);  // 这里的ParamType是一个和T有关的代码
// ...
// call: foo(expr);
```

+ ParamType是引用或者指针且不是转发引用


+ 如果ParamType是引用或者指针，则实参类型中的cv类型限定会被保留进T中，而实参的引用性会被忽略
+ 引用折叠：如果ParamType是**通用引用**(右值引用)，此时左值的实参会被认为是引用，右值的实参会被认为是右值引用
+ 如果ParamType没有引用，则实参的引用性会被直接忽略
	+ 实参的cv类型限定也会被忽略
		>为什么要这样？因为引用性被忽略了，形参肯定是实参的拷贝，此时即使没有cv限定，实参也是安全的。

		+ 在讨论这样的场景，实参类型是`const char* const`，则形参是`const char*`，所以形参是可以变化的，但是依然不能通过形参修改本来字符串，依然安全。

+ 数组实参，一般情况下，数组可以退化成指针，如果直接把数组名作为参数，则参数类型被推导为`T[]`，在C语言这个就会退化成指针，但是如果形参传入一个数组名的引用呢？它是为了引用传递进去的数组实参，此时数组的长度信息就应该拿到，所以需要模板添加非类型参数，就像下面代码
	```cpp
	template<typename T, std::size_t N>
	constexpr std::size_t arraySize(T (&)[N]) noexcept {  // 形参没有名字，我们只关注数组长度
		return N;
	}
	```

上面是模板类型推导的场景，下面引用关键字`auto`  
实际上绝大部分规则是一致的，但是在下面的场景

```cpp
auto x1 = 42;      // C++98
auto x2(42);       // C++98
auto x3 = { 42 };  // C++11
auto x4{ 42 };     // C++11
```

+ 在这样的场景下，前两者会被推导成`int`，而后两者会被推导成`std::initializer_list<int>`
+ 但是同样的情况在模板中，是可以被正确推导的，如果需要转换成`std::initializer_list`，反而需要在函数参数列表中使用`std::initializer_list<T>`

+ 在C++14中运行`auto`用于函数返回值或者Lambda函数的形参，这是使用的规则就是**模板类型推导**，同样不会自动向`std::initializer_list<T>`推导。

我们在引入`decltype`关键字。

首先介绍下
+ 对于`decltype(expression) var;`这里参数可以是数据类型或表达式
	+ 如果expr是一个没有用括号括起来的标识符，则var的类型与标识符类型相同，包括cv限定，但忽略引用性
	+ 如果expr是一个函数调用，则var的类型与函数返回类型相同
	+ 如果expr是一个左值（你会疑惑，上面不说了标识符了，但是还有什么场景标识符不是左值？这里实际指的是用括号括起来的标识符，这个肯定也是左值），则在上面的基础上，var的类型还会包含expr的引用。
	+ 其他
 
主要的问题发生在这样的情况
```cpp
template<typename Container, typename Index>
auto authAndAccess(Container& c, Index i) ->decltype(c[i]) {
	authenticateUser();
	return c[i];
}
```

我们希望传会一个传进数组的某个位置的引用

+ 在C++11中，`auto`支持单一语句的lambda表达式的返回类型，而在C++14扩展到允许自动推导所有lambda表达式和函数，即使它们内含多条语句  
	所以上面代码可以直接去掉`decltype`部分，直接使用`auto`的类型推导，但是`auto`的类型推导和`decltype`不一样，BUG  
	总之C++14有了这么个东西
	```cpp
	template<typename Container, typename Index>
	decltype(auto)
	authAndAccess(Container& c, Index i) {
		authenticateUser();
		return c[i];
	}
	```
	神奇不，这里`auto`表示这里要类型推导，而`decltype`又表示按照`decltype`的方式进行推导。


+ 关于auto：
	+ 有时很建议用
		```cpp
		std::unordered_map<std::string, int> m;
		for(const std::pair<std::string, int>& p : m) {}
		```
		这对吗？要知道`std::unordered_map`的key是`const`的，这和`p`的类型可不一样，而编译器会“贴心”的进行转换，即copy一下哈希表中的键值对做临时对象，然后p是这个临时对象的引用，这样就出现了语义错误，使用`auto`肯定不会有这样的错误。

	+ 有时不能用
		```cpp
		std::vector<bool> vec;
		...
		auto flag = vec[i];  // 错误，不仅是错误，而是UB！
		bool flag = vec[i];  // 正确
		```

		因为如果使用auto，flag将不再是bool类型，这是因为`std::vector<bool>::operator[]`不会返回容器中元素的引用，而是返回`std::vector<bool>::reference`对象（它能模拟bool的一切行为（涉及诸多技术）），它的本质是和实现有关的，有一种实现是一种**代理类**，你并不知道这里会发生什么（通常代理类的对象的生命周期不会设计活过一条语句）

		所以这里一个通用的原则是，不可见的代理类不适用auto，这里的不可见指除了智能指针之外的所有标准库代理类。  

	但是这就意味着我们放弃`auto`么？解决方案是

	+ 显式类型初始器惯用法（the explicitly typed initialized idiom)
		```cpp
		auto flag = static_cast<bool>(vec[i]);
		```
		卧槽，那么我不直接放弃auto呢？因为不使用auto会隐式类型转换，没有证据证明你是故意的，但是这里这样可以表明你是故意的。

+ 初始化问题：
	+ 一般认为有三种初始化方式：
		1. `int x(0);`
		2. `int y = 1`;
		3. `int z = {2};`

		通常1和3也能使用`=`：`int x = (0);` and `int z = {2};`

		这里认为通常忽略`=`

	+ 场景1：
		```cpp
		ClassName a;      // 使用构造函数
		ClassName b = a;  // 不是赋值运算，而是调用拷贝构造函数
		b = a;            // 是赋值运算，调用拷贝赋值运算符
		```
	+ 场景2：非静态数据成员默认初始化，`{}`和`=`都是可以的，而`()`不行
	+ 场景3：对于不可拷贝对象的定义，`{}`和`()`都是可以的，而`=`不行
	+ 场景4：对于内置类型间隐式的变窄转换（narrowing conversion），`{}`是会检测并在编译报错的，而`()`和`=`不会
	+ 场景5（编译层），你看代码`ClassName c();`你说这究竟是对象默认构造还是函数声明？而`{}`肯定不会

	我们发现`{}`是最具有广泛意义的写法。

	那么它的问题呢？就是和`std::initializer_list`的纠葛，会有很多问题。


## C++17推导指引和

https://en.cppreference.com/w/cpp/language/class_template_argument_deduction