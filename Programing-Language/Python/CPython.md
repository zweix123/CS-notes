[CPython](https://github.com/python/cpython)是Python的官方解释器。
+ Cython是Python的扩展语言，可将其代码直接编译成本地机器码

+ Python的运行流程
	1. 解释成bytecode字节码（`.pyc`文件）
		+ 查看字节码`dis`：
			```python
			import dis
			dis.dis("Python代码字符串")
			```
	1. 将字节码放到由C实现的虚拟机PVM上去解释运行

	>对比Java：
	>+ Java在解释运行前已经编译了，而Python确实也是运行前编译，也没有重复编译，但是会检测编译好的pyc是否过期
	>+ JVM会有JIT, Just-In-Time Compilation即时编译，将HotSpot热点代码编译成本地机器码
	>	>lua也有这玩意，而且优化的很不错，按理说Python也应该有

#### 不同list构造方式的大小
```python
>>sys.getsizeof([0] * 3), sys.getsizeof([0, 0, 0]), sys.getsizeof([0 for _ in range(3)])
(80, 88, 88)

>>dis("[0] * 3")
...
BINARY_MULTIPLY  
# -..-> list_repeat(): size = len(list) * n -> list_new_prealloc(size) -> PyMem_New(size): 需要多少size，就用多少size: 
# sys.getsizeof(list()) -> 56
# 64位操作系统，一个指针8 byte
# 56 + 8 * 3 = 80
...

>>dis("[0, 0, 0]")
...
LIST_EXTEND  # list_extend -> list_resize(len(list) + n)     # resize需要长度
...

>>dis("[0 for _ in range(3)]")
...
LIST_APPEND  # list_append -> app1(): n + 1 -> list_resize() # 多次resize n + 1
...
```

+ resize
	+ 挑战
		+ 内存随便
		+ 使用C中的malloc，使用一个system call，慢

		所以都是有优化算法

	+ list_resize()：比较复杂

对于上面的问题，可以理解为
+ list_resize(大) -> 更大
+ list_resize(不是那么大) -> 后续足够，不再更新

### 为什么None一定要用is
>`is`对应`is not`而不是`not` 

为什么判断一个名称是不是None一定要用`is`？

+ `if sam: ...`：None -> False, but `[]` -> False, `{}` -> False, `set()` -> False, `__bool__`可以被重载
+ `if sam == None`：`__eq__`可以被重载

+ 进一步：
	+ `==`：`compare_op`：比较使用`PyObject_RichCompare`，复杂，慢
	+ `is`：`is_op`：直接比较指针地址

### 什么可以作为dict的key

+ dict中对于set一个pair，会检测key是否有hash
+ python的所有的object都继承自一个基类，它有hash function，实现就是该对象地址（Python是的id）
	+ 这里有个锅，一旦overload eq和hash中任何一个，子类都不会继承这个基类中的hash
	+ 这里还有一个锅，就是hashtable会先比较hash，再使用eq比较（因为可能hash碰撞）
	+ 这里再有一个锅，如果对于同一个对象（上面都是讨论内容相同的不同对象），就没hash啊eq的说法，一看hash指针是一样，就直接认为是一样的

### 判断一个key是否在dict中

### 列表推导式语法
```
In []: dis("g = (n for n in lst if n in lst)")
  1           0 LOAD_CONST               0 (<code object <genexpr> at 0x7f75b37a9b00, file "<dis>", line 1>)
              2 LOAD_CONST               1 ('<genexpr>')
              4 MAKE_FUNCTION            0
              6 LOAD_NAME                0 (lst)
              8 GET_ITER                                                         # 得到生成器对象并存储g
             10 CALL_FUNCTION            1
             12 STORE_NAME               1 (g)
             14 LOAD_CONST               2 (None)
             16 RETURN_VALUE

Disassembly of <code object <genexpr> at 0x7f75b37a9b00, file "<dis>", line 1>:  # code object，等式右边被看做一个函数
              0 GEN_START                0

  1           2 LOAD_FAST                0 (.0)
        >>    4 FOR_ITER                 9 (to 24)                               # 一个正儿八经的for loop，调用iter
              6 STORE_FAST               1 (n)                                   # 得到一个iterable并保存
              8 LOAD_FAST                1 (n)
             10 LOAD_GLOBAL              0 (lst)                                 # 复制全局名
             12 CONTAINS_OP              0                                       # 比较
             14 POP_JUMP_IF_FALSE        2 (to 4)
             16 LOAD_FAST                1 (n)
             18 YIELD_VALUE
             20 POP_TOP
             22 JUMP_ABSOLUTE            2 (to 4)
        >>   24 LOAD_CONST               0 (None)
             26 RETURN_VALUE
```
所以从这里定义g到真的next g之间，如果更改了lst的内容，在next的时候n会遍历构造时的list，然后去比较修改后的lst
