# 概述

+ 词法分析的工具是：Unix的lex和Linux的flex，后者来自前者

  语法分析的工具是：Unix的yacc和Linux的bison，后者来自前者

# flex

+ flex：语法上是C的扩展，定义新的语法为实现正则表达式的匹配提供框架

  + 编译过程：

    ```mermaid
    graph LR;
    	flex[".flex<br>.l"] --flex--> c[lex.yy.c] --gcc--> exe[.exe]
    ```

+ 框架基本结构：由`%%`分隔成三个部分

  ```c
  /*This is commits*/
  /*declarations and definitions*/
  %option
  %state state_name
  
  %{ /*C语言的预处理指令和定义和定义*/
  
  }%
  
  /*模式预定义*/
  
  %%
  
  /*rules : pattern模式 action*/
  
  %%
  
  /*C code*/
  
  int main() {
  	yylex(); /*flex扫描器，使用匹配模式进行匹配，返回int*/
  }
  ```

  + `%option`
    + 历史原因flex在读取到EOF时需要调用`yywrap()`（`int yywrap() { return -1; }`），现使用`%option noyywrap`关闭
  + 模式预定义：`模式名称 内容`：可使用，可嵌套使用
  + rules：`pattern action`
    + pattern如果是正则表达式就直接用，如果使用模式预定义需要`{}`括起来
    + action也可用`{}`括起来，使用C语言
  + C code：函数的实现和主函数

+ flex的匹配：

  1. rules中匹配规则**优先级**递减

     同时flex匹配**最长**字符

  2. flex对没有匹配的字符，自动做原样输出操作，故在无需匹配的pattern设置无操作处理

     ```c
     /*在转换规则的最后放置*/
     \n  /*匹配\n*/
     .   /*除了\n之外的字符*/
     ```

+ flex预定义的宏、函数、变量：

  |           |                                                              |
  | --------- | ------------------------------------------------------------ |
  | `yylex()` | Scanner入口，返回记号流（int）                               |
  | `yytext`  | 匹配到的输入文本                                             |
  | `yyin`    | flex默认从标准输入读取，文件句柄为yyin<br>可通过`yyrestart()`修改 |
  | `ECHO`    | `#define ECHO fwrite(yytext, yylen, 1, yyout)`               |

  + yyin修改（多文件）：

    ```
    if (argc < 2) {
    	//stdin;
    	return 0; 	
    }
    for (int i = 1; i < argc; ++ i) {
    	FILE *f = fopen(argv[i], "r");
    	if (! f) {
    		peeror(argv[i]);
    		return -1;
    	}
    	yytestart(f);
    	yylex(); //
    	fclose(f);
    }
    ```

## 正则表达式

flex对正则表达式部分支持（普通而古老的部分）

| 正规表达式                      | 匹配                                           |
| ------------------------------- | ---------------------------------------------- |
| `c`                             | 匹配字符`x`                                    |
| `.`                             | 匹配除换行外的任意字符                         |
| `[abc]`                         | 匹配字符`a`或`b`或`c`                          |
| `[a-z]`                         | 匹配从`a`到`z`的字符                           |
| `[^a-z]`                        | 匹配除了从a到z的字符                           |
| `[abc-zAB]`                     | 匹配a、b、c到z、A或B<br>即上述规则可并列       |
| `c*`                            | 0个或多个c                                     |
| `c+`                            | 1个或多个c                                     |
| `c{1, 2}`<br>`c{1, }`<br>`c{1}` | 匹配1到2个c<br>匹配1个及以上c<br>匹配1个c      |
| `ab`<br>`a|b`<br>`a/b`          | 匹配ab<br>匹配a或b<br>匹配b前面的a             |
| `^a`<br>`a$`                    | 匹配行首a<br>匹配行尾a                         |
| `<start condition>c`            | 匹配满足condition的c<br>condition统配设置为`*` |

+ 正则表达式(Regular Expression)文本模式：普通模式和特殊字符（元字符）

  + 修饰符：`/正则表达式内容/flag`：其中flag做修饰符

    | 修饰符 | 功能                     |
    | ------ | ------------------------ |
    | `i`    | 不区分大小写             |
    | `g`    | 全局匹配                 |
    | `m`    | 使用`^`和`$`时用多行匹配 |
    | `s`    |                          |

  + 贪婪：`+`和`*`是贪婪的：尽可能多匹配文字——末尾加上`?`实现非贪婪/最小匹配

    + ege：`<h1>oabaoaba<h1>`
      1. `/<.*>/`匹配整个
      2. `/<.*?>`匹配`<h1>`

## lab1

+ TINY语言：词法结构：

  1. 保留字：8个：

     ```
     if then else end repeat until read write
     ```

  2. 特殊符号：4种基本整数运算符、2种比较（等号和小于）、括号、分号和赋值

     ```
     + - * /  = < ( ) ; :=
     ```

  3. 其他记号：

     1. 数：一个或更多的数字
     2. 标识符：一个或更多字母

  4. 注释：`{}`中

  5. 空白：空格、制表符和换行

  + 样本程序：

    ```
    { Samplie program
      in TINY language -
      computes factorial
    }
    read x; { input an integer }
    if 0 < x then { don't compute if x <= 0 }
    	fact := 1;
    	repeat
    		fact := fact * x;
    		x := x + 1;
    	until x = 0;
    	write fact { output factorail of x }
    end
    ```

# bison

+ 编译过程：

  ```mermaid
  graph LR;
  	.y --bison--> 1[y.tab.c] --gcc--> .exe
  	.l --flex --> 2[.c] --gcc--> .exe
  ```

  + 具体cmd命令：

    ```cmake
    bison --yacc -dv test.y
    flex test.l
    gcc -o test y.tab.c lex.yy.c //这里的test是指定生成的可执行文件的名字
    ```

+ bison框架基本结构：

  ```c
  %{
  #include <stdio.h>
  #include <string.h>
  int yylex(void);  //必须
  void yyerror(char *);  //必须
  %}
  
  %token NUM /*可作为表达式参数的“标记”*/
  /*是flex和bison交流的媒介之一，flex匹配的结果可以向bison返回对应token*/
  
  %%
  表达式 : 表达式 | 其他表达式 | 或者终结符 ;
  表达式 : 表达式 { 匹配到干什么的C语言 };
  表达式L: 表达式R { $$表示表达式L的引用, $1表示表达式R的第一个参数的索引, $2};
  表达式 : 表达式 { return ;  /*跳出此次匹配*/ }
  %%
      
  void yyerror(char *str) {  //bison运行错误时调用
      fprintf(stderr,"error:%s\n",str);
  }
  
  int yywrap() { return 1; }
  int main() {
      yyparse();  //调用bison的入口
  }
  ```

  + 对应这flex也需要修改

    ```c
    %{
    #include <stdio.h>
    #include "y.tab.h"  //this  //必须， 它是bison生成的文件
    void yyerror(char *);  //and this
    %}
    NUM [1-9]+[0-9]*|0
    %%
    
    {NUM} 	return NUM  //在.y文件中定义
    ...
    ```

## 传递更丰富的值

+ bison中：

  ```c
  %union {
      类型1 类型1名;
      类型2 类型2名;
      ...
  }
  %token <类型1名> 标记名1 标记名2
  %token <类型2名> 标记名3
  ...    
  ```

+ flex中：

  ```c
  /*
  yylval为两者传递中的值，bison中的unsion使之成为结构体
  yytext为flex匹配到的文本
  yylval.想要的类型名 = 函数(yytext)即实现内容的传递
  函数有 strup将yytext转换成bison中的字符串
        atoi将yytext转换成int
        atof将yytext转换成double
  在bison中使用$+数字自动使用token确定的类型
  */
  ```

## 建立语法树

bison运行的过程天然就是建树，利用`$`可以访问匹配的表达式本身的引用，递归进行

## lab2

------

1. 题目：$lexp     &\rightarrow atom \ | \ list \hfill \\
   atom     &\rightarrow \textbf{number} \ | \ \textbf{identifier} \hfill \\
   list     &\rightarrow \textbf{(} \ \text{lexp-seq} \  \textbf{)} \ \hfill \\
   \text{lexp-seq} &\rightarrow  \text{lexp-seq} \ \ lexp \ | \ lexp \hfill \\$

   ```
   lexp -> atom | list
   atom -> number | identifier  #number和identifier是终端
   list -> ( lexp-seq )
   lexp-seq -> lexp-seg lexp | lexp
   ```

   消除左递归：$lexp     &\rightarrow atom \ | \ list \hfill \\
   atom     &\rightarrow \textbf{number} \ | \ \textbf{identifier} \hfill \\
   list     &\rightarrow \textbf{(} \ \text{lexp-seq} \  \textbf{)} \ \hfill \\
   \text{lexp-seq} &\rightarrow  lexp \ T           \hfill \\ 
   T &\rightarrow    lexp \ T \ | \ \epsilon   \hfill$

   ```
   lexp -> aton | list
   atom -> number | identifier
   list -> ( lexp-seq )
   lexp-seq -> lexp T
   T -> lexp T | epsilon  #epsislon是小e
   ```

   

2. 题目：$E &\rightarrow E + T \ | \ T \hfill \\
   T &\rightarrow T \times F \ | \ F \hfill \\
   F &\rightarrow ( \ E \ ) \ | \ id \hfill \\$

   消除左递归：$E &\rightarrow T \ E \hfill \\
   E' &\rightarrow + T \ E' \ | \ \epsilon \hfill \\
   T &\rightarrow F \ T{'} \hfill \\
   T{'} &\rightarrow \times \ F \ T{'} \ | \ \epsilon \hfill \\
   F &\rightarrow ( \ E \ ) \ | \ id \hfill \\$

-----
