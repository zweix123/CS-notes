# 搜索

| dfs                                                 | bfs                                           |
| --------------------------------------------------- | --------------------------------------------- |
| 本质是使用栈：先进后出                              | 本质是使用队列：先进先出                      |
| 搜索空间被dfs分为栈内和栈外：对树的搜索栈内是线性的 | bfs队队列具有两段性和单调性：首次出队即为最短 |
| 码量小<br>回溯提供更多的灵活性                      | 基于迭代：不会爆栈                            |

+ 枚举：

  + 二进制枚举：
    ```c++
    type a[N], n;  // [1, n]
    type b[N], cnt = 0;
    void dfs(int u = 1) {  // u为考虑a[u]要不要选
    	if (u > n) {
            b[1, cnt]即为枚举结果
            return;
        }
        b[++ cnt] = a[u]; dfs(u + 1);
        -- cnt;			  dfs(u + 1);
    }
    ```

  + 排列：

    ```c++
    type a[N], n;  // [1, n]
    type b[N];
    bool vis[N];
    void dfs(int u = 1) {  // u为考虑b[u]这个位置选哪个
    	if (u > n) {
    		b[1, n]即为枚举结果
            return;
        }
        for (int i = 1; i <= n; ++ i) if (! vis[i]) {
            vis[i] = true;
            b[u] = a[i];
            dfs(u + 1);
            vis[i] = false;
        }
    }
    ```

  + 组合：

    ```c++
    type a[N], n, m;  // [1, n], C(n, m)
    int id[N] = {1};
    bool vis[N];
    void dfs(int u = 1) {  // u为考虑b[u]这个位置选哪个, 为保证不重不漏, 单调选择
    	if (u > m) {
            id[1, m]即为枚举结果的id
            return;
        }
        for (int i = id[u - 1]; i <= n; ++ i) if (! vis[i]) {
            vis[i] = true;
            id[u] = i;
            dfs(u + 1);
            vis[i] = false;
        }
    }
    ```

## BFS

+ 边权**相等且非负**的最短路问题可通过BFS解决

+ 边权只有0和1的最短路问题可通过**双端队列**`deque`解决：0放队首、1放队尾

  ```c++
  int dis[N];
  int pj(int tar) {
      memset(dis, 0x3f, sizeof dis);
    
      dis[1] = 0;
      deque<int> dqu;
      dqu.push_back(1);
      while (! dqu.empty()) {
          int node = dqu.front(); dqu.pop_front();
          for (int son, e = head[node]; e; e = lext[e]) {
              son = to[e];
              int len = val[e] > tar;
              if (dis[son] > dis[node] + len) {
                  dis[son] = dis[node] + len;
                  if (len) dqu.push_back(son);
                  else dqu.push_front(son);
              }
          }
      }
      return dis[n] <= k;
  }
  ```

+ 对于解空间极大（即每层的解的个数都成指数扩张），可使用**双向广搜**

### A*算法

> 用于一定有解的情况

将BFS的队列换成优先队列，按照一个评估指标排序，优先搜索最优的

评估指标：该点到起点的真实距离 + 该点到终点的估计距离 -> 该点所在的路径的解

评估函数：要求评估的该点到终点的距离必须小于等于该点到终点的真实距离，越接近越高效（为0退化为Dijkstra）

#### 第K短路

+ 有向图，给定起终点，路径可重叠，求第k短的路（要求一个路径至少有一个边（如果起终为一点））评估函数见代码

```c++
int st, ed;  //起点和终点
struct edge { int to, val; };
vector<edge> g[N];  //原图
vector<edge> g_[N];  //边取反的图，因为要求每个点要终点的最短路，用的是反向的dijstra
int K;  //题目要求的K `if (st == ed) ++ K`

int f[N];
void dijstra() {...}  //更新f使之存储到终点的最短距离

struct point {
    int f, dis, x;  //分别是（到终点的）估计值、（到起点的）真实值、结点编号
    bool operator < (const point & t) const {  // 评估函数
        return f + dis > t.f + t.dis;
    }
};
int cnt[N];
int astar() {
    priority_queue<point> heap;
    heap.push({f[st], 0, st});   
    while (heap.size()) {
        int node = heap.top().x, dist = heap.top().dis; heap.pop();
        ++ cnt[node];
        if (cnt[ed] == K) return dist;
        
        for (auto &e : g[node]) {
            int son = e.to, val = e.val;
            if (cnt[son] < K) 
                heap.push({dist + val + f[son], dist + val, son});
                
        }
    }
    return -1;
}
//input g and build g_ for 反向
//Dijkstrea for g_
//output astart()
```

## DFS

### 剪枝

1. 可行性剪枝：要知道最暴力的枚举是考虑所有可能性，然后判断行不行，这里可只枚举可能行的
2. 优化搜索顺序：优先搜索分支数量少的边
3. 排除等效冗余（少见）
4. 最优性剪枝：如果之后当前的搜索已经不优于记录的最优解，那么不再进行
5. （记忆化搜索）
