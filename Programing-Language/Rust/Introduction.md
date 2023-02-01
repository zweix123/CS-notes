# 概述

+ Rust源代码文件后缀名为`.rs`

+ 编辑器：VScode有较为完善的插件

调试：`dbg`宏：接受一个表达式的所有权，打印出代码中调用`dbg!`宏时所在的文件和行号以及该表达式的结果值并返回该值的所有权

## 安装

### Windows

0. > Rust的运行需要Visual Studio的相关组件

   + C++ build tool
   + Windows 10 SDK
   + 英文组件

   其中前两个在“C++桌面应用开发”中

   下载Visual Studio Installor下载相关组件即可

1. Rust官网下载对应CPU的下载可执行文件

2. 运行可执行文件，键入1（正确完成步骤0的话），等待下载（一会），回车退出

## 相关组件

### rustc

编译工具，生成可执行文件

+ 用法：`rustc filename`

### rustfmt

代码格式化工具

+ 用法：`rustfmt filename`

### cargo

1. 创建项目：`cargo new project_name`

   + git相关文件：`.git`和`.gitignore`
   + src文件夹：放置源文件代码
   + 

2. 构建项目：进入项目文件夹，`cargo build`

   + `cargo check`：创建源代码是否可编译而不实际编译它

3. 运行项目：项目文件夹下，`cargo run`：编译加运行

   会检测项目源代码是否变化，如果变化则自动编译，否则直接运行

+ 发布：`cargo build --release`
+ 查看依赖文档：`cargo doc --open`

+ 从`Crates.io`安装二进制文件：`cargo install 库`

  > 安装在`$HOME/.cargo/bin`中



+ 自定义扩展命令

#### 项目配置

+ `[profile.dev]`（`cargo build`的配置）和`[profile.release]`（`cargo build --release`的配置）
  + `opt-level = 0`：配置值从0到3，越高优化级别越高、越需要更多的时间编译，默认0	



#### 工作空间

