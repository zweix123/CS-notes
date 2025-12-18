## Cursor

- 就 UI 上，可能有刚从 VSCode 到 Cursor 的朋友不舒服侧边栏的位置不一样了，可以设置的![workbench orientation](https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Missing-Semester/cursor-sidebar.png)
  - 竖直：workbench.activityBar.orientation 设置为 vertical，

现在的 cursor 挺有意思的，记录一下 : )

说一下背景，我的主要开发语言有 Golang、Python 和 C++，这些语言在 VSCode 都能有不错的体验，我也几乎没用过 JB 家的 IDE。

- 在编辑器层面，cursor 是套娃的 VSCode（只能说 VSCode 虽然不是真开源，但是确实是公开了相当一部分的代码，而且其上活跃的插件社区是真开源）。在最初 cursor 刚出那会，我有体验过，就被它古典的 UI 劝退了（当时好像只支持 vim 模式？）。但是现在，它确实是补上了这部分能力。在安装 cursor 时选择 VSCode 模式（所以我也并不知道其他模式怎么样），它会自动载入我目前在 VSCode 的所有配置（插件、配置、快捷键）。打开之后，UI 和交互和 VSCode**几乎一样**！从 VSCode 抢人简直轻而易举。

  > 不仅是配置，在 cursor 里的操作“感觉”也一样，比如在终端通过命令打开，比如不同层级的配置。简直了，直接摘桃子啊。

- 那副驾驶怎么样呢？VSCode 也有 Copilot 呀？我为什么不在 VSCode 上用 Copilot 而用你套娃的 cursor（即使几乎一样）？

  - 首先 Copilot 提供什么能力？

    1. Chat
    2. AI 补全：通过将光标后的代码后移，然后以 inline completion 进行提示，按 Tab 接受
    3. 对于报错和警告，有 AI 解决的按钮

  - VSCode 的插件框架有什么限制？

    - VSCode 的插件框架应该是有诸多限制，需要在其能力之上开发

  - cursor 多了什么？
    - 提示的代码并不仅是 inline completion，还有“悬浮”的
    - 不仅能提示加，还能提示删除
    - 最最重要的：**Cursor 的上下文是整个项目/Workspace**，理论上 Cursor 应该会比 Copilot 聪明，代价是假如我的项目里有一个数据文件并打开，Cursor 就不说话了（按理说 Curosr 应该搞一个可以识别这样的文件的呀）（确实搞了）
    - 除此之外：Cursor 的划词提问比 VSCode 更流畅自然，比如可以选择终端文本，比如相关快捷键一致，比如选择文本相关上下文（AI 在 Cursor 是一等公民）
    - 嗨，说那么多干啥，看看官方文档：[cursor features](https://www.cursor.com/features)

  因为 VSCode 插件的限制，使其他副驾驶插件只能在光标后面“挤”出空间弹出补全代码，但是在 cursor 中，不仅这一种形式，除了添加、还有替换、还有删除，还有这些的**组合**。

- 再来说一下功能说的，我有接触有朋友觉得，AI 会干扰 TA 的编程思路，但是我觉得不会，当我们按照我们的思路完成前置代码以及一定的注释后，AI 可以理解我们的意思，帮我完成**我想完成**的代码，非常棒。

- Cursor 无限续杯：Curosr 的新用户可以试用 14 天的 Pro 版本以及 500 个问答额度，所以加上我们每 14 天可以得到一个新邮箱账号即可无限续杯。
  - 工具：
    - https://cursor-auto-free-doc.vercel.app/
  - 方案：
    - https://waite.wang/posts/tools/cursor-forever-free/

# 其他
