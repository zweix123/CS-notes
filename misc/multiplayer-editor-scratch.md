将画面分成单元格矩阵，对每个单元格编码。核心操作可以抽象成对字符串的操作

+ text-based user interface(TUI)

+ 挑战：
	+ 冲突解决：对于多个用户对同一位置的修改，如何优先哪些更改以及最后保持一致
	+ 实时协作
	+ 多用户同步

可以想象冲突解决是核心问题，有一系列解决该问题的技术

## Operational transformation

+ consistency and concurrency control

对一个用户来说，其他用户的操作针对本地的进行进行转换，解决冲突。

### CCI模型

+ Convergence收敛：正确性
+ Causality preservation因果关系保留：有序性
+ Intention Preservation意图保留：一致性

## Conflict-free replicated datatypes(CRDT)

是一个有明确定义接口的抽象数据结构，目的是跨多节点进行复制

+ 分类：
	+ state-based：传输同步整个状态机
	+ operation-based：传输单个操作计算并同步状态机


## Summary

+ OT维护的是用户的操作
+ CRDT维护的是编辑器的状态
	+ CvRDT是直接拷贝整个状态
	+ CmRDT是拷贝改变状态的操作

>区分用户操作和改变状态操作
