[exception language ref](https://en.cppreference.com/w/cpp/language/exceptions) | [exception lib ref](https://en.cppreference.com/w/cpp/error/exception)

+ `abort()`和`exit()`
+ [`throw` expression](https://en.cppreference.com/w/cpp/language/throw)和[try-block](https://en.cppreference.com/w/cpp/language/try_catch)
+ [noexcept](https://en.cppreference.com/w/cpp/language/noexcept)

+ 异常处理：[zclll.com: handling exception(translation)](https://zclll.com/index.php/cpp/tr18015exception.html)

+ 异常安全：
	+ 保证不抛出异常：
	+ 强烈异常保证：抛出异常后，不会产生任何副作用
	+ 基本异常保证：抛出异常后，对象仍然是有效的，即没有数据结构损坏且没有资源泄露，但是不知道处于什么状态，即值可能改变
	+ 无异常安全：
