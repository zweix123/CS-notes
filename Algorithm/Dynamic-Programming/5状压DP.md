# 状态压缩DP

## 棋盘式

> 又叫**基于连通性**的DP

0. 基本模型：在一个$N \times M$的棋盘上放$1 \times 2$的方块，问放满的方案数：

   1. 一个合法的方案分为横放和竖放，则方案数为横放方案数

   2. 状态表示：`f[第i列][第i-1列横放的二进制模式/第i列已经被占不能横放的二进制模式]`

      状态计算：`f[i][j] += f[i - 1][k]`：其中`k`是对`j`合法的位模式

   3. 状态起点：初始化为0，`f[0][0] = 1`

   4. 转移条件：

      1. `i`的`j`位模式不能和`i - 1`的`k`位模式不能有重合`j & k == 0`

      2. 在`i`列的`j`位模式（本列横放）和`k`位模式（i上列横放导致突出）之外的要满足可竖放：**连续位置为偶数**

         ```c++
         int pj(int bits) {
             int cnt = 0;  //计数：连续的0的个数 
             for (int i = 0; i < n; ++ i) {
         		if (bits >> i & 1) {  //如果是1，检测、清空
                     if (cnt & 1) return 0;  //如果是奇数
                 	cnt = 0;
                 } else ++ cnt;
             }
             if (cnt & 1) return 0;  //检测最后一段连续的0
             return 1;
         }
         ```


```c++
for (int j = 1; j <= m; ++ j) {
    for (int k = 0; k < 1 << n; ++ k) {
        f[j][k] = 0;
        for (int k_ = 0; k_ < 1 << n; ++ k_) {
            if (k & k_ || ! pj(k | k_)) continue;  //如果有重叠或者并在一起在本行的空位不能竖着用
			f[j][k] += f[j - 1][k_];
}}}
```

   5. 答案：`f[m][0]`：最后一列没有横放的

   + 不能像下面那样离线的处理，因为可能两个对竖着放不合法的位模式并起来就是合法的

+ 练习：

  + 在`n * n`的棋盘放置`k`个国王，国王周围8个位置不能放置，问有多少摆放方案

    `f[i][j][k]`：前`i`行共用`j`个国王并且第`i`行摆放的二进制模式为`k`的方案数

    起始：`f[0][0][0] = 1`；递推：`f[i][j][k] += f[i - 1][j - count(k)][合法的方案位模式]`

    + 合法位模式：

      1. 对本行：两两1之间不能相邻
      2. 对邻行：**在满足本行的情况下**，不能重叠，并且两行位模式符合情况1

      ```c++
      int pj(int bit) {
          for (int i = 1; i < n; ++ i) if ((bit >> i & 1) & (bit >> (i - 1) & 1)) return 0;
          return 1;
      }
      vector<int> state;  //合法状态
      vector<int> head[M];  //状态bit的合法相邻状态邻接表head[bit];
      
      for (int i = 0; i < 1 << n; ++ i) if (pj(i)) state.push_back(i);
      
      for (auto &a : state) {
      	for (auto &b : state) {
      		if (a & b) continue;
      		if (pj(a | b)) head[a].push_back(b);
      	}
      }
      ```

    + 小技巧：`i`从1循环到n + 1，然后答案为`f[n + 1][k][0]`：n + 1行花费全部的国王，并且n + 1行一个没有摆的方案数

    ```c++
    for (int i = 1; i <= n + 1; ++ i) {
    	for (int j = 0; j <= k; ++ j) {
    		for (auto &a : state) {  //当前层合法状态
    			for (auto &b : head[a]) {  //上一层合法并且和这一层也合法的状态 
    				int c = cnt[a];  //cnt[a]表示位模式a中1的个数，可以预处理
                    if (j >= c) f[i][j][a] += f[i - 1][j - c][b];
    }}}}
    ```

    + 这里的检测一行有无相邻还有一个方法：`int pj(int x) { return !(x & x >> 1); }`优美，而且扩展到相邻两位

  + 在`n * m`的G上，种玉米，玉米之间不能相邻（较于上题的井字，此是十字），玉米数目没有限制，但有些土地不能种玉米，求方案数。

    绝大部分和上一题类似，同行的情况不能相邻，相邻行的情况不能有重叠，还有一个，本行的种植情况要和是土地情况的子集（正难则反：本行的种植情况不能和土地情况的补集）

    另外就是套路中的离线处理，范围for使之就像维护集合本身，我们发现一行的所有集合情况有很多是空的，而操作的都只有合法的集合情况；在state中集合情况和索引一一对应，则可以计算的时候是比较集合（state值），但是在数组下标中使用集合的索引也可以（大概能省一些空间）

    下面使用索引来算：

    ```c++
    for (int i = 0; i < 1 << m; ++ i) if (pj(i)) state[i].push_back(i);
    for (int i = 0; i < state.size(); ++ i) {
        for (int j = 0; j < state.size(); ++ j) if ((state[i] & state[j]) == 0) {
            head[i].push_back(j);
        }
    }
    for (int i = 1; i <= n + 1; ++ i) {
        for (int j = 0; j < state.size(); ++ j) {
            if (state[j] & bits[i]) continue;  //bits[i]表示i行中不可以中的位模式
            for (auto &k : head[j]) 
                f[i][j] += f[i - 1][k];
        }
    }
    //f[n + 1][0];
    ```

  + 在`n * m`的地区安置炮兵，地图有山地和平原，只能在平原上放置炮兵，炮兵的攻击方位为“大十字”，十字的每个尖两个个（共2 * 4 + 1个方格），炮兵之前不能相互攻击，问最多能放多少

    在上面的基础上要维护两行：`f[i][j][k]`：表示在第`i`行，炮兵放置位模式为`j`，`i - 1`行的位模式为`k`的集合，其中的值是放置数量的最大值。另外空间会炸，所以要滚动数组。

    + 同一行两个1之前要空2个以上0

      ```c++
      int pj(int x) { return !((x & x >> 1) || (x & x >> 2)); }
      ```

    + `state`和`head[]`两个向量照常

    + core：

      ```c++
      for (int i = 1; i <= n; ++ i) {
      	for (auto &a : state) {
      		if (a & bits[i]) continue;  //考虑这行是否和地形冲突（之前的不同考虑，如果冲突转移过来是0）
      		for (auto &b : head[a]) {  //不和a冲突的b
      		for (auto &c : head[b]) {  //不会b冲突的c
      			if (a & c) continue;  //并且a和c也不冲突 
      			f[i&1][a][b] = max(f[i&1][a][b], f[i - 1&1][b][c] + cnt[a]); 
      }}}}
      //最后在最后一层的各个状态寻找最大值
      ```

    以上写法起始是一种比较优化的写法了，实际上找到不同行的关系的位运算表达式直接好几个for然后在里面判断也行

## 集合式

+ 本质是：搜索 $\rightarrow$ 记忆化搜索 $\rightarrow$ 形式转换为动态规划：在下面也能看到，推导时从状态转移变成递推了

0. 基本模型（Hamilton路径）：`n`个点的带权无向图，从起点`0`到终点`n - 1`的不重不漏的经过**所有点**的最短路径

   + 状态表示：

     + 集合：`f[i][j]`：表示从`0`到`j`，且经过的点的二进制表示为`i`的所有路径
     + 属性：最短路

     对于`i`这个路径的二进制表示：从低位起，对应位表示对应点，0表示没走过，1表示走过，`j`在这个位模式中，这个位模式表示路径上都有谁，但是先后顺序不定

   + 状态计算：对于`f[i][j]`，`i - (1 << j)`表示没有`j`的路径，然后在这个位模式中有各个点，看从这些点中到`j`的路径

     `f[i][j] = min(f[i][j], f[i - (1 << j)][k] + g[k][j])`（其中`i >> j & 1`并且`i >> k & 1`）

   ```c++
   memset(f, 0x3f, sizeof f);//最小值，初始化极大
   f[1][0] = 0;//起点
   for (int i = 0; i < 1 << n; ++ i) {  //所有路径方案
       for (int j = 0; j < n; ++ j) if (i >> j & 1) {//路径上有j
   		int ii = i - (1 << j);
           for (int k = 0; k < n; ++ k) if (ii >> k & 1) {//路径上除了j还有k
               f[i][j] = min(f[i][j], f[ii][k] + g[k][j]);
           }
       }
   }
   return f[(1 << n) - 1][n - 1];
   ```

1. 重复覆盖问题

   愤怒的小鸟，有`n`个pig，坐标为$(x_i, y_i)$，从$(0, 0)$发射，抛物线$y = a x^2 + b x + c$上的所有pig都被消灭，求最少的发射次数

   1. 两点唯一确定一条抛物线：$\begin{cases} y_1 = ax_1^2 + bx_1 \\ y_2 = ax_2^2 + bx_2 \end{cases} \Rightarrow \begin{cases} a = \frac{\frac{y_1}{x_1} - \frac{y_2}{x_2}}{x_1 - x_2} \\ b = \frac{y1}{x1} - ax_1\end{cases}$：$n^2$枚举两两点成线，再加上一层$n$枚举这个点能覆盖的点

      用`f[i][j]`：表示点`i`和点`j`形成的抛物线所有覆盖的点的二进制表示`state`

      ```c++
      for (int i = 0; i < n; ++ i) {
      	path[i][i] = 1 << i;
      	for (int j = 0; j < n; ++ j) {
      		double x1 = sam[i].x, y1 = sam[i].y,
      			   x2 = sam[j].x, y2 = sam[j].y;
      		if (! cmp(x1, x2)) continue;  //两个点不能在一条竖线上
      		double a = (y1/x1 - y2/x2) / (x1 - x2),
      			   b = y1/x1 - a * x1;
      		if (cmp(a, 0) >= 0) continue;  //a不能大于等于0
      		for (int k = 0; k < n; ++ k) {
      			double x = sam[k].x, y = sam[k].y;
      			if (cmp(y, a * x * x + b * x) == 0) path[i][j] |= 1 << k;
      		}
      	}
      }
      ```

   2. 然后`f[i]`：表示被击中的的pig的二进制模式的`i`的最少小鸟数

      从小到大枚举状态，找到一个位模式中没有被击中的pig，然后分别用这个pig和其他的pig连成的抛物线去扩充循环的状态，然后从已有的状态推导的这个新的状态的最优值

      ```c++
      memset(f, 0x3f, sizeof f);
      f[0] = 0;
      for (int a = 0; a + 1 < 1 << n; ++ a) {
      	int t = -1;
      	for (int i = 0; i < n; ++ i) {
      		if (!(a >> i & 1)) {
      			t = i;
      			break;
      		}
      	}//找到一个就可以，因为这不是状态转移，而是递推，状态从小到大枚举，并且找到第一个0保证递推是从小到大的
      	for (int i = 0; i < n; ++ i) {
      		int b = path[t][i] | a;
      		f[b] = min(f[b], f[a] + 1);
      	}
      }
      //f[(1 << n) - 1];
      ```

2. 某种最优生成树：对于一个图生成这样的最优生成树，每个边的权花销是边的长度和这个边“下面”的点的深度（起点深度为1）的积，要求找到总花销最小的。

   > 这个题目要开long long，但是下面的代码没有

   + `f[s][j]`：表示生成的树的结点的位模式的`s`，且树的深度是`j`的集合，值是这个集合的最小花费

     `f[s][j] = min{f[s0][j - 1] + j * cost}`：其中s0是s的真子集，cost是多的边权

     > 有问题，因为这里默认所有的新边都是从上一层来的，万一有的边是从中间的结点来的呢？这时j * cost中j对这部分就多了
     >
     > 不会，递推过程中被覆盖的了，从中间结点已经被推过了，此时有部分就是来自那，再从哪里算不会更优。

   + 预处理：

     ```c++
     memset(g, 0x3f, sizeof g);
     for (int i = 1; i <= n; ++ i) g[i][i] = 0;
     for (int a = 1; a < 1 << n; ++ a) {
         for (int i = 0; i < n; ++ i) if (a >> i & 1) {  //在这个集合中的点
             for (int j = 0; j < n; ++ j) if (g[i][j] != INF) {  //从这个点开始扩展
                 state[a] |= 1 << j;  //就和集合中的点有关的点放进去
             }
         }
     }
     //state[]中是每个状态所有扩展到的最大状态
     ```

   + 获得从一个状态到另一个状态的cost

     ```c++
     int get_cost(int now, int pre) {
         if ((state[pre] & now) != now) return -1;  //如果pre扩展不到now，就剪纸
         int buji = now ^ pre;
         int res = 0;
         for (int i = 0; i < n; ++ i) if (buji >> i & 1) {  //枚举在now中而不在pre中的点
             int tmp = INF;
             for (int j = 0; j < n; ++ j) if (pre >> j & 1) {  //找这些点到pre中的最小值
                 tmp = min(tmp, g[j][i]);
             }
             res += tmp;
         }
         return res;
     }
     ```

   + dp：

     ```c++
     memset(f, 0x3f, sizeof f);
     for (int i = 0; i < n; ++ i) f[1 << i][0] = 0;  //起点花销为0
     
     for (int a = 1; a < 1 << n; ++ a) {  //0是空，预处理了
         for (int b = a - 1 & a; b; b = b - 1 & a) {  //枚举真子集
             int cost = get_cost(a, b);
             if (cost == -1) continue;
             for (int k = 1; k < n; ++ k)
                 f[a][k] = min(f[a][k], f[b][k - 1] + cost * k);  //递推式其实不懂，因为起点也算了深度但是这没
         }
     }
     
     //min{f[(1 << n) - 1][]}
     ```

+ 并行课程2：[LC](https://leetcode.cn/problems/parallel-courses-ii/description/)：TODO
