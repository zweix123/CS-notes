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

算法库要求的迭代器类型：通过功能的多寡划分层次—高级类型支持底层类型所有操作![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/迭代器类别.jpg)

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

+  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/C++/特定容器算法.jpg)





## 随机数

包括随机数引擎类和适配器以及分布模板

