## 友元函数

不受访问说明符限制，位置不限（说明符数量不限），建议类开始或类结束集中声明

+ 要在友元声明外（类内），专门在进行一次函数声明

C++控制对类对象私有部分的访问，公有类方法提供唯一的访问途径。

C++提供另外一种形式的访问权限：友元。

> 友元与OOP：友元没有违反OOP数据隐藏的原则
>
> 友元是类的接口的扩展，概念上相同，友元的建立是语法的结果。
>
> 同时友元只能在类声明中声明，类依然控制着。
>
> 类方法和友元函数只是表达类接口的两种不同机制。

分类：友元函数；友元类；友元成员函数。

+ 友元函数：

  + 使用范围：为类重载二元运算符，且两个操作数不是同一类型。

    > A = B * 123;  // A = B.operator*(123)
    >
    > A = 123 * B;  //这个呢？
    >
    > 1. 提示使用方式—对服务器友好的-客户警惕的（server-friendliy，client-beware）解决方案？与OOP无关
    > 2. 非成员函数：又要访问内部数据，于是增加新特性——友元
    >
    > > 非成员函数不由对象调用，它使用对象是显式参数

  + 创建友元：

    + 原型：在类声明中，原型声明前加上关键字**`friend`**。
    + 定义：函数头与常规函数相同，不能有`friend`（除非函数定义也是原型），不用有`ClassName::` 。

    表明：虽然该函数是在类声明中声明，但它不是成员函数，不能使用成员调用

    ​			虽然该函数不是成员函数，但它与成员函数的访问权限相同。

  + 重载`+`运算符：

    ```cpp
    class className {
    	
    public:
        friend ClassName operator+(typeName a, const className & b) const;
    }
    ClassName operator+(typeName a, const className & b) const {
        ClassName res;
        res.成员 = a + b.成员;
        return res;
    }
    ```

    此时`typeName + ClassName`会被转换为`operator+(typeName, ClassName)`即可实现计算。

  + 重载`<<`运算符与`cout`结合：

    如果使用成员函数重载：`dvxdName << cout;`有点怪异。所以使用友元。

    ```cpp
    class className {
    	
    public:
        friend void operator<<(ostream & os, const className & c) const;
    }
    void operator<<(ostream & os, const className & c) {
        os << c.成员数据 << "zweix";
    }
    ```

    这样就可以`cout << className;`

    > 这个函数是不是ostream的友元呢？不是，因为os作为整体使用，而没有访问它的私有成员。

    但是不能这样`cout << dvxdName << endl << dvxdName;`

    > ostream原理：对于`cout << x << y;`等效于`(cout << x) << y;`
    >
    > 因为ostream类将operator<<()函数实现为返回一个指向ostream对象的引用。即返回一个指向调用对象的引用，所以（cout << x） 本身就是ostream的对象cout，所以可以继续。

    所以

    ```cpp
    ostream & operator<<(ostream & os, const className & c) {
        cout ...;
        return os;
    }
    ```

    就可以了。

  + 成员函数和友元函数的选择：必须选择并且只能选择其中一个。

    `ClassName operator+(const ClassName & a) const`

    `friend ClassName operator+(const ClassName &a, const ClassName &b) const`
    
    是一致的。
    
    > C++建议使用友元函数，因为其能让程序更适应自动类型转换，因为操作数都是参数，在匹配原型时可以自动转换。
    >
    > 1. 把运算符重载换成友元函数															//程序更简短，易出错，每次使用调用构造函数，费时
    >
    > 2. 将运算符重载重载为一个显式使用转换函数做参数的函数          //正好相反
    >
    >    `ClassName operator+(double x);`
    >
    >    `friend ClassName operator+(double x, ClassName & t);`

### 友元类及方法

友元的设定是由类定义的，虽然被授予访问私有部分的权限，但并不与面向对象编程思想相悖，”相反，它们提高了公有接口的灵活性“。

将类作为友元，友元类的所有方法可以访问原始类的私有成员和保护成员，也可以限制，只将特定的成员函数指定为另一个类的友元。

+ ***友元类***：在类声明内，公有、保护、私有部分都可，声明友元类前使用**`friend`**关键字，类外定义友元类。

友元类可以使用类的成员，如果友元类使用类的数据成员的方法只有一部分，可以不必友元整个类，只***友元成员函数***

不能传递

+ 前向声明（forward declaration）这里的`"友元"类`并不是上述友元类，而是友元函数在的类。

  1. + 友元成员函数在”友元“类中使用类

       ```cpp
       class ClassName {
       	friend type friendName::fName(ClassName &);
       }
       ```

       类在做此定义时，编译器应该已经知道“友元”类的存在，所以“友元”类应该定义在类前，但是“友元”类中的友元成员函数使用类的参数，说明类在友元类前——套娃：提供新语法前向声明

     + ```cpp
       class ClassName;
       class friendName {
       	fName(ClassName &);
       }
       class ClassName {
       	friend type friendName::fName(ClassName &);
       }
       ```

       这样就可以了。

  2. + 但是如果“友元”类中有方法使用了类的方法`type friendName::fName(ClassName & t) { t.fName(); }`此时“友元”类不知道类的内容，只知道其整体的存在。
     + 使“友元”类声明中只包含方法声明，并将实际的定义放在类(ClassName)后。

  3. 对于友元类的内联函数，仍可以使用inline关键字定义。

     > 内联函数的链接性是内部的，所以内联函数需要定义在头文件中，其他函数可以定义在实现文件中。

  > 友元类不需要前向声明是因为将类声明为友元类的过程中已经指出这个类了。

### 其他友元关系

+ 相互友元：两个类的成员可以相互访问

  依然要考虑在声明类时编译器能不能识别类，注意friend友元类时也是指出这个类了

  ```cpp
  class ClassName1 {
  	friend class ClassName2;
      type fName(ClassName2 &);
  }
  class ClasssName2 {
      friend class ClassName1;
      type fNmae(ClassName1 & t) { t.成员; }
  }
  ClassName1::fName(ClassName2 & t) { t.成员; }
  ```

   第一个类可以调用第二个类，但是不能定义（因为还不知道成员），第二个类则可以，第一个类的定义在两个类后。

+ 共同友元：两个类使用共同的友元

  ```cpp
  class ClassName1;
  class ClassName2 {
  	friend fName(ClassName1 &, ClassName2 &);
  }
  class ClassName1 {
  	friend fName(ClassName1 &, ClassName2 &);
  }
  fName(ClassName1 &a, ClassName2 &b) {}
  ```
