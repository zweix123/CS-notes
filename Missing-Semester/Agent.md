> 文章定位：是 setup 不是 awesome

配置内容分类

- 维度1——是否开源：开源 or 公司私有，这里只讨论开源的
- 维度2——是否智能体通用：智能体通用 or 某智能体独享，一般来说都是通用的，对于不通用的会单独说明；`npx skill add`命令是针对 Claude Code 、 CodeX 和 OpenCode 均安装。
- 维度3——种类：独立软件、skill、mcp、plugin，这里都会涉及
- 维度4——能力：通用能力（办公通用能力、编程通用能力）、垂类领域能力

- 必要工具：
  - Model Provider 管理：[farion1231/cc-switch](https://github.com/farion1231/cc-switch) 50k+star，事实标准，支持常用Agent。
  - Skills 管理：[vercel-labs/skills](https://github.com/vercel-labs/skills) 16k+star，事实标准，支持常用Agent。
  - 语音输入：目前 CodeX 本身支持，所以我没有做详细调研，有看到收费的 typeless 和开源的 input0
  - Token 节省： [rtk-ai/rtk](https://github.com/rtk-ai/rtk) && [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)
  - 记忆：目前各大 Agent 基本都内置记忆了，领域信息基本通过知识库提供而非记忆，这里不涉及。
  - CLI：
    - MCP CLI：[openclaw/mcporter](https://github.com/openclaw/mcporter) 5k+star，龙虾项目空间下的，即开即用。
    - App to cli：HKUDS/CLI-Anything
    - Web to cli：`jackwener/opencli`
    - Github to cli：TODO

## 配置

```bash
# codex 默认使用 websocket, 在使用VPN情况下会 Reconnecting 直到5次然后降级为 HTTP 方式
# mac: ~/.codex/.env
http_proxy=http://127.0.0.1:7897   # 使用自己VPN软件的端口
https_proxy=http://127.0.0.1:7897  # 使用自己VPN软件的端口
all_proxy=socks5://127.0.0.1:7897  # 使用自己VPN软件的端口
no_proxy=localhost,127.0.0.1,::1

# claude andrej-karpathy-skills
claude plugin install andrej-karpathy-skills@karpathy-skills -s user
```

## 全局

```bash
# 元能力
## skill creator, mcp-builder
npx skills@latest add https://github.com/anthropics/skills --skill "skill-creator" --skill "mcp-builder" --agent "claude-code" --agent "codex" --agent "opencode" -g -y
## Git 相关
npx skills@latest add https://github.com/github/awesome-copilot --skill "git-commit" --agent "claude-code" --agent "codex" --agent "opencode" -g -y
```

## 项目

### workflow

```bash
## -[ ] obra/superpowers
## -[x] mattpocock/skills
## -[ ] github/spec-kit
## -[ ] Fission-AI/OpenSpec
## -[ ] mindfold-ai/trellis
## -[ ] 公司自定义
npx skills@latest add https://github.com/mattpocock/skills \
    $(: 被依赖的 Skill ) \
    --skill "grilling" $(: 研讨原语 ) \
    --skill "domain-modeling" $(: 领域建模原语, 关联 CONTEXT.md 和 ADR 目录 ) \
    --skill "codebase-design" $(: 接口设计 ) \
    $(: grill ) \
    --skill "grill-me" --skill "handoff" --skill "to-questionnaire" $(: 用户调用 ) \
    --skill "prototype"                                             $(: UI原型原语 ) \
    $(: workflow ) \
    --skill "grill-with-docs" $(: specify and clarify ) \
    --skill "to-spec"         $(: like plan and task ) \
    --skill "tdd"                            $(: implement ) \
    --skill "code-review"                    $(: implement ) \
    --skill "improve-codebase-architecture"  $(: implement ) \
    --skill "implement"                      $(: implement ) \
    $(: misc ) \
    --skill "resolving-merge-conflicts" \
    $(: 指定智能体 ) \
    --agent "claude-code" --agent "codex" --agent "opencode" -y
```

### 前端项目

- 设计：
```bash
npx skills@latest add https://github.com/leonxlnx/taste-skill --skill "design-taste-frontend" --agent "claude-code" --agent "codex" --agent "opencode" -y
npx skills@latest add https://github.com/anthropics/skills --skill "frontend-design" --agent "claude-code" --agent "codex" --agent "opencode" -y
```

- 实现（vue）：
```bash
npx skills@latest add https://github.com/vuejs-ai/skills --agent "claude-code" --agent "codex" --agent "opencode" -y
```

### 图表生成

- draw.io：依赖 `drawio` 和 `graphviz`
```bash
npx skills@latest add https://github.com/Agents365-ai/drawio-skill --agent "claude-code" --agent "codex" --agent "opencode" -y
```
- excalidraw：TODO
```

```

- 技术相关（架构图、调用图、时序图）：
```bash
npx skills@latest add https://github.com/yizhiyanhua-ai/fireworks-tech-graph --agent "claude-code" --agent "codex" --agent "opencode" -y
```

## 存疑

对于网页内容读取，几乎每家Agent都内置了相关功能，并且比较强大，此时是否还需要专门的工具存疑了，这里只做记录，尽量不使用。

### Github Client

用于一个比较常见的场景，针对一个Github开源项目分析。

对于一个 Github 探索, 目前有若干方案, 直接使用 Github MCP Server, 据说是需要消耗较多的 Token, 或者直接使用 Github CLI -- `gh`, 但是因为 gh 原本是给人类可读的, 开源社区有对其的 AI 友好封装 -- `gh-axi`。

```bash
npx skills@latest add https://github.com/kunchenguid/gh-axi --agent "claude-code" --agent "codex" --agent "opencode"
```

### Web Client

```bash
npx skills@latest add jackwener/opencli --agent "claude-code" --agent "codex" --agent "opencode"
```
