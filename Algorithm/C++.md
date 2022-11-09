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

  