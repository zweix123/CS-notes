# 树形DP

## 树的直径

+ 定义：树上最长路径

+ 对于无权图：

  + 算法：

    1. 任取任意一点为根，找到深度最大的点(之一)`bm`
    2. 再以`bm`为根，找到深度最大的点——距离bm最远的点

  + 证明：`bm`一定是某条直径的端点


+ 有权图：

  + 状态表示：`d1[i]`表示以路径一端为`i`向下的所有路径的集合，其值是路径的**最大值**

    ​                    `d2[i]`表示以路径一端为`i`向下的所有路径的集合，其值是路径的**次大值**

  可以在dfs中递推然后在搜索外一个for找到答案，也可以在dfs中在线找ans，那么两个数组可以用dfs中的局部变量表示

  + 幼年版本：

    ```c++
    int d1[N], d2[N];
    void dfs(int node, int father) {
    	d1[node] = d2[node] = 0;
        for (int son, e = head[node]; e; e = lext[e]) {
            son = to[e];
            if (son == father) continue;
            dfs(son, node);
            if (d1[son] + val[e] >= d1[node]) d2[node] = d1[node], d1[node] = d1[son] + val[e];
            else if (d1[son] + val[e] > d2[node]) d2[node] = d1[son] + val[e];
        }
    }
    //dfs(1, 1); for (int i = 1; i <= n; ++ i) ans = max(ans, d1[i] + d2[i]);
    ```

  + 闫学灿版本

    ```c++
    int ans;
    int dfs(int node, int father) {
        int res = 0;
        int d1 = 0, d2 = 0;
        for (int son, e = head[node]; e; e = lext[e]) {
            son = to[e];
            if (son == father) continue;
            int d = dfs(son, node) + val[e];
            
            if (d >= d1) d2 = d1, d1 = d;
            else if (d > d2) d2 = d;
            
            res = max(res, d);
        }
        ans = max(ans, d1 + d2);
        return res;
    }
    //dfs(1, 1); return ans;
    ```

+ 直径的数量：

  ```c++
  int anslen, ansnum;
  int d[N], num[N];
  void dfs(int node, int father) {
  	d[node] = 0, num[node] = 1;
  	for (int son, e = head[node]; e; e = lext[e]) {
  		son = to[e];
  		if (son == father) continue;
  		dfs(son, node);
  		
  		int t = d[son] + val[e];
  		if (t + d[node] > anslen) {
  			anslen = t + d[node];
  			ansnum = num[node] * num[son];
  		} else if (t + d[node] == anslen) {
  			ansnum += num[node] * num[son];
  		}
  		
  		if (d[node] < t) {
  			d[node] = t;
  			num[node] = num[son];
  		} else if (d[node] == t) {
  			num[node] +=num[son];
  		}
  	}
  }
  ```

## 树的重心

+ 定义：重心的子树的最大结点数量最小

  1. 删除重心得到的所有子树的大小不超过$\frac{n}{2}$
  2. 树中所有点到某个结点的和，重心最小
  3. 两个树连接，新树的重心一定在两个旧重心之间的路径上
  4. 增删树的一个叶子，重心最多移动一条边
  4. 以节点u为根的子树的重心，在u所在的重链上。

  > 用户：电站：连到所有用户的总花费最小

+ 算法：根据定义，比较删除每个结点后形成的子树的大小的最大值，关键在于如何求得结点上方所形成的子树的大小：定义`sons[node]`表示以`node`的子树的大小，则去除`node`得到的子树的大小分别为$sons_{son_1}, sons_{son_2}, ...sons_{son_{num}}, n - sons_{node}$最后一项为顶点以上子树的大小

  ```c++
  int n;  //树的大小
  int tar = -1, num = INF;
  int dfs(int node, int father) {
      int res = 0;
      int sons = 1;
      for (int son, e = head[node]; e; e = lext[e]) {
          son = to[e];
          if (son == father) continue;
          int t = dfs(son, node);
  		res = max(res, t);
          sons += t;
      }
      res = max(res, n - sons);
      
      if (res < num) tar = node, num = res;
      
      return sons;
  }
  ```

### 所有子树重心

```c++
int sz[N], fa[N], ans[N], hson[N];
void dfs(int node, int father) {
    sz[node] = 1; fa[node] = father; ans[node] = node;
    hson[node] = 0;
    for (int son, e = head[node]; e; e = lext[e]) {
        son = to[e];
        if (son == father) continue;
        dfs(son, node);
        sz[node] += sz[son];
    	if (sz[son] > sz[hson[node]]) hson[node] = son;
    }
    if (! hson[node]) return ;  // 叶子
    int res = ans[hson[node]];
    int tar = sz[node] >> 1;  // 删除重心，各子树大小不超结点数一半
    for (; res != node; res = fa[res]) {
        if (sz[node] - sz[res] <= tar && sz[hson[res]] <= tar) break;
    }
    ans[node] = res;
}
```

## 树的中心

树的中心：中心距离其他结点的最大距离是（所有结点中的这个性质）最小的

> 应用：消防站和医院的建立：事件到达中心的最差花费最小

+ 考虑：

  1. 自`now`向下的路径的最大长度：利用`d1[]`数组易推

  2. 自`now`向上的路径的最大长度：首先肯定经过`now`的父节点`father`

     1. 如果最大路径是继续往上走，则参照`d1[]`的更新方式利用`up[]`数组递推

     2. 如果最大路径自`father`之后向下走

        1. 经过`now`，不合法不可取
        2. 不经过`now`，可以，取集合中的最大

        我们发现如果`d1[father]`由`now`更新的，则取`d2[father]`，否则取`d1[father]`

  更新up需要父节点的完全信息，而递推down时是子节点更新父节点，所以需要两个dfs

```c++
int d1[N], d2[N], up[N];  //含义如分析
int p[N];  //p[father]表示father的d1[]来自哪个儿子

void dfs_d(int node, int father) {  //通过回溯完善down
	d1[node] = d2[node] = 0;
    //如果树的权值存在负数，则应该把down初始化为-INF
    for (int son, e = head[node]; e; e = lext[e]) {
        son = to[e];
        if (son == father) continue;
        dfs_d(son, node);
        if (d1[son] + val[e] >= d1[node]) {
            d2[node] = d1[node]; d1[node] = d1[son] + val[e];
            p[node] = son;
        } else if (d1[son] + val[e] > d2[node]) {
            d2[node] = d1[son] + val[e];
        }
    }
    /*对应着如果node是叶子节点，此时down还是-INF，需要修正
      if (d1[node] == -INF) d1[node] = d2[node] = 0;*/
}
void dfs_u(int node, int father) {
    for (int son, e = head[node]; e; e = lext[e]) {
        son = to[e];
        if (son == father) continue;
		if (p[node] == son) up[son] = val[e] + max(up[node], d2[node]);
        else up[son] = val[e] + max(up[node], d1[node]);
        dfs_u(son, node);
    }
}
/*int ans = -1, big = INF;  //记录记录中心和它到其他节点的最远距离
  for (int i = 1; i <= n; ++ i) {
      int t = max(d1[i], up[i]);
      if (t < big) ans = i, big = t;
  }*/
```

> 当然可以暴力换根，树的直径的dfs可以求得距离root的最远距离

# 与其他问题的结合

## 依赖背包

对`n`个节点的有权值的完全二叉树，保留`m`条边，对于每个方案求权值为能到根节点的1的边的权值和（有些边虽然保留，但是它的某个祖先没有保留，则其也被断开），求最大值。

或者说：有`m`条边的包括根的连通块的最大边权和

本质是有依赖的背包问题的简化版

+ 状态表示：`f[i][j]`表示以`i`为根的子树中，选`j`条边的所有方案的集合，其值是最大值边权和

+ 状态计算：在`f[i][j]`中，对于每个结点的一个儿子，如果要从这个儿子的状态中转移过来则必须要保留**1**条边，而儿子的可以转移的状态有$f_{son, 0}, f_{son, 1}, f_{son, 2}, ..., f_{son, j - 1}$，这些状态转移到now时是转移到第二维+1的位置，所以`f[i][j]`取max

  $f_{i, j} = max\{ f_{i, j - 1 - k} + f_{son, k} + val[e] \} k \in [0, j - 1]$其中now提供`j - 1 + k`个边，儿子提供`k`个，连接`1`个，共`j`个

```c++
int m;
int f[N][M];
void dfs(int node, int father) {
    for (int son, e = head[node]; e; e = lext[e]) {  //物品组
        son = to[e];
        if (son == father) continue;
        dfs(son, node);
        
        for (int j = m; j >= 0; -- j) {   //体积
            for (int k = 0; k < j; ++ k) {   //方案
                f[node][j] = max(f[node][j], f[node][j - 1 - k] + f[son][k] + val[e]);
            }}
}}
//dfs(1, 1); f[1][m];
```

## 自动机模型

1. 没有上司的舞会：一棵树，有点权，约束选父亲不能选儿子，求使点权和最大的选择方案

   + 自动机模型：孩子和父亲，其一选了，另一个必然不能选；其一没有选，另一个都可

     ```mermaid
     graph LR; b[不选0]; a[选1] --> b; b --> b; b --> a;
     ```

   + 状态表示：`f[i][0/1]`：表示以`i`为根节点的子树的情况，`0`表示node没有选，`1`表示node选，其值为各自方案最大值

   + 状态计算：

     + 初始化：`f[node][0] = 0; f[node][1] = val[node];`：将自己的权值记录
     + 更新：
       1. `f[node][0] += max(f[son][0], f[son][1]);`：node不选，则孩子都可以
       2. `f[node][1] += f[son][0];`：node选，则孩子必须不选

   ```c++
   int f[N][2];
   void dfs(int node, int father) {
   	f[node][0] = 0; f[node][1] = val[node];
       for (int son, e = head[node]; e; e = lext[e]) {
           son = to[e];
           if (son == father) continue;
           dfs(son, node);
           
           f[node][0] += max(f[son][0], f[son][1]);
           f[node][1] += f[son][0];        
       }
   }
   //dfs(root, root); max(f[root][0], f[root][1]);
   ```

2. 战略游戏：对于一棵树，染色一个点，可以染色周围边，求让所有边都被染色的方案的染色点的个数的最小值

   > 没有上司的舞会：每条边上最多选一个点，最大权值
   >
   > ​            战略游戏：每条边上最小选一个点，最小权值

   + 自动机模型：对于相邻结点，如果当前结点不染色，那么周围结点必须染色；如果当前结点染色，则周围结点都可

     ```mermaid
     graph LR; a[不染0]; b[染色1]; a --> b; b --> b; b --> a;
     ```

   + 状态表示：`f[i][0/1]`表示`i`为根结点的子树的情况，`0`表示node没有染，`1`表示node染，其值为方案集合最大值

   + 状态计算：

     + 初始化：`f[node][0] = 0; f[node][1] = 1;`：记录node的状态
     + 更新：和没有上司的舞会对称

   ```c++
   int f[N][2];
   void dfs(int node, int father) {
       f[node][0] = 0, f[node][1] = 1;  //初始化node选不选
       for (int son, e = head[node]; e; e = lext[e]) {
   		son = to[e];
           if (son == father) continue;
           dfs(son, node);
           
           f[node][0] += f[son][1];  //如果node不选，那么node到son的边被染色必须选son
           f[node][1] += min(f[son][0], f[son][1]);  //如果node选了，那么son选不选无所谓
       }
   }
   //dfs(root, root); min(f[root][0], f[root][1]);
   ```

3. 皇宫守卫：对于一棵树，有点权，染色一个点，可染色周围的点，问让所有的点染色的方案的最小值

   > 战略游戏：每个点可以染色周围的边，要求所有的边染色
   >
   > 皇宫守卫：每个点可以染色周围的点，要求所有的点染色

   + 自动机模型：

     0. 父结点不染，但父结点的父结点染色：子结点可染可不染
     1. 父结点不染：子结点至少一个染色
     2. 父结点染色：子结点可染可不染

     ```mermaid
     graph LR; 0[不染色父亲染色0]; 1[不染色孩子染色1]; 2[染色2];
     	0 --向相邻结点转移--> 2
     	1 --向孩子转移--> 2
     	1 --向父亲转移--> 0
     	2 --向孩子转移--> 0
     	2 --向父亲转移--> 1
     	2 --向周围结点转移--> 2
     ```

   + 状态表示：`f[i][0/1/2]`：表示以结点`i`为根的子树的情况，`0/1/2`表示如上图所示，其值为方案集合最小值

   + 状态转移：

     + 初始化：
       0. `f[node][0] = 0;`：累加
       1. `f[node][1] = INF;`：取孩子染色最小值
       2. `f[node][2] = val[node];`：累加，先添加染色自己的代价
     + 转移：
       0. $f_{node, 0} = \sum { min(f_{son, 1}, f_{son, 2})}$：node由父节点染色，则son要么由son的儿子染色，要么被自己染
       1. $f_{node, 1} = \mathop{min}\limits_{选择一个儿子k}\{f_{k, 2} + \mathop{\sum}\limits_{son \neq k} min(f_{son, 1}, f_{son, 2})\}$：如果node被某个儿子染色，则要找到最小值——有一个结点被自己染色，其他结点既可以被其儿子染色，也可以被自己染色
       2. $f_{node, 2} = \sum { min\{f_{son, 0}, f_{son, 1}, f_{son, 2} \}}$：node染色，那么son既可以被父节点染色，也可以被子子节点染色，要么可以被自己染色。

   ```c++
   int f[N][3];
   void dfs(int node, int father) {
       f[node][0] = 0; f[node][1] = INF; f[node][2] = val[node];
       for (int son, e = head[node]; e; e = lext[e]) {
           son = to[e];
           if (son == father) continue;
           dfs(son, node);
           
           f[node][0] += min(f[son][1], f[son][2]);
           f[node][2] += min({f[son][0], f[son][1], f[son][2]});
       }
       
       //对于被孩子染色，其中f[node][0]就存储了所有子节点的min，但是其中包含要迭代的孩子，减去
       for (int son, e = head[node]; e; e = lext[e]) {
           son = to[e];
           if (son == father) continue;
           
           //f[son][2], f[node][0] - min(f[son][1], f[son][2]);
           f[node][1] = min(f[node][1], f[son][2] + f[node][0] - min(f[son][1], f[son][2]));
       }
   }
   //dfs(root, root); min(f[root][1], f[root][2]);  //根节点肯定不会被父节点染色
   ```
