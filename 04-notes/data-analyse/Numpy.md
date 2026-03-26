# 数据的维度
维度：一组数据的组织形式（一维展开，二维展开等等），数据之间形成某种特定含义，表达某种关系
## 维度
- 一维数据：由一组对等关系的有序或无序数据组成（可以使用列表，集合等来表示）
- 二维数据：由多个一维数据形成（可以由多维列表来表示，就是列表里面套列表）
- 多维数据：与二维数据类似（使用多维列表表示）
- 高维数据：使用键值对的形式来表示，可以用字典或者国际公认的数据表示形式

PS：一维数据还可以用数组表示，数组就是说列表中的数据类型相同

# Numpy库(数据分析的基本库）----ndarray
- Numpy底层的计算是由C语言实现，所以计算速度非常ok
- ndarray；多维数组对象

## ndarray的创建和变换
### ndarray的创建
1. 从python的列表元组来创建ndarray数组
```python
x = np.array(list/tuple)
x = np.array(list/tuple,dtype=np.float32)  # 可以根据dtype来指定数据类型
当没有指定数据頛时，numpy会自动根据情况来关联数据类型，例如都是整数则会创建整数类型
```
2. 使用numpy提供的创建函数
```python
np.range(n)    #类似range函数返回ndarry类型，范围从0到n-1
np.ones(shape)  #根据shape生成一个全是1的数组，shape是元组类型
np.zeros(shape)  #根据shape生成一个全是0的数组shape是元组类型
np.full(shape,val)  #根据shape生成一个数组，每个元素值是val
np。eye(n)  #创建一个n*n的单位矩阵，对角线为1其他为0
```




























