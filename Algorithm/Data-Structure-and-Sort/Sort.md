+ 逆序对：
  + 性质：
    + 一个序列通过交换转化成非降序序列的最小操作次数

+ 快速排序：

  + 策略：
    1. 在数列中取一个树做**基准数**
    2. 把比它大的数放右边，比它小的数放左边
    3. 再对左右区间重复步骤2，直到各区间只有一个数
  + 性能：平均复杂度$O(n \ log \ n)$，最坏复杂度$O(n^2)$
  + 优化：选择基准数的策略，小区间转换策略

  ```cpp
  template<typename T>
  void quick_sort(T q[], int l, int r) {
      if (l >= r) return;
      int i = l - 1, j = r + 1, x = q[l + r >> 1];  //基准数
      while (i < j) {  //整理左右区间
  		do ++ i; while (q[i] < x);
          do -- j; while (q[j] > x);
          if (i < j) swap(q[i], q[j]);
      }  //此时i、j相等或i - j == 1，所以使用哪个区别不大
      quick_sort(q, l, j);
      quick_sort(q, j + 1, r);
  }
  ```

+ 归并排序：

  + 策略：
    1. 将数列分成两个部分，递归到底
    2. 将两个子序列排序，合并，回溯

  ```cpp
  template<typename T>
  void merge_sort(T q[], int l, int r) {
  	if (l >= r) return ;
      //划分并递归
      int mid = l + r >> 1;
      merge_sort(q, l, mid);
      merge_sort(q, mid + 1, r);
      //将（已经排序好的）进行归并排序
      int k = 0, i = l, j = mid + 1;
      while (i <= mid && j <= r)	
          if (q[i] <= q[j]) tmp[k ++] = q[i ++];
      	else temp[k ++] = q[j ++];
     	while (i <= mid) tmp[k ++] = q[i ++];
      while (j <= r) tmp[k ++] = q[j ++];
      //回溯
      for (int i = l, j = 0; i <= r; ++ i, ++ j) q[i] = tmp[j];
  }
  ```