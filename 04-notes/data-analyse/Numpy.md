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
np.ones(shape)  #根据shape生成一个全是1的数组，shape是元组类型shape就是指几行几列   #np.ones((3,6))生成3行6列全是1的数组
np.zeros(shape)  #根据shape生成一个全是0的数组shape是元组类型
np.full(shape,value)  #根据shape生成一个数组，每个元素值是value(value是给定的）
np.eye(n)  #创建一个n*n的单位矩阵，对角线为1其他为0
```
不指定类型情况下，只有np.range是返回整数类型，其他都是浮点数

x.shape可以返回数组x的形状是几行几列（要先把数组赋值给x）
```python
np.ones_like(a)   #根据数组a的形状生成全是1的数组
np.zeros_like(a)
np.full_like(a，val)
```
3. 使用numpy中其他函数生成数组
```python
np.linspace()  #根据起止数据等间距的填充数据，形成数组
np.concatenate()  #将两个或者多个数组合并成新的数组
---
np.linspace(1,100,20)  #第一个元素是1最后一个是100，生成20个元素，不指定数据类型时都是浮点数
np.linspace(1,10,10,endpoint=False) #这个endpoint的意思是表示最后一个数是否是指定的终止数，在这个例子中是说最后一个数是否是10
np.concatenate((a,b))  #np.concatenate([a,b])  或者这个
```
- numpy中除了np.range（）以外生成的数据类型都是浮点数（不指定的情况下），因为实际的应用中很难刚好获得整数

### ndarray数组的变换（维度变换和元素类型变换）
#### 维度变换
```python
# 先创建一个数组
a = np.array([1,2,3,4,5,,6,7,8,9,10])
a.reshape((5,2))  #不改变数组元素，但是如果元素个数与规定的新的形状不匹配会报错，原数组是不变的就是说a还是上面那个形状
a.resize(shape)   #这个会修改原来数组，a的形状会被改变
a.swapaxes(ax1,ax2)  #将数组n个维度中的两个维度调换
a.flatten()  #对数组降维，使它变成一维数组，原数组不变
```
#### 类型变换
```python
# 首先要有一个数组
b = a.astype(nem_type）  # 可以简写为int由程序自动识别是int32或者int64
# 他一定会创建新的数组，不改变原数组
# astype更像是一个元素的拷贝

# ndarry数组向列表的转化
ls = a.tolist()   
```























