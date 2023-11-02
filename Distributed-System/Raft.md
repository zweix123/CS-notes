+ Ref
	+ [Paper](https://raft.github.io/raft.pdf)
	+ [Raft 可视化](http://thesecretlivesofdata.com/raft/)

Raft是一个管理Replicated Log的Consensus Algorithm

+ Paxos：在Raft之前，Paxos几乎是一致性算法的代名词
	+ 缺点：
		+ 很难准确理解，即使是对专业研究者和领域教授
			+ Paxos复杂难懂但是又没有其他适合教学的替代算法
		+ 很难正确实现。复杂加上某些理论描述模糊
			+ Paxos本身是点对点模型，最后为了性能考虑建议弱领导力的模型，但是在实际应用中通常是中心式的，所以There are significant gaps between the description of the Paxos algorithm and the needs of a real-world system. . . . the final system will be based on an **un-proven** protocol（注意Paxos的正确性是得到证明的，这里的un-proven是因为实现和理论的gap太大了）

	因为从工业界和学术界需求出发，斯坦福大学博士生Diego Ongaro及其导师John Ousterhout提出了Raft算法（2013年），它的最大设计目标是可理解性understandability

	+ 但是由于Raft是中心式的，所有理论上其性能是比不上Paxos的

+ Raft会以Library的形式存在于服务中，即每个服务的副本由两部分组成：应用程序代码和Raft库

# Theory

Raft集群是中心式的，中心即为Leader，其他节点正常情况为Follower，在选举期为Candidate  
![状态机](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Distributed-System/状态机.png)

+ Leader，具有完全的责任，是系统的入口
+ Follower
	+ Passive
	+ Client对其的Request会被重定向到Leader
+ Candidate，特殊状态，当Follower在一段时间没有收到心跳检测则变成Candidate，发起选举

分为，选举，日志复制，成员变更

## Leader Election

+ 任期Term，Raft将时间划分成长度不固定的任期，每个任期从Election开始，选举成功就normal operation，如果no emerging leader，则进入下一个term
	+ 每个节点都会记录当前任期
	+ 节点通信会携带任期信息
		+ 如果一个节点发现自己的比其他人的小，则立刻更新
		+ 如果Candidate和Leader发现自己的任期过期了，则立刻切换到Follower状态
		+ 如果一个节点接受到携带过期任期编号的请求，则拒绝

+ 通信，通过RPC
	+ RequestVote：由Candidate在选举期发起
	+ AppendEntries：由Leader发起
		+ 用于Append Replicated Log Entry
		+ Heartbeat

+ Heartbeat机制

+ Heartbeat机制
	+ 节点启动是Follower，只要持续从Leader和Candidate收到合法RPC请求，就一直是Follower
	+ Leader定期发送心跳（空的AppendEntries）给所有Follower，即Heartbeat
	+ 如果一个Follower在Election Timeout时间内没有收到，则变成Candidate

+ 选举过程：
	+ 当一个Follower试图发起选举时
		1. 增大自己当前的Term
		2. 切换到Candidate状态
		3. 选举自己作为Leader，并发的向集群其他节点发送RequestVote RPC
		4. 直到发生下面三种情况之一
			+ 该Follower赢得此次选举，成为Leader
			+ 另一个节点赢得此次选举，成为Leader
			+ 选举超时，每个产生有效Leader

		当一个Candidate赢得选举后，就会成为Leader，然后就立刻发送心跳信息给其他所有节点来建立自己的权威，防止新的选举的发生

	+ 获胜条件：如果一个Candidate获得集群**大多数节点针对同一任期的投票**，那么它就赢得了这个任期内的选举
	+ 选举规则：针对给定的任期，每个节点最多只能投一票，投票的标准是First-Come-First-Served
		>zweix: 一个任期一票

	+ 选举分裂：比如多个Follower几乎同时的发起选举，肯可能选票很分散，导致这轮选举没有Leader的产生
		>如果这些Candidate同时进入下轮选举，上面的情况可能会无限循环下去

		**随机选举超时**：每个Candidate等待选票的时间是从一些固定时长中随机选择一个选举超时时间，然后早超时的Candidate再次发起一轮选举成为Leader

+ 如果一个Candidate在等待选举时收到Leader的RPC，会对比任期编号，如果Leader的任期大于等于自己，则承认其为合法，否则则拒绝仍然是Candidate

	这个策略基本用于共同选举帮助称为Leader的节点顺利建立权威

	+ 我们再来看这么个情况，因为网络问题一个节点误成为Candidate，此时它的任期肯定比它之前的Leader大（至少不同），这会导致其他Follower给它投票致之成为Leader，当其在向集群发送心跳信息时，之前的Leader收到了一个任期更大的Leader的后，自己就变成Follower，仍然正确。

## Log replication

当选出来一个Leader后，它就开始服务客户端的请求

+ 复制流程：
	1. 每个Client的Request包含一条Comman，将由Replicated State Machine执行
	2. Leader会将这个命令追加到它自己的Log，然后并发的通过AppendEntries RPC将其复制给其他结点
	3. 复制成功（无冲突）之后，Leader才会将这个entry应用到自己的状态机，然后将执行结果返回给Client
	+ 如果Follower Fail or 很慢 or 丢包，Leader会无限重试AppendEntries（即使它已经给客户端发送了响应），直到所有Follower最终都存储了所有的Log entries

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

## Safely
安全的语义是确保状态机以相同顺序执行相同的命令流

任何 term 内的 leader 都包含了前面所有 term 内提交的 entries


# Impl

+ 所有server的持久性状态：
	+ `currentTerm`：当前最新任期，从0开始，单调递增
	+ `votedFor`：当前任期内投票投向的Candidate
	+ `log[]`：Log Entries，索引从1开始
		+ Entry：状态机命令和leader收到该entry的任期
+ 所有server的易失性状态：
	+ `ccom`