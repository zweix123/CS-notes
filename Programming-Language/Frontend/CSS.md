层叠样式表

+ 注释：`/* commit */`
+ 末尾使用`;`

+ 单位：
	+ `px`：设备上的像素点
	+ `%`：相对于父元素的百分比
	+ `em`：相对于当前元素的字体大小
	+ `rem`：相对于根元素的字体大小
	+ `vw`：相对于视窗宽度的百分比
	+ `vh`：相对于视窗高度的百分比

+ 定义：
	+ 行内样式表：作为HTML中Tag的属性`style`
	+ 内部样式表：
		```html
		<style type="text/css">
		
		</style> 
		```
	+ 外部样式表：
		```html
		<link rel="stylesheet" href="..." type="text/css">
		```

## 选择器

+ 样式渲染优先级
	+ 权重大小，越具体的选择器权重越大：`!important` > 行内样式 > ID选择器 > 类与伪类选择器 > 标签选择器 > 通用选择器
	+ 权重相同时，后面的样式会覆盖前面的样式
	+ 继承自父元素的权重最低

+ 标签选择器：标签 大括号
+ ID选择器：`#`ID 大括号
+ 类选择器（类指的是标签属性`class`）：`.`类名 大括号
	+ 可以有多个类名，在双引号中用空格隔开

+ 伪类选择器：用于定义元素的特殊状态
	+ 链接：
		+ `:link`：链接访问前的样式
		+ `:visited`：链接访问后的样式
		+ `:hover`：鼠标悬停时的样式
			```css
			.类名:hover {
				transform: scale(1, 1);
				transition: 200ms;
			}
			```
		+ `:active`：鼠标点击后长按时的样式
		+ `:focus`：聚焦后的样式

	+ 位置：
		+ `:nth-child(n)`：选择是其父标签第n个子元素的所有元素。
	+ 目标：
		+ `:target`：当url指向该元素时生效。

+ 复合选择器：
	+ 逗号`,`分割：同时选择
	+ 点`.`连接：
	+ 加号`+`连接：表示选择紧跟前一个元素的元素
	+ 空格` `分割：前一个元素下的所有后一个元素
	+ 大于号`>`分割：选择父标签是第一个元素的所有第二个元素

+ 通配符选择器：
	+ `*`
	+ `[attribute]`选择有某个属性的所有标签
	+ `attribute=value`选择属性为某值的所有标签

+ 伪元素选择器：将特定内容当做一个元素，选择这些元素的选择器被称为伪元素选择器。
	+ `::first-letter`：选择第一个字母
	+ `::first-line`：选择第一行
	+ `::selection`：选择已被选中的内容
	+ `::after`：可以在元素后插入内容
		```css
		ele::after {
			content: "插入内容"
		}
		```
	+ `::before`：可以在元素前插入内容

## 颜色
>颜色的RGB表示法，颜色可以用红绿蓝这三原色表示，我们让每个为0~255的值表示

+ 表示方法：
	+ 名字
	+ RGB的十六进制表示（六位）
		>0~255是2的8次幂，则一个三原色可以用两个十六进制表示

	+ `rgb(x, y, z)`
		+ 还能再添加一位表示透明度

## 字体

+ `font-size`大小
+ `font-style`斜体
+ `font-weight`粗细
+ `font-family`字体

## 文本
+ `text-align`：对齐：center left right
+ `line-height`：行高
+ `letter-spacing`：间距
+ `text-indent`：缩进
+ [`text-decoration`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/text-decoration)：装饰
+ `text-shadow`：阴影

## 背景

`background`

## 边框

`border`
