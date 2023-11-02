>SL, Standard Library 标准库

## string
[string lib ref](https://en.cppreference.com/w/cpp/string) | [basic_string](https://en.cppreference.com/w/cpp/string/basic_string)
>string是basic_string的特化版本，所以ref中没有string而是指向basic_string

+ 类型[`size_type`](https://en.cppreference.com/w/cpp/string/basic_string)，从ref中我们可以看到在传统C++中它是从Allocator中定义出来的，而那里是由`size_t`定义的，但是在Modern C++中，呃，它套娃下去我就看不懂了。

### 与C风格字符串的区别
可以把C语言的字符串看做整数数组，但是C++上的字符串则有重重封装

+ string类的末尾，C风格字符串的末尾是`'\0'`（注意这不是0，而是特殊的转义字符），在string类中使用[`npos`](https://en.cppreference.com/w/cpp/string/basic_string/npos)，
+ 头文件：string类是由`<string>`支持的，其他（`string.h`和`cstring`）都是支持C风格字符串相关操作的
