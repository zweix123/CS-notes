+ Refs：
	+ [OSTEP](http://www.ostep.org/)，南大蒋岩炎老师称之为操作系统最好的自学书籍
		+ 完全开源
		+ [作者Github](https://github.com/remzi-arpacidusseau)
	+ MIT6.s081:
		+ [野生讲义翻译](https://mit-public-courses-cn-translatio.gitbook.io/mit6-s081/)

+ 设计原则：将Policy策略和Mechanism机制相分离

## 分类

+ 狭义的操作系统指的是操作系统内核加上一个Shell
+ 广义的操作系统
	+ 操作系统内核：比如Linux内核，负责对硬件资源的管理与抽象，为操作系统提供基础的系统服务。
	+ 操作系统框架：比如Android框架，基于操作系统内核提供的服务为不同的应用领域提供编程接口与运行环境

### 内核简介

+ 简要结构
+ 宏内核
+ 微内核
+ 外核：操作系统内核在硬件管理方面主要有两个功能，资源抽象和多路复用。问题是抽象可能带来性能损失。抽象是通用抽象。
	+ 库操作系统LibOS：将对硬件的抽象封装到LibOS中，与应用直接链接，降低应用开发的复杂度。而操作系统内核只负责对硬件资源在多个库系统之间的**多路复用**支持
+ 多内核

### 框架简介

## 接口

+ 系统调用接口
+ POSIX接口，Protable Operating System Interface for uniX
+ 领域应用接口
	>是在前两者的基础上封装的

+ 区分：
	+ API：应用编程接口，源码层面交互接口，比如libc和内核
	+ ABI：应用二进制接口，二进制层面交互接口，比如ELF、EXE，调用约定和数据模式
