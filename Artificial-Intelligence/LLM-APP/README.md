+ Ref
    + [微信公众号 · 腾讯技术工程 · 不需要AI和数学知识背景，这篇文章带你学会大模型应用开发](https://mp.weixin.qq.com/s?__biz=MjM5ODYwMjI2MA==&mid=2649791944&idx=1&sn=9bd69fbe147a8e480158ee32348d88a6&chksm=bfce8dec0844bbb5f588d752074a57ff7a45c54368234bb2d7269e4fd6df7a8251f9d4c53a07&xtrack=1&scene=90&subscene=93&sessionid=1741609844&flutter_pos=0&clicktime=1741609846&enterid=1741609846&finder_biz_enter_id=4&ranksessionid=1741609804&ascene=56&fasttmpl_type=0&fasttmpl_fullversion=7634324-zh_CN-zip&fasttmpl_flag=0&realreporttime=1741609846877#rd)

## RAG(Retrieval-Augmented Generation)
> 检索增强生成技术

1. Chunk（分块）
2. Embedding（嵌入）：Any -> \[\]float
3. VectorDB（向量数据库召回）

+ 性能相关性因素：
    + RAG召回数据的相关性
        + Chunk策略
        + Embedding模型
        + 召回策略调优
    + 基座大模型的推理能力

+ 向量数据库：
    + [AlayaLite](https://github.com/AlayaDB-AI/AlayaLite)

### 问答场景

### Code Copilot

## AI-Agent

+ 大模型应用框架：
    + [eino](https://github.com/cloudwego/eino)

+ Function Calling：模型内置调用约定好的函数（Tool）；为大模型提供与外界交互能力；

函数本身可以是另一个大模型应用，就变成了AI-Native。

+ MCP(Modal Context Protocol)：即Tool或者LLM-APP提供的能力的格式化表达的约定。
