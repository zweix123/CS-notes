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
	+ Replicated State Machine复制状态机
		>基于这样的事实——程序，就是状态机

	后者较于前者的诱惑是：事件往往比状态要小

### VMware FT
+ 特征
	+ 单核CPU
	+ 机器级别的复制，复制寄存器和内存，不需要关心软件，只有运行在支持的CPU上

VMware是虚拟机公司，现在有两个机器上的对应的两个虚拟机器，Primary和Backup

+ 非确定性事件：
	+ 客户端输入：
		+ 随机数生成器
		+ 获取当前机器的时间
		+ 获取计算机的唯一ID
	+ CPU并发，没有讨论
 

## Consensus

下面我们来引入标题，分布式一个很重要的话题就是Fail-Tolerance，一个容错的方法就是Replication，一旦复制就要面对Consensus，为了保持一致性有两种方法：State Transfer状态转移和Replicated State Machine复制状态机，后者这种增量式的方式显然更具有性能诱惑力。

下面是出现Raft论文的复制状态机（一个理想）模型：  
![复制状态机模型](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/复制式状态机架构.png)

+ 共识算法特征：
	+ 安全性：在任何non-Byzantine条件（非拜占庭条件）下都能保证安全（从不返回错误结果）
	+ 高可用性：只要**大多数**节点能工作、彼此之间以及和客户端之间能通信，整体系统的功能就完全可用
	+ 可恢复性：Fail后能从持久存储回复
	+ 不依赖时序来保证日志的一致性：最坏情况下，时钟不准、消息验证都不能导致可用性问题
	+ 通常情况下，一个命令收到集群大多数节点的响应时，这个命令就算完成了，少量响应慢的机器不影响整体的性能


### Split Brain脑裂

中心式分布式系统的问题

不会出现脑裂的系统不能建立，但是可以建立**能够自动完成故障切换**的系统，即网络故障时将网络分成两份，即网络分区

+ Majority Vote过半票决/quorum多数投票：在任何时候为了完成任何操作，必须凑够过半的服务器来批准相应的操作；如果系统有$2 \times F + 1$个服务器，那么系统最多可以接受$F$个服务器出现故障，仍然可以正常工作
	+ 服务器数量必须是奇数
	+ 还有一个好处是，任意两组过半服务器，至少有一个服务器是重叠的。






