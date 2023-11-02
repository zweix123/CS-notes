+ 并发模型：时间片轮转

## channels

+ [缓冲](https://gobyexample-cn.github.io/channel-buffering)：

### 无锁!

https://gobyexample-cn.github.io/stateful-goroutines

## sync

### join

```go
import "sync"

var wg sync.WaitGroup

wg.Add(数字)  // 调用协程前

wg.Done()  // 协程中

wg.Wait()  // 等待到计数器回到0
```

### Mutex