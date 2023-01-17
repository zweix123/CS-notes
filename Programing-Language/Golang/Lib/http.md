
[TOC]



## Handler

标准库`net/http`中Web Server模型：系统中有一个Handler，每每收到一个HTTp请求，就创建一个goruntine去处理，或者使用一个多路复用器做路由，每每收到一个HTTP请求，将其分发给不同的Handler。

标准库中这样复用器的标准实现`http.DefaulServeMux`

```go
http.ListenAndServe(":8080", nil)
```

1.  第一个参数即`localhost:8080`
2.  第二个参数指的是将接受的http请求给到哪个Handler，是指针类型
    1.  可以真的传入一个Handler结构体的指针
    2.  这里的`nil`只的是自动匹配已有的Handler

启动这样一个Mux还有其他方法

```go
server := http.Server{
    Addr:    ":8080",
    Handler: nil,
}
server.ListenAndServe()
```

可以看出和上面的方法基本一样

那么Handler到底是个什么呢？

```go
type Handler interface {
	ServeHTTP(ResponseWriter, *Request)
}
```

其实是一个接口，实现了代码中的哪个函数，我们观察它的两个参数就能理解其合理性

1.  Response对象即保存我们对该请求的答复
2.  Request对象即保留对我们的请求的内容

那么一个实现了该接口的结构体创造的变量即可作为上面的Handler

这里还有一个问题，就是上面的Handler，确实如果指定某一个Handler没有问题，那么nil是如何匹配的呢——这就是http库做的事情，将我们写的Handler那么一个“域中”：

```go
http.Handle(url_pattern string, Handler)`
```

这样这个Handler对象即可纳入http的“感知”中，请求的url匹配其pattern，即会被上面的Mux分配给一个Handler。

现在的问题是我们想象如何变量，我们要创建一个结构体，然后为该结构体实现一个方法，接着为这个结构体创建一个对象，然后将这个对象，现在是一个Handler绑定到http中，好复杂，如果有多个Handler就太混乱了，http提供另一个写法。

```go
func HandleFunc(pattern string, handler func(ResponseWriter, *Request))
```

我们观察这个函数定义，其中pattern就是url路径，第二个handler是一个函数，我们发现这个函数就是Handler接口中的函数定义，所以我们直接在这个函数传参时实现一个函数就完成了让Mux管理一个Handler的操作。

这个函数叫Handler函数，即行为和handler类似的函数，其实现原理就是http为我们实现了上面的那个过程：

```go
http.Handle("/hello", http.HandlerFunc(func(ResponseWriter, *Request){
    w.Write([]byte("hello"))
}))
```

我们观察这个，其中Handle就是上面的，把一个handler纳入mux的管理的，然后后面有个套娃，里面是一个干净的函数，然后这个函数外面套了个`HandlerFunc`函数，它就相当于把这个函数变成一个Handler。那么它是怎么变的呢？这个`HandlerFunc`其实是一个**函数类型**（这里不理解需要再去学习一下语言基础），这个函数类型实现了名为`ServeHTTP`的方法，所以上面的那句话相当于将传入的函数（我们如何request请求）转换成了名为ServeHTTP的方法，而其内容。。。算了算了2022.1.12不能理解

### 内置Handler

*   `http.NotFoundHandler() Handler`：404
*   `http.RedirectHandler(url string, code int) Handler`：跳转
*   `http.StripPrefix(prefix string, h Handler) Handler`：去掉指定前缀，然后调用另一个Handler，前缀不匹配则返回404，相当于修饰器
*   `http.TimeoutHandler(h Handler, dt time.Duration, msg string) Handler`：调用另一个Handler，如果超时，返回msg，相当于修饰器
*   `http.FileServer(root FileSystem) Handler`

    > ```go
    > type FileSystem interface {
    >      Open(name string) (file, erro)
    > }
    > ```

    一些用法：

    ```go
    func main() {
        http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
            http.ServeFile(w, r, "./"+r.URL.Path)
        })
        http.ListenAndServe(":8080", nil)
    }
    ```

    这样的代码通过`ip:8080`访问当前目录下的所有文件（在浏览器中打开）

    ```go
    func main() {
        http.ListenAndServe(":8080", http.FileServer(http.Dir("./")))
    }
    ```

    利用上面的Handler这样也可以

    > 到这里就可以做一些实用的了，我们将自己笔记本上的一些东西暴露在互联网上，其他人可以任意的下载，上面说的在浏览器打开就是一种下载，如果浏览器不能渲染也可以下载本地。

## HTTP消息

### 基础知识

> 一些Golang之外的知识

*   HTTP报文格式：基于文本的
    *   请求报文：
        *   请求行request line：
            | 请求方法 | 空格 | URL | 空格 | 协议版本 | 回车符 | 换行符 |
            | ---- | -- | --- | -- | ---- | --- | --- |
        *   请求头部header：0个或多个
            | 头部字段名 | : | 值 | 回车符 | 换行符 |
            | ----- | - | - | --- | --- |
        *   空行blank line
            | 回车符 | 换行符 |
            | --- | --- |
        *   请求数据body

    *   响应报文：
        *   状态行status-line
        *   消息报头headers
        *   空行
        *   响应正文

*   url通用格式：`scheme://[userinfor@]host/path[?query][#fragment]`
    *   不以斜杠开头的：`scheme:opaque[?query][#fragment]`

*   html表单
    *   post
        ```html
        <form action="/process" method="post">  action对应路径, post即指出post
            <input type="text" name="first_name" />  各种key-value对
            <input type="text" name="last_name" />
            <input type="submit" />
        </from>
        ```
        这个表单即在post报文的body中，其格式通过表单的Content Type——`enctype`属性
        *   `application/x-www-form-urlencoded`：表单数据编码到url的query中
        *   `multipart/form-data`：name-value对转换成MIME消息部分，常用于上传文件
            ```html
            <form ...>
                ...
                <input type="file" name="uploaded">
            </form>
            ```
        *   `text/plain`
    *   get：上面html代码中的method为get，只能编码到url中

    <!---->

    *   Json Body

### 请求

*   结构体`http.Request`
    *   字段`URL`：指向结构体`url.URL`的指针
        ```go
        type URL struct {
            Scheme      string
            Opaque      string    // encoded opaque data
            User        *Userinfo // username and password information
            Host        string    // host or host:port
            Path        string    // path (relative paths may omit leading slash)
            RawPath     string    // encoded path hint (see EscapedPath method)
            OmitHost    bool      // do not emit empty host (authority)
            ForceQuery  bool      // append a query ('?') even if RawQuery is empty
            RawQuery    string    // encoded query values, without '?'
            Fragment    string    // fragment for references, without '#'
            RawFragment string    // encoded fragment hint (see EscapedFragment method)
        }
        ```
        *   url query:
            1.  直接访问`RawQuery`字段`string`
            2.  `r.URL.Query()`得到该字符串对应的`map[strubg][]string`
                > 这里为什么value是slice呢？因为url中可能有多个一样的key
        *   Fragment莫名消失

    *   字段`Header`：通过`Header`类型描述`type Header map[string][]string`
        1.  直接使用该字段
        2.  直接使用该字段作为map通过key得到value：返回字符串切片
        3.  使用该字段的`Get(key)`方法得到value  ：返回字符串

    *   字段`Body`：是`io.ReadCloser`接口
        ```go
        type ReadCloser interface {
            Reader  // a interface
            Closer  // a interface too
        }
        type Reader interface {
            Read(p []byte) (n int, err error)
        }
        type Closer interface {
            Close() error
        }
        ```
        使用
        ```go
        {
            length := r.ContentLength
            body := make([]byte, length)
            r.Body.Read(body)
            // print(string(body))
        }
        ```

    *   关于表单的字段`From, PostForm, MultipartForm`
        ```go
        {
            r.ParseForm()  // 先进行解析
            // 即可通过r.Form字段访问map[string][]string
            
            // url里可以有key-value对，而form也能转换成key-value对
            // r.PostForm字段则只提供form中的键值对
        }
        ```
        上面讲的enctype都是application/x-www-form-urlencoded那么如果是multipart/form-data呢？
        ```go
        r.ParseMultipartForm()
        r.MultipartForm  # 只有form中的key-value
        ```
        *   方法：
            `r.FormValue(key)`：得到value，取url和form的第一个（form）
            `r.PostFormValue(key)`：同上，但只读form，且要application/x-www-form-urlencoded类型

        *   文件上传：

            ```go
            func process(w http.ResponseWriter, r *http.Request) {
                // 一个方案
                r.ParseMultipartForm(1024)
                fileHeader := r.MultipartForm.File\[name的名字]\[第几个]  // File字段只找type为file的input，key为其中的name内容，有的上传块是可以上传多个的，所以这个vlaue是slice
                file, err := fileHeader.Open()  // 得到文件
                
                // 另一个方案
                file, _, err := r.FormFile("name名字")  // 只返回第一个value
                
                if err == nil {
                    data, err := ioutil.ReadAll(file)  // ioutil.ReadAll将文件读取为byte切片
                    if err == nil {
                        ...
                    }
                }
            }
            ```

    *   方法：访问请求的Cookie、URL、User Agent

### 响应

+   接口`http.ResponseWriter`，其指向`http.response`（小写非导出）这个struct

>   为什么它在函数参数中是没有`*`的？因为它是一个接口，其指向一个结构体，所以按值传递就是指针

+   方法`Write([]byte)`：写入resp的body中
    >   如果内容没有指明Content-Type，则通过字节切片的前512来推测

+   方法`WriteHeader(HTTP状态码 int)`：作为HTTP响应的状态码
    +   如果该方法没有显示调用，则在第一次调用Write方法前，隐式调用`WriteHeader(http.StatusOK)`
    +   调用后无法修改header

+   方法`Header`，返回headers的map，可进行修改
    +   `map.Set(key, value_)`


## 路由

+ （前置）Controller：
    +   静态资源
    +   分发请求

+   常见写法，将之前讨论的Handler这样处理
    创建一个子目录`controller`，其中有个master`controller.go`，还有很多路径`路径1.go`、`路径2.go`、...
    +   这里以路径`/home`为例
        ```go
        // ./controller/home.go
        package controller
        
        func registerHomeRoutes() {
            http.HandleFunc("/home", handleHome)
        }
        func handleHome(w http.ResponseWriter, r *http.Request) {
            ...
        }
        ```
    
    +   
        ```go
        // ./controller/controller.go
        package controller
        
        func RegisterRoutes() {
            registerHomeRoutes()
        }
        ```
    我们发现上面只有controller.go中的函数是大小，则main函数只需要调用一个函数`controller.RegisterRoutes()`即可

以上说的是静态路由，下面讨论路由参数

+   带参数路由：根据路由参数，创建出一族不同的页面
    >   使用相同的模板，但是部分数据不同
    ```
    "/sam"   // 不带参数
    "/sam/"  // 带参数，因为这个url更匹配带参数的url
    ```

+   第三方路由：
    >   +   `gorilla/mux` ：注重功能
    >   +   `httprouter`：注重性能

## HTTPS

```go
func ListenAndServeTLS(addr, certFile, keyFile string, handler Handler) error
// 中间两个分别是文件路径，
```

## HTTP2

HTTP2较于HTTP2快很多

HTTP1：在TCP中header+body，其中header无法被压缩

HTTP2：在TCP中建立stream，相当于多个管道，而且是全双工的，所以把一个请求分成多个Frame，这样各种数据类型可以单独发送，继而单独的优化
+   多路复用
+   允许对header压缩
+   默认安全，虽然其支持http和https
+   关键Server Push
    >   如果没有：
    >   请求-》发html-》缺。css-》发。css请求，法会。css
    我们作为html的坐着，其实我们知道一定要css
    有了server push则是一口气全都发过来。

```go
func handleHome(...) {
    if pusher, ok := w.(http.Pusher); ok {
        pusher.Push(css文件在项目中的路径。。。)
    }
}
```