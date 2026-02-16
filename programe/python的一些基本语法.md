# 列表中的一些语法和注意
- index('元素')可以查找该元素所在的位置，如果元素不存在会报错
- count('元素')会计算该元素在列表中出现的次数
- sort()可以实现列表的重新排序，reverse可以实现列表的逆向
## 列表的生成式
- 例如
  创建一个取值范围在1到99且能被3或者5整除的数字构成的列表
```python
items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)
```
- 有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
```python
nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)
```
- 有一个整数列表nums1，创建一个新的列表nums2，将nums1中大于50的元素放到nums2中
```python
nums1 = [35, 12, 97, 64, 55]
nums2 = [num for num in nums1 if num > 50]
print(nums2)
```
## 嵌套列表（可表示矩阵）
- 保存5个学生3门课程的成绩，可以用如下所示的列表
```python
import random
scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)
```
---
- 上面的代码[random.randrange(60, 101) for _ in range(3)] 可以产生由3个随机整数构成的列表，我们把这段代码又放在了另一个列表生成式中作为列表的元素，这样的元素一共生成5个，最终得到了一个嵌套列表。
- 代码for循环中的range中的3是说代码循环3次不是范围从0到3
---
# random库的学习
- 建议直接在标准库里面看不常用的
- 常用的：
- randim.random()随机生成0到1之间的浮点数
- random.randint(a,b)生成从a到b的随机整数（左右都是闭区间）
- random.randrange(a,b,c)生成从a到b的随机整数（左右都是闭区间,c是步长）
- random.choice(sequence)从sequence中随机抽取一个元素，sequence可以是列表，元组等
- random.shuffle(sequence)随机打乱列表的顺序，原列表发生变化

## 元组的相关知识
- 与列表类似，使用（）表示元组，元组是不可变的
- 下面是从洛昊老师那里复制的
```python
  # 定义一个三元组
t1 = (35, 12, 98)
# 定义一个四元组
t2 = ('骆昊', 45, True, '四川成都')

# 查看变量的类型
print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>

# 查看元组中元素的数量
print(len(t1))  # 3
print(len(t2))  # 4

# 索引运算
print(t1[0])    # 35
print(t1[2])    # 98
print(t2[-1])   # 四川成都

# 切片运算
print(t2[:2])   # ('骆昊', 45)
print(t2[::3])  # ('骆昊', '四川成都')

# 循环遍历元组中的元素
for elem in t1:
    print(elem)

# 成员运算
print(12 in t1)         # True
print(99 in t1)         # False
print('Hao' not in t2)  # True

# 拼接运算
t3 = t1 + t2
print(t3)  # (35, 12, 98, '骆昊', 45, True, '四川成都')

# 比较运算
print(t1 == t3)            # False
print(t1 >= t3)            # False
print(t1 <= (35, 11, 99))  # False
```
- 如果一个元组中只有一个元素，需要加上一个逗号，否则就不是元组，知识改变代码优先级的括号
### 打包和解包的操作
- 当我们把多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型；当我们把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量
```python
# 打包操作
a = 1, 10, 100
print(type(a))  # <class 'tuple'>
print(a)        # (1, 10, 100)
# 解包操作
i, j, k = a
print(i, j, k)  # 1 10 100
```
- 解包时，如果解包元素个数和变量个数不一样会报错
- 使用星号表达式可以解决上面问题，可以让一个变量接收多个值
```python
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)        # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)        # 1 [10, 100] 1000
*i, j, k = a
print(i, j, k)        # [1, 10] 100 1000
*i, j = a
print(i, j)           # [1, 10, 100] 1000
i, *j = a
print(i, j)           # 1 [10, 100, 1000]
i, j, k, *l = a
print(i, j, k, l)     # 1 10 100 [1000]
i, j, k, l, *m = a
print(i, j, k, l, m)  # 1 10 100 1000 []
```
- 需要注意两点：首先，用星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素；其次，在解包语法中，星号表达式只能出现一次。
- 解包语法对所有的序列都成立，这就意味着我们之前讲的列表、range函数构造的范围序列甚至字符串都可以使用解包语法
---
## 集合（set）
- 使用{}创建，其中必须有一个元素，否则不是集合而是一个空字典，里面元素必须是可哈希的，即可变类型不可放入集合，例如列表，集合都不可以放入集合。使用无法创建嵌套集合
- 集合有无序性，所以不可以使用索引进行遍历
### 集合的运算
```python
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print(set1 & set2)                      # {2, 4, 6}
print(set1.intersection(set2))          # {2, 4, 6}

# 并集
print(set1 | set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 10}

# 差集
print(set1 - set2)                      # {1, 3, 5, 7}
print(set1.difference(set2))            # {1, 3, 5, 7}

# 对称差
print(set1 ^ set2)                      # {1, 3, 5, 7, 8, 10}
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}
```
- 还可以使用！=和==判断集合是否相等，<和>等符号来判断子集等
### 集合的方法
```python
set1 = {1, 10, 100}

# 添加元素
set1.add(1000)
set1.add(10000)
print(set1)  # {1, 100, 1000, 10, 10000}

# 删除元素
set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)  # {1, 1000, 10000}

# 清空元素
set1.clear()
print(set1)  # set()
```
- 因为remove在元素不存在时会报错，所以先判断元素是否存在
- 集合类型还有一个名为isdisjoint的方法可以判断两个集合有没有相同的元素，如果没有相同元素，该方法返回True，否则该方法返回False，代码如下所示。
```python
set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True
```
- python 中还有一种不可变类型的集合，名字叫frozenset。set跟frozenset的区别就如同list跟tuple的区别，frozenset由于是不可变类型，能够计算出哈希码，因此它可以作为set中的元素。除了不能添加和删除元素，frozenset在其他方面跟set是一样的，下面的代码简单的展示了frozenset的用法
```python
fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1 & fset2)  # frozenset({1, 3, 5})
print(fset1 | fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1 - fset2)  # frozenset({7})
print(fset1 < fset2)  # False
```
## 字典
### 字典的创建
- 一种就是直接{}写
- 另一种就是
```python
# dict函数(构造器)中的每一组参数就是字典中的一组键值对
person = dict(name='王大锤', age=55, height=168, weight=60, addr='成都市武侯区科华北路62号1栋101')
print(person)  # {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}

# 可以通过Python内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

# 用字典生成式语法创建字典
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
```
### 字典的方法
- get方法获取值
```python
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.get('name'))       # 王大锤
print(person.get('sex'))        # None
print(person.get('sex', True))  # True
```
- keys等方法获取所有的键
```python
person = {'name': '王大锤', 'age': 25, 'height': 178}
print(person.keys())    # dict_keys(['name', 'age', 'height'])
print(person.values())  # dict_values(['王大锤', 25, 178])
print(person.items())   # dict_items([('name', '王大锤'), ('age', 25), ('height', 178)])
for key, value in person.items():
    print(f'{key}:\t{value}')
```
- update合并两个字典
```python
person1 = {'name': '王大锤', 'age': 55, 'height': 178}
person2 = {'age': 25, 'addr': '成都市武侯区科华北路62号1栋101'}
person1.update(person2)
print(person1)  # {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
```
- 可以通过pop或popitem方法从字典中删除元素，前者会返回（获得）键对应的值，但是如果字典中不存在指定的键，会引发KeyError错误；后者在删除元素时，会返回（获得）键和值组成的二元组。字典的clear方法会清空字典中所有的键值对，代码如下所示
```python
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.pop('age'))  # 25
print(person)             # {'name': '王大锤', 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.popitem())   # ('addr', '成都市武侯区科华北路62号1栋101')
print(person)             # {'name': '王大锤', 'height': 178}
person.clear()
print(person)             # {}
```
- 跟列表一样，从字典中删除元素也可以使用del关键字，在删除元素的时候如果指定的键索引不到对应的值，一样会引发KeyError错误，具体的做法如下所示。
```python
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
del person['age']
del person['addr']
print(person)  # {'name': '王大锤', 'height': 178}
```
