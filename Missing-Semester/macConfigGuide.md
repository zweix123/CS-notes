## 基本配置

+ [键盘基本配置](./keyboard.md#配置)
    + [键盘改键](./keyboard.md#改键)
+ 鼠标：下载Mos，使用默认配置
+ 其他：
    + 外观：深色
    + 桌面：颜色黑色

## 基本战力形成
### 下载浏览器Chrome并登陆谷歌账号
[浏览器Chrome配置](./WindowsConfigGuide.md#1浏览器chrome)
### 科学上网ClashX
>相当于Clash for Mac

+ 提示：记得备份软件和配置文件，配置不能通过URL直接导入，Windows中的配置文件后缀名是`yml`，macOS中是`yaml`，文件拷贝进来直接改名即可。
+ 配置：
    + 打开开启自启动
    + 使用`F2`作为开关快捷键

### 包管理器brew

1. 首先下载XCode：
    ```bash
    xcode-select --install
    ```

2. 按照[Manual](https://brew.sh/zh-cn/)执行下载命令

### 安装Git->SSH生成密钥->配置Github

1. Git安装: `brew install git`
2. Git配置: [笔记](./Git.md#config)
3. SSH生成密钥: [笔记](./SSH.md#tldr)
4. 将SSH公钥上传到Github上: [笔记](./Git.md#config-1)
5. 克隆CS-notes
### 下载Obsidian
+ 安装：直接安装
+ 其他：[笔记](./Markdown.md)
 
## 其他必装软件

### 命令行配置
[笔记](./TerminalConfigGuide.md#unix-linux-and-macos)
### 编辑器VSCode

+ 安装：直接安装
+ 配置：配置通过Github账号同步，配置一次后只需要登陆账号即可
  + 全面配置[笔记](./VSCode.md)

### 图片悬停

+ 配置：
    + 开机自启动
    + 其他使用默认
        + 快捷键
            + 截屏：F1
            + 贴图：F3（粘贴板中的文字，也能生成图片并悬停）
