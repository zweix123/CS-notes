# 终端复用器tmux

+ 功能：
  1. 分屏
  2. 允许断开ssh连接后，继续运行进程
     > `top`：查看进程（任务管理器）

     服务器中的进程如果断开连接则停止

+ 结构：树形：一个tmux可包含多个session，每个session可包含多个window，每个window可包含多个pane，其中pane是最小单位，每个pane都会打开一个shell对话框
	>通常开一个session只放一个windows，然后这个windows中开多个pane

1. `tmux`：新建一个session，包含一个window，window中包含一个pane，pane里打开了一个shell对话框
2. `按下Ctrl + a后手指松开，然后按%`：将当前pane左右平分成两个pane  
	`按下Ctrl + a后手指松开，然后按"`：将当前pane左右平分成两个pane
3. `鼠标点击`选择pane  
	`按下Ctrl + a后手指松开，使用方向键`选择pane  
	按住`Alt`键然后使用方向键选择pane
4. 鼠标拖动pane之间的分割线，可以调整分割线的位置  
	`按下Ctrl + a的同时使用方向键`调整分割线。
5. `按下Ctrl + a后手指松开，然后按z`：将当前pane全屏/取消全屏
6. `Ctrl + d`：关闭当前pane，如果当前window的所有pane均已关闭，则自动关闭window，如果当前session的所有window均已关闭，则自动关闭session
7. `按下Ctrl + a后手指松开，然后按d`：挂起当前session
	`tmux a`/`tmux attch`：返回挂起的session

+ `按下Ctrl + a后手指松开，然后按s`：选择其他session
	+ 方向键——上，选择上一项 session/window/pane
	+ 方向键——下，选择下一项 session/window/pane
	+ 方向键——右，展开当前项 session/window
	+ 方向键——做，闭合当前项 session/window
+ `按下Ctrl + a后手指松开，然后按c`：在当前session中创建一个新的window
+ `按下Ctrl + a后手指松开，然后按w`：选择其他window
	+ 方向键——上，选择上一项 session/window/pane
	+ 方向键——下，选择下一项 session/window/pane
	+ 方向键——右，展开当前项 session/window
	+ 方向键——做，闭合当前项 session/window

8. 复制粘贴：
	+ tmux内复制粘贴：
		+ `Ctrl + a`后松开手指，然后按`[`进入复制模式，之后鼠标选中的文本进入**tmux**的粘贴板。
		+ `Ctrl + a`后松开手指，然后按`]`，将tmux粘贴板中的文本粘贴出来
	+ tmux和其他软件复制粘贴：
		+ 选中：按`shift`键同时鼠标选中
		+ 之后复制粘贴同Shell
	+ `Shift` + `双击单词`：可以复制单词

+ tmux外关闭窗口：`tmux kill-session -t 0`（`tmux ls`）查看