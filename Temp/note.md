+ All expressions can use function call notation

+ 还记得数据结构中将中缀表达式转换成逆波兰式嘛？中缀表达式是人计算的，逆逆波兰式才是给计算机计算，我们模拟一下两种表达式的计算过程也确实是这样的，可是我们写的代码都是中缀表达式，那么计算机是怎么识别的呢？这其实是一个很自然的过程

  C++中有运算符重载，即`a + b`实际上是一个函数调用`operator + (a, b)`，我们发现后者就是一种逆波兰式，这个不明显我们再看一个`operator * (operator  + (a, b), operator - (c, d))`，这个是不是就明显了？

  实际上这里不是按照逆波兰式的通过一个栈线性进行，而是通过递归——expression tree
  
+ Types of Expressions:

  + Primitive expressions
  + Call exporessions