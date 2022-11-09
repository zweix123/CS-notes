# 运行时类型识别

运行时类型识别（run-time type identification, RTTI）

+ 应用场景：
  1. 在类继承的多态中，动态类型通过虚函数体现，但在不能定义虚函数的情况下，使用RTTI实现多态

1. **`dynamic_cast`**运算符：`dynamic_cast<type*/type&/type&&>(e)`
   + type必须是一个类类型且通常应含有虚函数
   + 1中e必须是有效指针，2中e必须是左值，3中e不能是左值
   + 成功条件：e的类型是目标type的公有基类、type类型、公有派生类
   + 失败：对指针返回0，对引用抛出bad_cast异常

+ 实例：Base类至少含有一个虚函数，Derived是Base的公有派生类

  + 指针类型：

    ```c++
    if (Derived *dp = dynamic_cast<Derived*>(bp)) {
        //使用dp指向的Derived对象
    } else {
        //使用bp指向的Base对象
    }
    ```

  + 引用类型：没有所谓的空引用，转换失败会抛出一个在`<typeinfo>`中名为`std::bad_cast`的异常

    ```c++
    try {
        const Derived &d = dynamic_cast<const Derived&>(b);
    	//使用b引用的Derived对象
    } catch(bad_cast) {
        //处理类型转换失败的情况
    }
    ```

2. **`typeid`**运算符

+ 指针类型的dynamic_cast：

+ RTTI是运行截断类型识别(Runtime Type Identificaton)的简称，旨在程序在运行阶段确定对象的类型提供一种标准方式。

  + 用途：基类指针可以指向派生类对象地址，如何确定基类指针指向对象的类型——RTTI只用于包含虚函数的类层次结构。

  + 原理：C++有三个支持RTTI的元素

    1. 如果可能的话，`dynamic_cast`运算符将使用一个指向基类的指针来生成一个指向派生类的指针；否则，该运算符返回0——空指针。

       ```cpp
       ClassName * p = dynamic_cast<ClassName *>(dvxdName);
       如果可以安全转换，运算符返回对象的地址，否则返回空指针。
       ```

       也可以用于引用，但是没有”空引用“，出现错误则请求不正确会引发bad_cast异常

    2. `typeid`运算符返回一个指出对象的类型的值——可以确定两个对象是否为同一类型

       `typeid(参数);` 参数接受两种：类名和结果为对象的表达式

       返回一个对`type_info`（头文件`<typeinfo>`旧为`<typeinfo.h>`定义的一个类）对象的引用，

       它重载了`==`和`!=`运算符可以实现两个返回值的比较

       它定义了`name()`的成员来返回一个随实现而异的字符串

    3. `type_info`（头文件`typeinfo`（以前为`typeinfo.h`）中的一个类）结构存储了有关特定类型的信息

       typeid运算符返回一个对type_info对象的引用
