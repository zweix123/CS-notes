# 概述

# web基础

+ **URI**(Uniform Resource Identifier统一资源标志符)：网址
  + **URL**(Universal Resource Locator统一资源定位符)：资源定位
  + URN(Universal Resource Name统一资源名称)      ：资源命名
+ 超文本(hypertext)：
+ http(Hyper Text Transfer Protocol超文本传输协议)：
  + https(... over Secure Socket Layer)：以安全为目标的http通道
    + SSL层：加密——信道安全，信息真实

## 网络过程

> F12后，打开Network选项页，挑选数据包，点击，右端既是其信息，其中Headers即报头，Priview即内容

+ 请求：

  1. 请求方法(Request Method)：

     ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/Python/请求方法.jpg)

  2. 请求的网址(Request URL)：统一资源定位符URL

  3. 请求头(Request Headers)：附加信息

     + Accpet：请求报头域，指定客户端可接受的类型信息

     + Accept-Language：指定客户端可接受的语言类型

     + Accept-Encoding：指定客户端可接受的内容编码

     + Host：指定请求资源的主机IP和端口号

     + Cookie/Cookies：标识登录状态

     + Referer：标识请求来自哪个页面

     + User-Agent（UA）：服务器识别客户的OS和浏览器及其版本

     + Content-Type/互联网媒体类型(Internet Media Type)/MIME类型： 表示具体请求中的媒体类型信息

       ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/Python/MIME.jpg)

  4. 请求体(Request Body)：post请求的表单数据，get则为空

+ 响应：
  1. 响应状态码(Response Status Code)：表示服务器的响应状态
  2. 响应头(Response Headers)：应答信息
     + Data：标识响应产生的时间
     + Last-Modified：指定资源的最后修改时间
     + Content-Encding：指定响应内容的编码
     + Server：包含服务器的信息
     + Content-Type：文档类型，指定返回的数据类型
     + Set-Cookie ：
     + Expries：
  3. 响应体(Response Body)：内容

+ 静态页面和动态页面

  + 静态页面：HTML
  + 动态页面：可根据URL的参数改变显示内容

+ 会话和Cookies：会话在服务端，Cookies在客户端，对前后有关系的对话过程，以Cookies表示复杂的身份认证信息，减小传递的开销

  > F12，选择Application选项卡，在Storage栏中的最后一项即为Cookies

  1. Name：Cookes的唯一编码，不可更改
  2. Value：Unicode字符为字符编码，二进制数据则为BASE64编码
  3. Domain：可以访问该Cookie的域名
  4. **Max Age**：该Cookie失效的时间，单位为秒，为正则计时，为负则不被报错，关闭则消失
  5. Path：Cookie的使用路径
  6. Size：Cookie的大小
  7. HTTP字段
  8. Secure字段：安全协议

+ 代理(proxy server)：网站的反爬虫机制，对访问频率过高的IP进行封IP

  + 用处：

    + 突破自身IP访问限制
    + 访问单位团体内部资源
    + 提高访问速度
    + 隐藏自身真是IP

  + 分类：

    1. 根据协议分：

       ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/Python/代理分类1.jpg)

    2. 根据匿名程度分：

       ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source/Programing-Language/Python/代理分类2.jpg)

## 前端基础

+ 组成：

  + HTML（超文本标记语言(Hyper Text Markup Language)）：
  + CSS（层叠样式表(Cascading Style Sheets)）：
  + JavaScript（类似Java的脚本语言）：

+ HTML：根据HTML DOM标准，HTML文档中的所有内容都是**节点**，将其视为**树结构**

  > DOM(Document Object Model,文档对象模型)：W3C(万维网联盟)的标准
  >
  > + 核心DOM：针对任何结构化文档的标准模型
  > + XML DOM：针对XML文档的标准模型
  > + HTML DOM：针对HTML文档的标准模型

  + 整个文档是文档节点
  + 每个HTML元素是元素节点
  + HTML元素内的文本是文法节点
  + 每个HTML属性是属性节点
  + 注释是注释节点

+ CSS：选择器是其定位节点的方式：节点 id、class.节点、标签买筛选

# 库

## urllib

+ python内置的HTTP请求库，无需install

+ module
  + `request`：模拟请求
  + `error`：
  + `parse`：提供URL处理方法
  + `robotparser`：识别网站的`robots.txt`文件，判断可爬否

> urllib.parse.urlencode({字典})：将参数字典转化为字符串

### request

+ `urlopen()`

  + 参数：`urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=Flse, context=None)`

    + data：接收**字节流编码格式**（bytes），将请求方法从GET变为POST
    + timeout：设置超时时间，单位为秒，超过则抛出异常(`urllib.request.URLError`)

  + 返回：`HTTPResponse`类型对象

    | 方法和属性                                            | 说明         |
    | ----------------------------------------------------- | ------------ |
    | `read()`                                              | 返回网页内容 |
    | `status`                                              | 结果状态码   |
    | else                                                  |              |
    | `readinto(), getheaders(), getheader(name), fileno()` |              |
    | `msg, version, status, reason, debuglevel, cloesd`    |              |
  
+ Request类：用来配置丰富的参数

  + 构造方法：`class urllib.request.Request(url, data=None, headerrs={}, origin_req_host=Node, unverifiable=False, methed=None)`

    + url：URL=字符串类型

    + data：=bytes类型

      > 字典类型可由urllib.parse.urlencode()编码

    + headers：请求头

    + url（字符串类型）（必须）：URL

    + data：bytes（字节流）类型

      > 字典可由urllib.parse.urlencode()编码

    + headers：请求头=字典

      > 还有`add_header()`方法添加

    + origin_req_host：请求方的host名称或者IP地址

    + unverifiable：请求是否是无法验证=bool

    + method：请求使用=string

    ```python
    from urllib import request, parse
    
    url = 'http://httpbin.org/post'
    headers = {
        'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        'Host' : 'httpbin.org'
    }
    dict = {
    	'name': 'Germey'
    }
    data = bytes(parse.urlencode(dict), encoding='utf8')
    req = request.Request(url=url, data=data, headers=headers, method='POST')
    response = request.urlopen(req)
    print(response.read().decode('utf-8'))
    ```
    
  
+ Handler类：超类：`BaseHandler`类

  > https://doces.python.org/3/library/urllib.request.html#urllib.request.BaseHandler

  + 验证：

    

## selenium


```c++
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://baidu.com')

driver.quit() 
```
