# 位运算

+ `lowbit(x) = x & (-x) = x & (~x + 1)`：`x`的二进制表示的最低位的`1`的十进制值
+ 集合运算：以集合`i`和`j`为例
  + 集合交集：`i & j`
  + 集合并集：`i | j`
  + 两集合不同的元素：`i ^ j`：元素即可能在`i`也可能在`j`
  + 在`i`不在`j`的元素：`i & (~j)`
  + 枚举子集：`for (int s = i; s; s = s - 1 & i)`
    枚举真子集：`for (int s = i - 1 & i; s; s = s - 1 & i)`
+ 拆分数：将一个数分成一半，小的一半通过各个位的1组成，高位通过跨过一段距离然后多余的部分又小的那部分1组成

  ```c++
  vector<int> split(int n) {
      vector<int> res;
      for (int i = 1; i <= n; i <<= 1) {
  		n -= i;
          res.push_back(i);
      }
      if (n) res.push_back(n);
      return res;
  }
  ```

# 二分

```c++
int l, r, ans = ;
while (l <= r) {
    int mid = l + r >> 1;
    if (check(mid)) l = mid + 1/r = mid - 1, ans = mid;
    else r = mid - 1/l = mid + r; 
}
// ans
```

# 倍增

## RMQ问题ST表解

```c++
//#include <cmath>
const int N = ;
const int LOG = ceil(log(N) / log(2)) + 1;

int f[N][LOG];
void ST_pre(int a[], int l, int r) {
    for (int j = 0; j < LOG; ++ j) 
        for (int i = l; i + (1 << j) - 1 <= r; ++ i) {
            if (! j) f[i][j] = a[i];
            else f[i][j] = max(f[i][j - 1], f[i + (1 << j - 1)][j - 1]);
        }
}
int query(int l, int r) {
	if (l > r) return 0;
    int len = r - l + 1;
    int k = log(len) / log(2);
    //lg2[N]; lg2[1] = 0; for (int i = 2; i < N; ++ i) lg2[i] = lg2[i >> 1] + 1;
    return max(f[l][k], f[r - (1 << k) + 1][k]);
}
/*ST_pre(待处理数组, 1, n)
 *query(..., ...)
 */
```

## 树上倍增求LCA

# 差分 & 前缀和

+ 前缀和：`pre[i] = a[1] + a[2] + ... + a[i]`：即`pre[i] = pre[i - 1] + a[i]`，有`a[i] = pre[i] - pre[i - 1]`
  + 二维前缀和：容斥原理
+ 差分：`c[i] = a[i] - a[i - 1]`：原数组是差分数组的前缀和

---

+ 树上（路径）差分和前缀和：

  1. 修改：`pre[x] += d; pre[y] += d; val[fa[lca(x, y)]] -= 2 * d`
  2. 查询：`pre[x] + pre[y] - pre[lca(x, y)] - pre[fa[lca(x, y)]]`

  + 路径的边：以每个结点唯一表示该节点到父亲的边（根节点无），此时查询则是`pre[x] + pre[y] - 2 * pre[lca(x, y)]`

# Else

## 双指针

+ 同类区间问题：

  ```c++
  for (int l = st, r; l <= ed; ++ l) {
      r = l;
      
      while (r + 1 <= ed && is_same(arr[l], arr[r + 1])) ++ r;
      //(l, r)为一个答案
      
      l = r;
  }
  ```

+ 单调序列问题：

  ```c++
  for (int l = st, r = st; r <= ed; ++ r) {
	  add(arr[r]);  // 累加上arr[r]的值
	  while (l < r && !is_ok()) sub(l ++);  // 调整左区间并减去其影响
      //r - l + 1即为一个答案
  ```

## 单调栈

> 找到每个数左边离它最近的比它大/小的数

```c++
for (int i = 1; i <= n; ++ i) {
    while (! st.empty() && check(st.top(), a[i])) st.pop();
    st.push(a[i]);
}
```

+ 数组模拟：`int t = 0; ++ tt; tt > 0`

顺序遍历，入栈天然有序，每个元素入栈前将所有对自己一定不构成威胁的的弹出了，那么栈顶就是过去最晚入栈（和自己最近），且”我“和”TA“之前的都是不构成威胁的。

## 单调队列

> 找出滑动窗口中的最大值/最小值

```c++
for (int i = 0; i <= n; ++ i) {
	while (! dqu.empty() && check_out(dqu.front())) dqu.pop_front();  //头部元素超过窗口大小
    while (! dqu.empty() && check(dqu.back(), i)) dqu.pop_back();  //维持单调
    dqu.push_back(i)
}
```

+ 数组模拟：`int hh = 0, tt = -1; ++ tt; hh <= tt`

## 滑动窗口

```c++
deque<int> win;
for (int i = 1; i <= n; ++ i) {
    if (! win.empty() && i - win.front() >= 窗口长度) win.pop_front();
    while (! win.empty() && check(win.back, i)) win.pop_back;
    win.push_back(i);
}
```

## 对顶堆
> 动态中位数：动态输入序列，随时查询中位数

```c++
//创建
priority_queue<int> down;  //大根堆，堆顶最大，在下面
priority_queue<int, vector<int>, greater<int> > up;  //小根堆，堆顶最小，在上面

//输入x，维护
if (down.empty() || x <= down.top()) down.push(x);  //优先下
else up.push(x);

//每次输入只影响一位，所以不用while
if (down.size() > up.size() + 1) up.push(down.top()), down.pop();
if (up.size() > down.size()) down.push(up.top()), up.pop();

//查询
down.top()
```

# 分治
