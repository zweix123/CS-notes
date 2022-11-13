# 绪论

+ SL(Standard Library)标准库：

+ STL(Standard Template Library)标准模板库：

# string类

> string类由头文件string支持，头文件string.h和cstring支持对C-风格字符串进行操纵的C库字符串函数，但不支持string类。

+ string类的构造函数：

  `size_type`是一个依赖于实现的整型，定义于`<string>`头文件

  string类将`string::npos`定义为字符串的最大值，通常是`unsigned int`的最大值

  缩写NBTS(null-terminated string)来标识以空字符结束的字符串-传统C字符串

  | 构造函数                                                     | 描述                                                         |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | `string(const char *s)`                                      | 将string对象初始化为s指向的NBTS                              |
  | `string(size_type n, char c)`                                | 创建一个包含n个元素的string类，其中每个元素都被初始化为字符c |
  | `string(const string & str)`                                 | 将一个string对象初始化为string对象str（复制构造函数）        |
  | `string()`                                                   | 创建一个默认的string对象，长度为0（默认构造函数）            |
  | `string(conat char *s, size_type n)`                         | 将string类初始化为s指向的NBTS的前n个字符，即使超过了NBTS结尾 |
  | `template<class Iter>`<br>`string(Iter begin, Iter end)`     | 将string对象初始化为区间$[begin, end]$内的前n个字符，其中begin和end的行为就像指针，用于指定位置，范围包括begin在内，但不包括end |
  | `string(const string & str, string size_type pos = 0, size_type n = npos)` | 将一个string对象初始化为对象str从位置pos开始到结尾的字符，或从位置pos开始的n个字符 |
  | `string(string && str) noexcept`                             | C++11新增，将一个string对象初始化为string对象str，并可能修改str（移动构造函数） |
  | `string(initializer_list<char> il)`                          | C++11新增，将一个string对象初始化为初始化列表il中的字符      |

+ 重载运算符：

  + `+=`：将一个字符串、字符、数值强制转换为字符后接到另一个字符串的后面。
  + `<<`、`>>`：重载输入输出
  + 赋值`=`：
  + []
  + `+`：将操作数组合为string

  + 比较运算符

+ I/O：

  > C-风格字符串：`cin >> str;`、`cin.getline(str, len);`、`cin.get(str, len);`
  >
  > string类：`cin >> str;`、`cin.getline(cin, str);`、

  + cin和getline自动调整目标string目标对象的大小，使之刚好能够存储输入的自身
  + getline有一个可选的第三个参数来指定使用哪个字符来确定输入的边界
  + cin：与空白字符停止，并将其丢弃。
  + getline：
    + 到达文件尾：输入流`eofbit`被设置（即`fail()`和`eof()`返回true）;
    + 遇到分界字符（默认为`\n`，将分界字符从输入流中删除，但不存储它）；
    + 读取到字符数达到最大允许值(npos和可供分配的内存字节数中的较小的一个),将设置输入流`failbit`(`fail()`返回true)strin

+ 与C-风格字符串的不同：

  + 对象名不是数组，不是指针，要指针还要`&str[seat];`

+ C++11新增：

  + `string str = { 'H', 'e', 'l', 'l', 'o' };`没有空字符。

+ 对象名不是数组，不是指针，要指针还要`&str[seat]`

+ C++11新增2 `string str = {'H', 'e', 'l', 'l''}`

+ string类的本质：基于模板类：

  ```cpp
  template<class charT, class traits = char_traits<charT>, 
  class Allocator = allocator<charT> >
      basic_string {};
  typedef basic_string<char> string;
  wchar_t wstring;
  char16_t u16string //C++11
  char32_t u32string //C++11
  ```

  traits类描述关于选定字符类型的特定情况，有预定义的char_traits模板具体化

  Allocator是一个管理内存分类的类

> 输入流对象的统计系统，用于跟踪流的错误状态：
>
> 检测到文件尾后将设置eofbit寄存器
>
> 检测到输入错误时将设置failbit寄存及
>
> 出现无法识别的故障时设置badbit寄存器
>
> 一切顺利时设置goodbit寄存器

# IO库

+ 头文件<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/IO库.jpg" style="zoom:50%;"> 名称空间`std`

  + IO库中的类对象不能拷贝、赋值——不能做函数形参或返回值——只能做引用
  + IO库中的方法为流重载了`<<`或`>>`运算符：ege：`endl(cout)`可写为`cout << endl;`

+ 流：C++将IO视为字节流，是对IO的抽象，为C++提供服务

  + 程序无需关注流的来自和出处，以同样的方式对待
  + 管理：
    1. 将流与程序关联起来，
    2. 将流与文件连接起来。

+ 缓冲区：用作中介的内存块，是信息在硬件和程序之间IO的临时存储工具，大小通常为512个字节或其整数倍

  > 从磁盘驱动器读取的速度很慢，C++采取一次读取一大块，然后程序在这大块信息中IO信息。

+ 刷新缓冲区(flushing the buffer)：程序首先填满缓冲区，然后把整块数据传输给硬盘，并清空缓冲区，以备下一批输出使用。

  + 隐式刷新：

    + 程序正常结束（程序崩溃可能不会刷新）

    + 流的默认刷新模型：

      1. `unitbug`方法    ：设置为使用后立刻刷新缓冲区模式
      2. `nounitbug`方法：还原

    + 流关联：当一个输入流被关联到一个输出流中，任何试图中输入流读取数据的操作都会先刷新关联的输出流

      > 一个输入流只能关联一个输出流，但是一个输出流可以关联多个输入流

      + cin和cout默认关联的

      + `tie`方法：
        1. 不带参数：返回指向（关联）输出流的指针
        2. 接受指向ostream的指针：将自己关联到ostream

  + 显式刷新：

    1. `flush`：不输出字符刷新
    2. `endl`：换行并刷新
    3. `ends`：输出空字符并刷新

+ condition state条件状态/stream state流状态：IO库类对象的数据成员：从ios_base类继承、定义为iostate类型(一种bitmask类型)

  <img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/IO库条件类型.jpg" style="zoom:65%;"><img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/流状态.png" style="zoom:55%;" />

  + 一个流一旦发生错误，该流会失效（不能再使用）

  + `iostate` ：提供表达式流状态的完成功能，作为位集合使用

    + IO库定义iostate类型的consepr值来表示特定的位模式：`goodbit、badbit、failbit、eofbit`

      其中badbit是系统级错误，不可恢复，置位流不可再用、而后两者是可恢复的错误

  + 重置状态

    `clear()`      ：将状态设置为它的参数，默认为0（清除所有位）；如果有参数则参数状态不变

    `setstate()`：只影响参数中已设置的位，不会影响其他位

  + **IO异常**：使用`exceptions()`：返回一个位字段，包含三位，分别对应，默认设置goodbit

    > 如果clear方法返回的位与exceptions方法返回的位 存在一样 引发`ios_base::failure` 异常
    >
    > > ios_base::failure异常类是由std::exception类派生来的

    可通过exceptions()方法修改

## iostream

标准输入输出头文件`iostream`：最开始是`ios_base` ：

<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/iostream.jpg" style="zoom:55%;"><img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/iostream流对象.jpg" style="zoom:55.5%;"> 

+ `cin`和`cout`为C++提供的标准I/O工具：包含在`iostream`头文件里，标准输入(standard input)：`cin`（发音see-in）是`istream`类的对象；标准输出(standard output)：`cout`（see-out）是`ostream`类的对象；两个类也有自己的成员函数。

  > 标准库还定义了其他ostream对象：
  >
  > + 标准错误(standard error)：`cerr`（发音see-err）：输出警告和错误信息
  > + `clog`（发音see-log）：输出程序运行时的一般性信息

  + 使用前作的准备：
    + 必须包含头文件iostream
    + 头文件iostream定义了一个用于处理输入的istream类和用于处理输出的ostream类
    + 头文件iostream声明了一个名为cin的istream变量（对象）和一个名为cout的ostream变量（对象）
    + 必须指明空间std；（为引用相关元素必须使用编译指令`using`或前缀`std::`）
    + 可以结合使用两个元素和运算符（<< 或 >>）来处理各种类型的数据。

  + 抽取运算符（` >>`）、插入运算符（`<<`）

### cout

+ 方法：

  + 重载`<<`左移运算符为插入运算符

    + 可识别C++所有基本类型（ostream类为每个类型都重载了运算符）

      > 对`char`类型认为是整数

    + 可识别一系列`char *`类型，使之将其识别为字符串并以终止空字符来确定何时停止

    + 可识别`void *`类型，来输入地址，如果想输出char型地址需要强制转换

    + 拼接输出：重载函数返回ostream类来实现拼接输出。

  + 其他方法：

    + `put()`：原型：`ostream & put(char);`；语法：`cout.put()`；被模板化，可用于`wchar_t`。

    + `write()`：原型：`basic_ostream<charT, tarits>& write(const char_type* s, streamsize n);` 可拼接。

      ​					语法：`cout.write(字符串地址，显式字符个数);`不会遇空字符停止！

    返回对象引用，可拼接。

+ 输出格式化：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/cout格式化.png" style="zoom:67%;">

  > ostream类由ios类派生来的，ios类由ios_base派生来的；而ios_base类存储了描述格式状态的信息，又由于ios_base是ostream类的间接子类，所有其方法可用于ostream类和其对象。

  + 计数系统：ios_base类的控制符(manipulator)(也是函数，但不是成员函数，所以不调用对象)

    控制范围：直到将格式设置为其他选择为止：

    | 控制符 | 效果 |
    | ------ | ---- |
    | `dec`  |      |
    | `hex`  |      |
    | `oct`  |      |

  + 调整字段宽度：使用cout成员函数width；

    语法：`int width()`返回字段宽度的当前设置；`int width(int i);`将字段宽度设置为i个宽度，并返回以前的字段宽度。

    影响范围：只能影响显示下一个项目，之后恢复到默认值。

    右对齐；如果不够自动扩充（所以width默认值是0），填充字符为空格

  + 填充字符：cout成员函数`fill(char);` 影响范围：一直有效到更改。

  + 设置浮点数的显示精度（默认6位、末尾0不显示）：

    > "精度"的含义取决于输出模式：
    >
    > + 默认模式				   ：显式的总位数
    > + 定点模式和科学模式：小数点后面的位数

    成员函数`precesion(int)`：总位数；影响范围：一直有效到更改

  + `cout`成员函数`setf()`：

    > ios_base类有一个受保护的数据成员，其中各位（标记）分别控制着格式化的各个方面。打开一个标记称为设置标记（或位），并意味着相应的位被设置为1。
    >
    > 控制符是一种标记。

    1. 原型一：`fmtflags setf(fmtflags);` 其中fmtflags是bitmask类型（用于存储各个位值得类型，可以是整型或枚举或STL bitset容器，主要思想是每个位可以单独访问）的typedef名，用于存储格式标记，该名称是在ios_base类中定义的。即该函数通过fmtflags设置位，并返回以前的设置。

       + 格式常量（类级静态常量）：

         | 常量                  | 含义                                  |
         | --------------------- | ------------------------------------- |
         | `ios_base::boolalpha` | 输入和输出bool值，可以为true或false   |
         | `ios_base::shwobase`  | 对于输出，使用C++计数前缀（0，0x）    |
         | `ios_base::shwopoint` | 显示末尾的小数点                      |
         | `ios_base::uppercase` | 对于16禁止输出，使用大写字母，E表示法 |
         | `ios_base::showpos`   | 在整数前面加上+                       |

    2. 原型二：`fmtflags setf(fmtflags, fmtflags);` 设置第一个参数的位，第二个参数指出要清除第一个参数得哪些位（清除位(clearing the bit)）

       + self(long, long)的参数

         | 第二个参数              | 第一个参数             | 含义                 |
         | ----------------------- | ---------------------- | -------------------- |
         | `ios_base::basefield`   | `ios_base::dec`        | 使用基数10           |
         |                         | `ios_base::oct`        | 使用基数8            |
         |                         | `ios_base::hex`        | 使用基数16           |
         | `ios_base::floatfield`  | `ios_base::fixed`      | 使用定点计数法       |
         |                         | `ios_base::scientific` | 使用科学计数法       |
         | `ios_base::adjustfield` | `ios_base::left`       | 使用左对齐           |
         |                         | `ios_base::right`      | 使用右对齐           |
         |                         | `ios_base::internal`   | 符号或计数前缀左对齐 |

    + 可用函数消除影响：`void unsetf(fmtflags mask);`：mask为对应的位，setf将其设置为1，则unsetf将其设置为0。

    + 可使用控制符代替setf函数

      | 控制符      | 调用 | 含义 |
      | ----------- | ---- | ---- |
      | `boolalpha` |      |      |

+ 头文件`<iomanip>`的带参数可用于cout的控制符：

  | 函数             | 功能     | 参数               |
  | ---------------- | -------- | ------------------ |
  | `setprecision()` | 设置精度 | 指定精度的整数     |
  | `setfill()`      | 填充字符 | 指定填充字符的char |
  | `setw()`         | 字段宽度 | 指定字段宽度的整数 |

### cin

+ 语法：`cin >> value_holder` 其中，value_holder为存储输入的内存单元，可以是变量、引用、被解除引用的指针、类结构的成员。解释方法取决于其类型。

+ 原型：`istream & operator>>(type &);`格式化输入函数(formatted input functions)

  + istream类重载`>>`右移运算符为抽取运算符
    + 可识别C++所有基本类型的引用
    + 可与hex、oct和dec控制符一起使用来指定将整数输入解释为对应格式
    + 可识别一系列`char *`类型，读取字符放到指定地址，到空白停止，并在一系列字符后添加空值字符使之成为字符串

+ 输入检查：

  + 输入跳过空白直到合适的输入（但不能跳过其他字符）
  + 遇到空白或类型不对应字符停止（该字符留在输入序列）。
  + 如果无对应可解释字符，则返回0（istream对象的错误状态被设置）


## fstream

+ 处理命名文件IO：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/fstream特有操作.jpg" style="zoom:67%;">

  + 如果open失败，failbit会被置位，需要复位后再次使用

  + fstream类对象销毁时，自动调用close

  + file mode文件模式：

    | 文件模式            | 说明                           |
    | ------------------- | ------------------------------ |
    | `in`(ifstream默认)  | 以读方式打开                   |
    | `out`(ofstream默认) | 以写方式打开（会丢弃已有数据） |
    | `app`               | 每次写操作前均定位到文件末尾   |
    | `ate`               | 打开文件后立即定位到文件末尾   |
    | `trunc`             | 截断文件                       |
    | `binary`            | 以二进制方式进行IO             |

1. 写入文本文件

   + 前提：

     1. 头文件`fstream`。（里面的`ofstream`类）和名称空间std;
     2. 定义类对象；使用成员函数与文件联系起来；使用运算符操纵数据。（类似iostream）

   + 使用：

     1. 方法open()接受一个C-风格字符串（常量、数组）作为参数，使定义的ofstream对象与文件进行联系。

        文件存在则截断该文件，将其长度截断到零——丢弃原来的内容

        文件不存在则创建文件。

     2. 声明的ofstream类可以使用cout的操作和方法。

     3. 方法close()关闭文件，如果忘记，程序正常终止自动关闭

     ```cpp
     #include <fstream>
     using namespace std;
     ...
     ofstream sam;
     sam.open("out.txt");
     char str[N]; cin >> str;
     sam.open(str);
     sam << ans << endl;
     sam.close();
     ```

     具体操作对比cout。

2. 读取文本文件

   + 前提：类似写入，使用类`ifstream` 

   + 操作：类似写入，具体操作对比cin。

     + 方法`is_open()`检查文件是否被成功打开，成功返回true，否则返回false。

       > 打开同文件下的文件。

+ 头文件：`<fstream>`（包含iostream）

+ 类：`ifstream`和`ofstream`类

  对象：

+ 方法：

  + 关联文件：

    + 两个类的构造函数

    + `open(char *)`

      > `string`类有`c_str()`方法将string类转换为C-风格字符串

  + 重载：两个类对象可以类似cin/cout一样使用

    > ostream是ifstram和ofstream类的基类，所以可以使用其所有方法。

  + 关闭：`close();`

    > 当对象过期，连接自动关闭

    关闭连接并不会删除流，只是断开，流管理装置仍然保留

  + 判断文件打开是否成功：

    + 老版本：`fail()`直接判定对象
    + 新版本：`is_open()`

+ 1. IO有缓冲
  2. 命令行：主函数参数`int main(int argc, char * argv[])`：argc为命令行字符串个数，argv为命令行该行的所有字符串，通常argv[0]是程序名

+ 文本模式：构造函数和open方法的其他参数（文件名字符串，模式常量）

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/文本模式常量.png)

  默认：

  + ifstream open和构造函数以ios_base::in（打开了文件以读取）
  + ofstream open和构造函数以ios_base::out|ios_base::trunc（打开文件，以读取并截短文件）

  > 位运算符OR用于将两个位值合并成一个可用于设置两个位的值

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/C++和C的文件打开模式.png)

  + `ifstream fin(filename, c++mode);`

    `fopen(filename, cmode);`

  + `ios_base::ate` and `ios_base::app` ：将文件指针指向打开的文件尾，前者只允许将数据添加到文件尾，后者将指针放到文件尾。

+ 二进制文件：每个字符有其二进制位模式

  文本模式：`ios_base::binary`

  成员函数：`read()`和`write()`

+ 随机存取

+ 内核格式化

## sstream

处理内存的IO：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/stringstream.jpg" style="zoom:67%;" />

将string对象中的信息放在stringstream对象中，然后将此对象作为iostream使用

## 旧版本

**单字符输入输出**：

```c++
istream & operator >> (char &);
istream & get(char &);
int get(void);
```

| `char ch` | `cin >> ch` | `cin.get(ch)`                                | `ch = cin.get()`                 |
| --------- | ----------- | -------------------------------------------- | -------------------------------- |
|           | 跳过空白    | 读取每个字符                                 | 读取每个字符                     |
|           | 输入被缓冲  | 输入被缓冲                                   | 输入被缓冲                       |
|           |             | 返回一个对象<br>即可连续使用<br>文件尾不修改 | 返回一个整型<br>或EOF(文件尾)    |
|           |             | 文件尾修改cout为false                        | 文件尾返回EOF                    |
|           |             |                                              | `cout.put(ch)`<br>参数必须字符型 |

+ OOP的函数重载特性使得同名不同参的两个成员函数共存在一个类里面——cin.get()

+ 文件结尾（EOF）：选择某个特殊字符（即哨兵字符（sentinel character））作为停止标记——C++输入工具与操作系统系统工作，来检测文件结尾并将这种信息告知程序——iostream定义符号常量`EOF`（-1）。

  > 1. 重定向：允许文件代替键盘输入
  > 2. 很多操作系统都允许通过键盘来模拟文件尾条件

  + 检测到EOF后，cin将两位（`eofbit`和`failbit`）都设置为1。

    > `eofbit`是检测EOF
    >
    > `failbit`是检测错误类型

    方法检测最近读取的结果。

    1. 成员函数`eof()`可查看eofbit是否被设置，检测到返回bool值false
    2. 成员函数`fail()`可常看eofbit或failbit是否被设置为1，是返回true否则返回false

    eof标记被是设置后，cin将不再读取输入，`cin.clear()`可能清除EOF标记。

+ istream类提供将其对象转换为bool值的函数，对象出现在需要bool值是，该函数会被调用，类的成员函数也有这属性。

  ```cpp
  cin.get(ch)  //ch = cin.get()
  while (!cin.fail());
  while (cin);
  while ((ch = cin.get()) != EOF)
  ```

+ ==EOF的值是-1，有些系统的char型可能不能存储。==

------

**字符串输入输出**见-数据-复合类型-字符串

| 函数     | `get`                                                        | `getline`                                                    |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 原型     | `istream & get(char *, int, char)`<br>`istream & get(char *, int)` | `istream & getline(har *, int, char)`<br/>`istream & getline(char *, int)` |
| 参数解释 | 第一个参数指存储字符串的地址<br>第二个参数指读取的长度（比字符串长度大1）<br>第三个参数指定用作分界符的字符 |                                                              |
|          | 两参数版本默认回车为分界符                                   |                                                              |
| 区别     | get遇到回车停止，并返回换行符—分界符                         | getline遇到回车停止，并丢弃换行符—分界符                     |

3. `istream & ignore(int = 1, int = EOF);`：读取到最大字符数或文件末尾

+ 意外字符串输入：

  1. 遇到文件末尾将设置`eofbit`

  2. 遇到流被破环将设置`badbit`

  3. 无输入（输入空行或即将到达文件尾）或输入到达或超过最大字符数将设置`failbit`

     | 方法    | 无输入                      | 输入最大                  |
     | ------- | --------------------------- | ------------------------- |
     | getline | failbit（换行符认为字符）   | failbit（到最大且行还有） |
     | get     | failbit（换行符不认为字符） | 无                        |

# Else

## bind

> C++11

+ 头文件`<functional>`：通用函数适配器，接受可调用对象，生成新的可调用对象*适应*原对象的参数列表——修正参数值

+ 语法：`auto newCallable = bind(callable, arg_list)`

  + arg_list中参数可能包含形如`_n`的名字，其中n为整数：占位符：表示newCallable的参数位置

    > 名字_n定义在`placeholders`的命名空间中，该命名空间又定义在std中，所有在用时要`using namespace std::placeholders`

+ 用法：

  ```c++
  type f(type arg1, type arg2);
  auto f_ = bind(f, _1, arg2_val);
  f_(arg1);
  ```

  本来需要两个参数的f，通过bind变成f\_，它的第2个参数使用arg_val这个默认值，之后调用f\_并提供一个参数即可

  + 顺序也可以不同，调用时对应映射
    + 可用于调换参数顺序

### ref/cref

> bind中的参数绑定是只绑定，如何引用绑定？

+ 头文件同bind
+ `ref()`：返回一个对象，包含给定的引用
+ `cref`：生成一个保存const引用的类

## pair

+ 头文件`<utility>`

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/pair.jpg)

+ `make_pair()`$\rightarrow$`{}`





# 迭代器

+ 迭代器：**`iterator`**；头文件`<iterator>`

+ 迭代器范围(iterator range)：由一对迭代器表示，分别指向同一个容器中的元素和尾元素之后的位置(one past the last element)——begin、end/first、last（会有歧义）——左闭合区间(left-inclusive interval)：$[begin, end)$

  + 方法：`begin()`和`end()`：

    + 重载：如果对象为const的，其返回也是const的

      或者：`cbeing/end()`：返回const

    > 反向迭代器：`rbegin/rend()`：也做了重载`rcbegin()/rcend()`

  | 迭代器定义方式 | 具体格式                                     | 获取方法          |
  | -------------- | -------------------------------------------- | ----------------- |
  | 正向迭代器     | `容器类名::iterator 迭代器名;`               | `begin()/end()`   |
  | 常量正向迭代器 | `容器类名::const_iterator 迭代器名;`         | `cbegin()/cend()` |
  | 反向迭代器     | `容器类名::reverse_iterator 迭代器名;`       | `rbegin()/rend()` |
  | 常量反向迭代器 | `容器类名::const_reverse_iterator 迭代器名;` |                   |

+ 运算符：++/--/==/！=

  + 随机迭代器：+/-/+=/-=/<>

    + 算术运算操作数是int：跳跃

      ​			   操作数是迭代器：距离，类型`defference_type`

+ Iterator Category迭代器类型：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/迭代器类别2.jpg)

  + 容器使用的迭代器类型：

    | 容器     | 迭代器类型 |
    | -------- | ---------- |
    | `array`  |            |
    | `vector` | 随机       |
    | `deque`  |            |
    | `list`   |            |
    | `set`    |            |
    | `map`    | 前向       |

## 其他迭代器

+  iterator正向迭代器：

+ reverse iterator反向迭代器：

  > 除了forward_list之外的容器都提供

  + `base()`方法：获得对应位置的正向迭代器

+ Insert iterator插入迭代器：`<iterator>`中的`back_inserter()`：接受一个指向容器的引用，返回一个与该容器绑定的插入迭代器

  ```c++
  vector<type> vec;
  auto it = back_inserter(vec);  //调用push_back
  for (int i = 1; i <= 9; ++ i) *it = i; //vec = {1..9}
  ```

   ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/插入迭代器.jpg)

+ Stream iterator流迭代器：将流当作一个**特定类型**的**元素序列**

  + 绑定流，使用`<<`或`>>`控制流
  + 默认初始化的迭代器可作为循环的尾后迭代器

  ```c++
  istream_iterator<int> in_iter(cin), eof;
  while (in_iter != eof) vec.push_back(*in_iter++);//1
  vector<int> vec(in_iter, eof);//2
  
  //结合算法库，极限压行
  cout << accumulate(istream_iterator<int>(cin),
                     istream_iterator<int>( ), 
                     0) << endl;
  ```

  + 操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/流迭代器.jpg)

+ move iterator移动迭代器

# Container容器

+ 头文件：`<容器名称>`，名称空间`std`，都是模板类

+ 常规方法：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/容器操作.jpg" style="zoom:120%;">

+ 容器赋值：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/容器赋值运算.jpg" style="zoom:80%;">
  + swap会改变迭代器或者索引或者指针

## Sequential顺序

> C++已经将其优化到几乎优秀于原始数据结构

+ 顺序容器(sequential container)：提供快速顺序访问元素

  <img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/顺序容器类型.jpg" style="zoom:120%;" />

  + | 容器类型                 | 随机访问 | 随机添加 | 首尾读写 |
    | ------------------------ | -------- | -------- | -------- |
    | `array`                  | 快       | 慢       |          |
    | `vector`                 |          |          |          |
    | `list`<br>`froward_list` | 慢       | 快       |          |
    | `deque`                  | 快       |          | 快       |

+ 添加：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/顺序容器添加操作.jpg" style="zoom:120%;" />
  + `insert`和`push_back`参数是元素，`emplace`使用参数构造元素
  + 内存分配策略：只在迫不得已时才重新分配新的内存空间
  
+ 访问：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/顺序容器访问.jpg)

+ 删除元素：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/顺序容器删除.jpg)

  顺序容器大小操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/顺序容器大小操作.jpg)

  容器大小管理操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/容器大小管理操作.jpg)

  + reserve不改变容器中元素的数量，只影响vector预先分配的内存空间

    + 不会减少容器占用的内存空间

    resize不改变容器分配的内存空间，只影响元素个数

  + size		：容器中元素的个数

    capacity：在不分配新内存空间的前提下最多可保存的元素

  
  + 添加/删除vector、string或deque元素要考虑迭代器、引用和指针可归纳失效
  

### array

> 原始数据结构：顺序存储线性表不可扩展

### vector

> 原始数据结构：顺序存储线性表可扩展

+ 扩张策略：在分配内存使分配比申请的要大的内存空间，减少容器空间重新分配次数

### deque

> 原始数据结构：双端队列

### list

> 原始数据结构：链式存储线性表 双向链表

### forward_list

> 原始数据结构：链式存储线性表 单向链表

+ 插入和删除：

  > 由于单向链表的插入和删除需要修改**前驱元素**，但是单向链表没有简单方法获得前驱，所以STL里的fowward_list通过前驱增删后面的元素

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/forward_list的插入和删除.jpg)

  + off-the-beginning首前迭代器：返回不存在的第一个元素的前驱

### 容器适配器

+ adaptor适配器：接受一个容器，使其操作看起来像适配器

+ 所有容器适配器都支持的操作和类型：

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/所有容器适配器都支持的操作和类型.jpg)

+ 构造：两个构造函数：空和拷贝

  1. 第一个模板参数：元素类型

  2. 第二个模板参数：重载默认容器类型：

     > stack和queue是基于deque实现的，priority_queue是在vector之上实现的。

     + stack要求push_back、pop_back、和back：可用除array和forward_list之外的容器构造
     + queue要求back、push_back、front、和 push_front：构造于list或deque之上，但不能用vector构造
     + priority_queue处理上述还要随机访问能力：构造于vector或deque之上，但不能基于list

#### stack

+ 头文件`<stack>`

+ 操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/栈操作.jpg)


#### queue

+ 头文件`<queue>`

+ 操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/队列操作.jpg)


#### priority_queue

+ 头文件和操作见queue
+ **使用`<`运算符确定相对优先级**

## Associative关联

关联容器支持高效的关键字查找和访问

+ 分类：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/关联容器类型.jpg)
  +  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/关联容器的类型别名.jpg)
  + 迭代器：双向迭代器
    + map：`pair<const type, tpye>`
    + set：`const type`

+ 对于有序关联容器：要求定义元素比较方法（strict weak ordering严格弱序）

  + 默认使用`<`运算符——重载
  + 用来组织一个容器中元素的操作的类型也是该容器类型的一部身份：定义时指明：`set<Object, decltype(cmp)*> sam();`

+ 操作：

  + 添加：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/关联容器插入操作.jpg)

    + 不可重复的insert返回pair：first是位置的迭代器，second是bool

      可重复的不会插入失败，只返回bool

  + 删除：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/关联容器删除元素.jpg)
  + 查找：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/关联容器查找操作.jpg)
    + 可重复的中相同元素相邻

### set

### map

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/map中的下标操作.jpg)

### unoreder

+ unordered associative container无序关联容器：不使用比较运算符，使用hash function哈希函数和关键字类型的==运算符
+ 无序容器在存储上组织为一组桶，每个桶保存零个或多个元素，使用哈希函数将元素映射到桶——性能依赖于哈希函数的质量和桶的数量和大小
+ 管理操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/无序容器管理.jpg)

# 泛型算法

> generic泛型的通用的

+ 在`std`名称空间定义，大部分包含在`<algorithm>`头文件，少部分包含在`<numeric>`头文件中（数值泛型算法）。

+ 多有重载版本：

  + 重载数组类型和容器类型
    + 数组使用地址或`begin()、end()`函数
    + 容器使用迭代器
  + 函数对象：默认升序，内置类型可提供`greater<type>()`设置为降序
    + 自定义复合类型需要重载
    + 提供函数（名）或函数对象
  + 迭代器令算法不依赖于容器，但算法依赖于元素类型的操作

+ 大部分标准库算法对一个范围内的元素进行操作，将此称为“输入范围”：两个参数表示：第一个元素和尾元素之后的位置

+ 分类：

  1. 只读算法：迭代器建议使用`cbeing/cend`

     + `find`：

       1. `find_if(begin, end, fun)`：返回满足条件的第一个元素

     + `accumulate(begin, end, 初值)`：求和：初值决定`+`操作类型

     + `equal(1.cbegin, 1c.end, 2.cbegin)`：比较序列是否相同

       > 假定第二个序列至少于第一个序列一样长

       对两容器类型要求不严格，对容器元素类型要求也不严格

  2. 写：

     + `fill`

       `fill_n(begin, num, val)`：假定写入安全

       ```c++
       fill_n(back_inserter(vec), num, val);
       ```

     + `copy(1.begin, 1.end(), 2.begin)`

     + `replace(begin, end, old_val, new_val)`

     很多算法有copy版本：

     ```c++
     replace_copy(1.cbegin, 1.cend,
                 back_inserter(2), old_val, new_val);
     ```

     1中未变，但是2中有了1变化的拷贝

  + 1. 重排（去除重复元素）：

       ```c++
       void work(vector<type> &vec) {
       	sort(vec.begin(), vec.end());
           auto end = unique(vec.begin(), vec.end());
           vec.erase(end, vec.end());
       }
       ```

    2. 离散化：

       ```c++
       void work2(vector<type> &vec) {
           decltype(vec) temp(vec);
           work(temp);
           for (auto &sam : vec)
               sam = lower_bound(temp.begin(), temp.end(), sam);
       }
       ```
       

+ 定制操作：很多泛型算法要求使用元素的某个运算符

  1. 传递参数（predicate谓词）

     > predicate:可调用的表达式，其结果能用作条件的值
     >
     > 1. unary predicate一元谓词
     > 2. binary predicate二元谓词

+ `for_each(begin, end, fun)`

+ 查找：

  | 原型                                          | 说明 |
  | --------------------------------------------- | ---- |
  | `find()`                                      |      |
  | `bool binary_search(begin, end, cmp)`         |      |
  | `type*/iterator upper_bound(begin, end, cmp)` |      |
  | `type*/iterator lower_bound(begin, end, cmp)` |      |

  + 对于bound：

    + tar在区间上：返回超尾
    + tar在区间下：返回begin——所以要检测

    + 序列中查找值的数量：`upper_bound - lower_bound`

+ 排序：`sort(begin, end, cmp)`

+ 去重：`unique(begin, end, cmp)`

+ 翻转：`reverse(begin, end, cmp)`


-----

## 泛型算法结构

### 迭代器类别

算法库要求的迭代器类型：通过功能的多寡划分层次—高级类型支持底层类型所有操作![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/迭代器类别.jpg)

算法库指明每个迭代器参数的最小类别

> 算法库：共享一组参数传递规范和一组命名规范

### 算法形参模式

```c++
alg(beg, end, other args);
alg(beg, end, dest, other args);
alg(beg, end, beg2, other args);
alg(beg, end, beg2, end2, other args);
```

### 算法命名规范

+ 提供操作代替默认`<`或`==`运算符

  + 接受*谓词*：重载函数名

+ 1. _if版本：接受一个谓词，返回谓词真值的
  2. _copy版本：参数列表最后多一个容器参数，将更改后的容器copy

  > _copy_if版本

## 特定容器算法

> 本质是迭代器类型和数据结构特点的。。。：
>
> 1. sort要求随机访问迭代器，但是list or forward_list不能
> 2. 对于链表这种：交换只是换两个的连接，而不是换一系列的元素，所以针对数据结构做特定的修改

+  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/特定容器算法.jpg)





## 随机数

包括随机数引擎类和适配器以及分布模板







