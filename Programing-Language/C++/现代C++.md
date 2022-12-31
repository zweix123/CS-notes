





+ 智能指针

  ```c++
  #include <iostream>
  
  template<typename T>
  class Ptr {
  public:
      explicit Ptr(T* ptr = nullptr) : ptr_(ptr) {}
      ~Ptr() {
          delete ptr_;
      }
      T* get() const { return ptr_; }
      T& operator*() const { return *ptr_; }
      T* operator->() const { return ptr_; }
      bool operator()() const { return ptr_; }
  private:
      T* ptr_;
  };
  
  class Class {
  public:
      void say() { std::cout << "Hello"; }
  };
  
  int main() {
      Ptr p(new Class());
      
      p->say();  // p.operator->()->say();
      
      return 0;
  }
  ```

  





+ 关于赋值函数中`if (this != &rhs)`的强异常安全性：赋值分为拷贝构造和交换两步

  ```c++
      Ptr(Ptr& other) {
          ptr_ = other.release();
      }
      T* release() {
          T* ptr = ptr_;
          ptr_ = nullptr;
          return ptr;
      }
      Ptr& operator=(Ptr& rhs) {
          Ptr(rhs).swap(*this);
          return *this;
      }
      void swap(Ptr& rhs) {
          using std::swap;
          swap(ptr_, rhs.ptr_);
      }
  ```

  注意这里的赋值运算符，是先通过拷贝构造函数构造一个新的对象，然后将这个对象和本对象进行交换，这样如果在构造这个对象是就出错，this不会受损

+ C++17废除的auto——ptr是直接将指针进行“移动”（转移所有权）

  ```c++
      Ptr(Ptr&& other) {  //参数把引用变成移动
          ptr_ = other.release();
      }
      Ptr& operator=(Ptr rhs) {  // 参数从引用变成普
          Ptr(rhs).swap(*this);
          return *this;
      }
  ```

  C++如果定义了移动构造而没有定义拷贝构造，则默认拷贝构造是delete的，此时该智能指针只能移动拷贝，赋值也只能赋值move后的，