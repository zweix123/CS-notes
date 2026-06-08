维度1：通用，公司专用
维度2：Agent通用，某Agent专用
维度3：skill，mcp，plugin
维度4：能力分类

## 编程相关skill（通过&Agent通用）

```bash
# 1. workflow
# 比如 obra/superpowers, Fission-AI/OpenSpec, 或者公司特化的

# git 相关
npx skills add https://github.com/github/awesome-copilot --skill "git-commit" --agent '*' -g -y 
npx skills add https://github.com/github/awesome-copilot --skill "git-commit" -g -y 
```