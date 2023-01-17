*   定义：a group of computers cooperating to provide a service this class is mostly about infrastructure services通过网络协调、共同完成一致任务的多台物理隔离的计算机，比如存储系统、大数据运算或者更奇妙的点对点文件共享。
    > 实际上在解决的问题时优先考虑不需要分布式的方案，因为分布式往往意味着复杂

## Drivens and Challenges

*   Drivens驱动力：Why do people build distributed systems?
    *   计算性能，即大量的并行parallelism计算、大量的CPU、大量的内存和大量的硬盘。to increase capacity via parallel processing
    *   提供容错fault-tolerates：一个机器崩溃完全可以将其任务切换到另一台。to tolerate faults via replication
    *   一些问题天然在空间上是分布的，比如转账。to match distribution of physical devices e.g. sensors
    *   达成一些安全性security的目标，比如一些代码不被信任，但是仍然需要和其进行交互，可以将代码分散，各部分通过特定的网络协议通信，限制**出错域**。to achieve security via isolation
*   Challenges挑战：
    *   并发Concurrency带来的复杂性。many concurrent parts, complex interactions
    *   故障failure处理tolerates是复杂的。must cope with partial failure
    *   如何评估性能。tricky to realize performance potential

## Abstraction and Implementation

*   抽象（This is a course about infrastructure for applications.）
    *   Storage存储，一个定义明确且有用的抽象概念
        构建一个多副本、容错的、高性能分布式存储实现

    *   Compute计算
        比如*MapReduce*

    *   Communicate通信
        我们希望设计接口，让第三方应用使用接口达到分布式的目的但是隐藏分布式的复杂性，即从用户来说，该系统就像一个非分布式存储和计算系统，但实际上又是一个有极高的性能和容错性的分布式系统

*   实现：
    *   RPC, Remote Procedure Call：掩盖在不可靠网络上通信的事实
    *   线程，即并发，那么就要涉及到并发控制

A big goal: hide the complexity of distribution from applications.

## 关于分布式系统的评估指标

*   可扩展性/可伸缩性Scalability，即只要增加机器数量，系统就应该提高相应的性能；对应的的，也能自由去掉机器
    以web服务为例，可以通过增加web服务器以分散用户的访问来增加系统可承受的访问量，但是诸如数据库这样的微服务不能通过简单的添加机器来解决。
    即可扩展性可描述为通过架构设计使很难实现的“通过增加机器的方式实现扩展”得以实现。

*   容错：在大数定理下，即使一个计算机出现错误的概率很低，但是当系统中的机器足够多时，出现错误几乎是必然。

    > 在特定的故障范围内

    *   可用性Availabilty
        比如通过复制replication，多副本

    *   自我可恢复性Recoverability：系统在寄掉后通过修复可以按之前的继续正常运行
        比如通过非易失存储non-volatile storage，不断将数据存入硬盘

    > 这里将实体机器放远一点有利于容错性，但是远距离的通信花费更多的时间

    *   一致性Consistency，多副本间数据一致
        *   强一致性Strong Consistency
        *   弱一致性
            可以想象，强一致性的保证需要各个机器间大量的通信，这里的开销非常大，所以虽然弱一致性可能导致系统出错，但是工程上仍然是有必要的