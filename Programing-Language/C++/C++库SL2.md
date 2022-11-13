# tuple

> 将一些数据合成单一对象，但是不想麻烦定义一个新数据结构来表示，tuple很好用

可以有任意数量的成员，

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/tuple.png)

+ 定义和初始化：
  + tuple的构造函数是explicit的
    + `make_tuple`
+ 访问成员：`std::get<第几个>(一个tuple对象)`，索引从0开始
+ 辅助类模板：
  + tuple数量：`tuple_size<decltype(一个tuple对象)>::value`（`size_t`）
  + 对应位置元素类型：`tuple_element<第几个, decltpe(一个tuple对象)>::type`
+ 运算：要求对每个元素使用对应运算符必须是合法的
  + 相等：只有相同数量才比较

# bitset

+ 初始化：

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/bitset初始化.png)

+ 操作：

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Programing-Language/C++/bitset操作.png)



# 正则表达式

`<regex>`





# 随机数

