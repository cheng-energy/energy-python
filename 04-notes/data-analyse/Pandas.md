# Pandas学习
## 利用pandas读取文件
### 读取csv文件
- pandas.read_csv(filepath,sep=',',usecols)
1. filepath 是文件路径
2. sep 是分隔符，csv默认是使用逗号分隔的
3. usecols 是指定读取的列明，列表的形式
- to_csv---把处理后的数据写入文件
```py
# 数据的读取与写入
import pandas as pd
from altair import to_csv

#数据的读入
df = pd.read_csv("D:\\BaiduNetdiskDownload\\数据分析\\sales.csv",usecols=['订单号','销售数量','单价','订单日期'])
# 数据处理
df['销售总额'] = df['单价']*df['销售数量']
# 数据写入
df.to_csv('D:/python/CODE/ST/数据存放/电影数据1')
```



## 数据的读取与写入
- 官网：https://pandas.pydata.org
### DateFrame
- 创建方法多样



































