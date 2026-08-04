> 文章定位：是setup不是awesome

配置内容分类
+ 维度1——是否开源：开源 or 公司私有，这里只讨论开源的
+ 维度2——是否智能体通用：智能体通用 or 某智能体独享，一般来说都是通用的，这里对于不通用的会单独说明；这里`npx skill add`命令是针对Claude Code、CodeX和OpenCode均安装的。
+ 维度3——种类：独立软件、skill、mcp、plugin：这里都会涉及
+ 维度4——能力：通用能力（办公通用能力、编程通用能力）、垂类领域能力

+ 必要工具：
    + Model Provider 管理：[farion1231/cc-switch](https://github.com/farion1231/cc-switch) 50k+star，事实标准，支持常用Agent。
    + Skills 管理：[vercel-labs/skills](https://github.com/vercel-labs/skills) 16k+star，事实标准，支持常用Agent。
    + 语音输入：目前CodeX本身支持，所以我没有做详细调研，有看到收费的typeless和开源的input0
    + Token 节省： [rtk-ai/rtk](https://github.com/rtk-ai/rtk) && [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)
    + 记忆：目前各大Agent基本都内置记忆了，领域信息基本通过知识库提供而非记忆，个人习惯一般定义全局提示词。
    + CLI：
        + App to cli：HKUDS/CLI-Anything
        + Web to cli：`jackwener/opencli`
        + Github to cli：TODO


基本配置
```
# .codex/.env
http_proxy=http://127.0.0.1:7897   # 使用自己VPN软件的端口
https_proxy=http://127.0.0.1:7897  # 使用自己VPN软件的端口
all_proxy=socks5://127.0.0.1:7897  # 使用自己VPN软件的端口

# claude andrej-karpathy-skills
claude plugin install andrej-karpathy-skills@karpathy-skills -s user
```

```bash
# 元能力
## skill creator
npx skills add https://github.com/anthropics/skills --skill "skill-creator" --skill "mcp-builder" --agent "claude-code" --agent "codex" --agent "opencode" -g -y  # 全局
## Git
npx skills add https://github.com/github/awesome-copilot --skill "git-commit" --agent "claude-code" --agent "codex" --agent "opencode" -g -y  # 全局

# Workflow
## -[ ] obra/superpowers
## -[ ] Fission-AI/OpenSpec
## -[x] mattpocock/skills && mindfold-ai/trellis
## -[ ] 公司自定义
npx skills add https://github.com/mattpocock/skills \
    --skill "grill-with-docs" $( : 研讨, 构建领域模型, 完善术语, 更新 CONTEXT.md 和 ADR ) \
    --skill "domain-modeling" $( : 领域建模, 关联 CONTEXT.md 和 ADR ) \
    --skill "codebase-design" $( : 完善术语 ) \
    --skill "to-spec" \
    --skill "to-tickets" \
    --skill "code-review" $( : 代码双轴审查 ) \
    --skill "resolving-merge-conflicts" $( : 根据意图解决冲突 ) \
    --agent "claude-code" --agent "codex" --agent "opencode" -y  # 项目

# 网页
## 设计
npx skills add https://github.com/leonxlnx/taste-skill --skill "design-taste-frontend" --agent "claude-code" --agent "codex" --agent "opencode" -y  # 项目
npx skills add https://github.com/anthropics/skills --skill "frontend-design" --agent "claude-code" --agent "codex" --agent "opencode" -y  # 项目
## 开发
npx skills add https://github.com/vuejs-ai/skills --agent "claude-code" --agent "codex" --agent "opencode" -y  # 项目
## 测试&交互
npx skills add jackwener/opencli --agent "claude-code" --agent "codex" --agent "opencode" -y  # 项目

# 项目探索, 对于一个 Github 探索, 目前有若干方案, 直接使用 Github MCP Server, 据说是需要消耗较多的 Token, 或者直接使用 Github CLI -- gh, 但是因为 gh 原本是给人类可读的, 开源社区有对其的 AI 友好封装 -- gh-axi, 目前使用这个方案
npx skills add https://github.com/kunchenguid/gh-axi --agent "claude-code" --agent "codex" --agent "opencode" -y # 项目

# 办公: 见文章开头

# 图表生成
## - drao.io
## 依赖 drawio && graphviz
npx skills add https://github.com/Agents365-ai/drawio-skill --agent "claude-code" --agent "codex" --agent "opencode" -y  # 项目
## - 直接生成图片(通常是和风格相关的)
##   - 技术图
npx skills add https://github.com/yizhiyanhua-ai/fireworks-tech-graph --agent "claude-code" --agent "codex" --agent "opencode" -y  # 项目
##   - 社交软件
```
