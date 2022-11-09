# 最小表示法

+ 定义：一个字符串的 字典序最小的 `shift`

+ 算法：

  1. 破环成链：将串重复一次变成两倍大小的串，此时所有的shfit都会在新串中出现且只出现一次

  2. 双指针：每个指针表示从当前位置开始长度为n的子串

     从两指针开始往后比较，直到出现不同，假设指针分别为`i`和`j`（`i < j`），且移动`k`位，且`s[i + k - 1] > s[j + k - 1]`

     此时`i`表示的串一定不是最小表示，同时以`i`到`i + k - 1`之间的任何一个指针所表示的串也都不是最小表示，因为如果是，则在`j`所对应的串中也能找到其对应的串，且在`k`这个位置出现不同并更不优，故每个指针只需扫描一次

  + 如果扫描完并且一致相同，则串一定是一个循环串，且`i`和`j`之间就是一个循环节

+ 代码：时间复杂度$线性$

  ```c++
  string get_min(string s) {  // 索引从0开始
      string ts = s + s;
      int n = s.size();
      int i = 0, j = 1;
      while (i < n && j < n) {
          int k = 0;
          while (k < n && ts[i + k] == ts[j + k]) ++ k;
          if (k == n) break;
          if (ts[i + k] > ts[j + k]) i += k + 1;
          else j += k + 1;
          if (i == j) ++ j;
      }
      return ts.substr((int)min(i, j), n);
  }
  ```


# trie树

```c++
struct Trie {
    int trie[MAXN][26], cnt[MAXN], idx;  // MAXN = 字符串的个数 * 字符串长度 * 26
    void insert(string &str) {
        int node = 0;
        for (auto &c : str) {
            int son = c - 'a';
            if (! trie[node][son]) trie[node][son] = ++ idx;
            node = trie[node][son];
        }
        ++ cnt[node];  // cnt表示每个结点表示的字符串的个数
    }
    int query(string &str) {
        int node = 0;
        for (auto &c : str) {
            int son = c - 'a';
            if (! trie[node][son]) return 0;
            node = trie[node][son];
        }
        return cnt[node];
    }
};
```

## 01trie树

可用于求一个数对一个数集的最大异或值并给出对应的数

```c++
struct Trie01 {
    int trie[MAXN * D][2], val[MAXN * D], idx;  // MAXN = 数的个数 * 2, D为数的二进制表示长度
    void insert(int x, int id) {  // 数和这个数在集合中的索引
        int node = 0;
        for (int son, i = D; i >= 0; -- i) {
            son = (x >> 1) & 1;
            if (! trie[node][son]) trie[node][son] = ++ idx;
            node = trie[node][son];
        }
        val[node] = id;
    }
    pair<int, int> get(int x) {  // 输入一个数，返回这个数在Trie维护的数集的最大异或值和对应的数的索引
        int node = 0, res = 0;
        for (int son, i = D; i >= 0; -- i) {
            son = (x >> i) & 1;
            if (trie[node][son ^ 1]) node = trie[node][son ^ 1], res |= (1 << i);
            else node = trie[node][son];
        }
        return {res, val[node]};
    }
};
```
