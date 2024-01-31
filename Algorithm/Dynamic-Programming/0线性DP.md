# 最长上升子序列LIS

> Longest Increasing Subsequence
>
> 最长下降或最长不下降同理

1. 暴力：$O(n^2)$：

   ```c++
   template<typename T>
   int LIS(int n, T h[]) {  // 索引从1开始
       vector<int> f(n + 1, 0);
       int res = 0;
       for (int i = 1; i <= n; ++ i) {
           f[i] = 1;
           for (int j = 1; j < i; ++ j) if (h[j] < h[i]) f[i] = max(f[i], f[j] + 1);
           res = max(res, f[i]);
       }
       return res;
   }
   ```

   + 最大上升子序列和问题：

     将转移方程变成`f[i] = max(f[i], f[j] + h[i]);`

2. 优化：$O(n \ log \ n)$

   `f[i]`表示长度为`i`的LIS的最后一个元素的值

   时序上从前往后遍历，对于新加入的元素，找到第一个大于等于新元素的位置，我们发现这个新元素代替这个位置的值会让结果更优。

   而这个找位置的过程可以二分优化，因为这个过程可以保证`f`单调

   结果即为`f`中有效值的个数

   ```c++
   template<typename T>
   int LIS(int n, T h[]) {  // 索引从1开始
       vector<int> f;
       for (int i = 1; i <= n; ++ i) {
           auto j = lower_bound(f.begin(), f.end(), h[i]);
           if (j == f.end()) f.push_back(h[i]);
           else *j = h[i];
       }
       return f.size();
   }
   ```

---

+ 定理：将一个序列分成最少的最长上升子序列的**数量**等于该序列最长下降子序列的**长度**


# 最长公共子序列LCS

> Longest Common Subsequence

+ 状态表示：`f[x1][x2]`表示从1到x1的第一个序列和从1到x2的第二个序列的LCS

+ 状态计算：

  + 边界：`f[1][1] = (a[1] == b[1])`

  `f[i][j] = max(f[i - 1][j - 1] + (a[i] == b[i]), f[i - 1][j], f[i][j - 1])`

+ $O(n^2)$

---

+ $O(n \ log \ n)$算法：

  在其中一个序列中统计每个字符出现的位置集合，得到一个键为字符，值为位置集合的map（每个位置集合从大到小排序），然后使用该map遍历另一个序列将每个**字符**替换成一个**数字**序列得到一个新的数字序列，并对该序列计算LIS即为最初两个序列的LCS长度。

  ```c++
  //一种写法
  vector<int> LCS_pre(vector<int> &a, vector<int> &b) {
  //	map<char, vector<int> > mp;
  //	for (char c = 'a'; c <= 'z'; ++ c) mp.insert({c, vector<int>()});
  	map<int, vector<int> > mp;
  	for (int i = 0; i <= 9; ++ i) mp.insert({i, vector<int>()});
  	for (int i = a.size(); i >= 0; -- i) mp[a[i]].push_back(i);
  	vector<int> res;
  	for (auto c : b) res.insert(res.end(), mp[c].begin(), mp[c].end());
      return res;
  }
  //LIS(LCS_pre(a, b));
  ```

# 最长公共上升子序列LCIS

> Longest Common Increasing Subsequence

`f[x1][x2]`表示第一个序列的前`x1`个字符和第二个序列的前`x2`个字符并以`b[x2]`结尾的LCIS

+ 暴力$O(n^3)$：

  ```c++
  for (int i = 1; i <= n; ++ i) {
      for (int j = 1; j <= n; ++ j) {
          f[i][j] = f[i - 1][j];
          if (a[i] == b[j]) {
              for (int k = 0; k < j; ++ k) if (b[j] > b[k]) f[i][j] = max(f[i][j], f[i - 1][k] + 1);
          }
      }
  }
  //for (int i = 0; i <= n; ++ i) ans = max(ans, f[n][i]);
  ```

+ 优化：我们观察上面的第三层循环，在一个`j`下是不断迭代的，则一个`i`循环下维护一个变量维护这个最大值

  下面的问题是每次都是和`b[j]`比较，怎么同一的，注意这里的`b[j]`的前面的条件是`a[i] == b[j]`，所以和`a[i]`比较即可

  ```c++
  for (int i = 1; i <= n; ++ i) {
      int maxn = 1;
      for (int j  =1; j <= n; ++ j) {
          f[i][j] = f[i - 1][j];
          if (a[i] == b[j]) f[i][j] = max(f[i][j], maxn);
      	if (a[i] > b[j]) maxn = max(maxn, f[i - 1][j] + 1);
      }
  }
  //for (int i = 0; i <= n; ++ i) ans = max(ans, f[n][i]);
  ```
