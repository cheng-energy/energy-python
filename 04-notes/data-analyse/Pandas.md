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



## 数据的查询，选择与过滤

![数据查看1](https://raw.githubusercontent.com/cheng-energy/energy-python/refs/heads/main/images/%E6%95%B0%E6%8D%AE%E6%9F%A5%E7%9C%8B.png)


![数据查看2](https://raw.githubusercontent.com/cheng-energy/energy-python/refs/heads/main/images/%E6%95%B0%E6%8D%AE%E6%9F%A5%E8%AF%A22.png)

![数据过滤](https://raw.githubusercontent.com/cheng-energy/energy-python/refs/heads/main/images/%E6%95%B0%E6%8D%AE%E8%BF%87%E6%BB%A4.png)






## 数据的清洗
- 处理缺失值，重复值，统一数据结构，异常值
`pd.set_option('文件路径'，30)--默认读取前30行`

```py
df.isnull()-----查看是否是缺失值
    df.dropna()----删除缺失值（删除整行数据）
    df.dropna(Aiis = 1)----删除缺失值所在的列。这个有一个返回值，会将删除之后的结果=给新的变量
    df.fillna()----填充缺失值
    df.ffill()----使用上一行的数据填充
    df.bfill()-----使用下一行的数据填充
df.duplicated()----查看重复值，直接调用是判断所有的列的数据都一样才认为是重复-可以点击源码查看参数，例如subset='A'就是基于A这个列来判断
    df.duplicated(subset='A'，keep=first)-----删除重复值,保留第一个重复的数据（默认是第一个），False是不保留
#异常值的处理（如销售数量出现负数）
# 查看异常值（条件过滤）
df[df['A']<0]
    df.drop(df[df['A']<0].index)----删除异常值
    df['A'] = df.['A'].abs()-----修复异常值，A列数据全取绝对值
#数据格式处理-例如日期格式不匹配
df['B'] = df['B'].replace('错误的格式数据','修改格式后的数据')----修改单个数据
df['B'] = df['B'].str.replace('/','-')----这个str是相当于原始字符串操作的访问器，然后使用replace把那一列所有数据的/改成-达到统一数据格式的目的



















