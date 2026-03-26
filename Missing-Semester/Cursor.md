# Cursor

+ 配置：workbench.activityBar.orientation -> 修改为vertical使侧边栏回到和VSCode一样在最右边竖着。

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


## Free-Cursor

- 原理：
  Cursor 的新用户会有两周的`Pro Trial`权限，两周内功能与`Pro`一致，补全与高速请求有限，但个人体验足够用；
  一个可以接受邮件的邮箱就是 Cursor 的一个用户，因为可以接受邮件就可以收到注册验证码，就可以注册。
  那么假如有无限的邮箱就相当于有无限的账号，就能无限白嫖 Cursor 的`Pro Trial`权限了。

- 白嫖方式的进化：
  - 第一阶段：
    - 一次性邮箱，一次性邮箱平台可以提供无限的暂时邮箱，可以用于创建账号；后面要么是平台提供的账号有重复，要么是 Cursor 对这些平台的域名做封禁，才方式不可用。
    - 邮箱别名，以 Gmail 举例，谷歌邮箱支持在前缀中，添加任意的`.`，或者在前缀的后面添加`+`并在之后添加任意字符串。对于这样的 gmail 邮箱，向其发送邮箱之后都会“重定向”到邮箱本身。此时对于 Cursor 来说就是不同的邮箱同时我们都能收到对应的验证码；后面 Cursor 应该是针对具有别名邮箱做处理。
  - 第二阶段：
    - Cursor 在每个客户端都维护一个机器码，假如在一个机器码使用过太多的账户，就被不被允许使用`Pro Trial`比如升级为`Pro`，[go-cursor-help](https://github.com/yuaotian/go-cursor-help)结局这个问题。
  - 第三阶段：
    - [cloudflare](https://cloudflare.com/)邮箱路由服务，该服务需要提供一个域名和一个有效邮箱，它会将域名作为邮箱服务的后缀，然后对使用该后缀的所有邮箱都“重定向”到提供的有效邮箱中，这是该服务的一种使用方式。此时我们可以任意构造前缀，就有了无数的用户，而这里的有效的邮箱可以收到验证码。

所以到这里思路上是明确的。

- 准备：

  - 一个域名
  - 一个可以接受邮件的邮箱（比如谷歌邮箱）

- 操作：
  - 在 cloudflare 上注册邮箱路由服务 -> 这个步骤可能需要看一下文档或者博客，这里不再赘述，结果就是使用`任意前缀@域名`发送邮件之后，可以在上面的邮箱可以收到。

其实到这里就可以无限白嫖了。

还可以考虑自动化一下，比如把上面的邮箱替换成一个提供 API 获取邮件的邮箱，就可以

1. 使用域名随机生成邮箱
2. 使用随机生成的邮箱通过脚本/爬虫在 Cursor 上注册
   - 通过 API 获取注册的邮件里的验证码
3. 【可选】在本机的 Cursor 上自动更新新用户
4. 使用 go-cursor-help 更新本地机器码
