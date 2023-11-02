# 表Table

## 线性表List

> 空表、前驱、后继

### 顺序存储: Sequence
```c++
template<typename Object>
class Vector {
public :
    explicit Vector(int initSize = 0) 
        : theSize(initSize), theCapacity(initSize + SPARE_CAPACITY) {
    	objects = new Object[theCapacity];         
	}
    Vector(const Vector& rhs) : objects(nullptr) {
        operator=(rhs);
    }
	~Vector() {
        delete[] objects; 
    }
    const Vector& operator = (const Vector& rhs) {
        if (this != &rhs) {
            delete[] objects;
            theSize = rhs.size();
            theCapacity = rhs.theCapacity;
            
            objects = new Object[capacity()];
            for (int k = 0; k < size(); ++ k)
				objects[k] = rhs.objects[k];
        }
        return *this;
    }
    void resize(int newSize) {
        if (newSize > theCapacity)
			reserve(newSize * 2 + 1);
        theSize = newSize;
    }
    void reserve(int newCapacity) {
        if (newCapacity < theSize)
            return;
        Object* oldArray = objects;
        
        objects = new Object[newCapacity];
        for (int k = 0; k < theSize; ++ k)
            objects[k] = oldArray[k];
        theCapacity = newCapacity;
        delete[] oldArray;
    }
    Object& operator [] (int index) {
        return objects[index];
    }
    const Object& operator [] (int index) const {
        return objects[index];
    }
    
	bool empty() const { return size() == 0; }
    int size() const { return theSize; }
    int capacity() const { return theCapacity; }
    
    void push_back(const Object& x) {
        if (theSize == theCapacity)
            reserve(2 * theCapacity + 1);
        objects[theSize++] = x;
    }
    void pop_back() { theSize--; }
    const Object& back() const { return objects[theSize - 1]; }
    
    typedef Object* iterator;
    typedef const Object* const_iterator;
    
    iterator begin() { return &objects[0]; }
    const_iterator begin() const { return &objects[0]; }
    iterator end() { return &objects[size()]; }
    const_iterator end() const { return &objects[size()]; }
    
    enum { SPARE_CAPACITY = 16 };
private :
    int theSize;
    int theCapacity;
    Object* objects;
};
```

### 链式存储: Linked List

> Double Linked List双向链表

```c++
template<typename Object>
class List {
private:
    struct Node {
    	Object data;
        Node *prev;
        Node *next;
        Node(const Object& d = Object(), Node *p = nullptr, Node *n = nullptr) : data(d), prev(p), next(n) {}
    };
public :
    class const_iterator {
    public :
        const_iterator() : theList(nullptr), current(nullptr) {}
        const Object& operator* () const { return retrieve(); }
        const_iterator& operator++ () {
            current = current->next;
            return *this;
        }
        const_iterator& operator++ (int) {
            const_iterator old = *this;
            ++ (*this);
            return old;
        }
        bool operator== (const const_iterator& rhs) const 
			{ return current == rhs.current; }
        bool operator!= (const const_iterator& rhs) const 
			{ return !(*this == rhs); }
    protected:
		const List<Object> *theList;
		Node *current;
        const_iterator(const List<Object> &lst, Node *p) : theList(&lst), current(p) {}
        void assertIsValid() const {
            if (theList == nullptr || current == nullptr || current == theList->head);
//                throw IteratorOutOfBoundsException();
        }
        Object& retrieve() const { return current->data; }
        
		friend class List<Object>;
    };
    class iterator : public const_iterator {
    public:
        iterator() {}
        Object& operator* () { return const_iterator::retrieve(); }
		const Object& operator* () const 
			{ return const_iterator::operator*(); }
        iterator& operator++ () {
            const_iterator::current = const_iterator::current->next;
            return *this;
        }
        iterator operator++ (int) {
            iterator old = *this;
            ++(*this);
            return old;
        }
 	protected:
        iterator(const List<Object> & lst, Node *p) : const_iterator(lst, p) {}
        friend class List<Object>;
    };
public :
    List() {
        init();
    }
    List(const List& rhs) {
        init();
        *this = rhs;
    }
    ~List() {
        clear();
        delete head;
        delete tail;
    }
    const List &operator= (const List& rhs) {
        if (this == &rhs) return *this;
    	clear();
        for (const_iterator itr = rhs.begin(); itr != rhs.end(); ++ itr) push_back(*itr);
        return *this;
    }
    iterator begin() {
//		return iterator(head->next);
        return iterator(*this, head->next);
    }
    const_iterator begin() const {
//		return const_iterator(head->next);
    	return const_iterator(*this, head->next);
	}
    iterator end() {
        return iterator(*this, tail);
    }
    const_iterator end() const {
        return const_iterator(*this, tail);
    }
    
    int size() const { return theSize; }
    bool empty() const { return size() == 0; }
    
    void clear() {
        while (! empty()) pop_front();
    }
    
    Object& front() { return *begin(); }
    const Object& front() const { return *begin(); }
    Object& back() { return *--end(); }
    const Object& back() const { return *--end(); }
    void push_front(const Object& x) { insert(begin(), x); }
    void push_back(const Object& x) { insert(end(), x); }
    void pop_front() { erase(begin()); }
    void pop_back() { erase(--end()); }
    
    iterator insert(iterator itr, const Object& x) {
        itr.assertIsValid();
        if (itr.theList != this);
//            throw IteratorMismatchException();
            
        Node *p = itr.current;
        theSize++;
        return iterator(*this, p->prev = p->prev->next = new Node(x, p->prev, p));
    }
    iterator erase(iterator itr) {
        itr.assertIsValid();
        if (itr.theList != this) ;
//			throw IteratorMismatchException();
        
		Node *p = itr.current;
        iterator retVal(*this, p->next);
        p->prev->next = p->next;
        p->next->prev = p->prev;
        delete p;
        theSize --;
        return retVal;
    }
    iterator erase(iterator start, iterator end) {
        for (iterator itr = start; itr != end; ++ itr)
			itr = erase(itr);
        return end;
    }
private:
    int theSize;
    Node* head;
    Node* tail;
    
    void init() {
        theSize = 0;
        head = new Node;
        tail = new Node;
        head->next = tail;
        tail->prev = head;
    }
};
```

## 栈Stack

+ 平衡符号（括号匹配）

+ 后缀postfix表达式

  > 后缀表达式在不使用括号的情况下实现算术符号的优先级

  + 中缀infix转换成后缀：
    1. 操作数立刻输出
    2. 对于操作符从栈顶开始检测，弹出优先级比其大于等于的操作符输出，最后将其压入栈
    3. 对于括号特殊处理，栈中的左括号只能被右括号弹出（并不输出）
    4. 输入完毕，栈中元素依次弹出

+ 函数调用：

  > 尾递归：递归语句在函数的末尾：不好的
  >
  > 可以机械的将尾递归转换成迭代

## 队列Queue

