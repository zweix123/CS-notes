# 概述绪论

泛型编程：泛型即独立于类型的，将具体的类型作为参数传递。

> typedef的缺陷：每次需要修改头文件，且只能生成一种

> ***代码的可重用性***：继承和泛型：让程序圆能够重用经过测试的代码，而不用手工赋值它们。简化编程工作，提高代码可靠性。

***模板***：提供参数化（parameterized）类型，即能让类型名作为参数传递给接收方来建立类或函数

+ 建立模板：**`template`**` <`**`class`**`/`**`typename`**` AnyType>;`或**`template`**`` <class或typename 泛型标识符>;``

  + 关键字**`template`**，告知编译器定义模板。

  + 尖括号（`<>`）中为*类型参数*（type parameter），类似函数参数，但是接受的是类型。可使用多个类型参数

  + 关键字**`class`**或**`typename`**选择其一，看作变量的类型名，该变量接受类型作为其值。

    C++98之前使用class、之后使用typename。

    > C++依然承认class，因为大量代码仍然使用class建立模板。

  + *泛型标识符*AnyType看作该类型变量的名称，命名规则和常规变量一致，多用`T`或`Type`。当模板被调用时，其被具体的类型值取代

    > zweix认为在设计逻辑上，class或typename起一个占位符的作用，来类似函数，实际上使用的使用泛型标识符。

+ 其他特性

  + 非类型（non-type）或表达式（expression）参数：指定特殊的类型而不是泛型作为类型参数，只能是整型、枚举、引用或指针

    `template <typename T, int n>;` n接受一个int型的参数，在模板中，n是接受的int型值的别称。

    模板代码不能修改表达式参数的值，也不能使用它的地址；实例化模板时，用作表达式参数的值必须是常量表达式

    + 性能：

      参数作数组长度时较于动态内存更快

      但每一个表达式参数都生成一个实例而不是一个类型一个定义

  + 默认类型模板参数：为类型参数提供默认值（类模板可以，函数模板不可以）

    对于非类型参数提供默认值，类模板和函数模板都可以

+ 使用模板：

  + 声明：“在其控制的区域”可以把泛型标识符当作内置类型使用。
  + 使用：通过实例化以确定类型按照模板方案定义具体。

+ 局限性：泛型的数据类型可能有不合适的运算符。

  + 泛型的数据类型可能有不合适的运算符。

  + > 模板中存储不同模板类型的变量应该是什么类型

    C++11提供关键字`decltype`：`decltype(expression) var;` 参数可以是数据对象或者表达式。

    作为声明语句关键字可以赋值语句结合。

    > 为确定类型，编译器必须遍历一个核对表。
    >
    > 1. 如果expression是一个没有用括号括起的标识符，则var的类型与该标识符的类型相同，包括const等限定符。
    >
    > 2. 如果expression是一个函数调用，则var的类型与函数返回类型相同。
    >
    >    > 并不实际调用函数，只是编译器查看函数原型来获悉返回类型。
    >
    > 3. 如果expression是一个左值，则var为指向为指向其类型的引用。因为这是第三步，已经排除了没有用括号括起的标识符。
    >
    > 4. 如果前面的条件都不满足，则var的类型与expression的类型相同。

+ *实例化*（instantiation）或*具体化*（specialization）：模板以泛型的方式描述，而具体化是使用具体的类型生成——为模板做进一步定义

  > 模板不声明定义，它是用于生成定义的方案。

  > 实例：

  + 实例化instantiation）：按照模板”方案“生成的具体定义。

    + 隐式实例化（implicit instantiaton）：在使用使用了模板的声明时，编译器自动为对应的类型生成定义。

    + 显式实例化（explicit instantiation）：直接命令编译器器生成定义。

      语法：声明实例前：声明前的关键字**`template`**和声明所需的类型用`<>`符号指示类型

      **`template`**` typeName fName<typeName>() {}` **`template`**` class ClassName<typeName> dvxdName;`

  + 具体化：不使用模板生成定义，而为一定类型专门进行定义。

    + 显式具体化（explicit specialization）：使用关键字前缀**`template`**` <> `
    + 部分具体化：
  
+ 模板别名（C++11）

  1. typedef机制：

     `typedef std::array<int, 2e5 + 7> arrN;`

     `arrN sam;`

  2. 使用模板提供一系列别名

     ```cpp
     template<typename T>
     	using 模板别名 = mobjName<T, 123>;
     模板别名<int> sam;  //sam是 mobjName<int, 123>的实例对象。
     ```

     + C++11允许该语法将using=用于非模板使之与常规typedef等价。

  3. 可变参数模板（variadic template）

# 函数模板

+ 语法：

  + 声明：建立模板+函数声明
  + 定义：建立模板+函数定义
  + 调用：函数名+模板类型+函数参数

  ```cpp
  template<typename T> void swap(T &a, T &b) {
  	T t = a; a = b; b = t;
  }
  {
  	int a = 1, b = 2;
      swap(a, b);  //隐式实例化  编译器根据参数自动生成实例
      swap<int>(a, b);  //显式实例化
  }
  ```

+ 模板定义以关键字`template`开始，后跟一个template parameter list模板参数列表（不能为空），由逗号分隔的一个或多个template parameter模板参数，用小于号和大于号包围起来

  + type parameter模板参数，使用关键字`class`(旧)、`typename`(新)

  + notype parameter非类型参数，使用对应类型为关键字

+ 显性具体化（explicit specialization）：为模板作进一步定义。

  1. C++标准定义（第三代具体化（ISO/ANSI C++标准） （C++））：
     1. 对于给定的函数名，可以有非模板函数、模板函数和显式具体化模板函数以及它们的重载版本。
     2. 显式具体化的原型和定义应以`template<>`打头，并通过名称来指定类型。
     3. 具体化优先于常规模板，而非模板函数优先于具体化和常规模板。

  + *实例化*（instantiation）或*具体化*（specialization）：按照模板”方案“生成的具体函数。

    1. *隐式实例化*（implicit instantiation）：直接使用对应函数，编译器根据参数确定类型参数的类型

    2. 显式实例化（explicit instantiation）：直接命令编译器创建特定的实例

       1. 声明：关键字**`template`**和声明所需的类型用`<>`符号指示类型（在函数名和后接括号之间）。

          ​			`template typeName fName<typeName>() {}`

       2. 调用：在使用函数时实例化：

             	     `fName<typeName>();`

  + 显式具体化：不使用模板来生成函数定义，而应专门给一定类型显式的定义函数定义；必须要有函数原型

    语法：`tempate <> tepeName fName<typeName>() {}`或`tempate <> tepeName fName() {}`

  + 模板函数的显式实例化：`function<type...>(arg...)`，这里类型参数列表和模板参数的声明不一定一一对应，C++会从左开始匹配，剩下的仍然是隐式实例化，如果参数列表不能将剩余的类型参数隐式实例化则会报错。

  + 区别：实例化：用模板生成具体类型的函数定义

    ​			具体化：不使用模板，专门为类型定义函数定义，必须要有自己的定义。==//?zweix为什么不直接使用常规函数呢？==

    ​			**两者冲突**。

+ 在模板函数中，函数返回不同模板类型的变量。

  此时不能使用decltype，因为它们不在作用域。

  C++新增声明和定义函数的语法：`auto fName() -> typeName;` 将返回类型移到参数声明后面，`-> typeName`被称为后置返回类型（trailing return type），其中auto是占位符，表示后置返回类型提供的类型。

  注意到这时参数列表就被定义了。所以后置类型可以使用decltype了。

+ 用一个函数模板初始化一个函数指针或为一个函数指针赋值时，编译器使用指针的类型来推断模板实参

# 类模板

+ 定义类模板：模板定义后接类声明，写法多分行

  ```cpp
  template <typename T>
  class ClassName{
  	...
  };
  ```

  定义类模板方法：模板定义后接方法定义，写法多分行。每个定义都需要

  ```cpp
  template <typename T>
  type ClassName<T>::fName1() {
      ...
  }
  template <typename T>
  type ClassName<T>::fName1() {
      ...
  }
  ```

  类声明定义了方法（内联定义），可省略模板前缀和类限定符。

  > 定义的模板文件不能运行，模板没有实例化，测试需要和实例化结合。

+ 使用：`ClassName<typeName> dvxdName;`

+ 其他特性

  + 用于常规类的技术可用于模板类：作为基类、作为组件类、作为其他模板的类型参数

    ```cpp
    template <typename T>
    class ClassName1 : public baseName<T> {};
    
    
    template <typename T>
    class ClassName2 {
    	baseName<T> dvxdName;
    }
    
    ClassName3 < baseName<typeName> > dvxdName;
    //C++98要求使用至少一个空字符将两个>符号分开，以免和>>运算符混淆，C++11不要求。
    ```

  + 模板参数作用域：

    + 类模板类型参数会覆盖外作用域的类型名
    + 类模板类型参数作用域内不能有重名类型参数

  + 类模板的类型成员：

    > `string::size_type`我们知道是一个类型
    >
    > `T:size_type`不能确定是一个类型，因为可能是类`T`的`static`成员

    C++假定通过作用域运算符访问的名字不是类型

    如果想使用需要`typename T::...`来显式说明

+ 具体化（specialization）：模板以泛型的方式描述类，而具体化是使用具体的类型生成类声明。

  > 类成员只有在使用时才实例化

  + 隐式实例化：`ClassName<typeName> dvxdName;`声明对象，指出类型，编译器使用模板生成具体的类定义，在编译器需要对象前，不会生成类的隐式实例化

  + 显式实例化：`template class ClassName<typeName>;`即使没创建或提及类对象，编译器也生成类声明和定义

  + 显式具体化：`template <> class ClassName<specialized-type-name> {}`;专门为一个类型设置独特的算法；早期版本没有前缀`template<>`

  + 部分具体化：

    + `template <class T1, classT2> class ClassName {};`使用`template <class T1> class ClassName<T1, int> {};`来部分具体化，也可以是其他部分。注意如果全部具象化，类名前的部分尖括号就空了成现实具体化了。
    + `template <class T*> `部分具体化指针，此时如果使用指针，T是typeName，否则T是typeName*。
    + `template<class t1, classt2> class ClassName <t1, t2, t2>;`通过部分具体化使用同一个参数。

+ 

+ 其他特性

  + 成员模板：模板可用于结构、类或模板类的成员

+ 成员模板：类内定义模板类，类内使用用户的类型参数使用类内的模板类

  成员模板可以在类内定义也可以在类外定义，注意模板的嵌套

  ```cpp
  template <typename T> 
  class ClassName {
  private:
      template <typename v> 
      class ClassName_;
  public:
      template <typename U>
      U fName();
  }
  template <typename T>
  	template <typename v>
  		class ClassName<T>::ClassName_ {
              
          }
  template <typename T>
  	template <typename U>
  		U fName() {
      
  }
  ```

+ 把模板用作模板参数`template <template <typename T> class ClassName> class ClassName_;`其中`template <typename T> class`是类型，`ClassName`是参数。

  实例化时`ClassName_<mobjName> dvxdName` 

  在类定义中可使用ClassName作为已知的模板进行实例的应用，编译器会将其翻译为实例中的mobjName

+ 类模板别名：

  > 旧版本可以为类型定义typedef：`typedef ClassName<T> TClassName`，但是这种使用方法类似文本替换，而模板不是类型，不能为该类模板定义指针和引用

  ```c++
  template<typename T> using twin = paair<T, T>
  twin<string> authors;  // authors是一个pair<string. string>
  
  template<typename T> using partNo = pair<T, unsigned>
  partNo<string> books;  // books是一个pair<string, unsigned>
  ```

  

## 友元

+ 非模板友元：类模板中的常规友元是所有模板实例的友元

  ```cpp
  template <class T>
  class ClassName {
      friend void show(ClassName<T> &);
  }
  ```

  要有实例化的部分，单纯的类模板是不存在的，这时每种参数都有自己的友元

+ 模板友元：为专门的模板定义友元

  + 声明：

    ```cpp
    template <class T>
    class ClassName {
        friend void show(ClassName<T> &);
    }
    ```

  + 定义：

    ```cpp
    void show(ClassName<int> & a) {};
    void show(ClassName<long long> & a) {};
    void show(ClassName<double> & a) {};
    ...
    ```

+ 约束（bound）模板友元，即友元的类型取决于类被实例化时的类型。

  1. 将函数定义为模板

     ```cpp
     template <typename T> void counts();
     template <typename T> void report(T &);
     ```

  2. 在模板中将函数声明为友元

     ```cpp
     template <typename TT>
     class ClassName {
     	friend void counts<TT>();
         friend void report<>(ClassName<TT> &);  //<>不需要指明类型，因为可以根据参数类型推断。
         friend void report<ClassName<TT> >(ClassName<TT> &);  //也可以
     }
     ```

     类声明中的函数声明的函数名后的`<>`指出这时模板具体化，其中类型参数为模板的类型参数。

  3. 在实例模板的时候，会对友元函数实例化

     为实例的友元是所有模板类的友元，实例后的友元是实例类型的模板的友元

+ 非约束（unbound）模板友元，即友元的所有具体化都是类的每一个具体化的友元。

  ```cpp
  template <typename T>
  class ClassName {
  	template <typename C> friend void show(C & c);
  }
  template <typename C> friend void show(C & c) {}
  ```

  友元会被调用时实例化，它是所有类型ClassName模板的友元。

+ 将模板类型参数声明为友元：

  ```c++
  template<typename Type> class ClassName {
      friend Type;
      //...
  }
  ```

# 其他模板问题

+ 控制实例化

  > 模板只有在使用时才会进行实例化，则相同的实例可能出现在多个对象文件中，是额外的开销，可通过explicit instantiation显式实例化

  + 实例化声明：`extern template declaration;`：不在本文件中生成实例化代码，而是在程序其他位置有该实例化的非extern声明（即定义）

  + 实例化定义：`template declaration;`：必须只有一个定义

    普通的实例化，对类成员是使用才实例化，这里会对类成员全部实例化

  `declaration`：`class ClassName<...>`/`type function(...)`

  程序在使用模板时会自动将其实例化，所以控制实例化应该在使用之前

+ 转发

## 可变参数模板

+ variadic template可变参数模板：接受可变数目参数的模板函数或模板类

+ parameter packet参数包：可变数目（零个或多个）的参数

  + 模板参数包
  + 函数参数包

  使用`...`指出接下来的参数表示零个或多个类型的列表

  ```c++
  template<typename T>
  ostream &print(ostream &os, const T &t) {
  	return os << t;
  }
  template<typename T, typename... Args>
  ostream &print(ostream &os, const T &t, const Args&... rest) {  // 这里有类型参数包的扩展
  	os << t << ", ";
      
  	return print(os, rest...);  // 这里是参数包的扩展
  }
  ```

  + `sizeof...`运算符：返回常量表达式表示个数

  + 通常递归调用

  + 包扩展：对于参数包，除了获得其大小还能expand扩展，同时需要提供每个扩展元素的pattern模式：通过在模式右边放省略号来触发扩展

    + 还能这样扩展

      ```c++
      rest为扩展包
      f()为参数只有一个的模板
      f(rest)...相当于f(包的第一个参数), f(包的第二个参数)...
      f(rest...)相当于f(包的所有参数)  // 不合法
      ```

  + 转发参数包

## 模板实例化

+ 函数：

  ```c++
  template<>
  type f(...) {
      
  }
  ```

+ 类模板

  ```c++
  template<>
  class ClassName<...> {
  	...
  }
  ```

  + 特例化成员：

    ```c++
    template<>
    type ClassName<...>::f(...) {
    	...
    }
    ```

    

# 实践

## 模板类声明和实现的分离

https://blog.csdn.net/weixin_40539125/article/details/83375452

> C++自定义模板类中的**模板函数**，声明和定义不能分离，即其必须在`.h`头文件中定义，没有用模板定义的地方可以在.`cpp`实现
>
> 解决方法就是**模板实例化**：减少编译实践+是的类定义与实现分离

+ 解决方案：当然还是写在头文件里啦
  1. 显示实例化（但是我写模板是为了啥？）
  2. `export`关键字（这个都废弃了都）

