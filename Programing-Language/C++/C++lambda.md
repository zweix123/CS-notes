# Lambda表达式

>  部分泛型算法需要除了对象之外的信息——谓词：
>
> > 形容谓词的几元即为参与运算的对象的个数
>
> Callable object可调用对象，重载了函数运算符的类的对象

+ 实质：编译器将Lambda表示翻译成一个未命名类的未命名对象
  + 其重载了函数调用运算符
  + 如果捕获方式是值捕获，则实际上该类为其创建数据成员和构造函数

+ 语法：`[capture list](parameter list) -> return type { function body; }`
  + capture list捕获列表：函数内部需要访问但是不作为传参的外部**局部**变量
  + paremeter list参数列表
    + 若无参数可省略括号
  + return type返回类型：
    + 若可推断可省略

# 捕获

 ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/lambda捕获列表.jpg)

+ 可变Lambfa：会改变被捕获的值：在参数列表首添加关键字**`mutable`**

