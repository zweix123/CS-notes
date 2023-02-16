## Intro

RPC, Remote procedure call远程过程调用：多机交互

---

+ IDL, Interface description language接口描述语言：一种编程语言的分类，协调一种数据结构

---

+ ProtoBuf, protocol buffers：一款由谷歌开发的序列化框架，可类比Json或XML，不过这些都是基于文本，而protobuf是二进制格式，更小更快更简单
	+ `.proto` file：一种IDL
	+ `protoc`, Protocol Buffer Compiler：编译proto file的complier
---
+ gRPC：A high performance, open source universal RPC framework
	+ 使用protobuf作为其IDL和底层信息交换格式
---
+ Thrift：IDL相关项目，是Facebook开发的跨语言的RPC服务框架，通过IDL定义接口，将接口编译成不同语言的代码
	>那它如何实现RPC的呢？
