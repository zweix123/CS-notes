+ ref：
	+ [知乎 · 格律 · 设计VLSI EDA(1)：EDA的What, Why, How](https://zhuanlan.zhihu.com/p/380962676)
	+ 《VLSI Physical Design: From Graph Partitioning to Timing Closure》

+ 相关竞赛：
	+ 集成电路设计自动化算法竞赛
	+ ICCAD比赛

+ Pre：
	+ 数电：电路设计和电路构成
	+ 数据结构和算法：图论和动态规划

+ Terms：
	+ PCB板：PCB, Printed Circuit Board：印刷电路板
	+ VLSI, Very Large-Scale Integration：超大规模集成电路
	+ CAD, Computer-Aided Design：计算机辅助设计
		+ EDA, Electronic Design Automation：电子设计自动化

# CPU设计

## 1. 设计芯片规格Design Specification

+ 指令集
+ 微架构
+ 仿真

## 2. 硬件设计描述Hardware Description

+ HDL, Hardware Description Language：硬件描述语言，典型的有Verilog

针对硬件设计描述，EDA工具主要提供下面两个帮助
1. 对已有设计库的自动化整合
2. 提高设计的抽象程度

### Library-baseed design，Re-targeting and Reconfiguration

社区中有一些例子，它们利用新抽象层次高的语言或者框架作为Verilog的生成器。

### HLS, High-Level Synthesis

## 3. 验证Verification

### Simulation-Base Verification 

### Fromal Verification

+ 形式模型检查Formal Model Checking：把设计转化成数学表征模型
+ 等价性检查Equivalence Checking
+ 定理证明Theory Proving

## 4. 逻辑综合Logic Synthesis

### 组合逻辑优化

### 时序逻辑优化

### 工艺映射

## 5. 物理综合Physical Synthesis

### 布局

### 布线

