## Linux

```c++
#include <sys/socket.h>
```

+ 创建套接字：

  ```c++
  int socket(int domain, int type, int protocol);
  //	-> 成功返回文件描述符，失败时返回-1
  ```

1. Server

   + 分配IP地址和端口号：

     ```c++
     int bind(int sockfd, struct sockaddr *myaddr, socklen_t addrlen);
     //	-> 成功时返回0，失败时返回-1
     ```

   + 转为可接受请求状态：

     ```c++
     int listen(int sockfd, int backlog);
     //	-> 成功时返回0，失败时返回-1
     ```

   + 受理连接请求

     ```c++
     int accept(int sockfd, struct sockaddr *addr, socklen_t *addrlen);
     //	-> 成功返回文件描述符，失败时返回-1
     ```

2. Client

   ```c++
   int connect(int sockfd, struct sockaddr *serv_addr, socklen_t addrlen);
   //	-> 成功时返回0，失败时返回-1
   ```

## Windows

```c++
#include <winsock2.h>
```

0. 设置版本、初始化库：

   ```c++
   int WSAStartup(WORD wVersionRequested, LPWSADATA lpWSAData);
   //	-> 成功时返回0，失败时返回非零的错误代码值
   ```

   + `wVersionRequested`：`Winsock`版本信息（`WORD=unsigned short`）：一个字节16位，以十六进制编辑，高8位是副版本号、低8位是主版本号。多使用宏函数`MAKEWORD(主版本号, 副版本号)`
   + `lpWSAData`：WSADATA结构体变量的地址值（`lpWSADATA`是`WSADATA`的指针）

   ```c++
   int main(int argc, char* argv[]) {
       WSADATA wsaData;
       //...
       if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
           ErrorHandling("WSAStartup() error!");
       
       return 0;
   }
   ```

   + 注销：把Winsock相关库还给Windows操作系统

     ```c++
     int WSACleanup(void);
     //	-> 成功时返回0，失败时返回SOCKET_ERROR
     ```

+ 创建套接字

  ```c++
  SOCKER socket(int af, int type, int protocol);
  //	-> 成功返回套接字句柄，失败时返回INVALID_SOCKET
  ```

1. Server

   + 分配IP地址和端口号

     ```c++
     int bind(SOCKET s, const struct sockaddr * name, int namelen);
     //	-> 成功时返回0，失败时返回SOCKET_ERROR
     ```

   + 转为可接受请求状态

     ```c++
     int listen(SOCKET s, int backlog);
     //	-> 成功时返回0，失败时返回SOCKET_ERROR
     ```

   + 受理连接请求

     ```c++
     SOCKET accept(SOCKET s, struct sockaddr *addr, int *addrlen);
     //	-> 成功返回文件描述符，失败时返回INVALIDD_SOCKET
     ```

2. Server

   ```c++
   int connect(SOCKET s, const struct sockaddr *name, int namelen);
   //	-> 成功时返回0，失败时返回SOCKET_ERROR
   ```

# Socket I/O

Linux将套接字看作是文件的一种，Windows则区分文件和套接字

Linux术语文件描述符，Windows术语文件句柄

## Linux

+ Low-Level File Access底层文件访问：由Linux提供（而不是ANSI标准）文件IO函数
+ File Descriptor文件描述符（文件句柄）：
  + 文件描述符0：对象：标准输入：Standard Input
  + 文件描述符1：对象：标准输出：Standard Output
  + 文件描述符2：对象：标准错误：Standard Error

这里文件描述符是代码中唯一对应文件的整数，起始0~2是Linux提供的，其他的从3开始索引

---

+ 打开文件

  ```c++
  #include <sys/types.h>
  #include <sys/stat.h>
  #include <fcntl.h>
  
  int open(const char *path, int flag);
  //	-> 成功返回文件描述符，失败时返回-1 
  ```

  + `path`：文件名的字符串地址

  + `flag`：文件打开模式信息：多参数使用或运算符

    | 打开模式          | 含义                       |
    | ----------------- | -------------------------- |
    | `O_CREAT` creat   | 必要是创建文件             |
    | `O_TRUNC` trunc   | 删除全部现有数据           |
    | `O_APPEND` append | 维持现有数据，保存到其后面 |
    | `O_RDONLY` rdonly | 只读打开                   |
    | `O_WEONLY` wronly | 只写打开                   |
    | `O_RDWR` rdwr     | 读写打开                   |

+ 关闭文件：

  ```c++
  #include <unistd.h>
  
  int close(int fd);
  //	-> 成功时返回0，失败时返回-1
  ```

  + `fd`：需要关闭的文件或套接字的文件描述符

+ 将数据写入文件：

  ```c++
  #include <unistd.h>
  
  ssize_t write(int fd, const void * buf, size_t nbytes);
  //	-> 成功时返回写入的字节数，失败时返回-1
  ```

  + `fd`：显示数据传输对象的文件描述符
  + `buf`：保存要传输数据的缓冲地址值
  + `nbytes`：要传输数据的字节数

  > + `size_t`是`unsigned int`类型
  >
  > + `ssize_t`是`signed int`类型
  >
  > 这些都是primitive元数据类型：在`sys/types.h`头文件的`typedef`声明
  >
  > 是因为C语言的数据类型和硬件有关，于是通过这种方式来实现修改少量代码来让代码中的类型适配

+ 读取文件中的数据：

  ```c++
  #include <unistd.h>
  
  ssize_t read(int fd, void * buf, size_t nbytes);
  //	-> 成功时返回接受的字节数（但遇到文件结尾则返回0），失败时返回-1
  ```

  + `fd`：显示数据接受对象的文件描述符
  + `buf`：要保存接受数据的缓冲地址值
  + `nbytes`：要接受数据的最大字节数

## Windows

+ handle句柄：Windows通过文件句柄和套接字句柄区分

```c++
#include <winsock2.h>
```

+ Send

  ```c++
  int send(SOCKER s, const char* buf, int len, int flags);
  //	-> 成功时返回传输字节数，失败时返回SOCKET_ERROR
  ```

  + `s`：表示传输对象连接的套接字句柄值
  + `buf`：保存待传输数据的缓冲地址值
  + `len`：要传输的字节数
  + `flags`：传输数据时用到的多项选项信息

+ Read

  ```c++
  int recv(SOCKET s, const char * buf, int len, int flags);
  //	-> 成功时返回接收的字节数（收到EOF时为0），失败时返回SOCKET_ERROR
  ```

  + `s`：表示数据接受对象连接的套接字句柄值
  + `buf`：保存接受数据的缓冲地址值
  + `len`：能够接受的最大字节数
  + `flags`：接受数据时用的多种选择信息

+ Close关闭套接字（Linux套接字和文件等价，使用close关闭套接字）

  ```c++
  int closesocket(SOCKET s);
  //	-> 成功时返回0，失败时返回SOCKET_ERROR
  ```

# Create Socket - Protocol

## Linux

```c++
int socket(int domain, int type, int protocol);
//	-> 成功返回文件描述符，失败时返回-1
```

+ `domain`：套接字中使用的Protocol Family协议族信息
+ `type`：套接字数据传输类型信息
+ `protocol`：计算机间通信中使用的协议信息

+ `domain`：选择一个协议族：

  + 头文件`sys/socket.h`中声明的协议族

    | 名称               | 协议族               |
    | ------------------ | -------------------- |
    | `PF_INET` pf_inet  | IPv4互联网协议族     |
    | `PF_INET6`         | IPv6互联网协议族     |
    | `PF_LOCAL`         | 本地通信的UNIX协议族 |
    | `PF_PACKET` packet | 底层套接字的协议族   |
    | `PF_IPX`           | IPX Novel协议族      |

+ `type`：选择传输方式

  1. 面向连接的套接字`SOCK_STREAM`：可靠的、按序传递的、基于字节的面向连接的数据传输方式的套接字

     + 传输过程中数据不会消失

     + 按序传输数据

     + 传输的数据不存在数据边界Boundary：

       > 收发数据的套接字内部有buffer缓冲，只要其不满，不意味着立刻去读取
       >
       > 如果其满了并且读入比读出快，也不会有数据丢失，因为面向连接的套接字会根据接收端状态进行传输，而且还有重传服务

       必须一一对应

  2. 面向消息的套接字`SOCK_DGRAM`：不可靠的、不按序传递的、以数据的告诉传输为目的的套接字

     + 强调快速传输而非传输顺序
     + 传输的数据可能丢失也可能损毁
     + 传输的数据有数据边界：一次发送就有一次接受
     + 限制每次传输的数据大小

+ `protocol`：同一协议族中存在多个数据传输方式相同的协议
  + IPv4协议族中面向连接的套接字`int tcp_socket = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)` ipproto_tcp
  + IPv4协议族中面向消息的套接字`int tcp_socket = socket(PF_INET, SOCK_STREAM, IPPROTO_UDP)` 

## Windows

```c++
SOCKET socket(int af, int type, int portocol);
//	-> 成功返回socket句柄，失败时返回INVALID_SOCKET
```

+ 参数同Linux

+ 返回类型SOCKER是结构体类型保存整型套接字句柄值

  函数返回整型

# Start Blind

### IPv4

Internet Address网络地址

+ IP地址类型：

  + IPv4 (Internet Protocol version 4)：4字节地址族
  + IPv6 (Internet Protocol version 6)：16字节地址族

+ IPv4格式：分为网络地址和主机地址，并分为ABCDE等类型，区别在于网络地址和主机地址长度，其中A、B、C、D类IP地址中网络地址分别占1、2、3、4个字节，剩下部分为主机地址，其中D类是多播IP地址

  + ABC类的区分：

    |      | 首字节范围 | 首地址         |
    | ---- | ---------- | -------------- |
    | A    | `0~127`    | 首位以0开始    |
    | B    | `128~191`  | 首2为以10开始  |
    | C    | `192~223`  | 首3位以110开始 |

### Port

> 计算机配有NIC Network Interface Card 网络接口卡 数据传输设备

端口号由16位构成（即范围为`0~65535`）：其中`0-1023`是知名端口Well-known. PORT：一般分配给特定应用程序

### Order

> CPU内保存数据的方式
>
> + 大端序Big Endian：高位字节存放在低位地址（字节从左到右是高到低、地址从左到右是低到高）
> + 小端序Little Endian：高位字节存放在高位地址

+ 网络中使用的字节序：网络字节序Network Byte Order，使用大端序

+ 字节序转换Endian Conversions，在填充sockadr_in前就转换成网络字节序，通过函数转换：

  ```c++
  unsigned short htons(unsigned short);
  unsigned short ntohs(unsigned short);
  unsigned long htonl(unsigned long);
  unsigned long ntohl(unsigned long);
  ```

  > h表示host主机 字节序   n表示网络network字节序

## Linux

```c++
int bind(int sockfd, struct sockaddr *myaddr, socklen_t addrlen);
//	-> 成功时返回0，失败时返回-1
```

+ `sockfd`：socket套接字

+ `myaddr`：参数类型是`sockaddr`，但是实际上传入的是`sockaddr_in`类型

  ```c++
  struct sockaddr_in {
      sa_family_t sin_family;  // 地址族Address Family
      uint16_t sin_port;  // 16位TCP/UDP端口号
      struct in_addr sin_addr;  // 32位IP地址
      char sin_zero[8];  // 不使用，做占位符，使之和sockaddr大小相同
  };
  
  struct in_addr {
      In_addr_t s_addr;  // 32位IPv4地址——In_addr_t s_addr
  }
  ```

  + `sin_family`
    + `AF_INET`：IPv4网络协议中使用的地址族
    + `AF_INET6`：v6
    + `AF_LOCAL`：其他
    
  + `sin_port`：需要转换成网络字节序

  + `sin_addr`：
  
    ```c++
    #include <arpa/inet.h>
    
    int_addr_t inet_addr(const char * string):
    //	-> 成功时返回32位大端序整数型值，失败时返回INADDR_NONE
    ```
  
    



# 通用

+ 可移植操作系统接口Portable Operating System Interface, POSIX：是为Unix操作系统建立的标准

