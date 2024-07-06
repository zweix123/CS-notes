## numpy

+ 通常引入方法：

  ```python
  import numpy as np
  ```

+ 数据类型：下面末尾的下划线是为与python原生的数据类型做区别

  + 布尔型：`bool_`
  + 整型：`int_、int8、int16、int32、int64`
  + 无符号整型：`uint8、uint16、uint32、uint64`
  + 浮点型：`float_、float16、float32、float64`

    + `np.nan`(not a number)：不等于任何一个数——任何两个nan不相等：数据分析中常用作数据缺失值
    + `np.inf`(infinity)            ：比任何浮点数都大><但inf之间是相等的。
  + 复数型：`complex_、complex64、complex128`
  + 其他

### ndarray

+ 多维数组对象：`a = np.array(...)`

  + 支持`a[]...[]`的索引方式，也支持`a[第一维度, ...]`的写法

  + 切片：ndarray的切片是“视图”

    > 列表的切片是创建新的对象

    + “深拷贝”：`a[切片].copy()`

    + 高维切片：

      以二维数组为例，想切片出子矩阵

      > `a[一个切片][再一个切片]`相当于`b = a[对行切片（第一个切片）], c = b[对行切片（第二个切片）]`

      `a[对第一维切片, 对切好的新矩阵进行第二维切片]`（切片：`:`全部，`数字`只要一条）

  + 花式索引：

    + `a[一个整数列表]`：选出列表元素对应位置的元素组成ndarray

    + 二维数组`a[列表，等长列表]`相当于两个列表对应位置取出做矩阵坐标，然后取出对应的数

    + 想取出矩阵的`(1, 1), (1, 3), (3, 1), (3, 3)`

      `a[[1, 1, 3, 3], [1, 3, 1, 3]]` = `a[[1, 3], :][:, [1, 3]]`

  + 布尔型索引：`a[a>5]`：本质是`ndarray[同样大小的布尔类型的ndarray]`

    > 原生写法：
    >
    > ```python
    > a = list()
    > b = list(filter(lambda x : x > 5, a))
    > ```

    + 多个条件：`a[(a > 5) & (a % 2 == 0)]`（要考虑优先级）

      不支持`and`（因为本质还是需要一个ndarray）

      > `&` 和`and`运算：就是C中`&`和`&&`的区别

+ 属性：

  + `a.dtype`数据类型
  + `a.size`元素数量
  + `a.shape`数组形状
    + `reshape(元组)`对已有数组进行维度变形，要求size前后一样
  + `a.T`转置

+ 创建：

  + `np.array(列表/range())`

    + `np.arange()`：相当于`np.array(range())`同时增加“步长可以是浮点数”的特性
    + `np.linspace(闭区间, “划分个数”)`

  + `np.zeros/ones/empty(数量, dtype='数据类型')`

    > 先申请空间再初始化，empty只申请空间不初始化

    + `np.eye(矩阵大小)`：生成单位矩阵

+ 批量运算：对数组中的元素分别运算

  + 对标量进行运算（+-*//**><）

    > 可以把ndarray看作矩阵，这里的标量是相对此来说

  + 向量运算（要求shape同）：+/**%==

### 接口

> 后续的DataFrame建立在Series、时间序列建立在ndarray，而Series也建立在ndarray，故此处的函数和方法在后续对象中都可使用

+ （常用）数学统计方法：

  > 方法与对象相关、使用在对象后，同时既然是方法就区别于属性要有括号

  ```python
  sum
  mean  # 平均值
  min/max
  argmin/argmax  # 最小/大值的索引
  std  # 求标准差  方差开根号  利用均值加减标准差可以大概估计数据范围
  var  # 求方差  数据离散程度  各值减去均值得和再除以均值
  ```

+ 通用函数

  > 函数是包内的，与具体对象无关，使用`np.函数(...)`

  + 一元函数：

    + `abs`、`sqrt`、`exp`（指数运算）、`log`（对数运算）

    + `trunc`（向0取整——截断）、`round`==`rint`（四舍六入五变偶）、`ceil`（向上取整）、`floor`（向下取整）
    + `modf`（区分整数部分和小数部分，返回两个ndarray）
    + `isnan`（判断ndarray中是否有nan）`a[~(np.isnan(a)]`取出非nan的数（是~而不是!因为前者是位运算后者是逻辑运算符）、`isinf`（同理）（其实由于inf之间是相等的，所以可以`a[a==np.inf]`）

  + 二元函数：

    ```python
    add
    substract
    multiply
    divide
    power
    mod
    maximum/mininum  # 取出两ndarray同一位置的更大/小值组成新索引，还记得方法min/max吗？
    ```

+ 随机数生成：在`np.random`子包内，较于普通的random库可以提供多一位参数产生给定形状（一个数字或元组）

  ```python
  rand  # 给定形状0到1之间的数
  randint  # 给定形状区间内的随机数
  choice  # 给定形状给定数组内随机元素  
  uniform  # 给定形状产生随机随点数（均匀分布）数组
  shuffle  # 打乱
  # 其他随机函数也有重写
  ```

## pandas

> 基于numpy构建，故两大数据结构对象都支持ndarray的特性，可使用numpy的函数和方法

+ 通常引用方式：

  ```python
  import pandas as pd
  ```

### Series

+ 类似一维数组，由一组数据和一组与之相关的index组成`sr = pd.Series(...)`

  + 即可使用下标进行访存，由可通过index进行

    > 当以整数作为index时下标失效，想通过下标进行访存使用方法`sr.iloc[下标]`

  + 花式索引：

    + `sr[index列表]`
    + 通过index切片（左右闭区间）

+ 构建：

  + `pd.Series(列表/ndarray, [index=对应index列表/ndarray])`
  + `pd.Series(字典)`

+ 特性：

  + 语法`index in sr`返回真假

  + 语法`for sam in sr`遍历数据部分（而不是index）

  + 属性`sr.index`返回index的ndarray

    属性`sr.values`返回数据的ndarray

  + 数据对齐：pandas在进行Series对象之间的运算时，会按index进行对齐，然后对应计算，非index集合交集的index结果为NaN

    + 数据完整性：pandas提供`add sub div mul`（`sr1.op(sr2. fill_value=0)`）实现数据完整性

  + 缺失数据NaN处理：

    + `sr.isnull/notnull()`返回index同sr，数据为布尔类型的Series。
    + `sr.dropna()`返回丢掉数据为NaN的部分，相当于`sr[sr.notnull()]`
    + `sr.fillna(值)`将nan填充为值

### DataFrame

+ `df`表格数据结构，包含一组**有序的列**，可认为由Series组成的字典，且Series之间共用一个index

  + 索引：
    + `df[列index/列下标][行index/行下标]`
      1. **先列再行**
      2. 仍有Series整数index冲突的问题
    + `df.loc[行index, 列index]、df.iloc[行下标, 列下标]`
      1. **先行再列**

+ 构建：

  + `pd.DataFrame(二维列表)`
  + `pd.DataFrame(value为列表的字典, [index=[索引的列表]])`
  + `pd.DataFrame(Value为Series的字典)`

+ 属性：

  + `df.index`：行索引ndarray
  + `df.columns`：列索引的ndarray
  + `df.values`：内容的ndarray（二维）
  + `df.T`：转置
  + `df.describe()`：返回各列的描述

+ 关于数据对齐和缺失数据处理问题：

  + `dropna()`丢失含有缺失值的一行
    + `how`参数：
      1. `'all'`只有全部为nan才丢失
      2. `'any'`有一个nan就丢失
    + `axis`参数
      1. 默认`0`：按行丢
      2. 设置`1`：按列丢

+ 方法特化：

  + `df.mean()`：返回对列求均值的Series

    `df.sum()`：同上

    + 添加参数`axis`设置“轴”

  + 排序：按值排序`df.sort_value(by=某列)`和按index排序`df.sort_index()`

    + 参数`ascending`传入布尔值表升/降序
    + 参数`axis`同上

### 时间序列

1. 标准库`datetime`：`datetime,datetime.strptime('表示时间的字符串', 格式)`（其中函数名中的p表示parser）

   > 对字符串内的格式有严格要求

2. pandas库下的子库`dateutil`：`dateutil.parser.parse('表示时间的字符串')`对字符串的格式非常灵活

> pandas一次为基础构建各种关于时间的函数

+ 批量处理：`pd.to_datetime(表示时间的字符串的列表)`

+ 时间范围：`pd.data_range(起点, 终点/periods（时间长度）[, freq])`

  + 参数`freq`时间频率，默认`D`天、H小时、W周、B工作日、SM半个月、M月、T分钟、S秒、A年；还可以比如20T表示而是分钟，实际上更智能20min这种自然语言就可以

+ 时间序列：以时间为标签的DataFrame

  + 索引：只精确到月则提供这个月内的数据

    同理也可以这样切片

  + 采样方法`resample`，参数同时间，对Series分组，对分组分出出来的应用通用函数

  + 还用方法`truncate`，参数有before和after

### 文件

+ 读：`pd.read_*()`、写：`pd.to_*()`

以`csv`（默认分隔符为逗号（`table`为默认分隔符为制表符））为例

+ 参数：

  + `sep`指定分隔符，可使用正则表达式

  + 指定列作为索引`index_col`，传入写的下标或index

  + 指定跳过行`skip_row`

  + 时间序列参数`parse_dates`

    + 传入`True`：把数据中所有可以作为时间都转换成时间
    + 传入`列`：指定

  + 函数把列手默认成index，参数`header`指定是否有列名，传入`None`表示不这样做，可使用参数`names`传入对应index

  + 读：`na_values`指定某些字符串表示缺失值

    写：`na_rep`指定缺失值转换成什么字符串，默认空

  + 写：指定列`usecols`

+ 可转换类型：csv、table、xml、json、html

## matplotlib

+ 引入：

  ```python
  import matplotlib.pyplot as plt
  ```

+ 画图：

  ```python
  plt.show()
  ```

以**折线图plot**为例

+ 传入：`plt.plot(x轴, y轴[, 其他信息])`，传入多条线则多次使用`plot`函数，同一线不同部分不同信息也可通过多次传入

  + 以字符串描述线性质：
    + `marker`：点的形状：
    + `132`：线的形状：
    + `color`：颜色：
  + `label`

+ 全局信息：

  + `plt.title()`

  + `plt.x/ylabel()`
  + `plt.x/ylim()`范围
  + `plt.x/ytickes()`刻度：参数为序列，表示哪些点的刻度显示
    + 可以提供两个序列，一个数字序列为丈量标记，另一个序列表示对应位置的符号
  + `plt.legend()`：设置曲线图例和每次的plot有关，值得是否显示每条线的label

+ 与DataFrame相结合

  + `df.plot()`

+ 画布和子图：

  1. 创建画布：`fig = plt.figure()`
  2. 添加子图：`axi = fig.add_subplot()`
  3. 子图作画：`axi.plot()`
  4. 展示打印：`plt.show()`

  + 调节子图间距：`subplots_adjust(left, bottom, right, top, wspace, hspace)`

----

+ 其他图形：
  + 条形图：`bar(位置序列,各位置高度[, color（可传入序列）, width])`

  + 饼图：`pie(占比[, labels, autopct（显示）])`

### K线图

> 曾经`matplotlib.finanace`子包中有许多绘制金融相关图的接口，现matplotib已将将其移出为独立的包`mplfinance`

```python
import mplfinance as mpl
```

+ 基本用法：`mpl.plot(df, type="candle")`


## pyecharts
[GitHub](https://github.com/pyecharts/pyecharts)