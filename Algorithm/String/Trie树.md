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
