+ Pre: 怎么存储一个巨大的文件呢？一个很自然的想法，sharding分片，这时就要面对那个经典问题了，在大数定理下，机器数量很大的时候出现错误几乎是必然的，那么怎么fault tolerance呢？又一个自然的想法，就是replication复制，有了副本，就要面对consistency一致性问题，为了解决一致性问题，机器间就要有额外的网络交互，即更强的一致性的代价是可能导致更低的性能，这里需要有工业上的平衡。  

	+ 强一致性
		1. 对用户来说，多个机器就像一个机器，甚至这个机器只单线程的服务于用户
		2. 多机副本完全相同
			+ 写需要同步到多个副本
			+ 读只需要读取一个机器
				>这显然更快且（如果强一致性可以保证的话就是）正确且只有这样才能保证容错

			这样如果读机器寄了，换到另一个副本的机器没有任何问题。

	强一致性会有这样的问题，如果为了强一致性的1，那么一个机器要面临多个用户的访问，一旦出现多个用户对同一个位置进行覆写，而机器为了强一致性的2会发生通信，万一对应位置副本的机器收到不同覆写消息的顺序不同怎么保证语义？这时如果其他用户再对这个位置读，我们不能保证他们的信息来自同一个机器，那么就很可能不同（这违反了一致性！）

	>所以强一致性是有代价的。

>GFS在2003发表于SOSP，这是一个更注重创新的会议，而GFS提到一致性算法基本都被讨论过。  
>+ GFS的规模非常大，远远大于学术界建立的系统
>+ GFS用于工业界，有些工程上的东西也很有价值
>+ 提出了这样的一个观点：弱一致性也是可以的（因为之前学术界认为一个错误的系统有什么用呢？GFS为了性能并不保证返回正确的数据）

+ 我们希望GFS有的特性
	+ 全局通用（一种通用存储）
	+ sharding
	+ automatic recovery
+ GFS在实现过程中不可避免出现的特性：
	+ GFS机器们在同一个数据中心中（实际上应该分布的更远一些）
	+ Google内部使用
	+ 适用于巨大文件，建议顺序处理（而不是随机），关注点是大吞吐量

## Implementation

+ GFS是中心式的
	+ master（Active-Standby模式）：可能有多个master机器，但是只有一个在工作，管理文件和chunk信息
	+ chunk server（大量）：每个机器有一两块磁盘存储文件数据

+ chunk: 一个文件的分片，大小为64MB
	+ 多个副本（通常是3个），选择一个作为primary chunk，写操作都在primary chunk上
		+ 每个primary chunk是在租约时间内担任

### Master

+ data structure
	+ file table: file name - list\[chunk id / chunk handle\] —— nv
		>课上chunk id和chunk handle是同义词，下面只使用handle
	
	+ chunk table: chunk handle - chunk data
		+ chunk data
			+ list\[server\] —— v, 可以通过通信恢复
			+ chunk version —— 持久状态和实现有关
			+ primary chunk server —— v, 这个本来就是动态的
				+ 租约过期时间

	>这里的nv：non-volatile非易失

+ log：数据结构存储在内存中，如果master failed，则数据丢失，所以在写数据时master会将一部分数据写入desk，即为log，并偶尔生成一个checkpoint（快照）
	>没有使用数据库是因为log追加多快呀

### chunk server
普通的Linux机器，有一到两块硬盘，使用linux文件系统存储chunk（比如以chunk handle来命名文件）

+ primary chunk主要用于写文件，但是当写入时不能保证有primary chunk有，所以下面讨论一下这种情况
	+ 怎么找到一个合格的primary chunk？
		+ 通过master的版本找到最新的版本（版本一致）（这也是为什么版本号在机器中是nv的原因）
		+ 找到有最新版本的chunk的server作为primary（其他作为secondary）
		+ 然后master会追加版本，写入磁盘，并通知对应chunk的所有server
		>这里的更新版本只会在执行primary时才更新

### read

1. clent: tuple(file name, offset) -> master: 
	1. master从file table中得到list, 因为每个chunk大小固定，所以index可以直接求出，继而得到chunk handle
	2. master从chunk table中得到server list, return client
2. client: 从list选择一个去读
+ client会cache return
3. client:\[chunk handle, offset\] -> chunk server: return data
+ 如何request超过64MB或者跨过chunk边界怎么办？
	+ GFS有相应的库，会将这样的request分成多个request

### write(append)

写文件需要client提供offset，但是对于追加写，client并不知道文件究竟多大，而且还会有多个client进行同时写，所以GFS提供接口获得文件最后一个chunk handle  
对于写文件可以从任何一个chunk server读即可，但是写文件必须通过primary chunk server

+ 如果没有primary chunk怎么办？
	1. master找到版本最新的chunk（最新指的是其保存的和master记录的版本一致）
		+ 为什么不取最大的呢？因为如果没有一个chunk相应，就卡死了；或者如果最大版本的server没有即时相应，就错误了。所以没有合适的就一直等待
		+ 如果master发现比自己版本还大的呢？**可能**是让自己的版本好增大到这个chunk的版本
	3. master增加版本号，写入磁盘
	4. 通知chunk，包括primary/secondary关系和版本号，chunk server会将版本号写入磁盘

好，现在有了Primary Chunk了，其他的作为Secondary Chunk，Primary可以接受client的request，并且将写请求应用到多个chunk server中  
master会通知primary和Secondary一个租约，primary在超过租约后必须停止成为primary，避免同时有多个primary（后面会提到），这个租约是所有机器都有的

+ 写：
	1. client将追加的数据发到primary和secondary的服务器，然后服务器将它们临时存储
	2. 所有server向client返回所有server都收到
	3. server向primary说：所有的server都收到了，开始追加吧
	+ 这个过程primary可能收到很多的消息，它按照某个顺序依次执行
		+ 首先检测当前chunk有足够空间
		+ 追加
		+ 通知所有secondary追加

		一旦有一个server失败了，primary就会告诉client失败了，需要重来  
		这个失败会导致各个副本存在hole（zweix觉得简直是非常的不一致），可能需要用户应用容忍乱序（当然对于要求顺序的数据可以采用单client写入而不要并发）

	+ 关于失败
		+ 只有成功了时才能保证一致性
		+ 无能通过版本维护，GFS的版本指的任期，和client的request无关
		+ 重发可能会快一些，因为server对需要append的数据缓存好了，但是这个追加流程依然是完整流程（即从找到末尾chunk handle开始）
		+ 如果失败的原因是server寄了怎么办（如果是丢包就重传即可）Master会定期ping进行检测，对于fail server则更新server list
			+ 如果ping失败是因为丢包而不是因为server fail怎么办？GFS的策略是租期，没到租期，即使无法和primary通信，也不指定新的，避免脑裂

+ 数据传输：链式传输，避免client承担大量net IO

+ split-brain脑裂：master怎么保证primary的存活？通过定期的ping，但是ping可能因为网络问题G，如果master立刻执行新的primary，那就有两个不知道彼此的primary在工作了
	+ 而GFS解决这个问题的方式就是通过租约，即使master认为当前primary已经G了，但是它的租约还没到，就不指定新的
	+ 那么为什么不让client每次都先问master找到最新primary呢？因为cline会cache，它不一定会记得知道哪个server的真的primary

+ GFS的问题（效益自不必多说，BigTable和MapReduce都是建立其上的）
	+ Master承担的东西太多了
		+ 信息
		+ IO
	+ 语义问题
	+ Master的fail 切换不是自动的。