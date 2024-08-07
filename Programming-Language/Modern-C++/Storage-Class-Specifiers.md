## 存储类别
[ref: storage class specifiers](https://en.cppreference.com/w/cpp/language/storage_duration)

| 存储类别描述    | storage duration | scope | linkage | 如何声明        |
| --------- | ---------------- | ----- | ------- | ----------- |
|           |                  | file  | 外部      | 默认          |
|           |                  | 块     |         | 函数内         |
|           |                  | file  | 内部      | `static`    |
| 定义在其他翻译单元 |                  |       | 外部      | `extern` 声明 |

### 存储持续性
描述了数据保存在内存中的时间长度

#### 自动存储持续性
在程序开始执行所属的函数或代码块时被创建，执行完后释放

1. 自动变量：（默认情况）函数中声明的函数参数和变量，存储持续性为自动，作用域为局部，没有链接性。
	+ 嵌套代码块不同层次代码块中的同名变量会：内层hide外层
	+ 寄存器变量：关键字`register`，向编译器**申请**该变量使用CPU寄存器存储自动变量，旨在提供访问变量速度
		>register关键在在C++11中失去作用，只是显示的指出变量是自动变量

#### 静态存储持续性
在整个程序执行期间都存在的存储方式

2. 静态变量：
	1. 外部变量/全局变量外部链接性（可在其他文件访问）：必须在代码块外声明。
	2. 内部链接性（只能在当前文件中访问）：必须在代码块外声明，并使用`static`限定符。
	3. 无链接性（只能在当前函数或代码块中访问）：必须在代码块内声明，并使用`static`限定符。


3. 外部变量/全局变量（相对于局部的自动变量）：链接性为外部，存储持续性为静态，作用域为整个翻译单元。
	+ 引用声明：关键字`extern`，且不进行初始化（如果使用关键字依然初始化则exrern失效）
	+ 多文件，只需一个定义，其他地方使用引用声明
	+ 引用的变量遵循自动变量的同名下处理规则
	+ 在函数中使用该关键字强调函数使用外部变量

4. 静态存储持续性、内部链接性、作用域整个翻译单元，关键字`static`
	+ 不在代码块内声明的变量天然外部链接，使用关键字限定为内部
	+ 在多文件程序中，此种变量只能在所属的翻译单元内使用

	**不**会与其他翻译单元的全局变量**冲突**，但会**覆盖**

5. 静态局部变量：静态存储持续性、无链接性，作用域局部，关键字`static`用于局部变量
	+ 局部变量存储持续性为自动，使用关键字限定为静态
	+ 静态局部变量在程序执行期间一直存在，但名称只在该作用域可见
	+ 再生：在其他代码块使用static再次声明同名变量，则使用同一块地址
	+ 初始化：初始化语句只在申请空间时执行一次

#### 动态存储持续性
由new和delete运算符管理的内存池

#### 线程存储持续性

### 作用域
描述了名称在翻译单元的可见范围

+ 全局（文件作用域）
+ 局部（块作用域）

### 链接性
描述了名称在不同单元间如何共享

+ 函数链接性：
+ 语言链接性：[ref](https://en.cppreference.com/w/cpp/language/language_linkage)
