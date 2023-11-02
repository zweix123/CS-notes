## 聚合

+ [aggregate聚合](https://en.cppreference.com/w/cpp/language/aggregate_initialization)
	+ 聚合断言：[判断一个类型是否是断言](https://en.cppreference.com/w/cpp/types/is_aggregate)

	+ 属性：
		+ 所有成员都是`public`的
		+ 没有定义任何构造函数
		+ 没有类内初始化
		+ 没有基类、也没有`virtual`函数

	+ 初始化：提供花括号括起来的成员初始值列表、顺序对应
	+ 字面值常量类：数据成员都是字面值类型的聚合类
		+ 属性：
			+ 数据成员都必须是字面值类型
			+ 至少有一个`constexpr`构造函数
			+ 使用默认析构函数

## 移动强异常安全惯用法

下面展示了一个现代的标准函数组合是什么样子的，不应该是构造和赋值运算符都有，而是有一个通用的赋值运算符，而适当实现构造相关。
+ 具体的：
	+ 分开的拷贝构造和移动构造（或者其中之一）
	+ 使用`std::swap`的`swap`成员
	+ 通用的`operator=`
	+ 以上各个函数都标为`noexcept`

对于赋值运算符相关的`if (this != &that)`，一是写法啰嗦，二是不够异常安全，比如在后面的赋值语句中发生异常的话，this对象的内容可能已经被破坏了。但是我们看下面的代码。

```cpp
template<typename T>
class unique_ptr {
	unique_ptr(unique_ptr&& that) {
		ptr_ = that.release();
	}
	T* release() {
		T* ptr = ptr_;
		ptr_ = nullptr;
		return ptr;
	}
	unique_ptr& operator=(unique_ptr that) {
		that.swap(*this);
		return *this;
	}
	void swap(unique_ptr& that) {
		using std::swap;
		swap(ptr_, that.ptr_);
	}
	...
};
```

一个标准移动构造函数和一个赋值运算符重载

+ 我们看其他标准函数的生成情况
	+ 由于有了一个移动构造函数，所以不会自动生成移动赋值运算符。
	+ 由于有了移动标准函数，所以不会自动生成拷贝标准函数。

	所以这里只有三个标准函数：构造、析构、移动构造，但是它依然可以移动赋值，因为对于赋值语句`p2 = std::move(p1);`相当于先调用移动构造生成赋值运算符重载的实参，然后再调用拷贝构造函数。

+ 这样设计的好处是什么？整个拷贝的过程分成两个部分：移动构造和赋值，而移动构造的过程就有成员的拷贝，如果出现错误则在移动构造这里就错误，此时赋值运算符重载调用中的`this`完好无损。

+ 实际上这份代码还是可扩展的，比如定义拷贝构造函数，此时赋值运算符依然生效，它完全依赖于构造参数时走的是移动构造还是拷贝构造。并且语义也是没问题的，虽然在赋值运算符中是移动的，但是进来的函数都是经过拷贝/移动的，没有浪费，没有语义问题。

## 0/3/5规则
