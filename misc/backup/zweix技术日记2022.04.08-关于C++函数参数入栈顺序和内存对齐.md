# 起因

> 引论：在调试程序时常需输出中间变量，于是想做一个小函数做工具

+ 需求：不定参数的输出

1. 首先想到的是C++11的`initializer_list`

   ```cpp
   template<typename T>
   void debug(const initializer_list<T>& vec)
   	{cout << "[ "; for_each(vec.begin(), vec.end(), [](T v){ cout << v << " "; }); cout << "]"; }
   ```

   + 调用：`debug({var1, var2, var3 ...});`

   这个大括号让我感觉调用方式不自然，于是考虑其他方法。

2. 想到C的`...`：查到`<stdarg.h>`，但被`_INTSIZEOF`劝退，但意识到它就是通过函数参数入栈时是连续的：

   ```cpp
   template<typename T>
   void debug(T n, ...) {
       for (T *i = &n + 1; i <= &n + n; ++ i) cout << " ["[i == &n + 1] << *i << ",]"[i == &n + n];
   	puts("");
   }
   ```

   原理：参数连续入栈，其地址是连续的，其中第一个参数的位置知道，同时其存储不定参数的数量

   + 局限：泛型变量只能是整型变量

+ 这个时候出现问题：在调用时`debug(5, 1, 2, 3, 4, 5);`的输出结果竟然是`0 1 0 2 0`。

  似乎跳两次才能到每个位置：

  ```cpp
  template<typename T>
  void debug(T n, ...) {
      for (T *i = &n + 2; i <= &n + 2 * n; i += 2)
          cout << " ["[i == &n + 2] << *i << ",]"[i == &n + 2 * n];
     	cout << endl;
  }
  ```

  结果确实是对的，但是为什么呢？

-----

# 原因

+ 在栈中，变量的地址并不是“连续”的，存在**内存对齐**，比如我使用的x64位的计算机，一次可读取8个字节，这个时候，如果连续存储，可能出现一个int（4位），不够我读，一个char（1位）后的long long（8位），可能需要读两次再舍掉一部分，于是干脆一个变量以一次所能读取的字节数划分，速度更快

  > 大概还有硬件相关的计组知识，这个我不懂

+ 所以解决方案就是每次跳要跳到下一个“内存块”

+ 那么问题就变成了如何计算这“一跳”的大小：

  如果存储当前变量需要的大小是`n`，内存块的单位是`d`（此处是8，这样是为了扩展题目），则求出一个数`x`

  1. $n \le x$
  2. $d \mid x$（$存在整数k，使得x = k \times d$）

1. 其实暴力是好写的：`int get(int n, int d) { for (int ans = n; ; ++ n) if (ans % d == 0) return ans; }`

这个时候再看`<stdarg.h>`这个库

## stdarg.h

### C预处理

+ C Preprocessor预处理器：本质——**文本替代**

  + ege：`#define #include #undef #ifndef #if #else #elif #endif #error # pragram`

+ 宏：由`#define`定义的：`#define 宏名(参数列表) 宏体`：其中参数列表可选

  + 对于带参数的宏：如何理解参数？

    > 如果学过编译原理一定熟悉token，这里更狭义一点，至**标记**，可以理解为名称

    这个==参数是“标记类型”的变量==：传入的是一个标记，参数是这个标记的别名，

    1. 直接用：在预处理时用传入的标记代替参数这个别名
    2. `#参数`：将传入的**标记**转换为**字符串**
    3. `##参数`：将参数中存储的标记（传入的标记）它所指向的**内容**变成**标记**：

    ```cpp
    #define hs1(n) ..n..
    #define hs2(n) ..#n..
    #define hs3(n) ..##n..
    
    int a = 1
    hs1(a); //..a..;
    hs2(a); //.."a"..;
    hs3(a); //..1..;
    ```

    + 3只能作为标记——名称，不能直接嵌入源代码

  + 多行：

    ```cpp
    #define f do{\
    \
    }while(0);
    ```

    + 每行都用`\`，不能有空行，不能有注释

  + 其他宏：`DATA TIME FILE LINE STDC`：STDC指代码是否是ANSI标准

### 正题

+ 攻坚克难：`#define _INTSIZEOF(n) ( (sizeof(n) + sizeof(int) - 1) & ~(sizeof(int) - 1) )`

> 我们需要几个辅助函数：获得一个变量的机器码和该机器码的补码
>
> + v1：只能处理整数：
>
>   ```cpp
>   template<typename T>
>   string vr(T x) {  //将T类型的x转换为其机器码
>       string res = "";
>       for (unsigned int i = sizeof(T) * 8 - 1; i > 0; -- i)
>           res += (x >> i) & 1 ? "1" : "0"; res += x & 1 ? "1" : "0";
>       /*
>       * 这里有两点
>       * 1. res在末尾加上新的字符，采取逆序，这样更低的位加在字符的末尾
>       * 2. sizeof返回值是unsigned int的，所以i也是unsigned int 的
>       *    但是无符号类型只能是正数，虽然最后要迭代到0，但是想退出必须要减至负数
>            而无符号类型不能，在整数环中又变成最大整数，这样就死循环了。
>       */ 
>       return res;
>   }
>   template<typename T>
>   
>   string fj(T x) {  //原码补码转换
>       string res = vr(x);
>       /*
>       * 1. 模拟原码和补码的转换过程——取反加一
>       * 2. 观察发现从后往前的第一个1之后的全部取反
>       */
>       int op = 0;
>       for_each(res.rbegin(), res.rend(), 
>           [&](char &c) {c ^= op; op = op == 1 || c == '1' ? 1 : 0; } );
>       /*
>       * + 利用for_each遍历string，利用反向迭代器实现逆序遍历
>       * + lambda表达式中如果op遇到了1或者自己本来是1就是1，否则是0
>       * + 遍历的char和op取反：注意0的ASCII码是48， 1是49，可以通过对1取反互相转换
>       * + 如果没有遇到1，op就是0，取反0则char不变，之后就取反
>       */
>       return res;
>   }
>   ```
>
> + v2：任何内置类型：
>
>   ```cpp
>   template<typename T>
>   string vr(T x) {
>       string res = "";
>       unsigned long long xx = ((unsigned long long *)(&x))[0];
>       for (unsigned int i = sizeof(T) * 8 - 1; i > 0; -- i)
>           res += (xx >> i) & 1 ? "1" : "0"; res += xx & 1 ? "1" : "0";
>       return res;
>   }
>   template<typename T>
>   string fj(T x) {
>       return vr(~(x - 1));
>   }
>   ```
>
>   + 补码只用于定点数

+ 现在可以观察一下这个宏有什么特点了：

  ```cpp
  #define _INTSIZEOF(n) ( (sizeof(n) + sizeof(int) - 1) & ~(sizeof(int) - 1) )
  #define ffjx(n) do{ \
      printf(#n " sizeof : %d\n", sizeof(n)); \
      cout << vr(sizeof(n)) << endl; \
      printf(#n " sizeof(int) - 1 : %d\n", sizeof(int) - 1); \
      cout << vr(sizeof(int) - 1) << endl; \
      cout << vr((sizeof(n) + sizeof(int) - 1)) << endl; \
      printf(#n " ~(sizeof(int) - 1) : %d\n", ~(sizeof(int) - 1)); \
      cout << vr(~(sizeof(int) - 1)) << endl; \
      printf(#n " _INTSIZEOF(n) %d\n", _INTSIZEOF(n)); \
      cout << vr(_INTSIZEOF(n)) << endl; \
      cout << endl; \
  } while(0)
  ```

  输入一个数发现结果就是这个数的”下一跳“大小

  则`int get(int n, int d) { return (n + d - 1) & ~(d - 1); }`

+ 解释：

  1. 观察d：

     > 一个二进制取补具有这样的特性：以最低位1为界，其左全部取反，其右保持不变

     + `~(d - 1)`：得到一个以最低位1为界，左边较于d全部取反，而右边不变——全是0
     + `d - 1`：得到一个以最低位1位界，左边不变，1变0，右边全是1（因为-1借位了）

     |      | 1    | 2    | 3    |
     | ---- | ---- | ---- | ---- |
     | 1    | 原码 | 0    | 全1  |
     | 2    | 反码 | 1    | 全0  |

  2. 此时从公式看最终结果

     | 1                                     | 2    | 3                    |
     | ------------------------------------- | ---- | -------------------- |
     | n的这部分一定会被保留（1和2相互补充） |      | 一定全0（(2, 3)全0） |

     + 这保证了一定是d的倍数
     + 那怎么保证一定比n大呢？其实这是显然的：低位1一定会进位上去，高位1被保留

     > 其实还有一个问题，怎么保证这是符合标准的最小的
     >
     > 1. 如果n在低位（3部分）有1，定义会被进位到2部分，并且只进一个（其他的不会满足进位）—d最低位1下没有且大于n
     > 2. 然后不会了

+ 现在看看其他部分：==不对，这部分源码不对，源码依然看不懂==|==stdarg中还有更深的东西，没办法手写，只能用他这库==

  ```cpp
  typedef char * va_list;
  #define va_start(ap,v) ( ap = (va_list)&v + _INTSIZEOF(v)  )
  #define va_arg(ap,t) ( *(t *)((ap += _INTSIZEOF(t)) - _INTSIZEOF(t))  )
  #define va_end(ap) ( ap = (va_list)0 )
  ```

  0. `va_list`：不要看它是`char *`觉得它的是字符串，其实是因为char是一个字节，所以可以把它看成一系列的字节

  1. `va_start`：其中ap应该就是`va_list`类型的，v是当前的值

  2. `va_arg`：

     1. 首先是它修改了`ap`：`ap`到了下一跳
     2. `+=`返回修改后的值，再减去这一跳的距离，就得到了跳之前的地址

     所以这个是取出当前`va_list`当前的地址的值，并且迭代到下一个位置

  3. `va_end`：清楚va_end

+ 现在可以完善我们的代码了：

  ```cpp
  template<typename T>
  void debug(T x, ...) {
  	int n = x;
  	va_list ap;
  	va_start(ap, x);
  	while (n -- ) std::cout << va_arg(ap, T) << " ";
  }
  ```

# 其他方法

所以我最开始的问题还是没有解决

1. ```cpp
   template<typename T>
   class debug {
   public :
   	debug(const std::initializer_list<T>& t) {
   		for (auto ite = t.begin(); ite != t.end(); ++ ite) std::cout << *ite << " ";
   	}
   };
   
   debug<int>{1, 2, 3};
   ```

2. ```cpp
   template<typename T>
   std::ostream& operator << (std::ostream& out, const std::initializer_list<T>& t) {
   		for (auto ite = t.begin(); ite != t.end(); ++ ite) out << *ite << " ";
       	return out << "\n";
   }
   
   operator<<(cout, {1, 2, 3});
   ```

不都是太满意

# 一波又起

有这样的函数：`inline int read() { int x; scanf("%d"; &x); return x; } `

有这样的调用：`debug(read(), read(), read());`

有这样的输入：`1 2 3`

有这样的输出：`3 2 1` ？！？！？！

+ 原理：

  > 栈是栈底是大地址，栈顶是小地址

  1. 函数的参数入栈是**从右到左**——左边后入，后入小地址，所以右边的地址数大于左边

----

但是这样是没法解释的

```cpp
const int N = 3;
struct point {
    char str[N];
}
void foo(point a, point b) {
    printf("%p\n%p\n", &a, &b);
}
int main() {
    foo(point(), point());
}
```

+ 随着N的变化，地址变化不对。无论是相对位置还是大小
