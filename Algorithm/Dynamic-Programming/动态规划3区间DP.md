# 区间DP

+ 模板题：石子合并：`n`堆石子，每堆石子个数`a[i]`，合并相邻两堆，代价为合并的石子个数，问合并为一堆的极值成本。

  + 状态表示：`f[i][j]`表示把`i`到`j`这一段石子合并的代价

    状态计算：
    $$
    \begin{aligned}
    f_{i, j} &= \mathop{min}\limits_{i \le k < j} f_{i, k} + f_{k + 1, j} + \mathop{\sum}\limits_{i \le k \le j} a[k] &i < j \hfill \\
    &= 0 \hfill  &i == j \hfill
    \end{aligned}
    $$

  + 复杂度：$O(n^3)$

  + 代码：

    + 迭代式：第一位循环长度，第二维循环左端点（右端点i + len - 1）

      ```c++
      //预处理前缀和pre
      memset(f, 0x3f, sizeof f); //此处以最小值为例
      for (int len = 1; len <= n; ++ len) {
      	for (int i = 1; i + len - 1 <= n; ++ i) {
              int j = i + len - 1;
              if (len == 1) f[i][j] = 0;
              else {
                  for (int k = i; k < j; ++ k) {
                      f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j] + pre[j] - pre[i - 1]);
      }}}}
      //f[1][n]
      ```

    + 记忆化搜索

## 环形化链

1. 在环中设置缺口然后进行处理$\rightarrow$**枚举缺口**：复杂度提高一维
2. 经典处理方法：将环拆开后复制一份接在后面：发现n的环上的区间都在2n的链上。

+ 例题：在石子合并的基础上说明n堆石子环形放置，首尾也算相邻

  ```c++
  for (int i = 1; i <= n; ++ i) a[i + n] = a[i];
  for (int i = 1; i <= n << 1; ++ i) pre[i] = pre[i - 1] + a[i];
  memset(f, 0x3f, sizeof f); //此处仍以最小值为例
  for (int len = 1; len <= n; ++ len) {
      for (int l = 1, r; l + len - 1 <= n << 1; ++ l) {  //注意此处的n*2
          r = l + len - 1;
  		if (len == 1) f[l][r] = 0;
          else {
  			for (int k = l; k < r; ++ k) f[l][r] = min(f[l][r], f[l][k] + f[k + 1][r] + pre[r] - pre[l - 1]);
          }}}
  int ans = 0x3f3f3f3f;
  for (int i = 1; i <= n; ++ i) ans = min(ans, f[i][i + n - 1]);
  ```

2. 能量项链（环形矩阵连乘）

   > 对于输入，`n`个矩阵，给出n个矩阵的行`a[i]`，则后一个的行是前一个的列，由于环性质，可以想象为一个环有点，一个段为一个矩阵

   ```c++
   //n, a[n];  //则每个矩阵是a[i] \times a[i + 1]
   for (int i = 1; i <= n; ++ i) a[i + n] = a[i];
   
   memset(f, 0x3f, sizeof f);  //同样以最小值为例
   for (int len = 2; len <= n + 1; ++ len) {  //这里有不同，因为两个位置合在一起是一个矩阵，所以选取个数为1是len = 2
       for (int i = 1, j; (j = i + len - 1) <= n << 1; ++ i) {
           if (len == 2) f[i][j] = 0;
           else {
   			for (int k = i + 1; k < j; ++ k) f[i][j] = min(f[i][j], f[i][k] + f[k][j] + a[i] * a[k] * a[j]);
           }}}
   // for() min
   ```

3. 凸多边形划分：对于给定的`n`条边的凸多边形，每个点有其权值`a[i]`，可以将其划分为**不重叠**的三角形，每个方案的值是所有三角形的三个顶点的权值之积的和，求最小。

   + 对于每个边，它的每个确定的三角形（选择除了边端点之外的边），都把凸多边形分割成了独立的两个小凸多边形

   + 实际上这种关系也可以出现在凸多边形内部的连线

   + 状态表示：`f[i][j]`表示点`i`和点`j`的连线作为一个三角形的边的方案

     ​					的最小值

     状态计算：$f_{i, j} = \mathop{min}\limits_{i < k < j} (f_{i, k} + f_{k, j} + a[i] * a[j] * a[k])$

   > 题目本来应该用高精度，但是__int128也能混过去

   ```c++
   for (int len = 3; len <= n; ++ len) {
   	for (int i = 1, j; i + len - 1 <= n; ++ i) {
   		j = i + len - 1;
   		f[i][j] = INF;   
   		for (int k = i + 1; k < j; ++ k) {
   			__int128 t = f[i][k] + f[k][j] + a[i] * a[j] * a[k];
   			if (f[i][j] > t) f[i][j] = t; 
   }}}
   //write(f[1][n]);
   ```

## 方案计数

+ 题目：对一个`n`个结点的二叉树，每个点有分数`w[i]`，对于每个子树的一个计算是`f(node) = w[node] + f(node) * f(node)`（规定`f(叶子) -> 1`），给该树的**中序遍历**，求最大的一种树形的分数以及其前序遍历（要求字典序最小）

  + 中序遍历*左根右*，所以枚举左右端点，可能的根就在其中
  + 路径还原：

  ```c++
  int n, a[N];
  
  int f[N][N];  //数组
  int g[N][N];  //区间i到j的最优值的方案的根，用于dfs
  
  for (int len = 1; len <= n; ++ len) {
      for (int i = 1, j; i + len - 1 <= n; ++ i) {
  		j = i + len - 1;
          if (len == 1) f[i][j] = a[i], g[i][j] = i;
          else {
              for (int k = i; k <= j; ++ k) {
  				int l = (k == i ? 1 : f[i][k - 1]);
                  int r = (k == j ? 1 : f[k + 1][j]);
                  int t = l * r + a[k];
                  if (t > f[i][j]) f[i][j] = t, g[i][j] = k;
  }}}}
  //f[1][n]
  
  //路径还原
  void dfs(int l, int r) {
      if (l > r) return ;
      int mid = g[l][r];
      cout << mid << " ";  //根
      dfs(l, mid - 1);   //左
      dfs(mid + 1, r);   //右
  }
  //dfs(1, n)
  ```

## 二维区间DP

+ 例题：$8 \times 8$的棋盘，每个格子有分`val[i][j]`，可切`n`刀（对于切完的两部分**只能**选择一部分继续进行）求方案使各小棋盘的总分的**均方差**最小。其中方差和均方差单调，所以式中计算和转移的是方差

  + 状态表示：`f[k][x1][y1][x2][y2]`：表示区间。。。在切`k`刀的方案的最优值，
  
    状态计算：在小区间中横切+数切
	
  
  + 这里采用记忆化搜索的方法，动态规划就是记忆化搜索

  ```c++
  int n, m = 8;  //n为切的刀数，m为矩阵大小
  int pre[N][N];
  double X;  //均值
  
  double f[N][N][N][N][N];  //dp数组，也是记忆化搜索的数组，初始化为-1表示未被搜索
  
  void init() {
      memset(f, -1, sizeof f);
      for (int i = 1; i <= m; ++ i) for (int j = 1; j <= m; ++ j) {
          read(pre[i][j]);  //input
          pre[i][j] = pre[i - 1][j] + pre[i][j - 1] - pre[i - 1][j - 1];  //二维前缀和
      }
      X = 1.0 * pre[m][m] / n;  //全局的均值其实是统一的
  }
  double get(int x1, int y1, int x2, int y2) {  //求一个小块的方差，幸好方差各个部分独立，并且此问题均值全局
  	double val = pre[x2][y2] - pre[x1 - 1][y2] - pre[x2][y1 - 1] + pre[x1 - 1][y1 - 1];
      return (val - X) * (val - X);
  }
  double dfs(int k, int x1, int y1, int x2, int y2) {
      if (f[k][x1][y1][x2][y2] >= 0) return f[k][x1][y1][x2][y2];
      if (k == n) return f[k][x1][y1][x2][y2] = get(x1, y1, x2, y2);
      
      double res = INF;
      
      for (int i = x1; i < x2; ++ i) {
          res = min(res, dfs(k + 1, x1, y1, i, y2) + get(i + 1, y1, x2, y2));  //横着切，再切上半部分
          res = min(res, dfs(k + 1, i + 1, y1, x2, y2) + get(x1, y1, i, y2));  //横着切，再切下半部分
      }
      for (int i = y1; i < y2; ++ i) {
          res = min(res, dfs(k + 1, x1, y1, x2, i) + get(x1, i + 1, x2, y2));  //竖着切，再切左半部分
          res = min(res, dfs(k + 1, x1, i + 1, x2, y2) + get(x1, y1, x2, i));  //竖着切，再切右半部分
      }
     	return f[k][x1][y1][x2][y2] = res;
  }
  //sqrt(dfs(1, 1, 1, m, m) / n)
  ```
