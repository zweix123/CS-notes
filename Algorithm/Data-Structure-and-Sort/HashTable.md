名字很多，概念本身名字很多，哈希表、散列表；在不同语言的实现也有很多名字，抓住主要矛盾即可

+ 哈希函数要求：
	+ 确定
	+ 均匀
	+ 快

+ 哈希表的实现方式：
	+ 开放寻址法
		+ 线性探测
	+ 拉链法

## 开放寻址法线性探测哈希表实现

```cpp
		
class HashTable {
public:
	HashTable(int size)
private:
	int size_;
	std::vector<>
};
```

## 开放寻址法线性探测可扩展哈希表实现、测试和分析

[实现代码](https://github.com/zweix123/ACT/blob/main/include/stl/hashtable.h) | [测试代码](https://github.com/zweix123/ACT/blob/main/test/test_stl_hash_table.cpp) | 分析见代码注释
