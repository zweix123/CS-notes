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
    + [milvus](https://github.com/milvus-io/milvus)
    + [AlayaLite](https://github.com/AlayaDB-AI/AlayaLite)

### 问答场景

### Code Copilot

## AI-Agent

+ 大模型应用框架：
    + [eino](https://github.com/cloudwego/eino)

+ Function Calling：模型内置调用约定好的函数（Tool）；为大模型提供与外界交互能力；

函数本身可以是另一个大模型应用，就变成了AI-Native。

+ MCP(Modal Context Protocol)：即Tool或者LLM-APP提供的能力的格式化表达的约定。
