存储是分布式系统中的一个重要抽象，在MIT 6.824中有大量的讨论，就像DDIA（Designing Data-Intensive Applications）上说的Many application today are **data-intensive**，as opposed to compute-intensive. Raw CPU power is rarely a limiting factor for these applications—bigger problems are usually the amount of data, the complexity of data, and the speed at which it is changing.

## Replication

+ Replication的目的：为了Fail-Tolerance
	+ Fail-Tolerance的目的：Availability

+ Replication的限制：
	+ 要求副本的问题是独立的
		+ 不能解决软件bug和硬件设计缺陷
		+ 不能解决比如同一批生产的机器都有散热的问题
	+ 还有一个方面就是所有副本都有在瞬间摧毁了，比如地震海啸毁掉数据中心，更极端是陨石撞地球，为了这样情况的高可用可能需要在外太空设置服务器
		>这其实引出来了一个工程问题，我们当然可能在外太空部署服务器，但是成本呢？

+ Replication的意义：因为复制就意味着需要成倍的资源消耗，工程上需要权衡效益和成本

+ Replication的方法：
	+ State Transfer状态转移：完整拷贝、互为副本
		+ 当然也可以类似Git一样进行增量的拷贝
	+ Replicated State Machine复制状态机：增量式的
		>基于这样的事实——程序，就是状态机

	后者较于前者的诱惑是：事件往往比状态要小

### Replicated State Machine

![复制状态机模型](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/复制式状态机架构.png)