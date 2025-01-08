+ HTML引入Js代码
	```html
	<script type="module">
		// Js code
	</script>
	```

	或者
	```html
	<script type="module" src="/static/js/index.js"></script>
	```

+ 模块
	+ 暴露
		```js
		export { 名称1, 名称2, ... };
		```

	+ 引入：
		```js
		import { 导入的名称1, 导入的名称2, ... } for "代码路径(文件路径或者URL)";
		```

+ 行末分号可有可无。

## 变量

+ 语法同习惯
+ 关键字：
	+ 变量
		+ `let`：定义块作用域
		+ `var`：即可以块作用域，有可以全局作用域
			+ 变量提升（Hoisting）问题：名称在`var`声明前可以使用，但是值是`undefined`的
	+ 常量
		+ `const`
	+ `delete`，用Python

## 类型
+ `typeof 变量` 查看变量类型，返回的类型是`string`

+ 关于判断：
	+ `==`和`!=`只按数据判断
	+ `===`和`!==`即判断数据、又判断类型

+ 关于字符串
	+ 字符串声明同Python
	+ 字符串填入数值：
		```js
		let t = `xxx ${arg} yyy`
		```

+ 特殊的类型：
	```js
	nill
	undefined
	```

## 流程控制

+ 分支同C++

+ 循环同Python

## 对象

和Python一样，万物皆对象（甚至更自由？）

和Python不一样，对象是map。

```js
let person = {
	name: "zweix",
	"age": 20,
	money: 0,
	friends: ['Bob', "Alice", "Lucy"],
	add_money: function(x) {
		this.money += x;
	}
}
```
+ 属性名可以使用字符串，比如上面的age

+ 访问：
	+ 点运算符
	+ 中括号运算符

## 函数

关键字`function`

```js
let main = function() {
	// 这是主函数
}
```

### 数组

同Python

+ 没有下标限制，认为是map的特殊形式？
+ 成员 
