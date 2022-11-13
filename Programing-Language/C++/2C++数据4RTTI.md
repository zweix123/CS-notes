# 动态内存

+ C++程序运行时的内存分配：静态内存 + stack栈内存 + heap堆内存/dynamically allocate动态存储

## new和delete

1. new：分配空间：返回指向内存块（的第一个元素）的指针

   + 基本类型：`type * p = new type;`
   + 数组类型：`type * p = new type[num];`

   1. 如果堆内存空间不足：

      + 单个元素：引用异常`std::bad_alloc`
      + 数组元素：引用异常`bad_array_new_length`

      1. 定位new：`new (nothrow) ...`：不让new返回异常，返回空指针

   2. const类型：`new const ...`

2. delete：释放空间：参数指针指向的空间回收但是指针本身还在（空悬指针dangling pointer），对空指针是安全的

   + 基本类型：`delete p;`
   + 数组类型：`delete []p;`：销毁顺序是逆序销毁的

+ 特性：

  + 两运算符**必须**配套使用，不能释放错误，不能不释放，不能重复释放
  + 数组类型指针指向内存块的第一个元素，数组长度不能用sizeof获得数组长，可作为数组名，但数组名不能修改，此仅为指针

+ 初始化：

  内置类型在类型名后面加上初始值，并将其用小括号括起。

  复合类型在类型名后面加上列表值，并将其用大括号括起来。

  > 如果没有括号是默认初始化，而有括号使用值初始化（值为空-0）

+ new替换函数：

  在全局名称空间中，有如下函数原型，使用运算符重载语法。

  ```cpp
  void * operator new(std::size_t);
  void * operator new[](std::size_t);  //分配函数(alloction function)
  void operator delete(void *);
  void opetator delete[](void *);  //释放函数(deallocation function)
  ```

  `std::size_t`是一个`typedef`，在使用new和delete时会进行转换

+ placement定位new运算符（头文件`<new>`）：`type *p = new (起始位置) type`：起始位置是指针（数组/数组中）
  + 不跟踪内存是否被使用，把管理的负担交给程序员
  + 不一定可以使用delete释放，因为使用的内存未必在堆内存


## 智能指针

> C++11的SL提供2种smart pointer智能指针来更容易、安全的管理动态对象

+ 头文件`<memory>`，名称空间`std`

  0. `auto_ptr`：98使用，11弃用

  1. **`shared_ptr`**：允许多个指针指向同一个对象

     **`weak_ptr`**：伴随类，弱引用，指向shared_ptr管理的对象

  2. **`unique_ptr`**：独占所指针的对象

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/智能指针操作.jpg)

+ 哑类：没有定义析构函数——智能指针不能自动析构它——定义**deleter删除器**

  ```c++
  void end_f(f *p) {deletef(*p); } //deletef被定义好
  shared_ptr<f> p(&, end_f);
  ```

+ 规范：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/智能指针规范.jpg)

### shared_ptr

+ reference count引用计数：相关联的计数器，自动管理，为0销毁

+ 使用：`shared_ptr<type> p(new type(val...))`

  + 这样`shared_ptr<type> p = new ...`是不行的，智能指针的构造函数是explicit的，不能隐式转换，必须直接初始化
  + 使用`make_shared<>()`函数是定义智能指针的好方法：`auto p = make_shared<int>(7);`

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/shared_ptr构造.jpg)

  + `get()`方法：

+ reference count引用计数：随着shared_ptr的拷贝和销毁而改变，一旦计数器变成0，则智能智能自动释放所管理的对象

+ 注意：

  + 智能指针做函数形参，new做函数实参，explicit不允许
  + 智能指针做函数形参，同类智能指针传入 -> 复制-拷贝-复制销毁 -> 引用计数变化 —— 传递引用


+ shared_ptr管理动态数组——必须提供自己定义的删除器：

  + `shared_ptr<type> sp(new type[len], [](type *p) { delete[] p; });`
  + 访问：`*(sp.get() + i);`

### unique_ptr

+ unique_ptr：拥有所指对象，没有标准函数库返回，必须采用直接初始化
+ 操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/unique_ptr构造.jpg)
+ 管理数组：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/unique_ptr指向数组的.jpg)

+ 做函数传参和返回：
  + 删除器：`unique_ptr<objjT, delT> p (new objT, fcn)`：类型为delT的对象释放objT对象，调用名为fcn的delT类型对象

### weak_ptr

+ weak_ptr：不控制所指向对象生存期的智能指针，指向shared_ptr管理的对象，**不改变**shared_ptr的引用计数
+ 操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/weak_ptr操作.jpg)

## aloocator类

> 如果想预先定义大量空间，以上方法对没有**默认初始化**的类型是不可以的

+ 位置：头文件`<mempry>`
+ 功能：提供*类型感知*的内存分配的方法，是模板
+ 内容：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/allocator类.jpg)

+ 使用：

  ```c++
  allocator<type> alloc;  //定义对象
  auto const p = alloc.allocate(n); //通过对象分配空间
  alloc.construct(p, ...); //构造对象
  ```

+ 其他算法：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/allocator伴随算法.jpg" style="zoom:80%;" />



## 重载

> 如果某些程序对内存分配有特殊的需求，需要自定义内存分配的细节，C++允许重载`new`和`delete`运算符

+ 工作机理：
  + **`new`**：
    1. new表达式调用名为`operator new`或`operator new []`的标准库函数，该函数分配空间
    2. 编译器运行相应的构造函数以构造对象并传入初始值
    3. 对象被分配空间并构造完成，返回一个指向该对对象的指针
  + **`delete`**：
    1. 对参数所指的对象或数组中的元素执行析构函数
    2. 编译器调用名为`operator delete`或`operator delete []`的标准库函数释放内存空间

+ 可在**全局**或者**类成员**重载运算符，编译器会优先检测类成员、在检测全局自定义，最后使用标准库定义
  + 重载为类成员：隐式静态，无需显示的声明`static`

+ 可重载的接口：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/动态内存接口.jpg)

  + `nothrow_t`是定义在new头文件中的一个无成员的struct，并定义了一个名为**`nothrow`**的const对象，用户可以通过这个对象请求非抛出版本，重载这部分运算符时也**必须**使用`noexcept`异常说明符

+ 关于`<cstdlib>`中的`malloc`和`free`

  ```c++
  void *operator new(size_t size) {
      if (void *mem = malloc(size))
          return mem;
      else 
          throw bad_alloc()
  }
  void operator delete(void *mem) noexcept { free(mem); }
  ```

## 定位new

placement new

+ 语法：place_address必须是一个指针

  ```c++
  new (place_address) type;
  new (place_address) type (initializers);
  new (place_address) type [size];
  new (place_address) type [size] { braced initializer list }
  ```

+ 销毁对象而不释放空间：`dvxd -> ~ClassName();`



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











