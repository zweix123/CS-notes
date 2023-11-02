# 术语
[动手学深度学习引言章](https://zh-v2.d2l.ai/chapter_introduction/index.html)

我们不能明确大脑从输入到输出的映射，但是大脑仍然能执行认知功能。很多计算机任务是可以描述算法的，但是有不能的。

+ 程序：输入到输出的映射
+ parameter参数：调整程序的行为
	+ 
		+ learning algorithm学习算法：选择“最佳参数集”的算法
		+ 标记的dataset数据集：可作为学习算法的输入
	+ 
		+ model模型：任一参数调整后的程序

		模型族：所有参数调整后的模型的集合
		
<br>

在机器学习中，learning学习即为训练模型的过程，找到最佳参数，即，我们用数据train训练模型
>programming with data数据编程：通过用数据集来确定程序行为的方法

<br>

+ objective function目标函数/loss function, cost function损失函数：用来量化模型的有效性
此时学习算法的目标则是调整模型参数以优化目标函数/最小化损失函数，比如梯度下降gradient descent


<hr>

+ dataset数据集：
	+ example, sample样本/data point数据点/data instance数据实例：数据集的组成
		+ 组成：名为features特征/covariates协变量的属性，通常是向量
		+ 数据dimensionality维度，如果一个数据集样本的特征向量长度一致，则这个长度大小即为维度
	+ 
		+ 训练数据集
		+ 测试数据集

## 监督学习
supervised learning：在“给定输入特征”的情况下预测标签，目标即为生成从输入特征到标签的模型（预测）
>还记得机器学习的目标嘛？有一个从输入映射到输出的模型，样本是输入（实际是特征、特征向量是输入），那么监督学习将输出称为label标签/target目标。此时一个样本是“特征-标签”对儿。

+ regression回归问题：标签是数值
	+ 目标函数的指标即为预测值和实际标签值的差异
+ 分类问题：
+ 标记问题：一个输入属于多个类别
+ 搜索问题：
+ 推荐系统：
+ 序列学习：多个输入之间有关系：共同构成输入或者上个输入预测下个输入
	+ 比如自然语言处理

## 无监督学习
unsupervised learning：监督学习的特点是要有打好标签的数据集，无监督学习则是没有明确的*目标*

+ clustering聚类：没有标签的情况下进行分类
+ principal component analysis主成分分析：输入的关系
+ 因果关系（causality）和概率图模型（probabilistic graphical models）问题
+ 生成对抗性网络（generative adversarial networks）：生成数据

## 强化学习
reinforcement learning
>上面的两个学习都是需要准备数据，然后去训练模型，这些都是**离线**的。

在强化学习问题中，智能体（agent）在一系列的时间步骤上与环境交互。 在每个特定时间点，智能体从环境接收一些观察（observation），并且必须选择一个动作（action），然后通过某种机制（有时称为执行器）将其传输回环境，最后智能体从环境中获得奖励（reward）。 此后新一轮循环开始，智能体接收后续观察，并选择后续操作，依此类推。 请注意，强化学习的目标是产生一个好的策略（policy）。 强化学习智能体选择的“动作”受策略控制，即一个从环境观察映射到行动的功能。

当环境可被完全观察到时，强化学习问题被称为马尔可夫决策过程（markov decision process）。 当状态不依赖于之前的操作时，我们称该问题为上下文赌博机（contextual bandit problem）。 当没有状态，只有一组最初未知回报的可用动作时，这个问题就是经典的多臂赌博机（multi-armed bandit problem）。

核心思想：使用数据和神经网络编程
