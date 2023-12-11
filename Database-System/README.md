+ Reference：
	+ [DB-Engines Ranking](https://db-engines.com/en/ranking)
	+ CMU 15445：
		+ B站Moody老师

+ 数据库下更细分方向：解析，计算，存储

## Primer

+ Data数据
+ DB, DataBase数据库
+ DBMS, DataBase Managment System数据库管理系统
+ Data Model：
	+ SQL：Relational
	+ no-SQL：
		+ key value pair
		+ graph
		+ document
+ DML, Data mainipulation language：可理解为通俗意义上的增删改查的方式
	+ Procedural：带过程的DML，即Relational Algebra关系代数
	+ No-Procedural/Decalarative：不带过程的DML，即Relational Calculus
	以上两者解耦
	+ SQL is the defacto事实 standard(many dialects方言)
>除了DML还有DDL, Data Definetion Language, DCL, Data Control Language或者

+ Impl：
	+ Data Model：A data model is a collection of concepts for describing the data in a databse.一种抽象的概念的描述
	+ Schema模式：A schema is a description of a particular collection of data, using a given data model.（what？和data model的区别是啥？）

	有说模式是数据模型的实例化，比如数据模型是关系型，然后一个确切的表是一个模式

	+ Table/Relation：A relation is an unordered set that contain the relationship of attributes that represent entities.
		+ 一个n-ary的Relation相当于Table with n columns
	+ Tuple/Attribute/Domain：A tuple is a set of attribute values(alse known as the domain) in the relation.
	+ Value：
		+ atomic/scalar标量的（对应vector向量的）
		+ `NULL`

+ Use
	+ primary key主键
	+ foreign key外键

## 关系代数与SQL

+ Select选择 ： $\sigma_{predicate}(R)$ ，按条件找行。
	```sql
	SELECT * FROM R
	WHERE redicate
	```

+ Projection投影： $\Pi_{A1, A2, ..., An}(R)$ ，取出对应列（或其变化后的）。
	```sql
	SELECT A1, A2, ..., An
	FROM R
	```

+ Union联合： $R \cup S$ ，合并表，汇总两个表中都有的列
	```sql
	(SELECT * FROM R) UNION ALL (SELECT * FROM S)  -- 不去重
	(SELECT * FROM R) UNION     (SELECT * FROM S)  -- 去重
	```

+ Intersectoin取交集： $R \cap S$ ，表取交集，取出两个表中都有的列的都有的行
	```sql
	(SELECT * FROM R) INTERSECT (SELECT * FROM S)
	```

+ Difference取补集： $R - S$ ，取出两个表都有的列的前者有而后者没有的
	```sql
	(SELECT * FROM R) EXCEPT (SELECT * FROM S)
	```

+ Product笛卡尔积： $R \times S$ ，全列排列组合（不同表的同名列认为不同）
	```sql
	SELECT * FROM R CROSS JOIN S;  -- 或者直接使用JOIN
	SELECT * FROM R, S;            -- 隐式调用
	```

+ Join连接： $R \bowtie S$ ，取出表共有行
	```sql
	SELECT * FROM R NATURAL JOIN S;  -- 通常也就直接使用JOIN
	```

+ 其他：
	+ 基础： $\vee$ and， $\land$ or
	+ Rename，Assignment，Duplicate Elimination，Aggregation聚集，Sort，Division。

## Storage

比如Redis被成为缓存，其所有数据在内存中，这里讨论面向磁盘的DBMS

![disk-oriented DBMS.png](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Database-System/disk-oriented DBMS.png)

+ 关于系统调用`mmap`：
	+ 众所周知，内存大小肯定远远小于硬盘，mmap可以在内存中构建虚拟内存其与硬盘一样大！软件直接访问虚拟内存，相当于访问具体的硬盘页，由操作系统实现将对应的页Load到实际的（物理）内存中，但是如果物理内存已经满了，此时如果还需要新的页，此时操作系统不知道已经Load的页哪些是不需要的，就卡住了。
	+ 只读还行，如果并发写的话，就有其他新的问题

	所有有很多相关的系统调用。

所以数据库希望自己去管理这种页的访问。
>The OS is not your firend

+ 好处：
	+ 对于脏页的写回实际可以控制
	+ prefetching
	+ 缓存替换策略
	+ 并发调度

+ 核心矛盾
	+ 数据库文件在磁盘中如何表示
	+ 数据库如果管理数据在内存和硬盘之间的流动

File Storage -> Page Layout -> Tuple Layout

+ A page is fixed-size block of data.
	+ It can contain tuples, meta-data, indexes, log recoreds
	+ each page is given a unique identifier

### Table Heap
表堆

可能是常规的具体的存储每个页的手段？即向xv6的free list一样所有的页一次排开，也不考虑他们的逻辑，主要是知道自己有哪些页？

那么能扩展么？肯定需要能扩展呀？

扩展时直接添加一个新的heap file？

所以在有关于heap flie的meta data？

怎么实现？
+ Link List
+ Page Directory

# MISC

+ Consistency（一致性）在不同语境下的含义
	+ 分布式领域中的Consistency即CAP理论中的“C”，严格的说应该值的是[Linearizability](https://cs.brown.edu/~mph/HerlihyW90/p463-herlihy.pdf)中的一致性模型。
	+ 数据库领域中的Consistency翻译成中文是一致性（或者说内部一致性（这个是和下面提到的外部一致性对应），但是普遍就叫一致性），它指的是ACID中的C，所以这个应该严格上来说应该是Consistency in ACID，指的是事务的执行一定保证数据库终端数据的约束不被破坏。
	+ 数据库领域中还有External Consistency外部一致性，是[这篇论文](https://www.semanticscholar.org/paper/Information-storage-in-a-decentralized-computer-Gifford/fafaebf830bc900bccc5e4fd508fd592f5581cbe?p2df)（3.1节），先定义Serializability可串行化，再定义External Consistency外部一致性，指的是符合绝对时间约束的Serializability，所以它描述的应该是ACID中的“I”隔离性。

	---

	+ 外部一致性为什么还需要在可串行化之上再加上一个“绝对时间”的限制？因为可串行化描述是单机数据库，而外部一致性描述是分布式数据库，即一个写、一个读、一次执行，但是读可能为空，这是符合可串行化的，但是也真实的发生在分布式数据库中了，所以要加上绝对时间的限制。
