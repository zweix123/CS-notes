+ 块：小括号
	```go
	import (
		...
	)
	const (
		...
	)
	var (
		num int32, 
		name string,
	)
	```

## 包
+ 每个Go程序都是由包构成的、程序从`main`包开始运行
	```go
	package 当前代码所在的包名
	```

+ 包的导入：`import 包名`
+ 包内容的导出名：Golang的包也有Public和Private的概念，不过是通过名称的首字母区分：如果一个名字以大写字母开头，则已导出，可以通过`包名.导出名`使用，否则未导出。
+ 相同包只能有一个`main`函数，相同包内不需要显示import即可使用相互代码中的名称

## 函数

还记得上面说的相同包之前的名称可以相互使用嘛？所以函数前后没有声明顺序要求
```go
func 函数名(函数参数) 返回类型 {
	函数体
}
```
> [Go's Declaration Syntax](https://blog.go-zh.org/gos-declaration-syntax)：关于为什么Go的名称语法看起来和C的差别这么大

+ 参数：
	```go
	func add(x int, y int) int {
		return x + y
	}
	```
	+ 当连续两个或多个函数的已命名类型相同时，除最后一个类型以外，其他的都可以省略
		```go
		func add(x, y int) int {
			return x + y;
		}
		```

+ 返回值：
	+ 多值返回：
		```go
		func f(...) (返回值1类型, 返回值2类型, ...) {
			return x, y...
		}
		a, b， ... := f(...)
		```
	+ 命名返回值和直接返回
		```go
		func f(...) (x 类型, y 类型) {
					// x和y被视作定义在函数顶部的变量
			return  // 没有参数的return语句返回已命名的返回值，即“直接返回”
		}
		```
		+ 返回值名称应该具有一定意义，可作为文档使用
		+ 直接返回应仅用于短函数中

+ [可变参函数](https://gobyexample-cn.github.io/variadic-functions)

*   函数值：  
	函数也是值。它们可以像其它值一样传递。  
	函数值可以用作函数的参数或返回值。

### 闭包

+ 当函数的返回值是一个函数时，它可以是个闭包
+ 闭包也可以递归，但需要将闭包函数提前声明
+ 使用闭包要[小心](https://go.dev/doc/faq#closures_and_goroutines)

### 错误处理

Golang有它独有的风格[go blog](https://go.dev/blog/error-handling-and-go)

#### Panic

+ Recover：从Panic中恢复
	```go
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered. Error:\n", r)
		}
	}()
	```

## 数据

+ 基本数据类型：
	```go
	bool
	
	string
	
	int  int8  int16  int32  int64
	uint uint8 uint16 uint32 uint64 uintptr
	
	byte // uint8 的别名
	
	rune // int32 的别名
		 // 表示一个 Unicode 码点
	
	float32 float64
	
	complex64 complex128
	```
	
	+ `int, uint, uintptr`大小跟随系统，同系统宽度
	+ [字符/字符串](https://go.dev/blog/strings)：  
		+ Go中的字符串常量是UTF-8编码，通过其实地址和长度表示，不可更改
		+ `byte`的本质是`uint8`，即一个字节，为了适配ASCII  
		+ `rune`的本质是`int32`，即四个字节，为了对应Unicode  
		+ 字符常量`'c'`是`int32`，即可以有中文字符（这在C/C++这种以ASCII为基本编码的语言中是不可以的）  
		+ 对于一个string类型的变量，使用`[]`运算符通过得到是`uint`，即中文不能这样访问  
			但`for each`中的每个value就是一个Unicode码点，即`int32`类型，可以直接输出中文

+ 变量定义的关键字`var`：可出现在包或函数级别
	+ 变量列表关于类型的位置和规则同函数

+ 初始化：
	```go
	var i, j int = 1, 2
	var a, b, c = 1, false, "Y"  // 如果初始值已存在，则可以省略类型
	```
	+ 未初始化的变量会被赋予**零值**：`0, false, ""`

+ 短变量声明（只能用于函数中）：`s := "Hello World!"`

+ 类型推导：在不带类型的`:=`语法和`var = `语法中，变量的类型由右值推导得出

+ 常量：使用`const`声明，即用`const`替换`var`

+ 类型转换：
	+ 基本类型转换：`T(x)`，将值 x 转换为类型 T。其中 T 是基本类型
	+ 指针类型转换：`T(p)`：：将指针 p 转换为类型 T 的指针。其中 T 可以是任何类型。
	+ 接口类型转换：
		+ `T(v)`：将实现了接口 v 的值转换为类型 T。其中 T 可以是任何类型。
		+ `v.(T)`：将接口值 v 转换为类型 T。其中 T 可以是任何类型。


### 枚举
```go
type EnumType int
const (
	EnumType1 EnumType = iota
	EnumType2
	EnumType3
)
// EnumType1、2、3即为枚举类型
```

### 指针
语法近C，零值为`nil`，没有指针运算
```go
var i int = 1
var p *int = &i      // 重定向
*p = 2  // i 变成 2   // 间接引用
```

+ 内置函数`new()`，用于创建指针
	```go
	ptr := new(Type)  // Type可以是任何类型，包括结构体、数组、指针、map等等。new函数返回一个指向该类型的零值的指针。
	```

### 结构体
一个结构体struct就是一组字段field，并使用点号来访问
```go
type Point struct {
    X, Y int
}
point = Point{1, 2}
point.X  // 结构体字段

p = &sam
P.X  // 是的，不需要(*p).A，可以这样隐式间接引用

// 其他初始化文法
var {
    point1 = Point{1, 2}
    point2 = Point{X: 1}  // point2.Y init 0
    point3 = Point{}
    p = &Point{}  // 直接创造结构体指针
}
```

### array
类型`[n]T`表示拥有`n`个`T`类型的值的数组
```go
var a [10]int
a[0] ... a[9]

b := [2]string{"aaa", "bbb"}
b := [...]string{"aaa", "bbb"}  // 推导
// 此两者等价
```

Golang中数组的语义不同于C，数组变量就是整个数组而不是数组首的指针，所以数组名的赋值是复制整个数组，可以将数组理解为特殊的结构体。

### slice
[go blog](https://go.dev/blog/slices-intro)
+ 数组的子数组引用：`s := arr[low:hight]`左开右闭
	+ 开始和结束是可选的，默认起末

+ 一个独立的类型：
	+ 1. `s := []string{"aaa", "bbb"}`和数组的自动推导长度相似，但是是完全不同的东西
	+ 2. 通过内置函数make创建`func make([]T, len, cap（可选）) []T`
		>内部会分配一个数组，然后返回该数组的slice

+ 长度和容量的关系：切片其实相当于一个特殊的结构体，其中包含指向子数组的起始地址指针，该切片长度和该数组容量
	+ 切片的长度：`len(切片变量)`：包含的元素个数
	+ 切片的容量：`cap(切片变量)`：该切片的第一个元素在原数组到原数组最后一个元素的个数
	>**切片是原数组的引用**：对切片来说，原数组仍然存在，则一个切片可以在当前切片的基础上从原数组**往后**扩展，即C++中的vector

+ 切片的零值：`nil`：长度和容量为 0 且没有底层数组

>切片的操作不复制底层数组，而是直接复用底层数组（这让slice和数组索引一样高效）
	
+ 向切片追加元素`func append(s []T, vs ...T) []T`  
	append的第一个参数s是一个元素类型为T的切片，其余类型为T的值将会追加到该切片的末尾

	+ 切片是数组的引用，这个操作会修改原数组，即用追加的值覆盖原数组对应的位置
	+ 如果底层数组空间不够，则分配更大的数组并修改切片的指向

+ 复制操作：`func copy(dst, src []T) int`

+ 切片的遍历
	```go
	for i. v := range slice {
		// i -> 切片索引
		// v -> 对应位置的值，是其值的副本
	}
	```

### map

空值为`nil`：既没有键，又没有值
```go
ts = make(map[key类型]value类型)  // 声明
ts[key值] = value值  // 设置
ts[key值]  // 访问
elem = ts[key值]
elem, ok = ts[key值]  // 如果该键不存在，elem为value类型零值，ok为false
ts = map[key类型]value类型 {  // 初始化  
    key值1: value值1, 
    key值2: value值2, 
    ...
}
delete[ts, key值]  // 删除
```


## 控制流

### 循环for

Golang只有一种循环结构
```go
for 初始化语句; 条件表达式; 后置语句 {
    // 规则同C
    // 初始化语句通常用`:=`语法，声明只可见于for语句作用域的变量
    // 初始化语句和后置语句是可选的，如果全部去掉可以省略分号（相当于其他语言的while了）
    // 如果上面三个一个语句都没有就是无限循环
}
```
+ for each:
	```go
	s := "This is a string var."
	for index, ch := range {
	
	}
	```

### 分支

*   if
    ```go
    if 表达式 {
        
    }
    ```
    *   简短`if`：if可以在表达式前执行一个简单的语句，该语句声明的变量的作用于仅在if的代码块中
*   else
    ```go
    if 表达式 {
        
    } else {
        
    }
    ```
    *   简短if中声明的变量在else中也能使用
*   switch
    ```go
    switch f := 表达式; f {
        case 值1:
            ...
        case 值2:
            ...
        default:
            ...
    }
    ```
    * 较于C而言golang的switch只会选择一个，即隐式的使用了break
	    * 使用`fallthrough`继续执行
    * 没有条件的switch，那么case的标准可以是关于外层变量的**表达式**
    * golang的switch可没有C中对变量类型那么多的限制
    * 多分支case：
	    ```go
	    // 多分支同样操作
	    switch ... {
	        case v1, v2, v3, v4:
	            ...
	        defalut:
	            ... 
	    }
	    ```

### 跳转

Go有`break`和`continue`，同时也有`goto`，不仅如此，Golang还有Label，前面的三个关键字都能使用，用在循环外，类似“装饰器”，用于跨层跳转

### defer

+ defer：`defer 函数调用表达式`：将函数推迟到外层函数返回之后执行，其参数会被立刻求值，但最后才调用
	+ 意义：相当于将一个函数手动压入栈中

+ 应用：
	+ 将应用关闭文件的语句defer
		+ 函数运行完毕符合逻辑
		+ 其实整个函数运行过程中可能发生错误，那么每个错误的地方都要终止函数（不是终止程序），终止函数就要关闭文件，defer后只需要写在一个地方（要求error处理完善）
	+ 锁：
		```go
			mutex.Lock()
			defer mutex.Unlock()
		```

## 面向对象

### 方法

Go 没有类。不过你可以为结构体类型定义方法。  
方法就是一类带特殊的 receiver 参数的函数。  
方法接收者在它自己的参数列表内，位于 func 关键字和方法名之间。  

```go
package main

import (
    "fmt"
    "math"
)

type Vertex struct {
    X, Y float64
}

func (v Vertex) Abs() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
    v := Vertex{3, 4}
    fmt.Println(v.Abs())
}
```
+ receiver：
	+ 是否是指针不关键，只影响是否深拷贝

*   构造**用**函数：名称以`new`或`New`后接类型名的方法
    *   名为`New`的构造用函数，该包只有一个核心结构体，这样更自然简洁

*   上面的语法同样可以用于非结构体类型
    ```go
    type MyFloat float64  // 相当于类型别名
    func (f MyFloat) Abs() float64 {
        if f < 0 {
            return float64(-f)
        }
        return float64(f)
    }
    ```
    *   接收者的类型定义和方法声明必须在同一包内
    *   不能为内建类型声明方法（所以上面使用别名）

+ 

### 接口

接口类型是由一组方法签名定义的集合。  
接口类型的变量可以保存任何实现了这些方法的值。
> 类似C++的虚基类对象或者Java的接口

```go
type 接口名 interface {
    函数名(...) 函数返回值
}
```

> 注意这里的函数接口没有接受者，所以需要函数的接受者匹配，即一个结构体则必须有该结构体作为接受者的方法，一个结构体指针必须有该结构体作为接受者的方法

*   这里的方法的接口是隐式实现的，没有说我这方法是为了这个接受者实现哪个接口、

*   接口值：直接使用接口变量会得到`(value type)`，可以作为函数参数和返回值
    > 或者为`nil`，对为nil的接口调用函数会panic

*   空接口`interface{}`，是一个类型
    *   类型断言
        > 一个空接口类型的变量可以指向任何值
        1.  `t := i.(T)`，其中i是一个空接口，如果其保存有类型`T`则将其值赋给t，否则则出发一个panic
        2.  `t. ok := i.(T)`，这里的话如果没有则t为nil，ok为false而不会panic
    *   类型选择：
        ```go
        switch v := i.(type) {
        case T:
            // v 的类型为 T
        case S:
            // v 的类型为 S
        default:
            // 没有匹配，v 与 i 的类型相同
        }
        ```

### embedding嵌入
>官网说这是在表达composition组合，但是感觉更像继承

当一个结构体的成员是另一个结构体**名**时，就像这个结构体有了一个没有类型的field，在构造时需要显示构造，在使用时可以递归调用成员或方法，但是也可以直接调用（就像这些方法来自最外层结构体一样），实际上最外层结构体继承了内部结构体的所有成员和方法

## 泛型
>妹想到吧，1.18后，Go也添加了对泛型的支持——类型参数

[source](https://gobyexample-cn.github.io/generics)
