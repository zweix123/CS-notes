# 哈希

## 字符串哈希

被哈希的值的数量超过哈希空间的一半，我们认为出现哈希冲突的概率超过一半

```c++
typedef unsigned long long ull;
struct Hash {
    ull p, mod;  // p是进制的底，mod是哈希的模数（哈希空间）
	ull f[N];  // f[]表示对象维护的字符串的哈希值前缀和
	void init(char *s) {  // 索引从1开始（0有意义）
        p = 131ull;
        mod = 18446744073709551615ull;
		for (int i = 1; s[i]; ++ i) f[i] = (f[i - 1] * p % mod + (ull)s[i]) % mod;
    }
    
    ull fpow(int n) {
        ull x = p, res = 1;
        for (; n; n >>= 1, x = x * x % mod) if (n & 1) res = res * x % mod;
        return res;
    }
    ull get(int l, int r) { return (f[r] - f[l - 1] * fpow(r - l + 1) % mod) % mod; }
    ull get(char *s_i) {
    	ull res = 0;
    	for (; *s_i; ++ s_i) res = (res * p % mod + (ull)*s_i) % mod;
    	return res;
	}
};
```

如果出现哈希冲突可调节进制的底和哈希的模数或者使用双哈希（将一种哈希类封装进一个类的方式使双哈希非常方便）

## 哈希表

1. 拉链法：牺牲性能保证正确性：允许冲突，将冲突的值放在一个邻接表中

   ```c++
   int head[N], lext[M], val[M], idx;
   void add(int x, int y) {
   	lext[++ tot] = head[x];
       head[x] = tot;
       to[tot] = y;
   }
   void insert(int x) {
       int k = (x % N + N) % N;
       add(k, x);
   }
   bool find(int x) {
       int k = (x % N + N) % N;
       for (int e = head[k]; e; e = lext[e]) {
           if (to[e] == x) return true;
       }
       return false;
   }
   ```

2. 散列表：牺牲性能保证正确性：允许冲突，将冲突的值放在哈希空间的下一个位置

   ```c++
   const int MAXN = 10000007;
   typedef long long ill;
   int f[MAXN], id[MAXN];
   ill get_hs(int x, int y) 
   	{ return x * 1000000001 + y; }
   int find(int x, int y) {
   	ill hs = get_hs(x, y);
   	int key = (hs % MAXN + MAXN) % MAXN;
   	while (f[key] != -1 && f[key] != hs) {
   		++ key;
   		if (key == MAXN) key = 0;
   	}
   	return key;
   }
   // key = find(...) if (id[key])
   /*
   int key = find(data[i].x, data[i].y);
   f[key] = get_hs(data[i].x, data[i].y);
   id[key] = i;
   */
   ```

# KMP算法

**下面两个算法建立的NFA自动机是一样的，区别在于对应字符串的索引**

+ 算法：

  > 朴素算法如果失配则移动一格从头匹配，那已经匹配的部分能不能利用起来，达到文本串中的指针不必往回移动，调整在模式串上的指针，之后两者可继续匹配，保证模式串指针之前的部分是匹配好的的目的？

  `nfa[]`描述一个NFA，存储一个结点在失配后应该跳转的结点（从`i`指向`i + 1`这个匹配成功的边被隐藏）

  > `border[i]`表示模式串中前`i`的前缀中，（非本身的）最长的前缀和后缀的长度
  >
  > 1. 这样的前后缀：这个后缀一定出现在文本串中，而这个前缀一定出现在模式串中，不需要再匹配（且最长）
  > 2. 这样的数值    ：从这个前缀之后匹配，这个索引位置和这个前缀长度有关

  本来自动机的结点和模式串的索引应没有关系，只是这里用数组模拟自动机，导致模拟结点的索引和模式串的索引有关系


```c++
struct KMP {
    int n; char *p;  // 模式串存储在类外
    int nfa[N];
    void pre(char *s) {  // 和读入解耦, 通过指针加法调整
        p = s; n = strlen(p);
        nfa[0] = 0;  // s[0]失配只能从s[0]开始重新匹配
        nfa[1] = 0;  // s[1]失配只能从s[0]开始重新匹配
		int k = 0;
        for (int i = 1; i < n; ++ i) {
            while (k && p[i] != p[k]) k = nfa[k];
            if (p[i] == p[k]) ++ k;
            nfa[i + 1] = k;  // 这里通过0..i的信息去更新i + 1, 如果这个点失配, 前缀的border保证
            				 // k其实是k表示的前缀的下一个, 因为索引起点的缘故刚好是k
        }
    }
    void match(char *s) {  // 文本串, 索引从0开始
        int k = 0;
        for (int i = 0; s[i]; ++ i) {
            while (k && s[i] != p[k]) k = nfa[k];
            if (s[i] == p[k]) ++ k;
            if (k == n) {    // nfa[n]表示的nfa的结点是出口, 表示匹配完毕
                // 匹配后之后的逻辑
            	k = nfa[k];  // nfa[n]表示的结点是不会再匹配的, 但是再匹配一定会失配, 这时利用之前的跳转一下
            }
        }
    }
} kmp;
```

1. 字符串索引从`0`开始，`nfa[0]`是自动机的入口，如果匹配到`s[0]`则进入`s[1]`，即`nfa[i]`表示`s[i]`失配的出边

+ 还原`border`：`0..i`的`border`存储在下一个结点（为什么这样设计的原因在注释中），所以在还原是错位即可

  > 这里的类的设计是模仿`<cstring>`的传参方式，上面的索引讨论是在类内，如果用户在使用时已经转换，则双重转换

+ 循环节：假设字符串确实有循环节

  + 循环节长度：终止结点跳转的位置的后缀就是一个循环节，大概是`n - kmp.nfa[n]`
  + 判断子串是否是原串的循环节（索引从0开始）
    1. 该串的起点和超尾都整除最短循环节长度
       1. 该子串长度整除原串长度

+ 索引从1开始计数版本：

  ```c++
  struct KMP {
      int n; char *p;  // 模式串存储在类外
      int nfa[N];
      void pre(char *s) {  // 要求索引必须从1开始
          p = s; n = strlen(p + 1);
          for (int i = 2, j = 0; i <= n; ++ i) {
              while (j && p[i] != p[j + 1]) j = nfa[j];
              if (p[i] == p[j + 1]) ++ j;
              nfa[i] = j;
          }
      }
      void match(char *s) {  // 要求索引必须从1开始
  		for (int i = 1, j = 0; s[i]; ++ i) {
              while (j && s[i] != p[j + 1]) j = nfa[j];
              if (s[i] == p[j + 1]) ++ j;
              if (j == n) {
                  // 匹配后的逻辑
              	
                  j = nfa[j];
  			}
          }
      }
  } kmp;
  ```

  1. 自动机结点分别为`0...n`，则`nfa[i]`到`nfa[i + 1]`的边是`s[i + 1]`

# AC自动机

```c++
//const int N = ;  // 模式串个数
//const int M = ;  // 模式串长度
//const int MAXN = ;  // 匹配串长

//trie tree
int trie[N * M][26], cnt[N * M], idx;  // 数组模拟结果体和指针，cnt表示这样的串有多少个
void insert(char *s, int st) {  // 索引从0开始
	int node = 0;
	for (int son, i = st; s[i]; ++ i) {
        son = s[i] - 'a';
        if (! trie[node][son]) trie[node][son] = ++ idx;
        node = trie[node][son];
    }
    cnt[node] ++;
}
int nfa[N * M];  // trie树上的自动机
void build() {
    queue<int> qu;
    for (int i = 0; i < 26; ++ i) if (trie[0][i]) qu.push(trie[0][i]);
    while (qu.size()) {
        int node = qu.front(); qu.pop();
        for (int son, e = 0; e < 26; ++ e) {
            son = trie[node][e];
            if (! son) continue;
            // 类比kmp过程
            int j = nfa[node], i = e;
            while (j && ! trie[j][i]) j = nfa[j];
            if (trie[j][i]) j = trie[j][i];
        	nfa[son] = j;
            qu.push(son);
        }
    }
}
int match(char *str, int st) {
    int res = 0;
    for (int i, j = 0, _ = st; str[_]; ++ _) {
        i = str[_] - 'a';
        while (j && !trie[j][i]) j = nfa[j];
        if (trie[j][i]) j = trie[j][i];
        // 这里匹配到的是最长的，而一个字符串被匹配，可能还有这个字符串的后缀子串，但是这个算法不会匹配到他们   
        for (int t = j; t; t = nfa[t]) {
            //匹配后的操作，此时t在结点上
            //此处以求各个模式串出现次数（多次无效）为例
            res += cnt[t];
            cnt[t] = 0;
            
        }
    }
    return res;
}
```

## Trie图

```c++
//const int N = ;  // 模式串个数
//const int M = ;  // 模式串长度
//const int MAXN = ;  // 匹配串长度

//trie tree
int trie[N * M][26], cnt[N * M], idx;  // 数组模拟结果体和指针，cnt表示这样的串有多少个
void insert(char *s, int st) {  // 索引从st开始
	int node = 0;
	for (int son, i = st; s[i]; ++ i) {
        son = s[i] - 'a';
        if (! trie[node][son]) trie[node][son] = ++ idx;
        node = trie[node][son];
    }
    cnt[node] ++;
}
int nfa[N * M];  // trie树上的自动机
void build() {
    queue<int> qu;
    for (int i = 0; i < 26; ++ i) if (trie[0][i]) qu.push(trie[0][i]);
    while (qu.size()) {
        int node = qu.front(); qu.pop();
        for (int son, e = 0; e < 26; ++ e) {
            son = trie[node][e];
            if (! son) trie[node][e] = trie[nfa[node]][e];  //---
           	else {											//---
                nfa[son] = trie[nfa[node]][e];				//---
                qu.push(son);								//---
                //这是一个dp的过程，如果有什么量需要传递的话arg[son] |= arg[nfa[son]]
            }												//---
        }
    }
}
int match(char *str, int st) {
    int res = 0;
    for (int i, j = 0, _ = st; str[_]; ++ _) {
        i = str[_] - 'a';
        j = trie[j][i];										//---
        // 这里匹配到的是最长的，而一个字符串被匹配，可能还有这个字符串的后缀子串，但是这个算法不会匹配到他们   
        for (int t = j; t; t = nfa[t]) {
            //匹配后的操作，此时t在结点上
            //此处以求各个模式串出现次数（多次无效）为例
            res += cnt[t];
            cnt[t] = 0;
            
        }
    }
    return res;
}
```
