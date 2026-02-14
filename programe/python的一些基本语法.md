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
