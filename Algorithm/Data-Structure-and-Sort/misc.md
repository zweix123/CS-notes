# 概述

## 通识

+ 级数：

  + $\sum_{i = 0}^N A^i = \frac{A^{N + 1} - 1}{A - 1}$

    + 特殊的有$\sum_{i = 0}^N 2^i = 2^{N + 1} - 1$
    + 当$0 < A < 1$时有$\sum_{i = 0}^N \le \frac{1}{1 - A}$

  + 算术级数：

    $\sum_{i = 1}^N i \  \ = \frac{N(N + 1)}{2} \approx \frac{N}{2}$

    $\sum_{i = 1}^N i^2 = \frac{N(N + 1)(2N + 1)}{6} \approx \frac{N^3}{3}$

    $\sum_{i = 1}^N i^k \approx \frac{N^{k + 1}}{|k + 1|} \ \ k \neq -1$

    + 当$k = -1$时，该值为调和级数$H_N = \sum_{i = 1}^N \frac{1}{i} \approx log_e^N$

      > 其误差趋近于Euler‘s constant欧拉常数$\gamma \approx 0.57721566$

+ 证明方法：归纳法和反证法

+ 复杂度定义：

+ Abstract Data Type, ADT抽象数据类型：带有一组操作和一些对象的集合

# 附录

```c++
//matrix.h
#ifndef MATIX_H
#define MATIX_H

#include <vector>
template <typename Object>
class matrix {
public :
	matrix(int rows, int cols) : array(rows) {
		for (int i = 0; i < rows; ++ i)
			array[i].resize(cols);
	}
    const std::vector<Object> & operator[] (int row) const {
        return array[row];
    }
    std::vector<Object> & operator [] (int row) {
        return array[row];
    }
    
    int numrows() const { return array.size(); }
    int numcols() const { return numrows() ? array[0].size() : 0; }
private:
	std::vector< std::vector<Object> > array;
};

#endif
```
