## 如何存图?
>包括树和平常的图

### 学术的方案

+ 树：
	+ 二叉树：在结构体中分出两个指针来表示左右child
	+ 平常的树：
		```cpp
		struct TreeNode {
			Object    element;      // 结点内容
			TreeNode* firstChild;   // 结点的第一个儿子
			TreeNode* nextSibling;  // 结点的右边第一个兄弟(如果有)
		}
		```

+ 图：

### 竞赛的方案

+ 小图：对结点编码，使用矩阵，矩阵下标表示结点编号，矩阵中的值即为边的信息
+ 偷懒：`vector<edge> g[点数]`，对结点编码，`g`的下标即为结点的编号，然后`push_back`每个边
+ 前式链向星：（并不明白为什么是这个名字）算了算了不想讲了反正这个数据结构挺优美的
	```cpp
	int head[N], lext[M << 1], to[M << 1], tot, val[M << 1];
	void add(int x, int y, int z) {
		text[++ tot] = head[x]; head[x] = tot; to[tot] = y; val[tot] = z;
	}
	```

	+ 初始化：tot -> 0, head\[\] -> 0
	+ 双向边：调整tot，通过`^`切换
