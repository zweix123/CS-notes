## Manual

### C

| year | name                                                                  | explain                                                             |
| ---- | --------------------------------------------------------------------- | ------------------------------------------------------------------- |
| 1978 | K&R C                                                                 | 来自Brian Kernighan, Dennis Ritchie的《The C Programming Language》 |
| 1989 | ANSI C/C89/C90                                                        |                                                                     |
| 1999 | [C99/C9x](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf) |                                                                     |
| 2011 | [C11/C1x](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf) |                                                                     |

+ GNU：[The GNU C Reference Manual](https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html) | [The C Preprocessor](https://gcc.gnu.org/onlinedocs/cpp/) | [The GNU C Library](https://www.gnu.org/software/libc/manual/html_mono/libc.html)

### C++

>1979年C++之父Bjarne Stroustrup因准备博士论文而接触Simula语言，其变种Simula 67是公认的首款支持面向对象的语言，之后Stroustrup开发“C with Classes”语言并制作其编译器Cfront（将C with Classes代码转换成C代码，本身由C with Classes编写）

+ https://isocpp.org/ ：这是C++标准委员会（ISO C++ Standards Committee）的官方网站，主要提供C++标准化的最新消息、标准文档、标准库以及C++社区的活动讯息等。
+ https://en.cppreference.com/w/Main_Page ：这是一个C++语言参考网站，提供了C++标准库的详细介绍、C++语言的语法、语义和特性的详细说明等。
+ https://cppcon.org/ ：这是一个C++社区的年度盛会，主要包括C++领域的最新技术和实践、C++标准的最新进展以及C++社区的最新动态等。
+ https://cplusplus.com/ ：这是一个面向C++初学者的网站，提供了C++语言基础知识、C++标准库的介绍、C++编程实践等内容。
+ cppquiz

## 文件命名

|         | C头文件 | C    | C++头文件 | C++    | 可执行文件 |
| ------- | ------- | ---- | --------- | ------ | ---------- |
| Windows | `.h`    | `.c` | `.hpp`    | `.cpp` | `.exe`     |
| Linux   | `.h`    | `.c` | `.hpp`    | `.cpp` | None       |
| Mac     |         |      |           |        |            |

## 项目结构

+ 分离式编译(separate compilation)：将组件放在独立的文件中，分别编译，在链接时组成一套。

  > 这**组**源代码文件为==一个==程序**文件**，每个单独的源代码文件称为***翻译单元***(translation unit)
  >
  > 所以上述的”独立的文件“中文件应该称为翻译单元。  //不同教材翻译问题

  + 目的：如果修改其一，只需要对它单独编译，然后与其他可链接文件链接。

+ 程序设计：将组件与主函数分开放在独立的文件，对于两者都使用的结构声明（实际上是一个声明，一个定义），放在头文件（标准头文件和自定义头文件）中；

  对于常用的结构，C++提供丰富的标准头文件，对于用户（程序员）定义的结构，在独立的文件中实现（方便实现）。

  1. 头文件（`.h`文件）：  //声明文件

     + 包含：函数原型、使用#define和const定义的符号常量、结构声明、类声明、模板声明、内联函数。  //声明不创建实体变量，只为源代码中定义时提供方案。

       > 标准头文件中老版ANSI C的头文件有后缀`.h`，C++标准库兼容C语言标准库，去掉后缀，添加前缀`c`，其内容从属于名称空间`std`。
       >
       > 自定义头文件使用后缀`.h`。

     + 管理：文件对同一头文件只能包含一次，但头文件可能包含使用者不知道的头文件。可利用编译指令解决
  
       > 防护(guarding)方案/防御式声明：
       >
       > 1. `#define`定义宏。
       >
       >    `#ifndef 宏 ... #endif` 判断宏是否被定义过，如果未定义则运行，否则跳过此部分。
       >
       >    ```cpp
       >    #ifndef NAME_H
       >    #define NAME_H  //在进入后立刻定义即可防止再次进入
       >    // place inclue file contents here
       >    #endif
       >    ```
       >
       >    编译器首次遇到该文件，名称没有被定义，则查看两者之间的内容，并定义名称，这时其他文件遇到名称时已被定义，则跳过。
       >
       > 2. `#pragma once`
       >
       >    可代替方案一的头文件保护功能，即保证文件只被include一次，但是有些编译器不能识别。
       >
       > **系统头文件使用这种技巧，同时也建议自定义的头文件也使用这种方法**

  2. 源代码文件（`.cpp`文件，与实现的头文件名称相同，include该头文件）：包含组件的定义代码。  //定义文件

  3. 源代码文件（`.cpp`文件，包含主函数，为一组源代码的入口，include需要的头文件）：包含使用结构和调用函数的代码。
  
  + 头文件因为有宏保护，所有头文件的引用上无需顾忌；但使用标准名称空间尽量使用作用域解析运算符(`::`)，**不要使用using编译指令**，避免在被使用时与使用文件的操作发生冲突。（因为#include是文本拷贝）
  
    而定义文件中头文件的引用和名称空间的编译不用担心，主函数只会在其中找寻对应组件的实现方式，而不会拷贝整个文件。
  
  + **系统头文件使用`<>`括起来；自定义头文件使用`""`括起来**，这是在提示编译器去哪里寻找头文件。

+ 使用类时通常多文件使用，并且类声明在一个`.h`文件，类方法定义在一个同名的`.cpp`文件，还有一个含主函数的文件。

  + 原型文件：`ClassName.h`

    ```cpp
    #ifndef CLASSNAME_H
    #define CLASSNAME_H
    
    class ClassName {
        ...
    }
    
    #endif
    ```

  + 定义文件：`ClassName.cpp`

    ```cpp
    #include "ClassName.h"
    #include <iostream>
    {
        std::cout << ...;
    }
    
    ClassName::fName
    ```

  + 使用文件：

    ```cpp
    #include "ClassName.h"  //双引号指出同文件下。
    ```

## 编译运行

### 1.翻译

1. 源代码出现的字符映射到源字符集，处理多字节字符和*三字符序列*（字符扩展）
2. 定位每个反斜杠后面跟着换行符的实例并删除$\Rightarrow$将*物理行*确定为*逻辑行*
3. 把文本划分成预处理记号序列、空白序列和注释序列（*记号*是由空格、制表符和换行符分隔的项）
	>编译器将注释替换为空格。

### 2.预处理
[GNU C Preprocessor](https://gcc.gnu.org/onlinedocs/cpp/) | [C++ Ref](https://en.cppreference.com/w/cpp/preprocessor)

`.c` -> `.i`

```bash
gcc -E xxx.c
```

### 3.编译

`-i` -> `.S` -> `.o`

+ 词法分析
	```bash
	clang -fsyntax-only -Xclang -dump-tokens xxx.c
	```

+ 语法分析
	```bash
	clang -fsyntax-only -Xclang -ast-dump xxx.c
	```

+ 语义分析
	>clang的语法分析也做了

	```bash
	clang -fsyntax-only -Xclang -ast-dump xxx.c
	```

+ 中间代码生成
	```bash
	clang -S -emit-llvm xxx.c
	```

+ 中间代码优化
	```bash
	clang -S -foptimization-record-file=- xxx.c
	```

+ 目标代码生成
	```bash
	clang -S xxx.c
	```

+ risc-v
	```bash
	clang -S xxx.c --target=riscv64 -march=rv64g
	```

### 4.链接