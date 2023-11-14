+ Ref
	+ [Paper](https://raft.github.io/raft.pdf)：强烈建议先独立按自己的学习方法读完论文再使用其他资料
		+ 论文开始时反复强调understandability，在选择算法组成时也是优先从这个方面考虑，但是不免主观，使用下面两个技术来让其更合适
			+ 问题划分：领导选举，日志变更，安全，成员变更
			+ 简化状态空间（与trade-off）
	+ [Raft 可视化](http://thesecretlivesofdata.com/raft/)

# Intro

Raft是一个管理Replicated Log的Consensus Algorithm

+ 什么是Replication：[笔记](./Storage/README.md#replication)
+ 什么是Consensus：[笔记](./README.md#consistenct-issues-and-consensus-algorithms)
+ 什么是Paxos：在Raft之前，Paxos几乎是一致性算法的代名词
	+ 缺点：
		+ 很难准确理解，即使是对专业研究者和领域教授
			+ Paxos复杂难懂但是又没有其他适合教学的替代算法
		+ 很难正确实现。复杂加上某些理论描述模糊
			+ Paxos本身是点对点模型，最后为了性能考虑建议弱领导力的模型，但是在实际应用中通常是中心式的，所以There are significant gaps between the description of the Paxos algorithm and the needs of a real-world system. . . . the final system will be based on an **un-proven** protocol（注意Paxos的正确性是得到证明的，这里的un-proven是因为实现和理论的gap太大了）

	因为从工业界和学术界需求出发，斯坦福大学博士生Diego Ongaro及其导师John Ousterhout提出了Raft算法（2013年），它的最大设计目标是可理解性understandability

	+ 但是由于Raft是中心式的，所以理论上其性能是比不上Paxos的

Raft会以Library的形式存在于服务中，即每个服务的副本由两部分组成：应用程序代码和Raft库

安全性和性能已经被证明/验证和比较

+ Features
	+ Strong leader：单领导人让数据的流向更简单
	+ Leader election：使用随机timer选举领导，在心跳检测的基础上引入少量机制，用来快速解决冲突
		+ 这里我翻译不好，我理解是一种trade-off，即随机化虽然增加了不确定性，但是也减少了状态空间
	+ Membership changes：使用joint consensus的方法更改集群，运行两种不同的配置重叠

# Decomposition

+ 约定：
	+ 我们称集群中的机器为server，那么自然外界的我们服务的就是client
	+ server有三个状态：leader，follower，candidate
		+ 一般情况下：只有一个leader，其他的都是follower

通常集群server数量为5，这样系统可以tolerate two failures。

+ leader简介：
	+ handle all client requests
		>如果client向follower发请求，follower会将其重定向到leader
+ follower简介：
	+ passive的，不发request，只response to request from leader and candidates
+ candidate简介

转换如下图  
![状态机](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/状态机.png)

+ terms任期：

	从下图可以看到
	+ term由连续的整数表示
	+ 有两种类型term
		+ election -> normal operation：一个及以上candidate尝试变成leader，其中一个candidate赢得选举，对应的server变成leader
		+ no emerging leader：发生split vote，即没有leader。很快的开始新一个term

		Reft保证每段Term做多只有一个leader

	![任期](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/term.png)

	term在raft中发挥一个逻辑锁的作用：每个server维护一个current term数字，其单调增长，当server通信时则进行exchanged
	+ 如果一个server的current term比另一个小，则小的更新
	+ 如果candidate或者leader发现它的current term out of date，它们立刻变成follower
	+ 如果一个server收到request的term小于它的current term，则拒收。

+ RPC：server重发rpc如果它没有收到response，且它们也会并行发送以获得最高性能
	+ `RequestVote`：candidate as server
	+ `AppendEntrie`：leader as server：
		+ 复制log entry
		+ heartbeat

## Leader Election
如果一个存在的leader fail了，必须选举新的leader

+ heartbeat机制：
	+ server启动时是follower，只有持续从leader收到heartbeat(没有log entry的`AppendEntries`)，就一直是follower
	+ 如果一个follower在election timeout时间内没有收到heartbeat则开启一个新的term

+ 选举流程：
	1. Follower增大自己的current term，并切换到candidate状态，选举自己作为leader，并发地向集群中的其他结点发送`RequestVote`

	 该Candidate一直持续到：自己或其他赢得选举或者选举分裂/选举超时
	 + 当一个Candidate收到`AppendEntries`，对方的term大于等于自己，则承认其地位，退回到follower，否则拒绝，继续。

	+ 获胜条件：获得集群中**大多数server对同一term的vote**
	+ 选举规则：对于给定的term，一个follower只能投递一票，follower投票的标准是First-Come-First-Served
		>保证一个term只有一个leader


	2. 当一个Candidate赢得选举，其变成Leader，并向其他server发送heatbbeat

	+ readomized election timeout随机选举超时：
		>选举分裂：如果有多个follower几乎同时发起选举，此时选票很分散，每个人都不能达成获胜条件，如果同时进入下一个任期，很可能还是这样（甚至更差），需要引入其他机制。

		+ 在follower等待heartbeat期也保证大部分只有一个follower变成Candidate
		+ 用于选举期间

## Log Replication
leader必须接受从clients来的log entry并将其复制到集群的server中

一旦一个leader被选举出来，它就开始服务客户端请求

+ 复制流程：
	1. 每个client request包含一个cmd，leader将其包装成entry并追加到自己的logs中，然后通过并发地`AppendEntries`将其发送给集群中的其他结点

	+ 如果由于follower crash或者其运行的慢或者网络丢包，leader会无限重发（即使它已经给了client response）直到所有的follower最终存储所有的log entries

	2. 当这个entry已经被safely replicated时，leader将这个entry放进自己的状态机中，并将结果返回给client

+ Logs组成：由Log Entry组成
	+ Entry数据结构：
		+ Index：唯一递增整数编号
		+ Term：创建该Entry的Leader的Term number
		+ cmd

+ Log文件结构：由Log Entry组成
	+ Entry数据结构：
		+ Index：唯一递增整数编号
		+ Term：创建该Entry的Leader的Term
		+ Command

+ Commit提交
	+ 一个节点的Entry，Commit is Entry被安全地应用到状态机后
	+ 一个Entry：
		1. 创建这个Entry的Leader将它复制到大多数节点
		2. 1中的提交也提交了Leader Log中的所有前面的Entry，包括之前由其他Leader创建的Entry

	+ Follower一旦确定某个Entry被提交了，就将这个Entry应用到它自己的状态机（in log order）

+ Log matching特性保证Log coherency高度一致性

	如果不同Log中的两个Entry有完全相同的Index和Term，那么
	1. 这两个Entry一定包含相同的命令
		>证明：

	2. 在两个Log中，从该Index往前的所有Entry都分别相同
		>证明：

	+ AppendEntries一致性检查：
		+ 在请求中，Leader会带上Log中前一个紧邻Entry的Index和Term
		+ 如果Follower Log中相同的Index没有Entry，或者有Entry但Term不同，则拒绝新的Entry

	组合以上各点，通过归纳法可以证明 Log Matching Property

+ 对Log不一致的应对
	>Leader的Fail会出现Log不一致
	
	还记得上面的AppendEntries中的一致性检查嘛？如果在这个环境发现不一致，则直接暴力复制给Follower一份Header的Log
	1. 找到最后两者共同认可的Entry
	2. 多余丢掉
	3. 同步

+ 优化：
	>在上面Follower会因为Log不一致拒绝AppendEntries，怎么减少这样的情况呢？



----Safely
任何server已经将log entry去apply到它的状态机中，其他server在这个索引下不会有apply其他命令

安全的语义是确保状态机以相同顺序执行相同的命令流

任何 term 内的 leader 都包含了前面所有 term 内提交的 entries


-----Impl

+ 所有server的持久性状态：
	+ `currentTerm`：当前最新任期，从0开始，单调递增
	+ `votedFor`：当前任期内投票投向的Candidate
	+ `log[]`：Log Entries，索引从1开始
		+ Entry：状态机命令和leader收到该entry的任期
+ 所有server的易失性状态：
	+ `ccom`