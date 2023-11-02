# Problem

## 构造不含一个串的<font color=Red>短</font>长串的数量

构造一个固定长度的串，要求串中不包含一固定串，求方案数（IO：N[, 50]）

`f[i][j]`表示构造串构造到第`i`个位置，然后正好匹配到模式串（KMP自动机）的`j`的位置的方案数

```c++
//input s + 1 and init of nfa
int solve() {
    f[0][0] = 1;  //啥都没有的方案数是1
    for (int i = 0; i < n; ++ i) {  // 这里是递推，本质是想要1~n
        for (int j = 0; j < kmp.n; ++ j) {  // j = m的状态不可取
            for (char c = 'a'; c <= 'z'; ++ c) {
                int u = j;
                while (u && c != s[u + 1]) u = kmp.nfa[u];
                if (c == s[u + 1]) ++ u;
                
                if (u == kmp.n) continue;  // 这个状态不可取
                f[i + 1][u] = 1LL * (f[i + 1][u] + f[i][j]) % MOD;  // j -> u;
            }
        }
    }
    int res = 0;
    for (int i = 0; i < kmp.n; ++ i) res = 1LL * (res + f[n][i]) % MOD;
    return res;
}
```

## 修改短长串不含<font color=Red>多</font>个串的修改数

修改一个给的串，要求串中不包含给的几个串，求最小修改次数（IO：个数[, 50]，短串长度不超50，长串长度不超1000）

`f[i][j]`表示维护到原串的第`i`个位置，匹配到AC自动机上的第`j`个结点的所有操作方案中操作数最小的

```c++
//input and init trie图(ac自动机)  // 注意边只有四种了
//f -> 0x3f
int solve() {
    f[0][0] = 0;
    for (int i = 0; i < len; i ++ ) {
		for (int node = 0; node <= idx; node ++ ) {
            for (int son, e = 0; e < 4; e ++ ){
                int op = (get(str[i + 1]) != e);
                son = trie[node][e];
                if (! cnt[son]) f[i + 1][son] = min(f[i + 1][son], f[i][node] + op);
            }
        }
    }
    int res = INF;
    for (int i = 0; i <= idx; ++ i) res = min(res, f[len][i]);
    if (res == INF) res = -1;
    return res;
}
```

## 构造不含一个串的<font color=Red>超</font>长串的数量

构造一个超长的串，其中不包含一个给定的小串的数量，结果取模（IO：长串 <= 1e9，小串 <= 20）

`f[i][j]`表示构造到第`i`位，匹配到模式串的第`j`位（末尾部分和模式串的前缀匹配）的所有字符串集合的元素数量

于是我们可以在`i`和`i + 1`之间递推：`f[i + 1][j经过kmp匹配后的位置] += f[i][j]`

另外就是这是构造，每位字符的选择是任意的，既对于第二维，相邻两位之间的起末是固定的，同时后一位若若干前一位积累
$$
[f_{i, 0}, f_{i, 1}, ..., f_{i, m - 1}]
\times
\left [
\begin{array}{}
0对i + 1 \ 0的贡献 &\ 0对下一位1的贡献 &... &0对下一位m - 1的贡献 \\
1对下一位0的贡献 &\ 1对下一位1的贡献 &... &1对下一位m - 1的贡献 \\
... \\
m - 1 &...
\end{array}
\right]
=
f[f_{i + 1, 0}, f_{i + 1, 1}, ...]
$$

```c++
Mat pre() {  // 预处理系数矩阵
    Mat A; A.n = A.m = strlen(str + 1);  // 其实就是m，m就是字符串长度
    
    memset(A.w, 0, sizeof A.w);
    for (int j = 0; j < m; ++ j) {
        for (char c = '0'; c <= '9'; ++ c) {
            int k = j;
            while (k && str[k + 1] != c) k = nfa[k];
            if (str[k + 1] == c) ++ k;
            //nfa自动机指针移动过程
            if (k < m) A.w[j][k] ++;  // 记录合法答案
        }
    }
    return A;
}
//初始向量[1, 0, 0, 0...]（0 ~ m - 1） -> 扩充成方阵，命名为f
//f = f * fpow(pre());
//ans = \sum{f.w[0][0...m - 1]}
```
