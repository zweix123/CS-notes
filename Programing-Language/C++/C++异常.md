> C++异常的主要目的是为设计容错程序提供语言级支持，即异常使得在程序设计中包含错误处理功能更容易，以免事后采取一些严格的错误处理方式。异常的灵活性激励着程序员在条件允许的情况下在程序设计中加入错误处理功能。

+ 异常终止：`abort()`函数（包含在头文件`<cstdlib>`或`<stdlib.h>`）：它向标准错误流（即`cerr`使用的错误流）发送消息"abnormal program termination(程序异常终止)"，然后终止程序，还返回一个随实现而异的值，告诉*调用程序的进程*处理失败。abort是否刷新文件缓冲区取决于实现

  可以强制退出的函数还有`exit()`刷新文件缓冲区，但不显示消息。

+ 返回错误码：将输出的值设置为`<cfloat>`中的`DBL_MAX`宏。

+ 异常机制：

  1. 引发异常：关键字`throw`紧随其后的值指出***异常特征***（会导致语句打断）

  2. 使用处理程序(exception handler)捕获异常：关键字`catch`表示捕获异常(catch关键字和异常类型用作标签，指出当异常被引发时，程序应跳到这个位置执行)(异常处理程序被称为catch块)：处理异常以catch开头，随后是位于括号中的类型声明，它指出了异常处理程序要相应的异常类型；然后是一个花括号括起来的代码块，指出要采取的措施。

  3. 使用`try`块：try块标识其中特定的异常可能被激活的代码块，它后面跟一个或多个catch块。try块是由关键字try指示的，关键字try的后面是一个由花括号括起来的代码块，表明需要注意这些代码引发的异常。

  ```cpp
  {
  	try {
          可能发生异常的地方
          可以是函数调用，则也会去函数里看，这里以函数异常为例
          f();
      }  //后面紧跟cathc
      catch (const char * s) {  //为异常特征命名。
          处理。
      }
      如果try里没事则跳过catch
      如果有多种异常状态可接多个catch块——顺序捕获
  }
  f() {
  	if (异常的条件) throw "有异常";  //这里异常特征被设置为"有异常"
  }
  如果没有try或者catch，则throw发现异常后执行abort()函数
  如果异常出现在try块外的代码，则称为未捕获异常（uncaught exception），默认情况程序意外停止
  ```

  + 将对象作为异常类型。

    ```cpp
    class bad {
        
    }
    
    {
        try {
    		fName();
        }
        catch (bad) {}
    }
    
    type fName() {
        if () throw bad; //可以设置构造函数
    }
    ```

    + 如果类有继承

      1. catch中可以使用基类的引用，来捕获其派生类的异常。
      2. catch的捕获是顺序，派生类异常要注意排序：将捕获位于层次结构最小面的异常类的catch语句放在最前面，将捕获基类异常的catch语句放在最后面。

  + 栈解退(unwinding the stack)：如果try没有调用引发异常的函数，而是调用了对引发异常的函数进行调用的函数，则程序流程将从引发异常的函数跳到包含try块和处理程序的函数：调转中对栈的变量（变量、对象）的释放（析构）。

    如果异常后有delte语句，则其管理的地址会发生内存泄露。

+ 异常规范(exception specificaton)（C++98新增，C++11摒弃）

  + 意外异常（unexpected excepton）

  C++11支持一种特殊的异常规范，使用关键字**`noexcept`**（置于函数列表后括号和分号前）指出函数不会发生异常

  如果在异常规范中发生异常，就必须与规范列表中的某种异常匹配（类继承则需要和派生的匹配）;否则称为*意外异常*(unexpected exception)（默认情况下这将导致程序异常终止）

+ 异常类：

  + 头文件`exception`头文件（旧为`<exception.h>`或`<except.h>`）定义了`exception`类：

    有一个`what()`虚拟成员函数，继承时可重定义。

  + 头文件`stdexcept`定义`logic_error`和`runtime_error`类系列（由`exception`派生出来的）

    1. `logic_error`类描述典型逻辑错误
       + `domain_error;` ：超过数学函数的定义域(domain)和值域(range)
       + `invalid_arrgument;` ：给函数传递一个意料外的值
       + `length_error;` ：没有足够的空间来执行所需的操作
       + `out_of_bounds;` ：指示索引错误
    2. `runtime_error`类描述可能在运行期间发生但难以预计和防范的错误
       + `range_error;` ：下溢(underflow)浮点数小数的最小值；上溢
       + `overflow_error;`
       + `underflow_error;`

+ `new`引发的错误：`bad_alloc`异常：头文件new包含bad_alloc类的声明，它是从exception类公有派生而来的

  ```cpp
  try {
      type p = new type;
  }
  catch (bad_alloc & ba) {
      cout << ba.what();
      exit(EXIT_FAILURE);
  }
  ```

  标记开关，当new失败返回空

  ```cpp
  type p = new (std::nothrow) type;
  if (p == 0) {
      exit(EXIT_FAILURE);
  }
  ```

