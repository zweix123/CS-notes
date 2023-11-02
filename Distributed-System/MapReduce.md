>大数据运算的代表

+ Reference：
	+ [论文](http://nil.csail.mit.edu/6.824/2022/papers/mapreduce.pdf)本文

### Demand

Google要处理互联网上海量的数据，对于这样数量级的数据，单机是不能在可接受的时间内处理完的，只能分布式的处理。
+ 将算法转换成分布式算法
+ 处理好分布式要面对复杂性

对于第一个问题，已经有些困难了，不是所有的算法都像Floyd一样天然有分布式的形态。

对于第二个问题，不仅会花费工程师大量的精力，而且这部分成本其实和其本来的工作关系不大。

能不能将分布式的复杂性封装起来，由框架设计者考虑，用户可以直接享用分布式的性能。

### Inspired

启发于函数式编程中的map和reduce源语。

工程师只需要考虑编写分布式程序的第一个问题，即将算法转换成符合“使用Map和Reduce的函数的编程范式”的算法，将两个实现交给MapReduce，系统内部来面对分布式的复杂性，继而满足需求。

>这其实是一个受限制的实现，因为将原本的算法转换成符合这个程序模型的实现
>+ 1. 需要成本
>+ 2. 可能无解

### Model
>一点小小的函数式编程震撼

+ Map
	+ 输入：键为文件名、值为文件内容的键值对
	+ 输出：键值对列表
+ Reduce
	+ 输入：键值对（值为中间数据中某个键的所有值的列表）
	+ 输出：键值对

### Implementation
>这是一个批处理的工作流

+ 用户输入
	+ Map的实现
	+ Reduce的实现
	+ 整数M：map task个数
		+ input files
	+ 整数R：reduce task个数
>这里有个问题是系统要将input files分成M份，每份通常是16MB或64MB大小，所以如果M和input files由用户指定，那么每份的大小应该是固定且不由系统控制的，不知道为什么。

1. 系统将input files划分成M份，每份通常是16MB或64MB大小，将所有程序拷贝到集群中的每个机器上
	+ 有一份程序是特殊的，叫master，其他的叫worker：master给空闲的worker指派map or reduce task
2. map阶段：
	1. 被指派map task的worker读取对应的input file split，将其解析成k-v s交给用户实现的Map function，输出的intermediate k-v s缓存在内存中
	2. 这些intermediate k-vs 定期写到Map worker的desk上，并且被parititioning function分成R份
		>划分函数通常是取模

		这些文件的名字、大小、位置会发送给master（一段message），master将其存在自己的data structure中

3. reduce阶段：
	1. master将part结果告诉reduce worker
	2. 当一个reduce worker被master通知，它通过RPC读取这些k-v s，读完后会sort（这样同样的key的存储位置就连续了），如果太大，则使用external sort
	3. reduce worker将排序后的intermediate data中连续的相同key的data执行用户实现的reduce function，其结果会append这个partition的output file中
	4. 该task结束，reduce worker会将这个output file rename（由GFS来保证这个操作的原子性）

4. 结束，交回程序控制权

+ master data structure：
	+ task status：idle, in-progress, completed
	+ worker id
	+ intermediate info

+ fault-tolerance
	+ worker failer
		+ master周期性的向worker发送心跳检测
		+ map worker fail：
			+ 所有完成的task的state init为idle
				>因为这些task的输出在这些worker的desk上，已经不能读取了

			+ 如果这些task被其他map worker re-execute，
			+ 还记得map worker 完成后会向master发送message，master只接受一个，如果一个message描述的是一个completed task，会忽略

		+ 对于reduce worker，它的fail会让它正在执行的task的state init idle
			>被failed reduce worker执行的task不需要re-execute，因为这些output已经存储到GFS上了

	+ master failed：这是一个中心式的分布式系统，如果master寄了，我们就认为它寄了
		>其实可以通过定时快照master的状态来恢复

+ stragglers