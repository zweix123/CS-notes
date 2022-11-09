> 语法说明：
>
> + `<>`：内嵌名称，表示对应名称，使用时**没有**`<>`
> + `()`：为SQL语言符号，                使用时**有**`()`
> + `[]`：表示可选，                           使用时**没有**`[]`
> + `|`  ：表示选择；

+ 注释：
  + 单行：`-- 注释` 有空格
  + 多行：`/*...*/`

+ 转义字符：
  + 前加`\`
  + 双写


# 概述概论

*结构化查询语言*(Structured Query Languauge, SQL)是关系数据库的标准语言

> SQL发音：字母S-Q-L或初始名称sequel；甚至有论文讨论

## 发展历程

+ 1974年，        由Boyce和Chamberlin提出，初叫Sequel，在IBM研制的数据库系统System R上实现；

+ 1986年10月，美国国家标准局(American National Standard Institute, ANSI)的数据库委员会X3H2批准了SQL作为关系数据库语言的美国标准；同年其发布了SQL标准文本；故称标准SQL语言为ANSI SQL，各大厂商的DBMS会对其进行扩展。

  1987年，        国际标准化组织(International Organization for Standardization, ISO)也通过此标准；

+ 标准文本更新情况：

  | 标准               | 大致页数 | 发布时期 |
  | ------------------ | -------- | -------- |
  | SQL/86             |          | 1986.10  |
  | SQL/89(FIPS 127-1) | 120      | 1989     |
  | SQL/92             | 622      | 1992     |
  | SQL 99 (SQL 3)     | 1700     | 1999     |
  | SQL 2003           | 3600     | 2003     |
  | SQL 2008           | 3700     | 2006     |
  | SQL 2011           |          | 2010     |
  
  > **没有**一个数据库系统能够支持SQL标准的**所有**概念和特性，大部分支持**SQL92**的大部分和99及03的一部分，许多还对基本命令集进行了不同程度的扩充和修改，添加新功能。

## 语言特点

1. 综合统一：集数据查询(data query)、数据操作(data manipulation)、数据定义(data definition)和数据控制(data control) 功能于一

   + 也把数据查询放在数据操作的范畴下
   + 数据操作和数据控制的区分：
     + 数据操作：对数据的操作（增改删查）
     + 数据控制：控制谁可以操作数据（授权）

   > 其他类型数据语言分为：
   >
   > + 模式数据定义语言(Schema Data Definition Language, 模式DDL)：用于定义模式
   > + 外模式数据定义语言(Subschema Data Definition Language, 外模式DDL或子模式DDL)：用于定义外模式
   > + 数据存储有关的描述语言(Data Storage Description Language, DSDL)：用于定义内模式
   > + 数据操纵语言(Data Manipulation Language, DML)：用于进行数据的存取与处置

2. 高度非过程化：无需了解存取路径，其选择和操作过程由系统自动完成

3. 面向集合的操作方法

4. 以同一语言结构提供多种使用方式

5. 语言简洁、易学易用

   | SQL核心功能                           | 动词                                  | 小写                     |
   | ------------------------------------- | ------------------------------------- | ------------------------ |
   | 数据定义                          DDL | `CREATE, DROP. ALTER`                 | `create, drop, alter`    |
   | 数据查询（包含于操纵）                | `SELECT`                              | `select`                 |
   | 数据操作/操纵（/更新）DML             | `INSERT, UPDATE, DELETE`              | `insert, update, delete` |
   | 数据控制                          DCL | `GRANT, REVOKE`<br>`COMMIT, ROLLBACK` | `grant, revoke`          |

## 基本概念

+ 数据库基础：

  + 数据库(database)：保存有组织的数据的容器

  + 数据库管理系统(**DBMS**)：顾名思义

  + 表(table)：某种特定类型数据的结构化清单：有库中唯一名字

    模式(schema)：关于数据库表的布局及特性的信息：**名称空间**

  + 列(colomn)：表中的一个字段

    数据类型(datatype)：所容许的数据的类型；每个表列都要数据类型限制存储的

  + 行(row)：表中的一个记录

  + 主键(primary key)：一或一组列，其值能唯一标识表中的每行

    ​                               ：任意两行不同，每行必须有，不能变化和重用

    > 国内称key为“键码”或“码”

+ SQL基本概念：

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Database-System/SQL对关系数据库模式的支持.png)

  外模式包括若干视图(view)和部分基本表(base table)，数据库模式包括若干基本表，内模式包括若干存储文件(stored file)

  SQL可对基本表和视图进行查询和操作，两者都是关系。一个关系就对应一个基本表，一个或多个基本表对应一个存储文件，一个表可以带若干索引，索引也在存储文件。

  视图是从一个或几个基本表导出的表，不独立存储（只放定义、不放数据），数据仍在导出视图的基本表中，所以视图是虚表。

# 数据类型

+ **空值**：NULL：不知道不存在无意义的值

  + 取空值的情况：

    1. 该属性应有值但还不知道
    2. 该属性不应该有值
    3. 由于某种原因不便填写

  + 空值的判断：`IS NULL` 和 `IS NOT NULL` 

  + 空值的约束条件：属性定义/域定义、加上`UNIQUE`限制 的 属性、码属性不能取空值。

  + 空值的算术运算、比较运算和逻辑运算

    > `UNKNOWN`：真假之外第三值 `unknown`
    >
    > 这和NULL不一样，unknown是明确的，就是不知道；而NULL则是未知的

+ 数据类型

  | 数据类型                                             | 含义                                                         |
  | ---------------------------------------------------- | ------------------------------------------------------------ |
  | ==串数据类型==                                       | 括在单引号内                                                 |
  | `CHAR(n)`<br>`CHARACTER(n)`                          | 长度为n的**定长**字符串<br>多余位置补空格<br>最大长度255     |
  | NCHAR                                                | CHAR的特殊形式，用于支持Unicode                              |
  | `VARCHAR(n),`<br>`CHARACTERVARYING(n)`<br>也称`TEXT` | 最大长度为n的**变长**字符串<br>                              |
  | NVARCHAR                                             | 同上                                                         |
  | `CLOB` `clob`                                        | 字符串大对象                                                 |
  | ==数值数据类型==                                     |                                                              |
  | `BLOB` `blob`                                        | 二进制大对象                                                 |
  | `BIT`                                                | 单个二进制位                                                 |
  | `INT, INTEGER` `integer`                             | 长整数（4字节）                                              |
  | `TINYINT`                                            | 1字节                                                        |
  | `SMALLINT` `smallint`                                | 短整数（2字节）                                              |
  | `BIGINT` `bigint`                                    | 大整数（8字节）                                              |
  | `NUMERIC(p, d)` `numeric`                            | 定点数，<br>由p位数字（不包括符号、小数点）组成，<br>小数点后面有d位数字 |
  | `DECIMAL(p, d), DEC(p, d)`<br>`decimal dec`          | 同NUMERIC                                                    |
  | `REAL` `real`                                        | 取决于机器精度的单精度浮点数                                 |
  | `DOUBLE PRECISION` `precision`                       | 取决于机器精度的双精度浮点数                                 |
  | `FLOAT(n)`                                           | 可选精度的浮点数，精度至少为n位数字                          |
  | `BOOLEAN`                                            | 逻辑布尔量                                                   |
  | ==日期和时间数据类型==                               |                                                              |
  | `DATE`                                               | 日期，包含年、月、日，<br>格式为YYYY-MM-DD                   |
  | `TIME`                                               | 时间，包含一日的时、分、秒，<br>格式为HH:MM:SS               |
  | `TIMESTAMP` `timestamp`                              | 时间戳类型                                                   |
  | `INTERVAL` `interval`                                | 时间间隔类型                                                 |
  | ==二进制数据类型==                                   |                                                              |

# 基本语法

+ 系统处理SQL语句时忽略所有空格，分多行易理解；

  ​               SQL语句以分号`;`结尾，与DBMS有关；

  ​               SQL语句不区分大小写，与DBMS有关。

+ 关键字(keyword)：作为SQL组成部分的保留字，不能用作表或列的名字。

  子句(clause)        ：SQL语句由子句构成，有些子句是必须的，而有的可选，一个子句通常由一个关键字加上所提供的数据组成。

+ 数据字典：是关系数据库管理系统内部的一组系统表，记录数据库中所有的定义信息（模式、视图、索引、完整性约束定义以及用户对操作权限、统计信息），关系数据库管理系统在执行SQL的数据定义语句时，实际上就是在更新数据字典。

## 数据定义

| 操作对象     | 定义方式        | 定义方式      | 定义方式      |
| ------------ | --------------- | ------------- | ------------- |
|              | 创建            | 删除          | 修改          |
| 模式`schema` | `CREATE SCHEMA` | `DROP SCHEMA` | 删除重建      |
| 表`table`    | `CREATE TABLE`  | `DROP TABLE`  | `ALTER TABLE` |
| 视图`view`   | `CREATE VIEW`   | `DROP VIEW`   | 删除重建      |
| 索引`index`  | `CREATE INDEX`  | `DROP INDEX`  | `ALTER INDEX` |

一个关系数据库管理系统的实例(instance)中可以建立多个数据库，一个数据库中可以建立多个模式，一个模式下通常包括的表、视图和索引等数据库对象。

### 模式

1. 定义模式：`CREATE SCHEMA <模式名> AUTHORIZATION <用户名>;` 如果没有制定模式名，那么模式名隐含用户名

   要创建模式，调用该命令的用户必须拥有数据库管理员权限，或得到数据库管理员授予的CREATE SCHEMA的权限

   实际上定义一个**命名空间**，可在该空间下继续定义该模式包含的数据库对象：基本表、视图、索引等。

   语句中可接受创建其它的子句`CREATE SCHEMA <模式名> AUTHORIZATION <用户名> [<表定义子句> | <视图定义子句> | <授权定义子句>];`

2. 删除模式：`DROP SCHEMA <模式名> <CASCADE | RESTRICT>;` `cascade restrict` 其中CASCADE和RESTRICT必选其一

   + `CASCADE`（**级联**）：在删除模式的同时把该模式中原有的数据库对象全部删除。
   + `RESTRICT`（**限制**）：如果该模式中已经定义了==的数据库对象，则拒绝该删除语句的执行。

### 基本表

+ 基本表的定义

  ```mysql
  CREATE TABLE <表名> (
      <列名><数据类型>[列级完整性约束条件]
      [, <列名><数据类型>[列级完整性约束条件]]
      ...
  	[, <表级完整性约束条件>]
  );
  -- 逗号分隔
  ```

  + 列级完整性约束条件
    + `PRIMARY KEY` `primary key`：主码
    + `UNIQUE` `unique`：取唯一值
    + `NOT NULL`：不能取空值
  + 表级完整性约束条件
    + `PRIMARY KEY (列名, 列名)` 主码是多个属性
    + `FOREIGN KEY (列名) REFERENCES 表名(列名)`   `foreign key references`：什么是外码，被参照表是，被参照列是。  //参照表和被参照表可以是同一个表。
  + 指定默认值：`DEFAULT 默认值`

+ 数据类型

  > 域，每个属性来自一个域，其取值必须是域中的值。
  >
  > 在SQL中域的概念用数据类型来实现

  不同的关系数据库管理系统中支持的数据类型不完全相同

+ 模式与表：一个基本表都属于某一个模式，一个模式包含多个基本表。

  1. 在表名中明显的给出模式名：`CREATE TABLE "模式名".表名(各列);`

  2. 在创建模式语句中同时创建表

  3. 设置所属的模式，在创建表时表名不必给出模式名；

     > 搜索路径(search path)：
     >
     > + 如果创建基本表和其他数据库对象时没有制定模式，系统确定该对象所属模式的方式
     >
     > + 包含一组模式列表，关系数据库管理系统会使用模式列表中第一个存在的模式在对数据库对象的模式名。
     >
     >   如果为空，则报错

     + 显式当前搜索路径：`SHOW search_path;`

     + 搜索路径的默认值是`$user, PUBLIC` `public`，指先搜索与用户名相同的模式名，不存在则使用PUBLIC模式

       数据库管理员也可以设置搜索路径：`SET search_path TO "模式名".PUBLIC;`，然后定义基本表如果没有设置模式名则自动建立默认模式的基本表

+ 修改基本表：

  ```mysql
  ALTER TABLE <表名>  -- 要修改的基本表
  [ADD [COLUMN] <新列名><数据类型>[完整性约束]]
  [ADD [CONSTRAINT]<表级完整性约束>]                  
  -- ADD子句用于添加新列（全为空）、新列级完整性约束条件、新表级完整性约束条件
  [DROP [COLUMN] <列名> [CASCADE|RESTRICT]]
  -- DROP COLUMN子句用于删除表中的列。指定如模式，只不过限制的是表以下的数据库对象
  [DROP CONSTRAINT<完整性约束名>[RESTRICT|CASCADE]]
  -- DROP CONSTRAINT子句用于删除指定的完整性约束条件
  [ALTER COLUMN <列名><数据类型>]
  -- ALTER COLUMUN子句用于修改原有的列定义，包括修改列名和数据类型
  ```

+ 删除基本表：`DROP TABLE <表名> [RESTRICT|CASCADE];`

  + 选择restrict：删除有限制条件：不能被其他表约束所引用（CHECK、FOREIGN KEY等），不能有视图，不能有触发器(trigger)，不能有存储过程或函数等。否则不能被删除
  + 选择cascade：删除没有限制条件，删除表的同时，相关的依赖对象，例如视图，都将被一起删除。

  默认情况是RESTRICT

   <img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Database-System/删除基本表.png" style="zoom:80%;" />

### 视图

+ 定义：有若干基本表或视图导出的虚表，只有定义，没有数据

1. 定义视图：

   1. 建立视图：

      ```mysql
      CREATE VIEW <视图名> [(<列名>[. <列名>]···)]  -- 组成视图的属性列名或全部省略或全部指定
      AS<子查询>  -- 任意的查询块
      [WITH CHECK OPTION]  -- 对视图进行UPDATE、INSET和DELETE操作时要保证更新、插入或删除的行满足视图定义中的谓词条件——子查询中的条件表达式
      ```

      > 建视图后，数据库只是将视图的定义放到数据字典，并不执行 AS后的，只有对视图查询时在执行子查询

      + 行列子集视图：一个视图是从单个基本表导出的，并且只是去掉了基本表的某些行和某些列，但保留的主码
      + 带表达式的视图：带虚拟列（因为视图并不实际存储，所以可以在视图中设置派生属性列）

      **建立的视图是与基本表关联的，如果基本表被修改，视图将无法正常工作——删除重建。**

   2. 删除视图：`DROP VIEW <视图名> [CASCADE]` `cascade` 将视图的定义从数据字典中删除；如果视图上还导出其他视图，则需要使用CASCADE级联删除语句一起删除（否则会拒绝）

      **基本表删除后，导出的视图都无法使用，但是视图的定义并没有清除，还需要显式的调用**

2. 查询视图：类似基本表

   > 1. 关系数据库系统管理系统执行前进行有效性检查（是否存在）
   > 2. 取出视图的定义

   3. *数据消解*(view resolution)把用户查询和定义内子查询结合并转换成对基本表的查询

   + 视图	：定义一直在数据字典
   + 派生表：语句执行时临时定义，用后即删

3. 更新(操纵)视图：由于视图是不实际存储数据的虚表，对视图的更新最终要转换为对基本表的更新、

   + 不可更新视图：其中的数据是由基本表中的其他列派生出的，ege：修改平均值

     > 不可更新的视图：理论证明不可更新
     >
     > 不允许更新的视图：实际系统不支持更新，本身可能是可更新的

+ 视图的作用：

  1. 简化用户操作

  2. 使用户能以多种角度看待同一数据

  3. 视图对重构数据库提供了一定程度的逻辑独立性

  4. 视图能够对机密数据提供安全保护

  5. 适当利用视图可以清晰地表达查询

     ege：极值的其他信息，建立视图筛选，自然连接原表后查询。



### 存储过程

+ 创建：
+ 执行：

### 索引

+ 索引：当表的数据量大时，查询操作会比较耗时，建立索引可以加快查询速度（提供多种存取路径），代价是占用更多的空间，同时表更新是，索引也要维护，有时间开销。

  建立与删除索引由数据库管理员或表的属主(owner)，即建立表的人，负责完成。关系数据库管理系统在执行查询时自动选择合适的索引作为存取路径，用户**不必也不能显式的选择索引**，索引是关系数据库管理系统的内部实现技术，属于内模式。

+ 分类：

  + 顺序文件上的索引：针对指定属性值升序或降序存储的关系，索引文件由属性值和相应的元组指针组成
  + B+树索引：将索引组织为B+树形式，叶节点为属性值或相应的元组指针，有动态平衡的优点
  + 散列(hash)索引：建立若干个桶，将索引属性按照其散列函数值映射到相应桶中，桶中存放索引属性值和相应的元组指针。**查找速度快**。
  + 位图索引：用位向量记录索引属性中可能出现的值，每个位向量对应一个可能值

1. 建立索引：

   ```mysql
   CREATE [UNIQUE][CLUSTER] INDEX <索引名>
   ON <表名>(<列名>[<次序>][, <列名> [<次序>]] ···);
   ```

   + UNIQUE：表名此索引的每个索引值只对应唯一的数据记录。
   + CLUSTER表示要建立的索引是*聚簇索引*
   + <表名>是要建立索引的基本表的名字，索引可以建立在该表的一列或多列上，个列之间用逗号分隔。各<列名>后可以用<次序>指定索引值的排序次序，==可选`ASC`（升序）或`DESC`（）降序，默认为`ASC`==

2. 修改索引：`ALTER INDEX <旧索引名> RENAME TO <新索引名>;`

3. 删除索引：`DROP INDEX <索引名>；`

## 数据查询

+ 基本格式：依次执行

  ```mysql
  SELECT [ALL|DISTINCT] <目标列表达式> [, <目标列表达式>] ...       -- 选什么列
  FROM<表名或视图名> [, <表名或视图名>···]|(<SELECT语句>)[AS]<别名>  -- 在哪里查
  [WHERE<条件表达式>]                                            -- 按什么条件
  [GROUP BY <列名1>                                             -- 结果按什么分组
   	[HAVING<条件表达式>]]                                      -- 以组为单位再次筛选
  [ORDER BY <列名2> [ASC|DESC]···];                             -- 结果按什么顺序输出
  ```

  + 先WHERE再GROUP：WHERE筛选过的数据可能导致GROUP缺失，HAVING的设计是为了弥补此问题。


### 基本查询

```sql
select all distinct * from;
```

```sql
SELECT [ALL|DISTINCT] <目标列表达式> [, <目标列表达式>] ...       -- 选什么列
FROM<表名或视图名> [, <表名或视图名>···]|(<SELECT语句>)[AS]<别名>  -- 在哪里查
```

+ 结果：**投影**：对目标表中所有元组**按目标列的要求**按对应**顺序、名称**形成新元组作为一个结果关系返回

+ 目标列表达式可选格式：

  1. 列名，多个则以逗号分隔；
  2. 通配符`*`：所有列；
  3. `[<表名>.]<属性列名表达式>[, [<表名>.]<属性列名表达式>]...`
     1. 属性列：选取不同表中的同名列——完全限定列名

     2. 作用域属性列的聚集函数和常量的任意算术运算组成的运算符公式：计算字段

        > 字段(field)：与列(colunm)意思基本相同；常：数据库列为列，计算字段的连接为字段

        + 字符串*拼接*(concatenate)：使用`+`或`||`；具体见DBMS的支持

          > + MYSQL不支持+，而||等效于OR，使用CONCAT()函数实现
          >
          > + 数据库填充字符串多余宽度使用空格（看DBMS的支持），使用函数去除：
          >
          >   `TRIM()、RTRIM()、LTRIM()`：分别取出两边、右边和左边

          + 列*别名*(alias)/导出列(derived column)：是一个字段或值的替换名；

            ​                                                         语法：`AS`子句，接在表达式后，后接别名

        + 算术计算：支持操作符`+、-、*、/`。

+ 可选项：去重：**默认**ALL

  + 正常取：`ALL`
  + 去重取：`DISTINCT`


### 条件查询

> 搜索条件(search criteria)/过滤条件(filter condition)

+ 查询满足条件的元组：使用`WHERE` `where` 子句，后接查询条件，该子句在`from`子句后

```sql
SELECT [ALL|DISTINCT] <目标列表达式> [, <目标列表达式>] ...       -- 选什么列
FROM<表名或视图名> [, <表名或视图名>···]|(<SELECT语句>)[AS]<别名>  -- 在哪里查
[WHERE<条件表达式>]                                            -- 按什么条件
```

| 查询条件             | 谓词                                            |
| -------------------- | ----------------------------------------------- |
|                      | `NOT`关键字：用于条件**前**，表示条件的否定     |
| 比较                 | `=, >, <, >=, <=, !=, <>, !>, !<`               |
| 范围                 | `BETWEEN AND, NOT BETWEEN AND` `-- between and` |
| 空值                 | `IS NULL, IS NOT NULL`                          |
| 集合                 | `IN, NOT IN`                                    |
| 字符匹配             | `LIKE, NOT LIKE`                                |
| 多重条件（逻辑运算） | `AND, OR, NOT`                                  |
| EXISTS               |                                                 |

+ 比较大小：`<>`和`!=`可以互换，不同DBMS可能有区别

+ 确定范围：`BETWEEN...AND...`和`NOT BETWEEN...AND...` 查找属性值在/不在范围：前下限（低值）， 后上限（高值）

+ 设计空值的查询：不能用`=`代替：NULL是一个不知道的值、无法相等 。

+ 确定集合：`WHERE 列名 IN|NOT IN(一个集合)`本质是一个`OR`子句的优化

+ 字符匹配：`[NOT] LIKE'<匹配串/搜索模式>' [ESCAPE'<换码字符>']` `escape`

  + 搜索模式(search pattern)：由字面值、通配符或两者组合构成的搜索条件

  + 通配符(wildcard)：用来匹配值的一部分的特殊字符

    1. 百分号`%`：代表任意长度（可为0）的字符串。

    2. 下划线`_`：代表任意单个字符

       > 数据库字符集：ASCLL一个汉字需要两个\_，GBK需要一个\_

    3. 方括号`[]`：指定字符集：匹配该字符集中的任意一个；看DBMS支持

       + 托字号`^`前缀字符：表否定`[^JM]%`

       ege：`'[JM]%'`以J或M开头的字符串；`[^JM]%`不以J或M开头字符串

    + 如果不含通配符可使用=（等于）运算符取代LIKE谓词，用!=或<>（不等于）运算符取代NOT LIKE谓词。
    + 如果查询字符串本身就含有通配符%或_，就使用ESCAPE'<换码字符>'*短语*对通配符进行转义，其指定换码字符，在匹配串中换码字符后接的%和\_不再具有通配符的含义。
    + 有的DBMS对字段多余的位置是填充空格，可能会影响搜索模式的匹配

    + 通配符放在最开始是最慢的

+ 多重条件查询：

  + 操作符(operator)/逻辑操作符(logical operator)：用来联结或改变WHERE子句中的子句的关键字
  + AND的优先级高于OR，但括号的优先级最高。
  
  > IN谓词就是OR运算符的缩写

### 数据排序

+ ORDER BY子句 `order`：用户可以用ORDER BY子句对查询结果按照一个或多个属性列的升序（ASC）或降序（DESC）排序，默认值为升序。（升序空值最后、降序空值最先 随系统）

```sql
order by asc desc  -- ascending, descending
```

```sql
SELECT [ALL|DISTINCT] <目标列表达式> [, <目标列表达式>] ...       -- 选什么列
FROM<表名或视图名> [, <表名或视图名>···]|(<SELECT语句>)[AS]<别名>  -- 在哪里查
[ORDER BY <列名2> [ASC|DESC]···];                             -- 结果按什么顺序输出
```

+ `ORDER BY`子句位置：保证在SELECT语句的最后；
+ 可通过非选择列进行排序
+ 多列排序：逗号分隔
  + 按列位置排序：将子句后的列名换为结果表中列的位置次序
+ 指定排序方向：关键字只指定其前面的那个列，多列要**分别**进行指定
  + ASC  ：升序，**默认**
  + DESC：降序

### 函数

+ 文本函数：

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Database-System/文本函数.png)

  + `SOUNDEX()`函数将任何文本字符串转换为描述其语音表示的字母数字模式的算法：按发音做出哈希，用于比较发音

+ 日期和时间处理函数：

+ 数值处理函数：

  ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Database-System/数值处理函数.png)

1. **聚集函数**(aggregate function)：运行在行组上（不用于具体字段），计算和返回单个值的函数

   + 用于`CELECT`子句和`GROUP BY`中的`HAVING`子句中，**不能用于WHERE子句**：

   | 语法                          | 功能                                   |
   | ----------------------------- | -------------------------------------- |
   | `COUNT(*)`                    | 统计元组个数                           |
   | `COUNT([DISTINCT|ALL]<列名>)` | 统计一列中值的个数                     |
   | `SUM([DISTINCT|ALL]<列名>)`   | 统计一列值的总和（此列必须是整数型）   |
   | `AVG([DISTINCT|ALL]<列名>)`   | 统计一列值的平均值（此列必须是整数型） |
   | `MAX([DISTINCT|ALL]<列名>)`   | 求一列值中的最大值                     |
   | `MIN([DISTINCT|ALL]<列名>)`   | 求一列值中的最小值                     |

   + 参数可以是表达式
   + + DISTINCT：去重；
     + ALL          ：        ；**默认**
   + 空值NULL：除COUNT(*)外都跳过

### 分组

```sql
group by having
```

```sql
SELECT [ALL|DISTINCT] <目标列表达式> [, <目标列表达式>] ...       -- 选什么列
FROM<表名或视图名> [, <表名或视图名>···]|(<SELECT语句>)[AS]<别名>  -- 在哪里查
[GROUP BY <列名1>                                             -- 结果按什么分组
 	[HAVING<条件表达式>]]                                      -- 以组为单位再次筛选
```

+ 位置：`WHERE`子句后

+ 功能：服务于聚集函数

+ 语法：

  + GROUP BY子句：将查询结果按某一列或多列的值分组，值相等的为一组

  ​                                     分组后聚集函数将作用于每一个组，即每一个组都有一个函数值

  + HAVING子句：对GROYP BY分组后的聚合函数的结果再次筛选

    > WHERE子句用于基本表或视图，不能使用聚集函数
    >
    > HAVING短语用于组，可以使用聚集函数

    HAVING可使用WHERE所有操作符，其设计是因分组操作是在初步过滤后，此时如果像对分组继续过滤不能使用WHERE。

### 多表查询

> 查询块：一个`SELECTR-FROM-WHERE`语句

+ 子查询(subquery)/嵌套查询(nested query)：嵌套在其他查询块中的查询块

  > 上层的查询块称为外层查询或父查询，下层查询块称为内层查询或子查询
  >
  > + 不相关子查询：子查询的查询条件不依赖于父查询——由内向外执行，可转换为连接查询
  >
  > + 相关子查询(correlateed subquery)：子查询的查询条件依赖于父查询—外层循环，每次用内
  >
  >   整个查询语句称为*相关嵌套查询*(correlated nested query)语句

1. 过滤：用于WHERE子句，执行顺序由内向外：

   1. 带有IN谓词的子查询：子查询结果为集合

   2. 带有比较运算符的子查询

      + 带有`=`号：自己返回必须小等于1

   3. 带有ANY（SOME）或ALL谓词的子查询

      ANY：子查询结果中的某个值；ALL子查询结果中的所有值

   4. 带有EXISTS谓词（存在量词）的子查询：不返回任何数据，只产生逻辑值真假true/false，可判断集合关系——元素有没有；NOT EXISTS（没有真，有假）

      > SQL没有全称量词。只能转换：全部等于不存在不

2. 计算字段：用于SELECT子句的列别名，可用父查询中的FROM的表

3. 派生表：基于派生表的查询：子查询出现在FROM子句中，子查询生成临时*派生表*(derived table)成为主查询的查询对象

   ```mysql
   SELECT Sname
   FROM Student, (SELECT Sno FROM SC WHERE Cno = '1') AS SC1
   WHERE Student.Sno = SC1.Sno;
   ```

   其中AS别名是为派生类定义别名，其中AS可省略，但是派生类必须有别名

-----

+ 连接查询：用于FROM子句，通过WHERE子句过滤

  > 完全限定名：多表的同名属性：前加表名

  + 连接查询的WHERE子句中用来连接两个表的条件称为*连接条件*或*连接谓词*。

    其格式为`[<表名1>.] <列名1> <比较运算符> [<表名2>.] <列名2>` 其中比较运算符主要有；

    此外连接谓词还可以：`[<表名1>.]<列名1> BETWEEN [<表名2>.]<列名2> AND [<表名2>.]<列名3>`；

    连接谓词中的列名称为*连接字段*，连接条件中的各连接字段类型必须是**可比**的。

1. 内部联结/等值联结：笛卡儿积

   + 可用表别名

   2. 自然联结：若在等值连接中把目标列中重复的属性列去掉则为自然连接

2. 自连结：为同一个表取别名（在FROM后变，SELECT可直接使用别名）

3. 外部联结：把悬浮元组保留在结果关系中并填空值NULL/只取部分

   + 语法格式：

     ```sql
     ...
     FROM Table1 [LEFT|RIGHT] OUTER JOIN Table2 ON 列/条件
     ```

   + LEFT和RIGHT指出条件针对的表，**必选其一**

   + 全外部联结`FULL OUTER JOIN`

-----

+ 组合/集合查询：把多个查询结果何在一起

  > SELECT语句的查询结果是元组的组合，所以多个SELECT语句的结果可进行集合操作

  + 包括：并操作`UNION` union、交操作`INTERSECT` intersect、差操作`EXCEPT` except

    > 并操作是天然去重的，`UNION ALL`可以不去重

  + 要求：参加集合操作的各查询结果的列数必须相同；对应项的数据类型也必须相同

  + 语法：`查询块 集合操作 查询块`

    + 排序：`ORDER BY`子句放在所有的最后对最后结果排序

## 数据更新/操作

1. 插入数据

   1. 插入元组：将元组插入指定表

      ```mysql
      INSERT
      INTO <表名> [(<属性列1>[, <属性列2>]···)]
      VALUES(<常量1>[, <常量2>]···);
      ```

      新元组的属性列1的值为常量1，属性列2的值为常量2

      INTO子句没有出现的属性列，新元组在这些列上取空值

      INTO子句没有指针任何属性列名，新元组必须在每个属性列均有值

   2. 插入子查询结果（多个元组）：

      ```mysql
      INSERT
      INTO <表名>[(<属性列1>[, <属性列2> ···])]
      子查询;
      ```
      
   3. 复制表：在创建表中使用，不用DBMS不同

2. 修改数据（更新操作）：

   ```mysql
   UPDATE<表名>
   SET<列名>=<表达式>[, <列名>=<表达式>]···  -- 确定列
   [WHERE<条件>]                          -- 确定行
   ```

   修改表中满足WHERE子句条件的元组，将对应列修改为对应表达式，如果没有WHERE则修改所有

   1. 修改某一个元组的值
   2. 修改多个元组的值
   3. 带子查询的修改语句——嵌套在WHERE

3. 删除数据：

   ```mysql
   DELETE
   FROM<表名>
   [WHERE<条件>];
   ```

   从指定表中伤处满足WHERE子句条件的所有元组，

   如果省略WHERE则删除所有元组，但表仍在字典中——删除表的数据，而不是表的定义

   1. 删除某一个元组的值
   2. 删除多个元组的值
   3. 带子查询ode删除语句——嵌套在WHERE

## 数据控制

### 事务

+ 事务处理(transaction processing)：同来管理成批执行的SQL操作的机制

  + 事务(transaciton)：指一组SQL语句；
  + 回退(rollback)：指撤销指定SQL语句的过程：只能回退数据操作
  + 提交(commit)：指将为存储的SQL语句结果写入数据库表
  + 保留点(savepoint)：指事务处理设置的临时占位符(placeholder)，可对其发布回退

+ 标识事务处理块：

  ```sql
  BEGIN TRANSACTION -- begin
  START TRANSACTIOn -- start transaction
  ```

+ 回退：`ROOLBACK`命令

+ 提交：`COMMIT`命令：在事务中使用

  > 一般SQL语句都是直接对数据库执行和编写，即隐含提交(implicit commit)

+ 保留点：

  ```sql
  SAVEPOINT 保留点名;
  SAVE TRANSACTION 保留点名;
  ```

  + 回退：

    ```sql
    ROLLBACK TO 保留点名;
    ROLLBACK TRANSACTION 保留点名;
    ```

  + 检查：

    ```sql
    IF @@保留点名 <> 0 回退;
    ```

+ 特性(ACID)

  1. 原子性(atomicity：

     事务中包含的所有操作要么全做，要么全不做；

     由**恢复机制**实现。

  2. 一致性(consistency)：

     事务的隔离执行必须保证数据库的一致性：事务开始前和结束后，数据库都处于一致性的状态；

     由**用户**负责，由**并发控制**实现

  3. 隔离性(isolation)：

     系统必须保证事务不受其他并发执事务的影响：

     通过**并发控制机制**实现

  4. 持久性(Durability)：

     一个事务一旦提交后，对数据库的影响必须是永久的；即使发生故障

     通过**恢复机制**实现

+ 概念：

  + 业务逻辑：两个或以上业务必须同时完成，或者同时失败
  + 技术逻辑：两个或以上写操作，必须同时完成，或同时失败

+ 运行：

  + 事务串行执行，同一时刻只有一个事务运行
    + 单处理机并行事务轮流交叉运行
    + 多处理机同时并发执行



### 游标

### 触发器

+ 触发器(trigger)/事件-条件-动作(event-condiition-action)规则：是用户定义在关系表上的一类由事件驱动的特殊过程。

  当特定的事件发生时，对条件进行检查，如果条件不成立不执行该动作

  > 触发器在SQL 99后才写入SQL标准

+ 定义：

  ```sql
  CREATE TRIGGER <触发器名>
  {BEFORE|AFTER} <触发事件> ON <表名>  -- before after
                                     -- 激活事件是在执行事件的前或后
  -- 激活事件： INSERT DELETE UPDATE 的单独或组合 后接 OF + 具体位置
  REFERENCING {NEW|OLD}ROW AS<变量>  -- referencing new old
                                   -- 指出引用标量
  FOR EACH {ROW|STATEMENT}  -- row statement
                            -- 定义类型，指明动作题执行频率
  -- 行级触发器（FOR EACH ROW）       ：语句中执行一个表的行执行一次
  -- 语句级触发器（FOR EACH STATEMENT）：一个语句执行一次          （默认）
  [WHEN<触发条件>]<触发动作体>  -- when
                             -- 仅当触发条件为真时才执行触发动作体（可忽略）                           
  /*
  触发体格式：
  begin
  print '';
  ...
  end;
  */
  ```

  + 只有表的拥有者才可以在表（不能是视图）上创建**一定数量**（由DBMS设计时确定）的触发器

  + 同一模式下，触发器名必须是唯一的，并且触发器名和表名必须在同一模式下。

  + 触发动作体：

    + 匿名PL/SQL过程块
    + 对已创建存储过程的调用

    1. 行触发器：可使用NEW和OLD引用UPDATE/INSERT事件之后的新值和之前的旧值。
    2. 语句触发器：不能

    如果触发动作体执行失败，激活触发器的事件（即对数据库的增、删、改操作）就会终止执行，触发器的目标表或触发器可能影响的其他对象不发生任何变化

+ 触发：谁先创建谁执行

+ 删除：`DROP TRIGGER <触发器名> ON <表名>;` 被删触发器必须存在，并由有权限的用户删除。

> 触发链：一个触发器动作激活另一个触发器。



# 数据库安全性

+ 定义：数据库安全是指保护数据库以防止不合法使用所造成的数据泄露、更改或破坏。

> 不安全的因素：
>
> 1. 非授权用户（黑客）对数据库的恶意存取和破坏
> 2. 数据库中重要或敏感的数据被泄露（机密）
> 3. 安全环境的脆弱性

## 安全标准

+ **TCSEC**：1985年美国国防部(Department of Defense, DoD)正式颁布的《DoD可信计算机系统评估准则》(Trusted Computer System Evaluation Criteria, TCSEC)（DoD85）

  > 又称桔皮书。

+ TCSEC之后，不同国家都开始启动开发建立在TCSEC概念上的评估标准

  + 欧洲的信息技术安全评估准则(Information Technology Security Evaluation Criteria, ITSEC)
  + 美国的信息学技术安全联邦标准(Federal Criteria, FC)草案

+ **CC**：1993年CTCPEC、FC、TCSEC和ITSEC联合、消除差异，集合成*通用准则*(Common Criteria, CC)项目

  CC V2.1版于1990年被ISO采用为国际标准，2001被我国采用为国家标准

![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Database-System/信息安全标准简史.png)

+ 1991.4，美国国家计算机安全中心(National Computer Security Center, NCSC)颁布了《可信计算机系统评估准则关于可信数据库系统的解释》(TCSEC\Trusted Database Interpretation, TCSEC/TDI，即紫皮书)，将TCSEC扩展到数据库管理系统：从 安全策略、责任、保证和文档 来描述安全性级别划分的指标并分为四组七个等级

  | 安全级别 | 定义                                                     | 含义                                   |
  | -------- | -------------------------------------------------------- | -------------------------------------- |
  | A1       | 验证设计(verified design)                                |                                        |
  | B3       | 安全域(security domains)                                 |                                        |
  | B2       | 结构化保护(structural protection)                        |                                        |
  | **B1**   | 标记安全保护(labeled security protection)                | 对标记主体客体实施强制存取控制以及审计 |
  | C2       | 受控的存取保护(controlled access protection)             |                                        |
  | C1       | 自主安全保护(discretionary security protection, **DAC**) |                                        |
  | D        | 最小保护(minimal protection)                             |                                        |

+ CC：

  1. 简介和一般模型

  2. 安全功能要求：11大类、66子类和135组件

  3. 安全保证要求：7大类  、26子类和74组件 评估保证级(Evaluation Assurance Level, EAL)

     | 评估保证级 | 定义                                                         | TCSEC安全评级 | 含义 |
     | ---------- | ------------------------------------------------------------ | ------------- | ---- |
     | EAL1       | 功能测试(functionally rested)                                |               |      |
     | EAL2       | 结构测试(structurally tested)                                | C1            |      |
     | EAL3       | 系统地测试和检查<br>(methodically tested and checked)        | C2            |      |
     | EAL4       | 系统地设计、测试和复查<br>(methodically designed, tested and reviewed) | B1            |      |
     | EAL4       | 半形式化设计和测试<br>(semiformally designed and tested)     | B2            |      |
     | EAL6       | 半形式化验证地设计和测试<br>(semiformally verified design and tested) | B3            |      |
     | EAL7       | 形式化验证的设计和测试<br>(formally verified design and tested) | A1            |      |

  4. 附录：保护轮廓(Protection Profile, PP)和安全目标(Security Targer, ST)

## 安全控制

<img src="https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Database-System/安全控制.png" style="zoom:80%;" />

### 用户身份鉴别

> 每个用户在系统中都有一个用户名，由*用户名*(user name)和*用户标识号*(UID)（唯一）组成

+ 鉴别方法：
  1. 静态口令鉴别：常用、简单、容被破解，保证长度、内容以及重复间隔，不可见
  2. 动态口令鉴别：较安全，ege：短信密码、动态令牌
  3. 生物特征鉴别：ege：指纹、虹膜、掌纹
  4. 智能卡鉴别：不可复制硬件，常与个人身份识别码(PIN)结合使用。

### 存取控制

：是一个子系统，需要语言支持。

+ 定义用户权限：定义用户权限，并将用户权限登记到数据字典中
+ 合法权限检查：

> C2级的数据库管理系统支持自主存取控制(Discretionary Access Control, DAC)：
>
> B1级的数据库管理系统支持强制存取控制(Mandatory Access control, MAC)

**自主存取控制方法**：用户可决定数据的存取权限和“授权”的权限授予何人

​                                  SQL标准支持

> 用户权限：由 数据库对象和操作类型 组成
>
> 授权(authorization)：定义存取权限
>
> + 关系型数据库系统中的存取权限：
>
>   | 对象类型   | 对象         | 操作类型                                                     |
>   | ---------- | ------------ | ------------------------------------------------------------ |
>   | 数据库系统 | 模式         | `CREATE SCHEMA` `create schema`                              |
>   |            | 基本表       | `CREATE TABLE, ALTER TABLE` `alter`                          |
>   |            | 视图         | `CREATE VIEW`                                                |
>   |            | 索引         | `CREATER INDEX`                                              |
>   | 数据       | 基本表和视图 | `SELECT, INSERT, UPDATE, DELETE, REFERENCES, ALL PRIVILEGES（所有权限）` <br>`insert, references, privileges` |
>   |            | 属性列       | `SELECT, INSERT, UPDATE, REFERENCES, ALL PRIVILEGES`         |
>
>   其中对列的权限：遵守表的主码和其他约束；INSERT指可插入元组，可指定列值，其他值为空或默认，这个授权要包含对主码INSERT的授权；UPDATE的授权可后接小括号（`UPDATE(<行或列或或表>)`）指定具体属性列名

+ 授权：授予（`GRANT` `grant`）和收回（`REVOKE` `revoke`）

  1. `GRANT`：

     ```sql
     GRANT<权限>[,<权限>]···  -- 把的什么权限
     ON<对象类型><对象名>[,<对象类型><对象名>]···  -- 什么对象
     TO<用户名>[,<用户名>]···  -- 授予给谁
     [WITH GRANT OPTION];-- 被授予用户可将该权限再授予他人，否则不行
                         -- 但允许循环授予
     ```

     发出语句的：数据库管理员、数据库对象创建者（即属主owner）、拥有该权限的用户

     接收权限的：一个或多个具体用户、PUBLIC（全体用户）

  2. `REVOKE`：

     ```sql
     REVOKE<权限>[,<权限>]···
     ON<对象类型><对象名>[,<对象类型><对象名>]···
     FROM<用户>[,<用户>]···[CASCADE|RESTRICT]
     -- CASCADE级联 一同收回它再授予的权限
     -- RESTRICT   只收回目标的权限
     -- cascade restrict
     ```

+ 创建数据库模式的权限：

  > 上述的是用户对数据的权限，对创建数据库模式的授权则是数据管理员对于用户（创建用户实现）

  ```sql
  CREATE USER <username>[WITH][DBA|RESOURCE|CONNECT]
  ```

  DBA resource connect

  + 只有系统的超级用户才有权限创建一个新的数据库用户

  + 新创建的数据库用户由三种权限：CONNECT（默认）、RESOURCE和DBA

    ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Database-System/CREATE USER权限.png)

  **不是SQL标准，不同关系数据库管理系统的语法和内容差别较大**

+ 数据库角色：被命名的一组与数据库操作相关的权限，角色是权限的集合

  ​                       为一组具有相同权限的用户创建一个角色，使用角色来简化授权

  1. 角色的创建：`CREATE ROLE<角色名>`

  2. 给角色授权：

     ```sql
     GRANT<权限>[,<权限>]···
     ON<对象类型>对象名
     TO<角色>[,<角色>]···
     ```

  3. 将一个角色授予其他的角色或用户

     ```sql
     GRANT<角色>[,<角色2>]···
     TO<角色3>[<用户1>]···  -- 被授予角色的权限是授予它的全部角色的权限和
     [WITH ADMIN OPTION] -- 被授予角色和用户可把这个权限再授予其他角色 
     -- with admin option
     ```

  4. 角色权限的收回

     ```sql
     REVOKE<权限>[,<权限>]···
     ON<对象类型><对象名>
     FROM<角色>[,<角色>]···
     ```

     此动作的执行者是角色的创建者或是拥有此角色的ADMIN OPTION

**强制存取控制方法**：系统为保证更好程度的安全性，不是用户能直接感知或进行控制；适用于对数据有严格而固定密级分类的部门。

+ 数据库管理系统所管理的实体：

  1. 主体：系统中的活动实体，包括实际用户和代表用户的进程
  2. 客体：系统中的被动实体，受主体操纵，包括文件、基本表、索引、视图等

  数据库管理系统对实体指派一个*敏感度标记*(label)

  + 敏感度标记：被分为若干级别：TS >= S >= C >= P
    + 绝密(Top Secret, TS)：
    + 机密(Secret, S)          ：
    + 可信(Confidential, C)：
    + 公开(Public, P)           ：

  1. 主体的敏感度标记称为*许可证级别*(clearance level)
  2. 客体的敏感度标记称为*密级*(classification level)

  > 原理：高敏感度标记的主体可以存取低敏感标记的客体

+ 规则：

  1. 仅当主体的许可证级别大于或等于客体的密级时，该主体才能读取相应的客体

  2. 仅当主体的许可证级别小于或等于客体的密级时，该主体才能写相应的客体

     防泄漏：防止数据的密级从高流向低

标记与数据不可分（即使复制）

安全检查：对操作先进行DAC检查，再进行MAC检查，才进行语义检查。

### 审计

审计(audit)功能是数据库管理系统达到C2以上安全级别必不可少的一项指标

提供了一种事后检查的安全机制。

+ 审计功能就是把用户对数据库的所有操作自动记录下来放入*审计日志*(audit log)中，审计员可以利用审计日志监控数据库中的各种行为，重现导致数据库现有状况的一系列时间，找出非法存取数据的人、时间和内容

1. 审计事件：

   + 服务器事件
   + 系统权限
   + 语句实践
   + 模式对象事件

2. 审计功能：

   + 基本功能：多种查阅方式：基本、可选、优先
   + 多套审计规则：数据库初始化时设定
   + 审计分析和报表功能
   + 审计日志管理功能：ege：防误删
   + 查询审计设置和审计记录信息的专门视图

3. `AUDIT`语句（设置审计功能）和`NOAUDIT`语句（取消审计功能） `audit`

   存储在数据字典，要把审计开关打开（系统参数audit_trail设为true），才可在系统表SYS_AUDITTRAIL中查看审计信息。

   > 审计分类：
   >
   > + 用户级审计：任何用户可设置的审计，
   >
   >   ​                       是用户对自己创建的数据库表或视图进行审计
   >
   > + 系统级审计：只能由数据库管理员设置
   >
   >   ​                       用来检测成功或失败的登录请求、检测授权和收回操作以及其他

   1. 设置审计:

      ```sql
      AUDIT ALTER, UPDATE
      ON 表;
      ```

   2. 取消审计：

      ```sql
      NOAUDIT ALTER, UPDATE
      ON 表;
      ```


### 加密

+ 基本思想：根据算法将原始数据（明文(plain text)）变换为不可直接识别的格式（密文(cipher text)），使不知解密算法的人无法获知数据

1. 存储加密：

   1. 透明：内核级加密，对用户完全透明

      在写入磁盘时加密，用户读取时解密

   2. 非透明：通过多个加密函数实现

2. 传输加密：

   1. 链路加密：在数据链路层对报头和报文均加密，中间节点需要密码设备

   2. 端到端加密：在发送端加密，在接收端解密，只加密报文，不加密报头，可被截获

      ![](https://cdn.jsdelivr.net/gh/zweix123/CS-notes-img@master/Database-System/端到端加密.png)

      + 确认可靠性：通过各自持有 由 指明数字证书认证(Certificate Authority, CA)中心或企业内建CA颁布的数字证书：先提供对方证书，然后使用 本地的CA新人列表和证书撤销列表(Certificate Revocation List, CRL)进行验证
      + 协商加密算法和密钥：利用 公钥基础设施(Public Key Infrastructure, PKI)

### 其他

+ 视图

除自主存取控制和强制存取控制外，还有*推理控制*以及数据库应用中*隐蔽信道*和*数据隐私保护*等技术

+ 推理控制(inference control)：ege：我可以查自己的职务的工资，但我不可以查找别人的工资，不过我可以查询别人的职务，也许我可以通过自己的它人的职务来得到别人的工资。
+ 隐蔽信道(covert channal)：ege：对于unique约束列，通过插入进行试探
+ 数据隐私(data privcacy)：控制不愿被它人知道或它人不便知道的个人数据的能力

# 数据库完整性

+ 数据库完整性(integrity)是指数据的正确性(correctness)和相容性(compat-ability)
  + 正确性：数据是符合现实世界语义、反应当前实际状况的；
  + 相容性：数据库同一对象在不同关系表中的数据是符合逻辑的。

> 数据的安全性：保护数据库防止恶意破坏和非法存取
>
> 数据的完整性：防止数据库中存在不符合语义、不正确的数据

+ 为完整性数据库管理系统应提供的功能：
  1. 提供定义完整性约束条件的机制
  2. 进行违约处理
+ 约束(constraint)：管理如何插入或处理数据库数据的规则

### **实体完整性**

+ 定义：在`CREATE TABLE`（建表）中用`PRIMARY KEY` `primary key` 短语定义主码

  + 列级定义主码：在每个属性定义后面添加语句。
  + 表级定义主码：在表的最后将定义的主码统一定义，如果有多个主码，必须使用此

  ```sql
  CREATE TABLE student (
  	Sno CHAR(9) PRIMARY KEY,  -- 列级定义主码
      Sname CHAR(20) NOT NULL,
      Sex CHAR(2),
      Sage SMALLINT,
      Sdept CHAR(20),
  --  PRIMARY KEY(Sno)          -- 表级定义主码
  --  PRIMARY KEY(Sno, Cno)     -- 多个必须使用在表级定义
  );
  ```

+ 使用：实体完整性检查和违约处理：用户在插入记录或更新主码时自动进行

  1. 检查主码值是否唯一，如果不唯一则拒绝插入或修改

     > 全表扫描 -> DBMS自动建立（B+树）索引以提高效率

  2. 检查主码的各个属性列是否为空，只要有一个为空就拒绝插入或修改

### **参照完整性**

+ 定义：在`CREATE TABLE`（建表）中的`FOREIGN KEY` `foreign key` 短语定义外码

  ​                                                                 `REFERENCES` `references` 短语定义外码参照哪些表的主码

  ```sql
  CREATE TABLE SC (
  	Sno CHAR(9) NOT NULL,
      Cno CHAR(4) NOT NULL,
      Grade SMALLINT,
      PRIMARY KEY(Sno, Cno),                   -- 表级定义实体完整性
      FOREIGN KEY(Sno) REFENCES Student(Sno),  -- 表级定义参照完整性
      FOREIGN KEY(Sno) REFENCES Student(Cno)   -- 表级定义参照完整性
  );
  ```

+ 使用：参照完整性检查和违约处理：对被参数表和参照表进行增删改操作时检查

  + 被参照表：
    + 插入元组 -> 可能破坏参照完整性 -> 拒绝
    + 修改外码值 -> 可能破坏参照完整性 -> 拒绝
  + 参照表：
    + 删除元组 -> 可能破坏参照完整性 -> 拒绝/级联删除/设置为空值
    + 修改主码值 -> 可能破坏参照完整性 -> 拒绝/级联修改/设置为空值

  违约操作：

  1. 拒绝(NO CATION)执行：默认策略

  2. 级联(CASCADE)操作：

     主码没有了，以其为参照的外码不合适了，级联着一同修改

  3. 设置为空值：

     主码没有了，以其为参照的外码不合适了，直接把其元组设置为空值

     当此外码为该表主码时，不能取空值

  后两者需要显式的定义：可为每个情况单独定制

  ```sql
  CREATE TABLE SC (
  	Sno CHAR(9) NOT NULL,
      Cno CHAR(4) NOT NULL,
      Grade SMALLINT,
      PRIMARY KEY(Sno, Cno),                 
      FOREIGN KEY(Sno) REFENCES Student(Sno) 
      	ON DELETE CASCADE   -- 当主码删除时，级联删除外码
      	ON UPDATE CASCADE   -- 当主码修改时，级联修改外码
      FOREIGN KEY(Sno) REFENCES Course(Cno) 
      	ON DELETE NO ACTION -- 当主删除改时，拒绝
      	ON UPDATE CASCADE
  );
  ```

  ==设置为空值怎么设置？==

### **用户定义完整性**

：个性化定制，利用实体和参照完整性进行

+ 属性上的约束条件

  1. 属性上的约束条件的定义：在`CREATE TABLE` 定义时进行，（可重叠使用）
     + 列值非空(`NOT NULL`)
     + 列值唯一(`UNIQUE`)
     + 检查列值是否满足一个条件表达式(`CHECK` 短语)

  + 检查和违约处理：插入元组和修改属性值时进行，不满足拒绝执行

+ 元组上的约束条件

  1. 属性上约束条件的定义：在`CREATE TABLE` 定义时进行，使用`CHECK` 短语，放在表级位置

  + 检查和违约处理：插入元组和修改属性值时进行，不满足拒绝执行

### 完整性约束命名子句

**完整性约束命名子句**

> 除了在CREATE TABLE时定义，还可以为这些约束子句进行命名

+ 语法：

  + 定义：`CONSTRAINT<完整性约束条件名><完整性约束条件>` `constraint`

    ```sql
    CREATE TABLE tableName (
    	sam1 type
        	CONSTRAINT name1 NOT NULL,
        sam2 type
        	CONSTRAINT name2 UNIQUE,
        sam3 type
        	CONSTRAINT name3 CHECK...,
        sam4 type, 
        CONSTRAINT name4 CHECK(),
        CONSTRAINT name5 PRIMARY KEY(sam1)
    );
    ```

  + 修改：在`ALTER TABLE`中使用`DROP`或`ADD`

    ```sql
    ALTER TABLE tableName
    	DROP CONSTRAINT name2;
    ALTER TABLE tableName
    	ADD CONSTRAINT name6 ...;
    ```

## 域

域是一组具有相同数据类型的值的集合，属性值来自域

*域的完整性限制*：对域的修改可以只修改域，而不需要修改每个属性的域

+ 建立域：`CREATE DOMAIN` `domain`

  ```sql
  CREATE DOMAIN Gender CHAR(2)
  ```

+ 设置约束条件：在创建是进行

  ```sql
  CREATE DOMAIN Gende CHAR(2)
  	CHECK(VALUE IN ('男', '女'));
  ```

  也可以为限制命名

  ```sql
  CREATE DOMAIN Gende CHAR(2)
  	CONSTRAINT GD CHECK(VALUE IN ('男', '女'));
  ```

  对应着可以进行删除和添加

  ```sql
  CREATE DOMAIN Gende
  	DROP CONSTRAINT GD;
  ```

  ```sql
  CREATE DOMAIN Gende
  	ADD CONSTRAINT GDD CHECK(VALUE IN ('0', '1'))
  ```

## 断言

+ 断言(declarative assertions)：指定更具一般性的约束，可以定义设计多个表或聚类操作的完整性约束
+ 创建：`CREATE ASSERTION<断言句><CHECK 子句>;` `assertion`

+ 删除：`DROP ASSERTION<断言句>;`

