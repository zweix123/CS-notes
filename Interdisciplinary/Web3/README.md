+ Reference：
	+ MIT15.S12
	+ [区块链技术指南](https://yeasy.gitbook.io/blockchain_guide/)

## Consistenct issues and Consensus Algorithms
+ Reference：
	+ [分布式一致性与共识算法](https://draveness.me/consensus/)

我们已经在[这里](Distributed-System/README.md)讨论了一些分布式系统中的一致性问题和共识算法，而区块链是典型的分布式场景，且面对拜占庭将军问题

+ POW, Proof-of-Work工作量证明
	+ 内容：请求服务的节点必须解决一个**一般难度但是feasible可行的问题**且该问题验证容易
	+ 具体：寻找一个什么使区块的SHA-256是一个小于某个数的值
	+ 赢家得到区块记账权并通过Gossip协议发送给尽量多的节点
	+ 由于工作量证明需要耗费大量的算法，比特币大约10min才会产生一个区块的大小也只有1MB，仅能包含三四千笔交易，平均下来每秒只能够处理个位数的比较，这就导致比特币网络的拥堵状况非常严重。

+ POS, Proof-of-State权益证明
	+ 用于Ethereum以太坊，该算法算力要求小、所以性能更好，每秒30个交易

+ DPOS, Delegated Proof-of-Stake委托权益证明

## 交易描述
### UTXO
>Unspent Transaction output

### 账户余额模型
