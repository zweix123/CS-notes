STL(Standard Template Library)标准模板库



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

+ Iterator Category迭代器类型：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/迭代器类别2.jpg)

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

   ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/插入迭代器.jpg)

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

  + 操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/流迭代器.jpg)

+ move iterator移动迭代器

# Container容器

+ 头文件：`<容器名称>`，名称空间`std`，都是模板类

+ 常规方法：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/容器操作.jpg" style="zoom:120%;">

+ 容器赋值：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/容器赋值运算.jpg" style="zoom:80%;">
  + swap会改变迭代器或者索引或者指针

## Sequential顺序

> C++已经将其优化到几乎优秀于原始数据结构

+ 顺序容器(sequential container)：提供快速顺序访问元素

  <img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/顺序容器类型.jpg" style="zoom:120%;" />

  + | 容器类型                 | 随机访问 | 随机添加 | 首尾读写 |
    | ------------------------ | -------- | -------- | -------- |
    | `array`                  | 快       | 慢       |          |
    | `vector`                 |          |          |          |
    | `list`<br>`froward_list` | 慢       | 快       |          |
    | `deque`                  | 快       |          | 快       |

+ 添加：<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/顺序容器添加操作.jpg" style="zoom:120%;" />
  + `insert`和`push_back`参数是元素，`emplace`使用参数构造元素
  + 内存分配策略：只在迫不得已时才重新分配新的内存空间
  
+ 访问：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/顺序容器访问.jpg)

+ 删除元素：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/顺序容器删除.jpg)

  顺序容器大小操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/顺序容器大小操作.jpg)

  容器大小管理操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/容器大小管理操作.jpg)

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

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/forward_list的插入和删除.jpg)

  + off-the-beginning首前迭代器：返回不存在的第一个元素的前驱

### 容器适配器

+ adaptor适配器：接受一个容器，使其操作看起来像适配器

+ 所有容器适配器都支持的操作和类型：

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/所有容器适配器都支持的操作和类型.jpg)

+ 构造：两个构造函数：空和拷贝

  1. 第一个模板参数：元素类型

  2. 第二个模板参数：重载默认容器类型：

     > stack和queue是基于deque实现的，priority_queue是在vector之上实现的。

     + stack要求push_back、pop_back、和back：可用除array和forward_list之外的容器构造
     + queue要求back、push_back、front、和 push_front：构造于list或deque之上，但不能用vector构造
     + priority_queue处理上述还要随机访问能力：构造于vector或deque之上，但不能基于list

#### stack

+ 头文件`<stack>`

+ 操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/栈操作.jpg)


#### queue

+ 头文件`<queue>`

+ 操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/队列操作.jpg)


#### priority_queue

+ 头文件和操作见queue
+ **使用`<`运算符确定相对优先级**

## Associative关联

关联容器支持高效的关键字查找和访问

+ 分类：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/关联容器类型.jpg)
  +  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/关联容器的类型别名.jpg)
  + 迭代器：双向迭代器
    + map：`pair<const type, tpye>`
    + set：`const type`

+ 对于有序关联容器：要求定义元素比较方法（strict weak ordering严格弱序）

  + 默认使用`<`运算符——重载
  + 用来组织一个容器中元素的操作的类型也是该容器类型的一部身份：定义时指明：`set<Object, decltype(cmp)*> sam();`

+ 操作：

  + 添加：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/关联容器插入操作.jpg)

    + 不可重复的insert返回pair：first是位置的迭代器，second是bool

      可重复的不会插入失败，只返回bool

  + 删除：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/关联容器删除元素.jpg)
  + 查找：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/关联容器查找操作.jpg)
    + 可重复的中相同元素相邻

### set

### map

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/map中的下标操作.jpg)

### unoreder

+ unordered associative container无序关联容器：不使用比较运算符，使用hash function哈希函数和关键字类型的==运算符
+ 无序容器在存储上组织为一组桶，每个桶保存零个或多个元素，使用哈希函数将元素映射到桶——性能依赖于哈希函数的质量和桶的数量和大小
+ 管理操作：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/无序容器管理.jpg)

