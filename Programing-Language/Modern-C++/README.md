## MISC

+ 使用`nullptr`而不是`0`或者`NULL`，因为`0`除了可以表示空指针还表示整数，而`NULL`的具体含义和实现有关。  
	这不仅影响函数重载决议，还影响类型推导。
	+ 如果非得使用`0`或者`NULL`就要注意避免重载指针和整型

+ 断言：
	+ [assert](https://en.cppreference.com/w/cpp/language/aggregate_initialization)：运行期断言
	+ [static_assert](https://en.cppreference.com/w/cpp/language/static_assert)：编译器断言

+ [concepts](https://en.cppreference.com/w/cpp/language/constraints)

+ `constexpr`关键字：除了`const`常量的语义外，还有编译器可知的意思，所以一个最起码的差别就出现了，const是可以这样的
	```cpp
	int sz;
	...
	const auto sz_ = sz;  // 没有问题，这里仅仅表示sz_不在可变，而不能不需要它在编译器都知道，但是constexpr可不行。
	```

	+ 当`constexpr`修饰函数时，其实是相当自由的，如果某个函数调用可以在编译器确定，则在编译器计算， 否则依然可以调用。 

	再深入的说，constexpr是为了获得字面量，在C++14中，可不仅是内置类型才能是字面量，自定义类型（在构造函数前添加关键字）也可以做字面量。

	+ 如果将类的Set方法可以设置为constexpr么？一方面不行，因为constexpr也意味着const，而且Set方法的返回值是 `void`，void可不是一个字面量，但是这两个限制在C++14中被放开
		>意思是constexpr不意味着const？

### Pimpl惯用法

+ Pimpl（pointer to implementation）惯用法
	+ 不完整类型
	+ 初学者错误，析构错误，是因为默认析构在使用static_assert查看是否是不完整类型，我们需要让类的函数知道这个类型，所以在.cpp中，不完成类型的完整定义要在其他函数的实现前，即使使用default，也应该放在.cpp 中
