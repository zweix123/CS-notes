+ 随机数

  ```c++
  #include <random>
  #include <chrono>
  std::mt19937_64 rnd(std::chrono::steady_clock::now().time_since_epoch().count());
  //使用: rnd();
  ```

+ 关闭流：

  ```c++
  std::ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0); 
  /* 1. stdio系和iostream系不能混用
   * 2. endl不能使用
   */
  cout.precision(小数位数), cout.setf(ios::fixed);  // 设置小数位数，不需要重复设置
  ```
  
+ `<algorithm>`：

  + 二分查找系列：

    ```c++
    binary_search();
    lower_buond();
    upper_bound();
    ```

+ STL：

  + `<bitset>`

    ```c++
    set(pos)/reset(pos);  // 设置成1/0
    count();              // 1的个数; size() - count()就是0的个数
    any();    //是否有1
    none();   //是否全0
    ```

+ `__int128`：空间两倍于`long long`，需自定义IO，支持整数运算符

  > 初始化极值可通过`memset`初始化数组实现

+ 复数：

  ```c++
  #include <complex>
  complex<float/double/long double> object(实部, 虚部);
  //重载: operator+ operator- operator* operator/
  object.real();  // 返回实部
  object.imag();  // 返回虚部
  abs(sam);  // 返回模
  arg(sam);  // 返回幅角
  ```

+ `builtin`内置函数：

  ```c++
  int __builtin_clz(unsigned int);  // 前导0的个数
  int __buildin_ctz(unsigned int);  // 后缀0的个数
  int __builtin_ffs(unsigned int);  // 后缀0的个数+1(最后一个1的位置, 索引从1开始)
  int __buildin_popcount(unsigned int);  // 1的个数
  ```

  有对应的

  + `unsigned long`版本：在函数名后加`l`
  + `unsigned long long`版本：在函数名后加`ll`

# 哈希表unordered_map
> 使用拉链法实现，如果哈希碰撞太多，则查找会退化到线性
+ 自定义哈希函数：
  ```c++
  // 注意需要以下头文件
  #include<unordered_map>
  #include<chrono>
  
  struct custom_hash {
      static uint64_t splitmix64(uint64_t x) {
          // http://xorshift.di.unimi.it/splitmix64.c
          x += 0x9e3779b97f4a7c15;
          x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
          x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
          return x ^ (x >> 31);
      }
  
      size_t operator()(uint64_t x) const {
          static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
          return splitmix64(x + FIXED_RANDOM);
      }
  };
  
  unordered_map<int, int, custom_hash> mp;
  ```
  