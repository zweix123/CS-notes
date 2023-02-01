
+ Rust语句以分号`;`结尾

+ Rust的名称命名：

  + 项目名、文件名

    函数名和变量名：使用下划线命名法（snake case蛇形命名法）：所有字母小写并使用下划线分割单词

+ 注释：

  + 单行注释：双斜杠`//`
  + 文档注释：三斜杠`///`，可使用makedown

## 数据对象

+ 变量：
  + 默认变量是immutable不可变的：创建的变量在绑定一个值后不可变：`let 变量名 = 值;`
  + 可将变量设置为mutable可变的：`let mut 变量名;`

+ constant常量：绑定到一个常量名且不运行更改的值：`const 常量名 = 常量表达式;`
  + 默认变量和常量区别：常量只能设置为常量表达式
  + 命名约定：全大写并以下划分分割单词
+ shadow遮蔽：可声明和前面变量具有相同名称的新变量
  + shadow和mutable的区别，shadow的前后变量类型可不同

## 数据类型

> Rust是一种statically typed静态类型语言，即在编译时编译器知道所有变量的类型，每个值都有确切的data type数据类型

### 标量类型

> scalar标量类型，表示单个值

+ interger整型：

  | 长度  | 有符号类型 | 无符号类型 |
  | ----- | ---------- | ---------- |
  | 8位   | `i8`       | `u8`       |
  | 16位  | `i16`      | `u16`      |
  | 32位  | `i32`      | `u32`      |
  | 64位  | `i64`      | `u64`      |
  | 128位 | `i128`     | `u128`     |
  | arch  | `isize`    | `usize`    |

  + 整型字面量默认`i32`类型

  + `arch`取决于程序运行的计算机的字长

  + 整型字面量：

    + 使用类型后缀来指定类型

    + 使用下划线作为可视分隔符以便读数

    + 整数不同进制：

      | 进制     | 前缀 |
      | -------- | ---- |
      | 十六进制 | `0x` |
      | 八进制   | `0o` |
      | 二进制   | `0b` |

    + 字节（仅限于`u8`）：`b'内容'`

+ floating-point number浮点型：
  + `f32`
  + `f64`（默认）
+ bool布尔类型：关键字`bool`，字面量`true`和`false`
+ char字符型：四个字节、Unicode标量值
  + 字符型字面量：单引号括起来的字符

### 复合类型

> compound type复合类型

+ tuple元组：长度固定、类型可不一致的一系列值

  + 通过在小括号内写入以逗号分割的值列表来创建，每个位置一个类型

    ```rust
    let tp : (i32, f64, u8) = (500, 6.4, 1);
    let tp = (500, 6.4, 1);
    ```

  + 获得元组中的值：

    + destructure结构：`let (x, y, z) = tp;`
    + 使用一个句号脸上要访问的值的索引（索引从0开始）：`tp.0`

  + 没有任何值的元组`()`是特殊的类型

  + 只有一个值的元组`(x)`是特殊的类型：unit type单元类型，这个值`x`是unit value单元值

+ array数组：**长度固定**、类型必须一致的一系列值

  + 通过在方括号内写入以逗号分割的的值列表来创建

    ```rust
    let ar : [类型; 长度] = [...];
    let ar : [值; 个数];  // 值一样的数组
    ```

  + 访问：`ar[索引]`（索引从0开始）

  > 在编译时发现索引不合法会panic
  >
  > 在运行时发现索引不合法也会panic（C/C++可不会）

#### 结构体

> structure

> 较于元组，各个部分可以有名称

+ field字段：每一部分数据的名字和类型

1. 声明：

   ```rust
   struct struct_name {
       field1: bool,
       field2: i32,
       field3:..., 
   }
   ```

2. 创建实例/字段初始化：通过为每个字段指定具体值来创建这个结构体的实例：以结构体的名字开头，接着在大括号中使用`key: value`键-值对的形式提供字段

   + 不要求和它们在结构体声明顺序一致

   + 字段初始化简写语法：

     ```rust
     fn build_struct(field1: ..., field2: ...) -> struct_name {
         struct_name {
             field1,
             field2,
             ...
             没有提供参数的字段: 什么值,
         }
     }
     ```

   + 结构体更新语法：

     ```rust
     let struct_name2 = struct_name {
         一些struct_name2自己的字段初始化,
         ..struct_name1,  // 这里是代码, 表示其他部分由struct_name对应的字段初始化, 必须在最后面
     }
     ```

     这里的复制相当于移动和克隆

3. 使用字段：`实例名.字段名`

+ 元组结构体：

  ```rust
  struct Sam(type1, type2, ....);
  
  let sam = Sam(...);
  ```

+ 没有任何字段的unit-like structs类单元结构体

  ```rust
  struct Uls;
  let uls = Uls;
  ```

+ 打印：在定义前添加`#[derive(Debug)]`

### 枚举

enumerations枚举，variants成员

```rust
enum IpAddrKind {
    V4,
    V6,
}
let four = IpAddrKing::V4;
fn route(ip_type: IpAddrKind) { }
```

本质存储的是类型的别名，可以将其和真实的类型关联

```rust
enum IpAddr {
    V4(String),
    V6(String),
}

let home = IpAddr::V4(String::from("127.0.0.1"));
let loopback = IpAddr::V6(String::from("::1"));

enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

let home = IpAddr::V4(127, 0, 0, 1);
let loopback = IpAddr::V6(String::from("::1"));
```

+ `Option`枚举：空值，Rust没有空值，但是有标准库的`Option<T>`

  ```rust
  enum Option<T> {
      Some(T),
      None,
  }
  let some_number = Some(5);
  let some_string = Some("a string");
  
  let absent_number: Option<i32> = None;
  ```
  
  那么这个和空值的好处在哪里呢？因为`Option<T>`和`T`是不一样的

## 方法

方法和函数一样，不过方法根据结构体上下文而确定

```rust
impl struct_name {
	fn model_name(&self, ...)... {
        ...
        self.field;
    }
}
```

+ `impl`块implementation：其中的内容和某个结构体类型相关联

  + 所有在impl块中定义的函数被成为associated function关联函数

+ `self`参数：方法的第一个参数必须是

  > 实际是`self: &Self`的缩写，impl块中Self类型是impl块的类型的别名 

  + 如果第一个参数不是`self`，则其不是方法，这样的关联函数常用作返回 一个结构体新实例的构造函数

    调用方式：`impl块名::关联函数名(...);`

+ 调用：`实例.方法(...);`

+ 方法和字段可以重名，有括号来区分，不过有时与字段同名的方法将被设定为只返回字段中的值，这样的方法是getters

## 函数

+ Rust的函数定义以`fn`开始，后跟函数名和一对圆括号，大括号告诉编译器函数体起末位置

+ Rust的函数定义位置不关键，前面可以调用后面

+ parameter参数：特殊变量、函数签名的一部分，**必须**声明每个参数类型，多个参数以逗号分割

  > 函数拥有parameter参数是形参，向参数提供具体的值是argument实参

+ statement语句是执行一些操作但不返回值的指令
+ expression表达式计算并产生一个值
  + 用来创建新作用域的大括号（代码块）`{}`也是一个表达式

+ 函数返回值：
  + 返回值类型：在函数参数列表的右括号后面、函数体代码块左括号前面通过`-> type`指定
  + 返回：
    + 通过`return`关键字显式返回
    + 隐式返回最后的表达式（一个代码块就是一个表达式）：这个表达式没有分号做结尾
    + 如果没有隐式或显式的返回，则返回单位类型`()`表示不返回值

## 控制流

+ arm分支：

  ```rust
  if 条件 {
      
  } else {
      
  }
  
  if 条件 {
      
  } else if 条件 {
      
  } else if 条件 {
      
  } else {
      
  }
  ```

  + 条件必须是`bool`值，不会自动转换

  + `if`是一个表达式，所以可以有返回值

    ```rust
    fn gcd(a: i32, b: i32) -> i32 {
        return if b == 0 { a } else { gcd(b, a % b) };
    }
    ```

+ loop循环

  + `loop`

    + 空循环：

      ```rust
      loop {
          //一直循环, 除非break或者终止程序
      }
      ```

    + loop label循环标签：给loop命令并专门break某个loop

      ```rust
      'label: loop {
          ...
          loop {
              break 'label;  // 跳出两个循环
          }
      }
      ```

    + 循环返回：loop循环本身是一个大括号的表达式，也能返回值，通过`break`（相当于函数的`returm`）

  + `while`条件循环：

    ```rust
    while 条件 {
        
    }
    ```

  + `for`：

    ```rust
    for element in 复合类型变量 {
        
    }
    ```

    + range：`(起...超尾)`/`(...).rev()`

+ `match`：

  ```rust
  match 一个枚举实例 {
      枚举名::枚举类型 => 结果,
      ...
  }
  ```

  + 普通的枚举是exhaustive穷举式的
  + 通配模式：
    + `other`匹配并绑定
    + `_`匹配但不绑定

+ `if let`通过等号分割的一个模式和一个表达式

  ```rust
  let some_u8_value = Some(0u8);
  if let Some(3) = some_u8_value {
      println!("three");
  }
  //
  enum UsState {
     Alabama,
     Alaska,
  }
  enum Coin {
     Penny,
     Nickel,
     Dime,
     Quarter(UsState),
  }
  let coin = Coin::Penny;
  let mut count = 0;
  if let Coin::Quarter(state) = coin {
      println!("State quarter from {:?}!", state);
  } else {
      count += 1;
  }
  ```
  

# 所有权

> Rust无需garbage collector, GC垃圾回收器也能保证内存安全，即通过ownership所有权

> 代码在运行时可供使用的内存，根据结构不同分成Stack栈内存和Heap堆内存
>
> + 栈：栈数据结构，所有数据必须占有已知且固定大小
>
> + 堆：缺乏组织，用于在编译时大小未知或大小可能变化的数据
>
>   > 在堆上allocating分配内存：memory allocator内存分配器 在堆的某处找到一块足够大的空间且标记并返回该地址的point指针
>
> | 比较     | 栈               | 堆           |
> | -------- | ---------------- | ------------ |
> | 分配速度 | 快：直接放栈顶   | 慢：需要分配 |
> | 访问速度 | 快：直接计算未知 | 慢：通过指针 |

+ Rust中的每一个值都有一个被成为其owner所有者的变量
+ 值在任一时刻有且只有一个所有者
+ 当所有者（变量）离开作用域，这个值将被丢弃

---

+ scope作用域

Rust在使用堆内存的变量离开作用域时自动释放（通过`drop`函数）

---

以String为例进行分析，一个String对象的存储空间有两部分

+ 栈：固定大小的空间，存储字符串的信息，诸如在堆中的地址、空间大小
+ 堆：可变大小的空间，存储字符串本身。

> 1. shallow copy浅拷贝：将栈内存的信息拷贝给新变量，这时两个指针指向同一地址，这时在管理堆内存是会出现double free二次释放的错误
> 2. deep copy深拷贝：不仅复制栈中的信息，还将堆复制一份，同时将指针指向新的堆空间
> 3. move移动：将栈内存拷贝过去，其中的指针依然指向对应的堆内存，而原变量的栈内存直接失效，从而保证不会内存泄漏

**Rust默认使用移动来拷贝**既有栈空间又有堆空间的数据结构

+ clone克隆：显式深拷贝，使用方法`.clone()`
+ 名为`Copy`trait的特殊标注：对于存储空间只有堆空间的数据对象，则无所谓深浅拷贝，即使是深拷贝也能硬编码

----

则在函数传参中也是，诸如String这样的对象是移动进函数中，在本作用域中其变量名不再有效，而诸如内置标量类型由于Copy依然有效。

> 那如果我们传入时不想传入所有权呢？

1. 返回元组将所有权返回

2. references引用：即传入指针，不过在写法上同普通变量

   ```rust
   fn f(s: &String)...  // &引用
   f(&s);  // &创建引用
   ```

   > borrowing借用：创建一个引用的行为

> 一个引用也是不可变变量，所以别说通过这个引用（本质是指针）去修改原数据结构，实际上这个变量本身都不能修改。

+ 可变引用：

  ```rust
  fn f(s: &mut String)...
  f(&mut s);
  ```

+ slice：
  + 定义：一部分值的引用
  + 语法：使用一个由中括号中的`[starting_index..ending_index超尾]`（两个`.`）指定的range创建一个slice
    + 如果开始于起点，或者结束于末尾，则可以省略，两端都省略就是整体

  + 类型：
    + String的slice是str类型
# 模块系统

> The module system

+ package包：
  + `cargo new`一个项目就是一个包
+ crate：
  + Cargo约定`src/main.rs`就是一个与包同名的二进制crate的crate根
  + Cargo约定`src/lib.rs`就是一个与包同名的二进制crate库
  + Cargo约定`src/bin`目录下，一个包可以拥有多个二进制crate

+ 模块：将一个crate代码分组，提高可读性和重用性，控制内容的公私有性

  + 创建库：

    ```rust
    cargo nwe --lib 库名
    ```

  + 创建模块：

    ```rust
    mod 模块名 {
        
    }
    ```

  + 引用模块：

    + absolute path绝对路径：从crate根开始，以crate名或字面量`crate`开头
    + relative path相对路径：从当前模块开始，以`self`、`super`或当前模块的标识符开头

+ 私有性：

  > Rust默认绝大部分是私有的，需要手动设置共有

  + 语法：在对应关键字前添加关键字`pub`

  + 注意：各个关键字存在嵌套关系
    + 私有是子层次向父层次的私有，父层次对子层次没有私有性
    + 该关键字就是接触上面的私有性
    + 该关键字是都其影响关键字本身有影响，该关键字内的关键字仍然私有，需要对应设置`pub`，继而顺着`pub`向上公有

  + 结构体字段是默认私有的
  + 枚举成员是默认公有的

+ 引入：关键字`use`：将。。。暴露到当前作用域

  > 习惯上不引入到具体的函数和数据，而是到其父层次

  + 引入同名的模块：关键字`as`为其创建别名
  + 嵌套路径：`use::...::{a, b, c::..};`
  + glob运算符：`use::...::*`把包下内容全部引入
  + re-exporing重导入：`pub use...`：则使用当前代码的代码也能使用导入的模块

+ 外部包：在`Cargo.toml`中的`[dependencies]`下添加`库名 = "要求的最低版本"`（会从`crate.io`中下载依赖）

# 标准库std

## 集合collections

### Vec

+ 定义：`Vec<T>`

+ 构造：

  ```rust
  Vec<i32>::new();  //
  vec![.., .., ..];  // 宏
  ```

+ 操作

  ```rust
  v.push(...);
  v.get(索引) -> Option<&T>
  v[索引]
  
  for x in &v {}
  for x in &mut v { *x...; }
  ```

  + 类型不同的Vec

    ```rust
    enum SpreadsheetCell {
        Int(i32),
        Float(f64),
        Text(String),
    }
    
    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    ];
    ```

### String

+ 构造：

  ```rust
  String::from("字符串字面量");
  一个字符串字面量或者存储字符串字面量的变量.to_string();
  ```

+ 操作

  + 追加：`s.push_str("追加的字面量");`
  + 拼接：
    + `+`运算符：`s3 = s1 + &s2`
      1. `s1`被移动了
      2. `s2`使用索引是因为调用`add`函数，该函数的参数是索引类型
    + 宏：`format!("{}", 字符串);`

  > String不支持索引，因为String的本质是`Vec<u8>`即按直接存储，但Rust使用CTF-8编码，不同字符空间不同，索引需要计算有效字节数，效率并不高。

  + 遍历：

    ```rust
    for c in s.chars() { }
    for b in s.bytes() { b is 原始字节; }
    ```

### HashMap

+ 定义：`HashMap<K, V>`

  引入：`use std::collections::HashMap;`

+ 构造：

  ```rust
  let teams  = vec![String::from("Blue"), String::from("Yellow")];
  let initial_scores = vec![10, 50];
  
  let scores: HashMap<_, _> = teams.iter().zip(initial_scores.iter()).collect();
  ```

+ 读取：

  + 读取：

  + 遍历：

    ```rust
    for (key, value) in &hm { }
    ```

+ 更新：

  + 覆盖：插入`hm.insert()`

  + 修改：

    ```rust
    实例.entry(键).or_insert(值);
    ```

    + `entry`检索键是否则，无则插入、有则返回引用
    + `or_insert`对调用的键进行插入、返回引用



# 错误处理

Rust有两种错误：

+ recoverable可恢复错误：`Result<T, E>`

  ```rust
  use std::fs::File;
  enum Result<T, E> {
      Ok(T),
      Err(E),
  }
  let f = File::open("hello.txt");
  let f = match f {
  	Ok(file) => file,
      Err(error) => {
  		panic!("Problem opening the file: {:?}", error)
      },
  };
  ```

  + `match` 能够胜任它的工作，不过它可能有点冗长并且不总是能很好的表明其意图。`Result<T, E>` 类型定义了很多辅助方法来处理各种情况。其中之一叫做 `unwrap`，它的实现就类似于示例 9-4 中的 `match` 语句。如果 `Result` 值是成员 `Ok`，`unwrap` 会返回 `Ok` 中的值。如果 `Result` 是成员 `Err`，`unwrap` 会为我们调用 `panic!`

    ```rust
    let f = File::open("hello.txt").unwrap();
    ```

    对应着的

    ```rust
    let f = File::open("hello.txt").expect("Failed to open hello.txt");
    ```

  + propagating传播错误：使用 `?`运算符：向调用者返回错误得函数

    + 能链式调用
    + 可用作返回Result的函数

+ unrecoverable不可恢复错误：`panic!`宏

  + 默认：unwinding展开：当执行宏时，程序会打印出错误信息，并展开清理栈数据，然后退出
  + abort终止：在cargo.toml的`[overfile]`后添加`panic = 'abort'`

# 泛型generics

+ 定义泛型函数：

  ```rust
  fn function<T>(type: ...T...) -> ... {}
  ```

+ 使用泛型函数：直接传参，自动识别

+ 定义泛型结构体：

  ```rust
  struct struct_name<T> {
      ...: T,
      ...
  }
  let ... = struct_name { ...: 值, ...};
  ```

  + 可有多个类型参数

+ 定义枚举泛型：比如`Option<T>`和`Result<T, E>`

+ 方法定义中的泛型：

  针对一个泛型结构体`struct_name<T>`

  ```rust
  impl<T> struct_name<T> {
      
  }
  ```

  + 为泛型构建具体类型

    ```rust
    impl struct_name<type> {
        
    }
    ```

---

+ 效率问题：Rust通过monomorphization单态化保证效率：通过填充编译时使用的具体类型，将通用单拉转换成特定代码的过程。这样没有运行时的开销。

## trait

> 类似其他语言的interfaces接口

+ 定义trait

  ```rust
  trait trait_name {
      fn f1(&self...) -> ...;
      
  }
  ```

+ 为类实现trait

  ```rust
  struct struct_name {
      field;
  }
  
  impl trait_name for struct_name {
      
  }
  ```

+ coherence相干性/orphan rule孤儿规则：只有当trait或者要实现trait的类型位于crate的本地作用域时才是为该类型实现trait。相反不能为外部类型实现外部trait。

+ 默认实现：在trait定义中实现方法
  + 对类型使用默认实现，则实现大括号为空，当然也可以部分实现

+ 把trait作为参数：参数列表中`name: impl trait名字`：该参数支持任何实现了指定trait的类型

  + Trait Bound语法：一种语法糖，对于上面的用法，如果有多个参数是trait，一方面太过冗长，另一方面这其实意味着其实这多个参数的实际传入实参的类型可以不同（好像不可以）：

    ```rust
    fn f<T: t_name>(参数: T...) ... {}  // 没有impl
    ```

  + 通过`+`指定多个trait

    ```rust
    fn f(arg1: impl t_name1 + t_name2)...
    ```

    + 当然也适用于Trait Bound

  + 使用where来简化trait bound

    ```rust
    fn some_function<T: Display + Clone, U: Clone + Debug>(t: T, u: U) -> i32 {
    
    fn some_function<T, U>(t: T, u: U) -> i32
        where T: Display + Clone,
              U: Clone + Debug
    {
        
    }
    ```

+ 返回实现trait类型：

  ```rust
  fn f(...) -> impl t_name {
      
  }
  ```

## 生命周期lifetime

+ 实现：borrow checker借用检查器

# 函数式编程

## 闭包closures

+ 定义：保存进变量或者作为参数传递给其他函数的匿名函数

+ 语法：

  ```rust
  let 闭包名字 = |参数列表（逗号分割）| {
      闭包体
  }  // 如果只有一行则这个大括号可以省略
  可以像调用函数一样调用闭包
  ```

  + 类型：通常可以通过上下文推断，也可以显式定义
    + 闭包不是泛型，虽然类型可以通过推断，但是是不可变的

  + 泛型闭包和`Fn`trait

## 迭代器iterator

迭代器是lazy惰性的

+ 构造：

+ Iterator trait

  ```rust
  pub trait Iterator {
      type Item;
      
      fn next(&mut self) -> Option<Self::Item>;
  }
  ```

  + `type`定义associated type关联类型

+ `next`

  + consume消费：在迭代器上调用`next`方法改变迭代器状态

  + consuming adaptors消费适配器：调用`next`方法的方法

    ```rust
    v.iter().map(|x| x + 1).collect();
    ```

  + iterator adaptors迭代器适配器：允许我们将当前迭代器变为不同类型的迭代器，可链式调用多个迭代器适配器

    ```rust
    v.iter().filter(|x| x == 1).collect();
    ```

+ 性能：


# 智能指针

> Rust中指针和引用的区别
>
> 引用：只借用数据的指针
>
> 指针：拥有它们指向的数据

## bos

`Box<T>`

+ box允许将一个值放在堆上而不是栈上：本身在栈中，其指向的数据在堆中

  > Rust的特性导致在栈上的大量的拷贝是相当耗时的，在堆上的反而很快



## Deref

## Drop

## Rc引用计数智能指针

## RefCell

# 模式匹配

