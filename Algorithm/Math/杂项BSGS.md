> Baby Step Giant Step大步小步算法

解决$a^x \equiv b(mod \ p)$问题，求最小非负数解

### 简单版

在$(a, p) = 1$时求最小非负整数解
$$
由(a, p) = 1, 则因欧拉定理, 有a^{\phi(p)} \equiv 1(mod \ p), 即a的幂次在模p下每\phi(p)一循环. 则x的范围是[0, \phi(p) - 1]
$$
BSGS算法在这个区间内通过分块计算，分块的大小$k \ge \sqrt{p}$，

> 在实际计算中，计算p的欧拉函数比较麻烦，直接放缩把p作为右区间

variable不够用了，我们令字母t替换字母x

则解可表示为$t = kx - y(x \in [1, k], y \in[0, k - 1])$，`t`可以取到`[1, k * k]`，实现中特判0

> 这里用减法表示在下面取模恒等式中变换更方便，也正因为是减法，所以t的最小取值是1

$$
\begin{align}
a^t = &a^{kx - y} &\equiv &b              &(mod \ p) \\ 
      &a^{kx}     &\equiv &b \times a^{y} &(mod \ p)
\end{align}
$$

+ 实现：我们将等式的右边（即关于m的部分）打一个哈希表，然后枚举左边（关于n的部分），去检测恒等式是否成立

```c++
#include <unordered_map>
int bsgs(int a, int b, int p) {
    if (1 % p == b % p) return 0;
    int k = sqrt(p) + 1;
    std::unordered_map<int, int> hash;
    for (int i = 0, j = b % p; i < k; ++ i) {
        hash[j] = i;
        j = (ill)j * a % p;
    }
    int ak = fpow(a, k, p);
    for (int i = 1, j = ak % p; i <= k; ++ i) {
        if (hash.count(j)) return (ill)i * k - hash[j];
        j = (ill)j * ak % p;
    }
    return -1;
}
```

### 大步小步版

> 上面的算法那里体现算法名字的大步小步呢？

修改未知数的表示$t = kx - y, x \in [1, \frac{p}{k}], y \in [0, k]$，而最后$a^{kx} \equiv b \times a^y \ (mod \ p)$，若给左边打表，我们可以通过调节k来控制枚举

> 场景：同样的a，多次修改b，多次询问，则每次查询的时间复杂度

> 这里的表达式可以得到0的未知数

```c++
#include <unordered_map>
struct BSGS {
    int a, p;
    const int K = 46347;  // 每次查询的复杂度
    std::unordered_map<int, int> hash;
    void init(int aa, int pp) {
        a = aa; p = pp;
        hash.clear();
        int K_ = p / K + 1;
        int ak = fpow(a, K, p);
        for (int i = 1, j = ak; i <= K_; ++ i) {
            if (! hash.count(j)) hash[j] = i;  // 尽可能选择小的x
            j = (ill)j * ak % p;
        }
    }
    int query(int b) {
        int res = p + 1;
        for (int i = 0, j = b; i <= K; ++ i) {
            if (hash.count(j)) res = min(res, hash[j] * K - i);
            j = (ill)j * a % p;
        }
        return res == p + 1 ? -1 : res;
    }
};
```

### 任意模数版

$(a, p) \neq 1$
