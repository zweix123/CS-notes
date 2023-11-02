```html
<!DOCTYPE html><!--必须有-->
<html>

<head>
    <title>标签的内容/搜索引擎收录的标题</title>
    <meta charset="UTF-8"><!--字符集-->
    <meta name="description" content="搜索引擎收录的描述">
    <meta name="keywords" content="搜索, 收录, 搜索的, 关键字">
    <link rel="icon" href="logo.url">
</head>

<body>

</body>

</html>
```
+ 关于路径，最好从项目根目录开始，以`/`开头
+ DOM

## Tag

+ 特殊字符：
	+ 左右小括号`&lt;`和`&gt;`
	+ 空格`&nbsp;`
	+ 引号`"`：`&quot;`
	+ `&`：`&amp;`

+ `div`：块状元素，默认带`Enter`
	+ 标题：`h1`、`h2`、`···`、`h6`
	+ 段落：`p`
	+ 等宽字体段落（保留空格）->代码：`pre`
	+ 有序列表：`ul`
	+ 无效列表：`ol`
	+ 表格：`table`
		+ 单元格：`td`（这个属于span）

+ `span`：行内元素，默认不带`Enter`
	>回车：`<br>`

	+ 斜体：`i`
	+ 加粗：`b`/`strong`
	+ 删除线：`del`
	+ 下划线`ins`
	+ 超链接`a`
		+ 绝对地址（包括协议）
### 媒体
+ 图片`img`
	+ `src`：文件链接
	+ `alt`：文本描述
	+ `width`/`height`：数字，单位像素`px`
+ 音频`audio`
	如果第一个失效则使用第二个
	```html
	<audio controls>
		<source src="/audios/sound1" type="audio/mpeg"/>
		<source src="/audios/sound2" type="audio/mpeg"/>
	</audio>
	```
+ 视频`video`
	+ `type="video/mp4"`

这里的`controls`属性也表示是否提供相关媒体标签的控制组件

### 表单

+ 表单`form`
	+ 属性`action`指表单提交的URL/路径/函数/方法
+ `label`：使用属性for按id绑定input
+ 单行文本框`input`
	+ `type`：
		+ `text`
		+ `number`
		+ `email`
		+ `password`
		+ `radio`：即为选项，通过name分类，value则为其对应的值
		+ `file`
	+ `name`：参数名称（用于发get）
	+ `id`：
	+ `maxlength`/`minlength`
	+ `required`：是否必填
	+ `placeholder`：当表单控件为空时，控件中显示的内容

`<button type="submit">submit</button>`以GET形式提交表单信息

+ 多行文本框`testarea`
	+ `rows`初始行数
	+ `cols`初始列数

+ 选项：
	```html
	<select>
		<option value=""></option>
		<option selected value=""></option><!--默认-->
	</select>
	```

### 表格

### 折叠

```html
<details>
<summary><b>head</b></summary>
body
</details>
```

### 语义标签
<img alt="img_sem_elements.gif" src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/resource/Fronted/语义标签.gif" style="cursor: pointer;">
