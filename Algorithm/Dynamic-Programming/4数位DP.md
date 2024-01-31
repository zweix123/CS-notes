# 数位DP

+ 特征：询问大区间$[X, Y]$内具有某个性质的数的个数：大区间不易枚举

+ 技巧：定义`int dp(int n)`表示区间$[0, n]$内具有某个性质的数的个数，则答案为$[X, Y] \Rightarrow dp(Y) - dp(X - 1)$

+ 套路：问题转化为枚举不大于`dp`函数的参数`n`的数的个数，可将其拆分为：$(a_{n - 1}, a_{n - 2}, ..., a_{1}, a_{0})$，从高位开始考虑：如果高位取小于当前位的数，则更低位可取进制内的所有数；如果取当前位，则更高位确定，考虑更低位；如果取大于当前位，不可能。

  故数位DP的计算空间类似一个二叉树：

  ```mermaid
  graph TB; 
  	root(( ));
  	n_1l["0~a_{n - 1} - 1"]; n_1r["a_{n - 1}"]; root --> n_1l; root --> n_1r;
  	n_2l["0~a_{n - 2} - 1"]; n_2r["a_{n - 2}"]; n_1r --> n_2l; n_1r --> n_2r;
  	n_mid["a_{2}"]; n_2r -..-> n_mid;
  	1l["0~a_{1} - 1"]; 1r["a_{1}"]; n_mid --> 1l; n_mid --> 1r;
  	0l["0~a_{0} - 1"]; 0r["a_{0}"]; 1r --> 0l; 1r --> 0r;
  ```

+ 模板：

  ```c++
  const int N = 32 + 7;  //数位长度
  int f[N][N];           //计算左分支的f
  void init() {          //预处理f
      
  }
  
  int dp(int n) {
      if (!n) return ..;  //数字0能否被统计？
      
  	vector<int> nums;
  	for (; n; n /= ..) nums.push_back(n % ..);  //取出n的各个位，数组存储方式与数字表示方向相同
      int res = 0;  //记录答案
      int last = 0;  //记录高位右分支的某些信息
      for (int i = nums.size() - 1; i >= 0; -- i) {  //从高位开始
          int x = nums[i];
          if (x) {  //求左分支中数的个数  //如果是0那么没有左分支
  		
          }
      }
      return res;
  }
  
  int main() {
      init();
  	
      int l, r; while (cin >> l >> r); cout << dp(r) - dp(l - 1);
  
      return 0;
  }
  ```

## Problem

### 只含01且num[i] = 2

**题目**：求区间中这样的数的个数：转化为`B`进制下只有0和1，且`1`的个数为`K`

+ 分析：按当前位的大小：

  + 0：没有左分支，进入右分支$\rightarrow$继续迭代/如果是终点呢？即n本来的数字的计数
  + 1：有左分支
    + 当前位可以取0：`res += `$C_{之后的位的长度 \rightarrow i}^{K - last}$：在之后的位安置剩下的1
    + `last`：记录更高位1的数量$\rightarrow$`++ last;`$\rightarrow$进入右分支/如果`last > K`停止迭代
  + 大于1：有左分支
    + 当前位可以取0：如上
    + 当前位可以取1：`res += `$C_{之后的位的长度 \rightarrow i}^{K - last - 1}$：当前位消耗一个1（要求`K - last - 1 >= 0`）
    + 不能进入右分支，因为大于1的位对于更低位形成的数字是不合法的

  则辅助数组`f`为组合数：$C_a^b = C_{a - 1}^{b} + C_{a - 1}^{b - 1}$

```c++
void init() {
    for (int i = 0; i < N; ++ i) for (int j = 0; j <= i; ++ j) f[i][j] = f[i - 1][j] + f[i - 1][j - 1];
}
int dp(int n) {
    ...
    for (; n; n /= B) nums.push_back(n % B);
	for (...) {
        int x...
        if (x == 0) {
			if (!i && last == K) ++ res;
        }
        else if (x >= 1) {
            res += f[i][K - last];  //取0
            if (x == 1) {
				++ last; 
                if (last > K) break;
            } else {
                if (K - last - 1 >= 0) res += f[i][K - last - 1];
                break;
            }
        }
    }
}
```

### 不降数

**题目**：大区间中这样的数的个数：每位数字从左到右不下降

+ 分析：对于当前数位：

  + $0 \backsim a_{n - 1} - 1$：当前值不能小于`last`（last表示更高位末尾值（`if (x < last) break;`）），如何求低位的方案书

    + 状态表示：`f[i][j]`表示长度为`i`位，且最高位为`j`的数的个数
    + 状态转移：对于`f[i][j]`，来自`f[i - 1][k]`：其中`k >= j`

    `res += `$\sum f_{i + 1, j} \ (last \le j \and j < x)$

    ```c++
    void init() {
        for (int i = 1, j = 0; j <= 9; ++ j) f[i][j] = 1;
        for (int i = 2; i < N; ++ i) {
            for (int j = 0; j <= 9; ++ j) {
                for (int k = j; k <= 9; ++ k) {
                    f[i][j] += f[i - 1][k];
                }
            }
        }
    }
    ```

  + $a_{n - 1}$：

    + 如果`x < last`则n本身不可行
    + 否则`last = x`（相当于`last = max(last, x)`），进入右分支/如果到达右末结点，则n本身也符合

```c++
void init();  //如上

int dp(int n) {
    if (!n) return 1;
    ...
    for (...) {
        int x...;
        {
            for (int j = last; j < x; ++ j) res += f[i + 1][j];
		}
        {
            if (x < last) break;
            last = x;
        }
        if (!i) ++ res;
    }
}
```

### 邻位差至少2

**题目**：统计大区间内这样的数的个数，不含前导零且相邻两个数之间之差至少为2

+ 分析：

  + $0 \backsim a_{n - 1} - 1$：

    1. 往前：取的数要和`last`(last记录更高位的最末位的数字)符合条件
    2. 往后：固定最高位，总位数确定，符合条件的数的个数
       + 状态表示：`f[i][j]`：表示`i`位，最高位为`j`的数的集合，值为个数
       + 状态计算：$f_{i, j} = \sum f_{i - 1, k} \ (\left|{j - k}\right| \ge 2)$

    ```c++
    void init() {
    	for (int i = 1, j = 0; j <= 9; ++ j) f[i][j] = 1;
        for (int i = 2; i < N; ++ i) {
            for (int j = 0; j <= 9; ++ j) {
                for (int k = 0; k <= 9; ++ k) {
    				if (abs(j - k) >= 2) f[i][j] += f[i - 1][k];
                }}}}
    ```

  + $a_{n - 1}$：查看n本身的位，符合，更新last，进入右分支，否则break，如果可以到`!i`则n本身可以

```c++
int dp(int n) {
    if (n <= 0) return 0;
    ...;
    int last = -2;  //保证第一位可以
    for (...) {
        int x...;
        
        for (int j = (i == nums.size() - 1); j < x; ++ j) {  //如果在最高位，不能从0开始，那是前导零
                                                             //如果不是，因为有last，所有可以从0开始
            if (abs(j - last) >= 2) res += f[i][j];
        }
        if (abs(x - last) < 2) break;
        last = x;
        if (!i) ++ res;
    }
    //以上计算的都是和n一个位数的情况，
    //还要特判整体位数是小于n的情况
    for (int i = 1; i <= nums.size(); ++ i) for (int j = 1; j <= 9; ++ j) res += f[i][j];
    return res;
}
```

### 数位和%P=0

**题目**：统计大区间内这样的数的个数，各位数字之和对`P`取模为0

+ 分析：对于当前位：

  0. $0 \backsim a_{n - 1} - 1$：`(更高位的和 + 枚举的当前位j + 更低位的和) % P == 0`

     + 更高位：`last`：更高位的各位数字之和

     `j + 更低位的和 == (-last) % P`$\rightarrow$代码中枚举当前为的`j`，所以下面的k

     + 状态表示：`f[i][j][k]`：表示数位长度为`i`，最高位为`j`，且各位数字之和对P取模的结果为k的方案集合，其值为个数
     + 状态计算：$f_{i, j, k} = \sum f_{i - 1, j\_, (k - j) \% P}$

     ```c++
     int f[N][10][P_MAX];
     void init() {
         for (int i = 1, j = 0; j <= 9; ++ j) f[i][j][mod(j, P)] = 1;
         for (int i = 2; i < N; ++ i) {
             for (int j = 0; j <= 9; ++ j) {
                 for (int k = 0; k < P; ++ k) {
                     for (int j_ = 0; j_ <= 9; ++ j_) {
                         f[i][j][k] += f[i - 1][j_][mod(k - j, P)];
                     }}}}}
     ```

  1. $a_{n - 1}$：更新last，进入右分支，叶子特判

```c++
int dp(int n) {
    ...;
    for (...) {
        int x...;
        for (int j = 0; j < x; ++ j) {
            res += f[i + 1][j][mod(-last, P)];
        }
		last += x;
        if (!i && last % P == 0) ++ res;
    }
    ...;
}
```

### 统计0~9出现次数

**问题**：累加大区间内所有的数位，统计0~9分别出现多少次（acwing338）
