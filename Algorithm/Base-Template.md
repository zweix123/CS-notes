#### 快读快写

```cpp
template<typename T>
inline void read(T &x) {
    x = 0; T k = 1;
    char c = getchar();
    for (; c < '0' || c > '9'; c = getchar()) if (c == '-') k = -1;
    for (; c >= '0' && c <= '9'; c = getchar()) x = x * 10 + c - 48;
    x *= k;
}
template<typename T>
inline void write(T &x) {
    if (x < 0) putchar('-'), x = -x;
    if (x > 9) write(x / 10);
    putchar(x % 10 + 48);
}
```

#### 龟速乘

```cpp
const int MOD = 1e9 + 7;
ill ftimes(ill a, ill b) {
	if (a < b) swap(a, b);
	ill res = 0;
	for (; b; b >>= 1, a = (a + a) % MOD) if (b & 1) res = (res + a) % MOD;
	return res;
}
```

#### 快速幂

```cpp
int fpow(int d, ill n, int mod) {
    int res = 1 % mod; d %= mod;  // mod可能等于1吗?
    for (; n; n >>= 1, d = (ill)d * d % mod) if (n & 1) res = (ill)res * d % mod;
    return res;
}
```

#### 高精度

以`vector`逆序存储十进制各位（可能含有前导0）

+ 高精度加法：

  ```cpp
  // C = A + B, A >= 0, B >= 0
  vector<int> operator + (vector<int> &A, vector<int> &B) {
      if (A.size() < B.size()) return B + A; //add(B, A);
      vector<int> C;
      int t = 0;
      for (int i = 0; i < (int)A.size(); i ++ ) {
          t += A[i];
          if (i < (int)B.size()) t += B[i];
          C.push_back(t % 10);
          t /= 10;
      }
  	if (t) C.push_back(t);
  	return C;
  }
  ```

+ 高精度减法：

  ```cpp
  // C = A - B, 满足A >= B, A >= 0, B >= 0
  vector<int> operator - (vector<int> &A, vector<int> &B) {
      vector<int> C;
      for (int i = 0, t = 0; i < A.size(); i ++ ) {
          t = A[i] - t;
          if (i < B.size()) t -= B[i];
          C.push_back((t + 10) % 10);
          if (t < 0) t = 1;
          else t = 0;
      }
      while (C.size() > 1 && C.back() == 0) C.pop_back();
  	return C;
  }
  ```

+ 高精度乘低精度：

  ```cpp
  // C = A * b, A >= 0, b >= 0
  vector<int> mul(vector<int> &A, int b) {
      vector<int> C;
      int t = 0;
      for (int i = 0; i < A.size() || t; i ++ ) {
          if (i < A.size()) t += A[i] * b;
          C.push_back(t % 10);
          t /= 10;
      }
      while (C.size() > 1 && C.back() == 0) C.pop_back();
      return C;
  }
  ```

+ 高精度除以低精度：

  ```cpp
  // A / b = C ... r, A >= 0, b > 0
  vector<int> div(vector<int> &A, int b, int &r) {
      vector<int> C;
      r = 0;
      for (int i = A.size() - 1; i >= 0; i -- ) {
          r = r * 10 + A[i];
          C.push_back(r / b);
          r %= b;
      }
      reverse(C.begin(), C.end());
      while (C.size() > 1 && C.back() == 0) C.pop_back();
      return C;
  }
  ```

#### 区间合并

```cpp
typedef pair<int, int> pii;
void merge(vector<pii>& segs) {
    vector<pii> res;
    sort(segs.begin(), segs.end());
    int st = -2e9, ed = -2e9;
    for (auto &seg : segs) {
        if (ed < seg.first) {
            if (st != -2e9) res.push_back({st, ed});
            st = seg.first; ed = seg.second;
        } else ed = max(ed, seg.second);
    }
    if (st != -2e9) res.push_back({st, ed});
    segs = res;
}
```

#### 离散化

+ 包含正负数的桶：通过`x + MAXN`将数字移动到自然数范围

+ 不需要保序的离散化：`map<离散前类型, 离散后类型> ids;`

+ 保序离散化：

  ```cpp
  const int BEGIN = 0;  // 离散后的整数的起始大小
  template<typename T>
  void discretize(T *a, int l, int r) {
      vector<T> dct;
      for (int i = l; i <= r; ++ i) dct.push_back(a[i]);
      sort(dct.begin(), dct.end());
      dct.erase(unique(dct.begin(), dct.end()), dct.end());
  	
      for (int i = l; i <= r; ++ i)
          a[i] = lower_bound(dct.begin(), dct.end(), a[i]) - dct.begin() + BEGIN;  // 表达式取出作为函数
  }
  ```
