[Support Top-K data structure and commands #2424](https://github.com/apache/kvrocks/issues/2424)

# 前置调研

+ Top-K，TOP-K，top-k，TopK，TOPK，topk，topk：这里统称topk

## What：Redis中的topk

+ Redis有多个版本
    + Redis CE：基础版
    + Redis Stack：扩展版
    + Redis Enterprise：企业版

topk是一个Redis Stack的功能（[How to install redis-stack in mac](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/mac-os/)）

+ 相关命令（[office website](https://redis.io/docs/latest/commands/?group=topk)）：我之前并没有使用过Redis，下面所有的命令第一个参数都是`key`，我理解这个相当于“表名”，只是为了符合Redis的使用逻辑，将其定义为key，一个key对应一个topk的“实例”，下面统称为键；后面的`ele`才是实际要维护的值，下面统称元素。
    + 初始化键：[TOPK.RESERVE](https://redis.io/docs/latest/commands/topk.reserve/)，TODO可选参数疑似和算法有关
    + 查询键参数：[TOPK.INFO](https://redis.io/docs/latest/commands/topk.info/)
    + 添加元素：[TOPK.ADD](https://redis.io/docs/latest/commands/topk.add/)
    + 批量添加元素：[TOPK.INCRBY](https://redis.io/docs/latest/commands/topk.incrby/)
    + 查询元素数量：[TOPK.COUNT](https://redis.io/docs/latest/commands/topk.count/)(deprecated)，返回的数量是小于其实际数量的估计值
    + 查询元素是否是topk：[TOPK.QUERY](https://redis.io/docs/latest/commands/topk.query/)
    + 查询所有元素：[TOPK.LIST](https://redis.io/docs/latest/commands/topk.list/)，难道Redis会存储所有的元素么，即使它不是topk

## How：Redis实现topk

+ [redis topk doc](https://redis.io/docs/latest/develop/data-types/probabilistic/top-k/)
    + 论文：[HeavyKeeper](https://www.usenix.org/conference/atc18/presentation/gong)
        + 开源实现：[heavy-keeper-project](https://github.com/papergitkeeper/heavy-keeper-project)

        坑啊！论文链接里的论文的内容比开源代码附带的论文要少！

这里提供一份笔记，翻译推荐使用Scholaread，该论文数学公式较多，啥翻译软件都得趴菜。

### HeavyKeeper

概率算法

flow and packet：不做区分，下面只使用flow

场景：网络通信统计  
场景特点：绝大部分流量极小，极小部分流量非常大

+ mouse flows（小鼠流）：极小流量的flow
+ elephant flows（大象流）：极大流量的flow

+ 旧策略旧算法
    + cout-all（全部计数）：使用CM Sketch统计所有包的流量大小，并使用min-heap跟踪topk
        + CM Sketch：计数器池（池大小大于k），一个流哈希到一个计数器并计数
        + min-heap（小根堆）：如果一个流对应的计数器小于小根堆的根，则替换

        这样难道不会有较大的误差么？除非计数池的大小比k大非常多。应该就是这样，可能池子非常大，因为论文提到该策略说其内存占用较大。

    + admit-all-countsome（全部接收，部分计数）：有多种实现，一个基本的实现是，维护一个计数小根堆，每当来到一个流，如果在堆中，则增加计数。否则，则直接代替堆顶并**继承**其计数。
        + 该算法的正确性建立在只有很小的流量属于大象流的场景
        + 会对小鼠流有误判，特别是当堆的大小上限和k比较接近时
        + 新实现：CSS，在旧的Stream-Summary提出新的数据结构TinyTable

策略：count-with-exponential-weakening-decay（指数衰减计数）  
效果：既保留大象流，又大幅度减少在小鼠流的空间浪费  

![The data structure of HeavyKeeper.png](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Database-System/Kvrocks/The%20data%20structure%20of%20HeavyKeeper.png)

+ 一个流的属性
    + 通过一个哈希函数有一个哈希值（这里有 $d$ 个哈希值）
    + 全局唯一的ID
    + 通过ID得来，体积更小，可能冲突的**指纹**

使用 $A_j[t]$ 表示上图中的一个单元，即第 $j$ 的arrays、第 $t$ 的buckets，使用 $A_j[t].F$ 表示指纹， $A_j[t].C$ 表示计数。

一个新的包/流，被 $d$ 个哈希函数映射到 $d$ 个桶，论文称之为 d mapped buckets。  
如果一个包/流哈希到对应单元的指纹相同，则称 flow **held** at bucket。

+ 增：
    1. 对应桶计数为0，则设置指纹并增加计数
    2. 对应桶计数大于0且指纹相同，自增1
    3. 对应桶计数大于0但指纹不同，它以概率 $Pdecay$ （并非全局统一，见下文）自减1，如果减少为0，则走1的规则
+ 查：选择哈希出来的 $d$ 个单元中指纹相同的并取最大；如果没有指纹相同的，则是小鼠流。

衰减概率Decay probability

$$
P_{decay} = b^{-C} \ (b > 1)
$$

+ b：预定义的指数基数
+ C：当前单元的计数值

当一个单元的计数值越大，它越难以衰减。

一个直觉的实现：一个HeavyKeeper和一个小根堆，流量先在HeavyKeeper里记录，并获取估计值，如果其ID已经在小根堆存在，则刷新大小。如果没存在并且**大于**堆顶，则替换。

+ 问题：指纹碰撞检测，小鼠流和大象流的指纹一样，则小鼠流会被误判
    + 优化1和优化2：指纹碰撞检测和选择性自增

    + 基于定理：当一个流被插入到HeavyKeeper后，且不在小根堆中，如果它的值比堆顶大，则一定是恰好多1。
        + 反证法容易得。

    + 自增时，如果流的ID不在堆里，则必须对应单元的计数小于堆顶才自增
        >考虑小鼠流碰撞了，它使用的是大象流的计数，而其因为是小鼠流，（假如）肯定不在堆中，而大象流大概率比堆顶要大，所以就是这样的情况，不会给它自增

        + 论文错误：这里应该是小于等于，不然永远不会有第二个元素进入堆

    + 放入堆时（没在堆才考虑是否放入），只有恰好估计值（就是 $d$ 个 held 的单元的计数的最大值）是`堆顶+1`才放入

    在这样的情况下，只有指纹冲突且恰好小鼠流冲突的大象流的计数等于堆顶才会误判

+ 优化3：小根堆的更新和查询都是log的，如果直接使用链表呢？直接设置一个阈值，如果估计值比这个大，就认为是大象流

![伪代码](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Database-System/Kvrocks/伪代码.png)

论文的后面部分讲的是HeavyKeeper的其他应用、数学证明和实际效果。

## NoSQL的开发

+ Redis是“缓存”，Kvrocks应该属于“持久化存储”，两者并非对位。
+ Redis已经成为事实标准
    + 接口形式
    + 通信协议

    Kvrocks虽然不和Redis成对味，但是兼容通信协议。

+ Redis可以理解为是一个键为字符串，值为多种类型的大哈希表

## Kvrocks的开发

+ Kvrocks向外界表达的数据结构都必须存储在RocksDB中，而不是使用STL的、存储在内存中的来实现。
+ Kvrocks如何添加新的命令？可查看宏`REDIS_REGISTER_COMMANDS`和函数`MakeCmdAttr`，或者直接看其他命令实现文件的最底部。

# 设计文档

论文提到的性能优化，有两个问题，怎么找到Top-k的最小值，阈值怎么选择。所以还是使用小根堆。

因为可以使用数组实现小根堆，所以有两个方案

+ 哈希表列表+小根堆
+ 哈希表列表+数组

## 命令设计

```
src/commands
       |----- cmd_top_k.cc
```

```cpp
REDIS_REGISTER_COMMANDS(
    // https://redis.io/docs/latest/commands/topk.reserve/
    // TOPK.RESERVE key topk [width depth decay]
    // 可选参数
    MakeCmdAttr<CommandTopKReserve>("topk.reserve", -3, "write", 1, 1, 1),
    // https://redis.io/docs/latest/commands/topk.info/
    // TOPK.INFO key
    MakeCmdAttr<CommandTopKInfo>("topk.info", 2, "read-only", 1, 1, 1),
    // https://redis.io/docs/latest/commands/topk.add/
    // TOPK.ADD key items [items ...]
    // 可选参数
    MakeCmdAttr<CommandTopKAdd>("topk.add", -3, "write", 1, 1, 1),
    // https://redis.io/docs/latest/commands/topk.incrby/
    // TOPK.INCRBY key item increment [item increment ...]
    // 可选参数
    MakeCmdAttr<CommandTopKIncrby>("topk.incrby", -4, "write", 1, 1, 1),
    // https://redis.io/docs/latest/commands/topk.query/
    // TOPK.QUERY key item [item ...]
    // 可选参数
    MakeCmdAttr<CommandTopKQuery>("topk.query", -3, "read-only", 1, 1, 1),
    // https://redis.io/docs/latest/commands/topk.list/
    // TOPK.LIST key [WITHCOUNT]
    // Flag
    MakeCmdAttr<CommandTopKList>("topk.list", -2, "key", 1, 1, 1), 
)
```

## 其他

+ 更新网站：https://kvrocks.apache.org/docs/supported-commands/