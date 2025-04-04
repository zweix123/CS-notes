+ Reference
	+ MIT的[6.824](https://pdos.csail.mit.edu/6.824/schedule.html)
		+ [野生字幕翻译](https://mit-public-courses-cn-translatio.gitbook.io/mit6-824/)（作者没有说翻译的哪一年的课程，我个人猜测是21年的）

## 为什么需要分布式

+ Drivens驱动力：
	+ 并发：大量的CPU、大量的内存、大量的硬盘和大量的并行计算
	+ 容错fault-tolerates：一个机器崩溃完全可以将其任务切换到另一台
	+ 一些问题天然在空间上是分布的，比如转账
	+ 安全security：比如有些代码不被信任，但仍然需要和它交互，可将其部署在单独的机器，通过网络协议使用，限制**出错域**

+ Challenges挑战：主要是由于并发带来的
	+ 多机交互
	+ 故障处理
	+ 性能评估

## 分布式性能评价

+ 可扩展性/可伸缩性Scalability，即只要增加机器数量，系统就应该提高相应的性能；对应的，也能自由的去掉机器  
	以web服务为例，可以通过增加web服务器以分散用户的访问来增加系统可承受的访问量，但是诸如数据库这样的微服务不能通过简单的添加机器来解决。即可扩展性可描述为通过架构设计使很难实现的“通过增加机器的方式实现扩展”得以实现。

+ 容错Fault-Tolerance：在大数定理下，即使一个计算机出现错误的概率很低，但是当系统中的机器足够多时，出现错误几乎是必然（在特定的故障范围内）。

	+ 可用性Availabilty：service continues despite failures  
		比如通过复制replication，多副本，当然多副本就要不可避免的考虑一致性问题

	+ 自我可恢复性Recoverability：系统在寄掉后通过修复可以按之前的继续正常运行  
		比如通过非易失存储non-volatile storage，不断将数据存入硬盘

	>这里将实体机器放远一点有利于容错性，但是远距离的通信花费更多的时间

+ 一致性Consistency，多副本间数据一致
	+ 强一致性Strong Consistency：
	+ 弱一致性：  
		可以想象，强一致性的保证需要各个机器间大量的通信，这里的开销非常大，所以虽然弱一致性可能导致系统出错，但是工程上仍然是有必要的  
		或者是需要对比所有副本的数据

## Consistenct issues and Consensus Algorithms
>一致性问题和共识算法

+ Reference
	+ https://draveness.me/consensus/

+ 什么是一致性？一个解释是：集群中所有节点中的数据完全相同并且能够对某个Proposal提案达成一致
+ 什么是共识算法？保证分布式系统一致性的方法

+ 一致性算法应该在并行系统中发挥的责任（出自Raft）
	+ 安全：在所有非拜占庭情况，即使网络延迟，分区、丢包、duplication或者重排
	+ 可用性
		+ （一定程度上）容忍fail
		+ 可恢复
	+ 不依赖时序，错误时钟和非常延迟的消息也是正确的
	+ 保证集群大部分可响应

+ CAP理论
	>+ C：一致性Consistency
	>+ A：可用性Availability
	>+ P：分区容错性Partition tolerance

	+ 来自加州伯克利大学的Eric Brewer的[论文]()
	+ 内容：**证明**在**异步**的网络模型中，节点由于没有时钟、仅仅能够根据接收的消息做判断，导致系统只能在一致性、可用性和分区容错性，这三种特性中保证两种
		+ 这里的一致性是强一致性或者说绝对一致性
		+ 现实世界不存在绝对异步的网络环境，就算时钟不能相同、但时钟的更新频率可以完全相同

+ 拜占庭将军问题：多个军队准备进攻城池，如果有**大多数**军队一起进攻就能攻下，而是否选择进攻也是听从**大多数**的。但是如果出现叛徒军队对不同军队传播不同消息呢？

+ ELP不可能定理
	+ 来自Fisher、Lynch和Paterson的[论文](https://ilyasergey.net/CS6213/_static/02-consensus/flp.pdf)
	+ 内容：No completely asynchronous consensus protocol can tolerate even a single unannounced process death在网络可靠并且存在节点失效的异步模型系统中，不存在一个可以解决一致性问题的确定性算法。
	+ 但是**科学告诉你，什么是不可能的；但工程则告诉你，只要付出一些代价，就可以把它变成可能**，这就是工程的魅力。

+ 传统一致性算法，这是在这个主题下要讨论的，主要解决非拜占庭将军问题
	+ Paxos，其实是**一类**协议，是被证明正确性的
		+ Basis Paxos
		+ Multi-Paxos
	+ Raft：Multi-Paxos的变种

+ 区块链的共识算法，区块链可以说是拜占庭将军问题了，和当前主题不同，在[这里](Interdisciplinary/Web3/README.md)讨论

### Split Brain脑裂

中心式分布式系统的问题

不会出现脑裂的系统不能建立，但是可以建立**能够自动完成故障切换**的系统，即网络故障时将网络分成两份，即网络分区

+ Majority Vote过半票决/quorum多数投票：在任何时候为了完成任何操作，必须凑够过半的服务器来批准相应的操作；如果系统有$2 \times F + 1$个服务器，那么系统最多可以接受$F$个服务器出现故障，仍然可以正常工作
	+ 服务器数量必须是奇数
	+ 还有一个好处是，任意两组过半服务器，至少有一个服务器是重叠的。

## 2PC

此2PC非数据库中事务的2PC。

中心式的分布式系统实现中，中心节点为coordinator，被中心节点调度的其他业务节点为participant。

此时分布式事务分成两个阶段。

1. 提交请求（投票）
	1. coordinator向participant发送请求和事务内容
	2. participant执行事务内容并记录undo日志（用于回滚）和redo日志（用于重放）
	3. participant完成后向coordinator返回执行结果
2. 提交（执行）：成了自不必多数，但是如果有一个participant出现问题，就全部回滚。
	+ 不过既然有了redo，可能可以快速的向no重发，然后整合。

+ 问题：
	+ 中心式，中心节点挂了就G了
	+ 我们发现整个过程是同步的，并发问题很大
	+ 这已经很强一致了，但是仍然可能不一致，即部分participants根本没收到请求
		+ 设置超时假装no不久行了？如果这个participant永久的G了呢？怎么自适应？


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
