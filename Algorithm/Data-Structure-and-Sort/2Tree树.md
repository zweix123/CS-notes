# 树Tree

+ 相关术语：

  + root根、edge边、leaf叶子结点

  + child儿子、parent父亲、siblings兄弟结点

    grandparent祖父、grandchild孙子

    ancestor祖先、descendant后裔，如果一对祖先后裔不同则是真祖先、真后裔（真proper）

  + path路径：点到点、length长：路径上边的条数、depth深度：结点到根的路径的长、height高：树中深度最大的叶子的深度

+ 实现：由于每个结点的儿子数量是不确定的，通常每个结点建立一个链表，从左到右分别指向

  ```c++
  struct TreeNode {
      Object   element;       // 结点值
      TreeNode *firstChild;   // 结点的第一个儿子
      TreeNode *nextSibling;  // 该节点其右边的第一个兄弟（如果有）
  };
  ```

1. 应用1：操作系统的目录结构

   > UNIX文件系统中每个目录还有一项指向该目录本身和另一项指向该目录的父目录，所以不是树是treelike类树

+ preorder tarversal前序遍历  ：对结点的处理工作是在它的诸儿子结点被处理之前进行的

  postorder traversal后序遍历：对结点的处理工作是在它的诸儿子结点被处理之后进行的

## 二叉树Binary Tree

+ 定义：每个结点不能有多于两个儿子的树

  > + 平均深度$O(\sqrt{N})$

+ 实现：

  ```c++
  struct BinaryNode {
      Object     element;  // The data in the node
      BinaryNode *left;    // Left child
      BinaryNode *right;   // Right child
  }
  ```

+ inorder traversal中序遍历：左根右

1. 表达式树：树叶是operand操作数、其他结点是operator操作符
   + 不同遍历方式对应不用表达式的形式
   + 将表达式转换成表达式树：维护一个维护结点的栈，依次读入
     1. 操作数：构造成结点压入栈
     2. 操作符：构造成结点，弹出栈顶两个元素作为其左右儿子，在讲该结点压入栈

## 二叉查找树Binary Search Tree

+ 定义：结点值为相互之间有偏序关系的值，对于每个结点其左子树的所有项的值都小于该结点、右子树都大于

```c++
template<typename Object, typename Comparator=less<Object> > class BinarySearchTree {
public:
    BinarySearchTree();
    BinarySearchTree(const BinarySearchTree & rhs);
    ~BinarySearchTree() {
        makeEmpty();
    }
    
    const Comparable & findMin() const;
    const Comparable & findMax() const;
    
    bool contains(const Comparable & x) const {
        return contailns(x, root);
    }
    bool isEmpty() const;
    void printTree() const;
    
    void makeEmpty();
    void insert(const Comparable &x) {
		insert(x, root);
    }
    void remove(const Comparable &x) {
        remove(x, root);
    }
    
    const BinarySearchTree & operator= (const BinarySearchTree & rhs) {
        if (this != &rhs) {
            makeEmpty();
            root = clone(rhs.root);
        }
        return *this;
    }

private:
    struct BinaryNode {
        Comparable element;
        BinaryNode *left;
        BinaryNode *right;
    	
        BinaryNode(const Comparable & theElement, BinaryNode *lt, BinaryNode *rt) : element(theElement), left(lt), right(rt) {}
    };
    
    BinaryNode *root;
    Comparator isLessThan;
    
    void insert(const Comparable & x, BinartNode * & k) const {
        if (t == NULL) t = new BinaryNode(x, NULL, NULL);
        else if (isLessThan(x, t->element)) insert(x, t->left);
        else if (isLessThan(t->element, x)) insert(x, t->right);
        else ;  // Duplicate; do nothing
    }
    void remove(const Comparable &x, BinaryNode * &t) {
        if (t == NULL) return ;  // Item not found; do nothing
        if (isLessThan(x, t->element)) remove(x, t->left);
        else if (isLessThan(t->element, x)) remove(x, t->right);
        else if (t->left != NULL && t->right != NULL) {
			t->element = findMin(t->right)->element;
            remove(t->element, t->right);
        } else {
            BinaryNode *oldNode = t;
            t = (t->left != NULL) ? t->left : t->right;
            delete oldNode;
        }
    }
    BinaryBde * findMin(BinartNode *t) const {
		/*
        if (t == NULL) return NULL;
        if (t->left == NULL) return t;
        return findMin(t->left);
    	*/
        if (t != NULL)
            while (t->reight != NULL)
                t = t->right;
        return t;
    }
    BinaryBde * findMax(BinartNode *t) const;
    bool contains(const Comparable &x, BinaryNode *t) const {
        if (t == NULL) return false;
        else if (isLessThan(x, t->element)) return contains(x, t->left);
        else if (isLessThan(t->element, x)) return contains(x, t->right);
        else return true;  // Match
    }
    
    void makeEmpty(BinaryNode* &t) {
        if (t != NULL) {
            makeEmpty(t->left);
            makeEmpty(t->right);
            delete t;
        }
        t = NULL;
    }
    void printTree(BinaryNode *t) const;
	BinartNode * clone(BinaryNode *t) const {
        if (t == NULL) return NULL;
        return new BinaryNode(t->element, clone(t->left), clone(t->right));
    }   
}
```

+ 平均深度$O(logN)$：

  + 深度的证明：

    + internal path length内部路径长
    + $D(N)$具有N个结点的某课树T的内部路径长且$D(1)=0$

    一颗N结点树是由一颗$i$结点左子树和一颗$N - i - 1$结点右子树以及深度为0的根结点组成，则可以递推

    $D(N) = D(i) + D(N - i - 1 + N - 1$因为所有子树的大小都是等可能的出现

    这对二叉查找树是成立的，因为子树的大小只依赖于第一个插入到树中的元素的相对的rank

    但是对二叉树不成立，此时D（i）和D（N - i - 1）的平均值都是$\frac{1}{N}\sum_{j = 0}^{N - 1}D(j)$，故$D(N) = \frac{2}{N}[\sum_{j = 0}^{N - 1}D(j)] + N - 1$

  

+ 上面实现的问题：删除只从右子树开始，会出现，树的形态向左偏从而导致效率下降

  + balance平衡：不允许结点深度过深
    + AVL树
  + self-adjusting自调整：在操作后进行调整
    + splay tree伸展树



### AVL树

> AVL Adelson-Velskii and Landis
>
> balance condition平衡条件

将空子树高度定义为-1，AVL的平衡条件是要求每个结点的左子树和其右子树的高度最多差1

理论上AVL的树的高度最多$1.44log(N + 2) - 1.328$，但其实际高度只比logN稍微多一点

+ 插入——rotation旋转
