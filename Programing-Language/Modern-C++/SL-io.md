## IO
[iostream ref](https://en.cppreference.com/w/cpp/io/basic_iostream) -> [fstream ref](https://en.cppreference.com/w/cpp/io/basic_fstream) | [sstream lib ref](https://en.cppreference.com/w/cpp/header/sstream)


# IO库

+ 头文件<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/IO库.jpg" style="zoom:50%;"> 名称空间`std`

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

  <img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/IO库条件类型.jpg" style="zoom:65%;"><img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/流状态.png" style="zoom:55%;" />

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

<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/iostream.jpg" style="zoom:55%;"><img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/iostream流对象.jpg" style="zoom:55.5%;"> 

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

+ 输出格式化：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/cout格式化.png" style="zoom:67%;">

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

+ 处理命名文件IO：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/fstream特有操作.jpg" style="zoom:67%;">

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

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/文本模式常量.png)

  默认：

  + ifstream open和构造函数以ios_base::in（打开了文件以读取）
  + ofstream open和构造函数以ios_base::out|ios_base::trunc（打开文件，以读取并截短文件）

  > 位运算符OR用于将两个位值合并成一个可用于设置两个位的值

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/C++和C的文件打开模式.png)

  + `ifstream fin(filename, c++mode);`

    `fopen(filename, cmode);`

  + `ios_base::ate` and `ios_base::app` ：将文件指针指向打开的文件尾，前者只允许将数据添加到文件尾，后者将指针放到文件尾。

+ 二进制文件：每个字符有其二进制位模式

  文本模式：`ios_base::binary`

  成员函数：`read()`和`write()`

+ 随机存取

+ 内核格式化

## sstream

处理内存的IO：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Programing-Language/C++/stringstream.jpg" style="zoom:67%;" />

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

