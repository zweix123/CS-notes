> 文章定位：是setup不是awesome

配置内容分类
+ 维度1——是否开源：开源 or 公司私有，这里只讨论开源的
+ 维度2——是否智能体通用：智能体通用 or 某智能体独享，一般来说都是通用的，目前Claude生态比较好，我也只用Claude，这里都是for Claude配置的
+ 维度3——种类：独立软件、skill、mcp、plugin：这里都会涉及
+ 维度4——能力：通用能力（办公通用能力、编程通用能力）、垂类领域能力

## 必要工具

+ Model Provider 管理：[farion1231/cc-switch](https://github.com/farion1231/cc-switch) 50k+star，事实标准，支持常用Agent。
+ Skills 管理：[vercel-labs/skills](https://github.com/vercel-labs/skills) 16k+star，事实标准，支持常用Agent。
+ 语音输入：
    + 收费：typeless
    + 开源：[input0](https://github.com/10xChengTu/input0)
+ 其他：
    + 在命令输出到达LLM上下文之前对其进行过滤和压缩以节省Token：[rtk-ai/rtk](https://github.com/rtk-ai/rtk)
    + claude 记忆：[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

## 编程通用
> 全局配置

skill
```bash
# 元能力
## skill creator
npx skills add https://github.com/anthropics/skills --skill "skill-creator" --agent "claude-code" --agent "codex" -g -y
# npx skills remove --agent "claude-code" --agent "codex" --global "skill-creator" -y

# workflow
# 比如 obra/superpowers, Fission-AI/OpenSpec, 或者公司特化的

# 基本开发能力
## git
npx skills add https://github.com/github/awesome-copilot --skill "git-commit" --agent "claude-code" --agent "codex" -g -y
# npx skills remove --agent "claude-code" --agent "codex" --global "git-commit" -y
```

plugin
```bash
# multica-ai/andrej-karpathy-skills
claude plugin marketplace add forrestchang/andrej-karpathy-skills
claude plugin install andrej-karpathy-skills@karpathy-skills -s user

# jarrodwatts/claude-hud
claude plugin marketplace add jarrodwatts/claude-hud
claude plugin install claude-hud -s user
# 需要额外命令启动, 详情见项目文档
```

## 编程增强
> 建议只配置到对应的项目中（而非全局）

```bash
# lackeyjb/playwright-skill
claude plugin marketplace add lackeyjb/playwright-skill
claude plugin install playwright-skill@playwright-skill -s project
# 其余操作见项目说明

# jackwener/opencli
# install opencli and chrome extension extension
mkdir -p ~/opencli-workspace
cd ~/opencli-workspace
npx skills add jackwener/opencli --agent "claude-code" --agent "codex" -y

# Lum1104/Understand-Anything
claude plugin marketplace add Lum1104/Understand-Anything
claude plugin install understand-anything -s project
```

## 综合办公

+ 图片生成：[baoyu-skill](https://github.com/JimLiu/baoyu-skills/blob/main/README.zh.md)
