# 金融

+ 量化策略：
  1. 输入：行情数据、财务数据、自定义数据、投资经验
  2. 策略：
     1. 选股
     2. 择时
     3. 仓位管理
     4. 止盈止损
  3. 输出：买入信号、卖出信号、交易费用、收益

+ 金融技术面分析：

  + K线：每天具体信息

    竖立矩形两端有突出的线（上/下影线），四个点分别表示开/收盘价和最高/低价，矩形为K线实体

    + 阳线（红色空）：涨
    + 阴线（非红色/绿色）：跌

  + MA（均线）：MA数字：取前若干天（收盘价格）做评估然后连起来的线

  + KDJ（随机指标）：

  + MACD（指数平滑移动平均线）：

# 





# py

## Tushare

```python
import Tushare as ts
```

+ 一些旧的接口：
  + `ts.get_k_data("股票编号")`返回DataFrame
    + `code`证券代码
    + `ktype`数据类型：D日线、W周线、M月线、5 15 30 60表对应分钟
    + start/end
  + `get_today_all()`



# 双均线策略

+ 内容：查找历史金叉死叉日期
+ 适用：非震荡市
+ 均线：对于每一个交易日，都可以计算出前N天的移动平均值，然后把这些移动平均值连起来，成为一条线，就叫做N日移动平均线，常用：5 10 30 60 120 240
  + 5天和10天的是短线操作的参照指标，称作日均线指标
  + 30天和60天的是中期均线指标，称作季均线指标
  + 120天和240天的是长期均线指标，称作年均线指标
+ 金叉：短期均线上穿长期均线，买入信号
+ 死叉：短期均线下穿长期均线，卖出信号

## Project

## 平台实现

```python
def initialize(context):
    set_benchmark('0003000.XSHG')
    set_cption('user_real_price', True)
    set_order_cost(...)
    
    g.security = ['601318.XSHG']
    
    g.p1 = 5  # 5日均线
    g.p2 = 10  # 10均线
    
def handle_data(context, data):
    for stock in g.security:
        '''
        如何得到金叉死叉
        1. 死叉和金叉一定是交替的
        2. 每个叉都是全部买入或卖出股票
        即叉和持股状态有关系
        '''
        # 金叉：如果5日均线大于10均线并且不持仓
        # 死叉：如果5日均线小于10均线并且持仓
        
        df = attribute_history(stock, g.p2)
        ma10 = df['close'].mean()
        ma5 = df['close'][-5:].mean()
        
        if ma10 > ma5 and stock in context.partfolio.positions:
            order_target(stock, 0)
            
        if ma10 < ma5 and stock not in context.partfolio.positions:
			order_value(stock, context.portfolio.available_cash * 0.8)
            
	record(ma5_ = ma5, ma_10 = ma10) # 画新线
```

# 量化平台-joinquant

+ API文档
+ 数据字典
+ 策略模拟



1. 代码区

```python
def initialize(context):
    # 全局对象g中存储数据，什么数据对应什么属性
    # g.security = '601877.XSHG' # 代码.上市地区，也可以是列表
    
    # get_index_stocks(指数代码字符串, ) # 获取指数成分股 # 沪深300：000300
    g.security = get_index_stocks('000300.XSHG')
    
    set.option('use_real_price', True) # 用真实的价格True # 必须加
    set_order_cost() # 设置佣金/印花税（手续费） # 使用API示例，固定
    
    set_benchmark(股票代码字符串) # 基准线（红色）
    # 这样做相当于最开始就全部进仓这支股票，然后的收益——股票涨跌
    
def handle_data(context, data): # 每天干什么
    get_current_data() # 获取当天信息
    
    attribute_history(代码字符串, 往前获取几天...) # 获得历史数据
    
    # 怎么样下单
    order(代码字符串, 股数) # 买入（按股数下单） # 国内买卖股票必须是一百的倍数
    order_value(.., .., ...) # 按钱数买股
    order_target() # 买到多少股
    order_target_value() # 买到多少钱
    # 上述如果传入负数或者第三个传入小于当前则是卖出
```

+ 手续费：

  + 交易（买入或卖出）股票需要向券商交付佣金：万分之三，最低5块

    + 卖出股票时需要印花税（交给国家）：千分之一

    > 这里的比例是按金额计算

+ initialize和handle_data函数只需定义，不需要显式调用（自动调用）

+ `context`：信息

  + `portfolio`：账户信息

    + `position`：位：是一个字典的，参数股票代码

      + `avg_cost`：开仓均价，这个股票所有股票买入的平均值

      + `total_amount`：总仓位，持有多少股

      + `closeable_amount`：可卖出的仓位

        > 仓位就是持股

        因为T+num制度导致并不是持股都是可买的

2. 可视化区：
   + 蓝线：策略收益
   
     红线：
   
   + 按天回测：默认开盘价
   
3. 命令行区：
   + 日志
   + 错误

## Eg

+ 策略：
  + 设置股票池为沪深300的所有成分股
  + 如果当前股票小于10元/股且当前不持仓，则买入
  + 如果当前股价比买入时上涨了25%，则清仓止盈
  + 如果当前股价比买入时下跌了10%，则清仓止损

```python
from jqdata import *

def initialize(context):
    g.security = get_index_stacks('00300.XSHG') # 沪深300
    set_option('use_real_price', True)
	# 股票类每笔交易时的手续费是：买入时佣金万分之三，卖出时佣金万分之三加千分之一印花税, 每笔交易佣金最低扣5块钱
	set_order_cost(OrderCost(open_tax=0, close_tax=0.001, open_commission=0.0003, close_commission=0.0003, close_today_commission=0, min_commission=5), type='stock')
    
def handle_data(context, data):
    
    # 一般情况下先买后买（有更多的钱）
    
    tobuy = [] # 存要买入的股票，原因见策略1解释
    for stock in g.security:
        p = get_current_data()[stock].day_open # 获得当前股票的开盘价
        amount = context.portfolio.position[stock].total_amount # 持股数量
        
        if p <= 10 and amount == 0: # 策略1
            # 买入，怎么买，一般是全买或者80%的钱买，那么这300只股票怎么分？
            tobuy.append(stock)
	# context.portfolio.available_cash # 手上的钱
    cash_pre_stock = context.portfolio.available_cash / len(tobuy)
    # 这里是均分（很粗糙）
    for stock in tobuy:
        order_value(stock, cash_pre_stock)
    # 策略1ok
    
    for stock in g.security: # 可以和上面结合这里为了清楚
        p..
        amount..
        cost = context.portfolio.positions[stock].avg_cost
        if amount > 0 and p >= cost * 1.25: # 止盈
            order_target(stock, 0) # 全部卖出
           
        if amount > 0 and p <= cost * 0.9: # 止损
            order_target(stock, 0) # 全部卖出
```

## 如何开发

+ 元素：
  + 上下文信息保存
  + 获取信息
  + 下单函数
  + 用户接口
  + ...





# 因子(市值)选股

因子：选择股票的某种标准：增长率、市值、市盈率、ROE（净资产收益率）

+ 选择策略：

  + 对于某个因子，选取表现最好（因子极值）的N支股票持仓
  + 每隔一段时间调仓一次：不是每天，可能是一周或者一个月

  > 小市值策略：选取股票池中市值最小的N只股票持仓
  
+ `get_fundamentals`查询财务数据

  + 参数：
    + `query_object`

  + 结果：
    + `market_cap`：市值 


以 选择市值、选择最小的10（相信它们以后会涨）、一个月一调仓的策略

```python
def initialize(context):
    set_benchmark...
    set_option...
    set_order_cost...
    
    g,security = get_index_stock('000300.XSHG')
    g.q = query(valustion).filter(valueation.code.in_(g.security))
    # valustion市场数据表
    # filter 过滤器 where
    
    # 如何使用呢？
    # df = get_fundamentals(g.q)
   	
    # 这里有个新的问题。因子选股是不是每天以执行，而是一段时间，handle_data不合适了。joinquant提供定时运行函数
    run_monthly(handle, 1)
    
    g.N = 20

def handle(context):
    # 选出来
    df = get_fundamentals(g.q)[['code', 'market_cap']]
    df = df.sort('market_cap').iloc[:g.N, : ]
    
    # 怎么调仓
    
    to_hold = df['code'].values # 我们最后要持有这些股票
    # 那么所有不在这里的持仓的股票都要卖出去
    for stock in context.portfolio.position:
        if stock not in to_hold:
            order_target(stock, 0)

	to_buy = [stock for stock in to_hold if stock not in context.portfolio.positions] # 在to_hold找到没有持仓的股票
    
    if len(to_buy) > 0:
	    cash_per_stock = context.portfolio.available_cash / len(to_buy)
        for stock in to_buy:
            order_value(stock, cash_per_stock)
           
    
    
```

+ 定时运行函数：`run_monthly、run_dayliy、`
  + 参数：
    1. 要绑定的函数——函数名
    2. 在这个月的第几个交易日调用

## 多因子

### 评分模型

> 既然是多因子，那么如何让所有的因子都均权的参与评估，因为可能有那种一个指标一般，但是另一个指标极好的情况
>
> 整一个加权平均值，对于越小越好的是减法，加权是为了平衡指标本身数值的差距

#### 标准化

+ `min-max`标准化：$x^{*} = \frac{x - min}{max - min}$
  + 把原始数据转化为一个0到1的数
  + 缺点：如果有新数据加入，可能导致min和max的变化
+ `Z-score`标准化：$x^{*} = \frac{x - \mu}{\sigma}$
  + 将原始数据转化为均值0，标准差为1的正态分布的随机变量

改编之前的策略

```python
def initialize(context):
    set_benchmark...
    set_option...
    set_order_cost...
    
    g,security = get_index_stock('000300.XSHG')
    g.q = query(valustion, indicator).filter(valueation.code.in_(g.security))
    # valustion市场数据表
    # filter 过滤器 where
    
    # 如何使用呢？
    # df = get_fundamentals(g.q)
   	
    # 这里有个新的问题。因子选股是不是每天以执行，而是一段时间，handle_data不合适了。joinquant提供定时运行函数
    run_monthly(handle, 1)
    
    g.N = 20
    

def handle(context):
    # 选出来
    df = get_fundamentals(g.q)[['code', 'market_cap', 'roe']]
    
    # 归一化
    df['market_cap'] = (df['market_cap'] - df['market_cap'].min) / (df['market_cap'].max - df['market_cap'].min)
    df['roe'] = (df['roe'] - df['roe'].min) / (df['roe'].max - df['roe'].min)
    
    # 创建新的列
    df['score'] = df['roe'] - df['mark_cap']
    # 选roe更高，市值更小的
    
    df = df.sort('score').iloc[:g.N, : ]
    
    # 之后不变
    
    # 怎么调仓
    
    to_hold = df['code'].values # 我们最后要持有这些股票
    # 那么所有不在这里的持仓的股票都要卖出去
    for stock in context.portfolio.position:
        if stock not in to_hold:
            order_target(stock, 0)

	to_buy = [stock for stock in to_hold if stock not in context.portfolio.positions] # 在to_hold找到没有持仓的股票
    
    if len(to_buy) > 0:
	    cash_per_stock = context.portfolio.available_cash / len(to_buy)
        for stock in to_buy:
            order_value(stock, cash_per_stock)
           
    
    
```



#### 多权重



# 均值回归理论

+ 价格的波动以其均线为中心——当价格偏离均线时，会重新调整回归均线

+ 偏离度=（mean - price） / mean

```python
def initialize(context):
    g.security = get_index_stocks('0003000.XSHG')
    g.ma_days = 30 # 均线时间
    g.stock_num = 10 # 持股数量
    
    run_monthly(handle, 1) # 一月一调仓
    
def handle(context):
    
    sr = pd.Series(index=g.security)
    for stock in sr.index:
        # 均线
        ma = attribute_history(stock, g.ma_days)['close'].mean()
        # 价格
        pr = get_current_data()[stock].day_open
        # 偏离度
        ratio = (ma - p) / ma
        # 选择向下偏离最大的（因为它会涨回去）
        sr[stock] = ratio
	# 从sr中选择最大的持股数量的股票 
    to_hold = sr.nlargest(g.stock_num).index.values #  列表
    
    
    # 那么所有不在这里的持仓的股票都要卖出去
    for stock in context.portfolio.position:
        if stock not in to_hold:
            order_target(stock, 0)

	to_buy = [stock for stock in to_hold if stock not in context.portfolio.positions] # 在to_hold找到没有持仓的股票
    
    if len(to_buy) > 0:
	    cash_per_stock = context.portfolio.available_cash / len(to_buy)
        for stock in to_buy:
            order_value(stock, cash_per_stock)
```





# 布林带Bollinger Band策略

由三条线组成，中间是均线，上下线是压力线和支撑线/上轨和下轨

+ 中间线：20日均线
+ up线=20日均线+N*SD（20日收盘价）
+ down线=20日均线-N*SD（20日收盘价格）

+ 策略：
  + 当股价突破阻力线时，清仓
  + 当股价跌破支撑线时，全仓买入
+ 优化：
  + N的取值问题
  + 布林带宽度等

```python
def initialize(context):
    g.security = '600036.XSHG'
    g.M = 20
    g.k = 2

def handle_data(context, data):
    sr = attribute_history(g.security, g.M)['close']
    ma = sr.mean()
    up = ma + g.k * sr.std
    down = ma -g.k * sr.std()
    price = get_current_data()[g.security].day_open
    cash = context.portfolio.available_cash
    if p <= down and g.security not in context.portfolio.positions:
        # 触底线，然后没有买，就买
        order_value(g.security, cash)
    elif p > up and g.g.security in context.portfolio.positions:
        # 碰上限，然后有买，就卖
        ordrt_value(g.security, 0);
    
```

+ 比如一些连续跌破下限，应该买入，但是可能这意味着会一直跌，那买入就亏了



# PEG策略

PEG是个人，彼得林奇

它说过

任何一家股票如果定价合理的话，市盈率就会与股票增长率相等

+ 市盈率：（PE） =   股价（P） / 每股收益（EPS） 

  + 每股收益：
    + 收益增长率G，就是每股收益EPS的增长率

  市盈率 约等于 市值 / 净收益——几年回本

  + PEG = PE / （G * 100）：越小说明股价越被低估，

+ 策略：
  + 计算股票池中所有泵顺从的PEG指标
  + 选择PEG最小的N只股票调仓
  + 注意：顾虑掉市盈率或收益增长率为负的股票

```python
def initialize(context):
    g.security = get_index_stocks('0003000.XSHG')
    g.N = 20
    g.q = query(valuation.code, valuation.pe_ratio, indicator.inc_net_profit_year_on_year).filter(valuation.code._in(...))
    
    run_monthly(handle, 1) # 一月一调仓
    
def handle(context):
    
    df = get_fundamentals(g.q)
    df = df[(df['pe_ratio'] > 0) &  (df['inc_net....'] > 0)]
    df['peg'] = df['短'] / (df['长'] * 100)
    
    df = df.sort(columns = 'peg')
    to_hold = df['code'][:g.N].values # 没有value则是Series。value后是list
    
    # 那么所有不在这里的持仓的股票都要卖出去
    for stock in context.portfolio.position:
        if stock not in to_hold:
            order_target(stock, 0)

	to_buy = [stock for stock in to_hold if stock not in context.portfolio.positions] # 在to_hold找到没有持仓的股票
    
    if len(to_buy) > 0:
	    cash_per_stock = context.portfolio.available_cash / len(to_buy)
        for stock in to_buy:
            order_value(stock, cash_per_stock)
```



# 动量策略和反转策略

+ 动量策略：如果某只股票在前一段时间表现较好，那么下一段时期该股票仍将有良好表现
+ 反转策略：如果某只股票在前一段时期表现不好，那么下一段时期该股票将会反转，即表现变好



+ 策略：相当于在股票池中收益最大最小的股票

```python
def initialize(context):
    g.benchmark = '000300.XSHG'
    g.N = 10
    
    
    run_monthly(handle, 1) # 一月一调仓
    
def handle(context):
    
    stocks = get_index_stocks(g.benchmark)
    
    df_close = history(30, field = 'close', security_list=list(stoacks)).T # 一堆股票好多天的收益率
    # 这与这里转置了
    df_close['ret'] = (df_close.iloc[:, -1] - df_close.iloc[:, 0]) / df_close.iloc[:, 0]  # 30天前减去今天再除以今天
    
    sorted_stacks = df_close.sort('ret', ascending = False).index.values
    # 收益从大到小选择，选最好的就是动量策略
    
    
    to_hold = sor...[ : g.N]
    
    后面是操作
```

+ `history`：可以选多只股票





# 猴子交易法则



+ 起始时随机买入N只股票，每天卖掉收益率最差的M只，在随机买入剩余股票池的M只——随机选股、周期调仓
+ 改进：应用反转策略：买入历史收益率最低的N只股票，调仓日留下反转程度大的股票，卖掉表现最长的M只股票，再买入收益率最低的M只股票

```python
def initialize(contest):
    set_be
    
    g.security = get_index_stocks('..')
    g.period = 30
    g.N
    g.change = 1  # 每次调整的
    g.init = True # 是否第一次执行
    
def get_sorted_stocks(context, stocks):
    df = hitsory(g.period, filed = 'close', security_list=stocks).T
    
    df_close = history(30, field = 'close', security_list=list(stoacks)).T # 一堆股票好多天的收益率
    # 这与这里转置了
    df_close['ret'] = (df_close.iloc[:, -1] - df_close.iloc[:, 0]) / df_close.iloc[:, 0]  # 30天前减去今天再除以今天
    
    sorted_stacks = df_close.sort('ret', ascending = False).index.values
    return sort_sta



def handle(context):
    if g.init:
        stocks = get_sorted_stocks(context, g.security)[: g.N]
        cash = con..._cash * 0.9 / len(stocks) # 平均分
        for stock in stocks:
            order_value(stock, cash)
        g.init = False
        return 
    # 上面是第一次执行，下次是调仓
    stocks = get_sorted_stocks()
    
    for stock in stocks[-g.change : ]:
        order_target(stock, 0)
    stocks = get_sorted_stocks(cons..)
    
    
    for stock in sotcks:
        if len(,,,position) >+ g.N:
            break
         if stock not in ..post:
            买入
    
```

