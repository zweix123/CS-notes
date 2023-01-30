# 中央处理器CPU

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/CPU的基本结构全家福.jpg)

+ CPU的功能：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/CPU功能.jpg)

+ 运算器和控制器的功能：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/运算器和控制器的功能.jpg)

+ 运算器的基本结构：

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/CPU运算器结构.jpg)

  > 通用寄存器：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/通用寄存器.jpg)

  + ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/运算器的基本结构1.jpg)

    1. 专用数据通路方式：根据指令执行过程中的数据和地址的流动方向安排连接线路

       1. ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/运算器和寄存器的连接1.jpg)
       2. ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/ALU和计算器的连接2.jpg)

    2. CPU内部单总线方式：将所有寄存器的输入端和输出端都连接到一条公共的通路上：

       ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/ALU和寄存器的连接3.jpg)

       

+ 控制器的基本结构：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/CPU控制器结构.jpg)

## 指令执行过程

+ 机器周期/CPU周期：

+ 指令周期：CPU从主存中每取出并执行一条指令所需的全部时间，常由若干CPU周期表示

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/机器周期和指令周期的关系.jpg)

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/指令周期.jpg)

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/指令周期比较.jpg)

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/指令周期流程.jpg)

1. 取址周期：

   ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/取址周期.jpg)

2. 间址周期：以一次间址为例

   ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/间址周期.jpg)

3. 执行周期：略

4. 中断周期：

   ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/中断周期.jpg)

+ 指令执行方案：

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/指令执行方案.jpg)

## 数据通路

+ 数据通路：数据在功能部件之间传送的路径

+ 数据通路的基本结构：

  1. CPU内部单总线方式
  2. CPU内部多总线方式
  3. 专用数据通路方式

+ 内部总线是指同一部件，如CPU内部连接各寄存器及运算部件之间的总线

  系统总线是指同一台计算机系统的各部件，如CPU、内存、通道和各类I/O接口间相互连接的总线。



1. 数据通路-CPU内部单总线方式：![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Computer-Organization&Architecture/数据通路-CPU内部单总线方式.jpg)

2. 专用数据通路：https://www.bilibili.com/video/BV1BE411D7ii?p=80&spm_id_from=pageDriver

## 控制器

### 硬布线

### 微程序



## 流水线
