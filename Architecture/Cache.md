+ 矛盾：
	+ CPU处理速度和内存访问速度之间的矛盾——于是有了缓存
		+ CPU要访问的数据在Cache有缓存，则为Hit命中，否则是Miss
	+ 存储的价格和性能的矛盾——于是有了多级缓存
		+ CPU的Cache细分为几层：Register -> L1 Cache -> L2 Cache -> L3 Cache -> Memory -> Mass Storage，读写延迟依次增加、实现成本依次降低

+ 局部性原理：空间局部性和时间局部性

+ 程序的指令部分和数据部分一般分别存放在两片不同的Cache中，即I-Cache指令缓存和D-Cache数据缓存
	```
	> lscpu | grep cache 
	L1d cache:                       256 KiB
	L1i cache:                       256 KiB
	L2 cache:                        2 MiB
	L3 cache:                        16 MiB
	```

## 结构

相联方式不同，直接相联、全相联、Set Associative组相联，其中组相联是前两者的这种，兼顾性能和价格，最常见

+ Set/Index组、Way路、Line行
+ 物理地址表示：Tag（对应Way）、Index（对应组）、Offset（对应行）

这里的组是在地址中的密集表示，比如8bit表示256个组，而Tag则是一个较宽的字节，在对应组中的若干个路中到对应的。相当于缓冲是一个`std::array<std::map<Way, Bytes>>`
