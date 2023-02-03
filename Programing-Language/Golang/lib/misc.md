## `os`包
提供了用于处理操作系统相关内容的函数/值且以一种独立于平台的方式



### Hello World
```go
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	// var s, sep string
	// s, sep := "", ""

	// for _, arg := range os.Args[1:] {
	// 	s += sep + arg
	// 	if sep == "" {
	// 		sep = " "
	// 	}
	// }

	// for i := 1; i < len(os.Args); i++ {
	// 	s += sep + os.Args[i]
	// 	sep = " "
	// }

	fmt.Println(strings.Join(os.Args[1:], " "))
}
```

## Json

+   Json对象简介：
    用大括号括起来，里面有属性有值，属性后面跟着冒号然后跟着其值
    每个名都需要用双引号括起来
    值的类型可以是字符串、数值、布尔类型、null

+   Go的Struct：
    ```go
    type structName struct {
        Tag tag_type
        ...
    }
    ```

两者存在差异

+   Golang提供语法去做映射
    +   名映射：tag
        ```go
        type company struct {
            ID     int    `json:"id"`
            Name   string `json:"name"`
            Coutry string `json:"country"`
        }
        ```
    +   类型映射：
        +   Go bool: Json boolean
        +   Go float64: Json num
        +   Go string: Json strings
        +   Go nil: Json null

---

+ 对未知类型的Json的映射：
	+ `map[string]interface`存储任意JSON对象
	+ `[]interface{}`存储任意的Json数组

+   使用:
    +   解码，读:
        ```go
        dec := json.NewDecoder(io.Reader)  // 参数实现Reader接口，创建一个解码器
        dec.Decode(&sam)  // 解码器开始解码，并将内容写入sam，sam为上面说的类型
        ```
    +   编码，写：
        ```go
        enc := json.NewEncoder(w io.Writer)  // 同上
        enc.Encode(res)  // 同上
        ```