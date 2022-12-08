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

