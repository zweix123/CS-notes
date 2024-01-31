+ 多态，狭义的多态即面向对象编程范式下的多态，是一种动态的多态，通过函数重载和继承等等技术实现。还有一种多态是编译器多态、静态的多态，即泛型编程和模板编程，强调了的是对代码的复用，不同类型同构代码。

+ 鸭子类型（Duck typing）是一种动态类型系统的概念，它关注的是对象的行为而不是对象的类型。鸭子类型的基本思想是，当我们在编程中使用一个对象时，我们并不关心它的具体类型，而只关心它是否具有特定的方法或属性。

+ 这里不严格区分模板函数和函数模板、模板类和类模板。

## Template Introduction

+ 建立模板：
	```cpp
	template<class TypeName> ...
	template<typename TypeName>  ...  // C++98
	```

	这里的`TypeName`即*泛型标识符*

+ non-type非类型参数/expression表达式参数，该值类型只能是整型、枚举、引用或者指针
	```cpp
	template<typename WightType WIGHT> ...
	```

	+ 模板内的代码不能修改其值，也不能对其取址
	+ 在实例化模板时，用作非类型参数的值必须是常量表达式

+ 模板类型模板参数：

	|          | 类型参数 | 非类型参数 |
	| -------- | -------- | ---------- |
	| 类模板   | 可以     | 不可以     |
	| 函数模板 | 可以     | 可以       |

+ 使用模板

+ Instantiation实例化：让编译器通过模板代码针对具体类型生成对应代码
	+ implicit instantiation隐式实例化：在使用模板时，编译器自动为其生成对应类型的代码
	+ explicit instantiation显示实例化：在调用代码中手动要求编译器生成对应类型代码

+ Specialization具体化：不使用模板生成函数或类定义，而是专门为特定类型进行定义
	```cpp
	template <> ... funcName(...) { 要具体化的代码; }
	template <> class ClassName<...> { 要具体化的代码; };
	```
	+ 部分具体化：

### Function

```cpp
// 函数模板
template<typename T> void swap(T& a, T& b) { .. }
swap(a, b);       // 隐式实例化
swap<int>(a, b);  // 显示实例化
```

+ trailing return type后置返回类型
	```cpp
	auto 
	decltype
	```

### Class

+ 友元
+ CRTP, Curiously Recurring Template Pattern奇异递归模板模式

# 编译器计算/模板元编程
>C++模板是图灵完备的

## `type_traits`
>[cpp ref](https://en.cppreference.com/w/cpp/header/type_traits)

+ [`std::intergral_constant`](https://en.cppreference.com/w/cpp/types/integral_constant)

## SFINAE
>Substitution Failure Is Not An Error，替换失败非错
