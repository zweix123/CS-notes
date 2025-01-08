+ 链接：前端相关的链接太多啦
    + CSS样式照猫画虎
        + [CSS-Tricks](https://css-tricks.com/)
        + [bootstrap](https://getbootstrap.com/)：我到底也不知道这个是干啥的
        + 可拖拽的对象：[Draggable objects](https://www.redblobgames.com/making-of/draggable/)
    + 选一个好看的图标/图片吧
        + [icon](https://fontawesome.com/icons)
    + 语言：
        + Js：
            + [Eloquent JavaScript](https://eloquentjavascript.net/)

+ 组件术语
    + Navbar：导航栏
    + Sidebar：侧边栏

## 技术栈
以下技术栈是正交的，比如你可以使用别的包管理器，使用别的脚手架，使用别的前端框架（vue），可以使用JavaScript开发

### VSCode
VSCode原生支持前端的技术栈，包括lsp、format、lint

### 包管理器-node

### 脚手架-vite

创建（注意是在当前目录下创建一个子目录，这个子目录就是创建的项目的根目录）
```bash
npm create vite@latest # 命令行交互创建目录和项目
```
上面的命令是在当前路径下再创建一个子目录，然后生成的文件都在这个子目录中，但是假如已经初始化好git项目，希望将生成都在当前路径呢？

进入项目根目录

下载/更新依赖库
```bash
npm install
```

执行
```
npm run dev
```

打包
```bash
npm run build
```

#### 插件

+ [vite-plugin-singlefile](https://www.npmjs.com/package/vite-plugin-singlefile)：将产物放在一个HTML（CSS和JS都塞进去，其他静态文件通过相对路径访问）

### 前端框架-React

### 语言-TypeScript

+ Quick Start：
    + [TypeScript for Beginner Programmers](https://ts.chibicode.com/)
