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

