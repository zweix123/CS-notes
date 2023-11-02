+ Reference
	+ MIT的[6.824](https://pdos.csail.mit.edu/6.824/schedule.html)
		+ [野生字幕翻译](https://mit-public-courses-cn-translatio.gitbook.io/mit6-824/)（作者没有说翻译的哪一年的课程，我个人猜测是21年的）
		+ 日志打印技巧：https://blog.josejg.com/debugging-pretty/


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

+ CAP理论
	>+ C：一致性Consistency
	>+ A：可用性Availability
	>+ P：分区容错性Partition tolerance

	+ 来自加州伯克利大学的Eric Brewer的[论文](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.67.6951&rep=rep1&type=pdf)
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

+ 区块链的共识算法，区块链可以说是拜占庭将军问题了，和当前主题不同，在[这里](../Web3/README.md)讨论