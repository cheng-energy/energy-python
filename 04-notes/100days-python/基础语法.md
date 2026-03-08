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
---
## 函数部分
### 位置参数
- 例如
```python
def make_judgement(a, b, c):
    """判断三条边的长度能否构成三角形,可以返回True不可以返回False"""
    return a + b > c and b + c > a and a + c > b
```
上面make_judgement函数有三个参数，这种参数叫做位置参数，在调用函数时通常按照从左到右的顺序依次传入，而且传入参数的数量必须和定义函数时参数的数量相同
- 还可以通过变量名来控制输入的数字的位置，例如print(make_judgement(b=3,c=2,a=1),这样调用
- 强制位置参数可以使用/来设置，就是def make_judgement(a, b, c，/):   ，在调用这种函数时，不可以出现变量名（不可以像上一行一样调用）
### 关键字参数
- 命名关键字参数只能通过“参数名=参数值”的方式来传递和接收参数，大家可以看看下面的例子。
```python
# *后面的参数是命名关键字参数
def make_judgement(*, a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b


# 下面的代码会产生TypeError错误，错误信息提示“函数没有位置参数但却给了3个位置参数”
# TypeError: make_judgement() takes 0 positional arguments but 3 were given
# print(make_judgement(1, 2, 3))
```
好像就是   print(make_judgement(b=3,c=2,a=1)  只能像这样调用函数
---
### 函数的默认参数
- Python 中允许函数的参数拥有默认值例如
```python
def add(a=0, b=0, c=0):
    """三个数相加求和"""
    return a + b + c


# 调用add函数，没有传入参数，那么a、b、c都使用默认值0
print(add())         # 0
# 调用add函数，传入一个参数，该参数赋值给变量a, 变量b和c使用默认值0
print(add(1))        # 1
# 调用add函数，传入两个参数，分别赋值给变量a和b，变量c使用默认值0
print(add(1, 2))     # 3
# 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
print(add(1, 2, 3))  # 6
```
需要注意的是，带默认值的参数必须放在不带默认值的参数之后，否则将产生SyntaxError错误，错误消息是：non-default argument follows default argument，翻译成中文的意思是“没有默认值的参数放在了带默认值的参数后面”。
### 可变参数
- Python 语言中可以通过星号表达式语法让函数支持可变参数。所谓可变参数指的是在调用函数时，可以向函数传入0个或任意多个参数。将来我们以团队协作的方式开发商业项目时，很有可能要设计函数给其他人使用，但有的时候我们并不知道函数的调用者会向该函数传入多少个参数，这个时候可变参数就能派上用场。

- 下面的代码演示了如何使用可变位置参数实现对任意多个数求和的add函数，调用函数时传入的参数会保存到一个元组，通过对该元组的遍历，可以获取传入函数的参数。
```python
# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    total = 0
    # 对保存可变参数的元组进行循环遍历
    for val in args:
        # 对参数进行了类型检查（数值型的才能求和）
        if type(val) in (int, float):
            total += val
    return total


# 在调用add函数时可以传入0个或任意多个参数
print(add())         # 0
print(add(1))        # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, 'hello', 3.45, 6))  # 12.45
```
- 如果我们希望通过“参数名=参数值”的形式传入若干个参数，具体有多少个参数也是不确定的，我们还可以给函数添加可变关键字参数，把传入的关键字参数组装到一个字典中，代码如下所示。
```python
# 参数列表中的**kwargs可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)
```
---
### 用模块管理函数
- 不管用什么样的编程语言来写代码，给变量、函数起名字都是一个让人头疼的问题，因为我们会遇到命名冲突这种尴尬的情况。最简单的场景就是在同一个.py文件中定义了两个同名的函数，如下所示
```python
def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')

    
foo()  # 大家猜猜调用foo函数会输出什么
```
当然上面的这种情况我们很容易就能避免，但是如果项目是团队协作多人开发的时候，团队中可能有多个程序员都定义了名为foo的函数，这种情况下怎么解决命名冲突呢？答案其实很简单，Python 中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的函数，在使用函数的时候，我们通过import关键字导入指定的模块再使用完全限定名（模块名.函数名）的调用方式，就可以区分到底要使用的是哪个模块中的foo函数，代码如下所示。
- moudle1.py
```python
def foo():
    print('hello, world!')
```
- moudle2.py
```python
def foo():
    print('goodbye, world!')
```
- test.py
```python
import module1
import module2

# 用“模块名.函数名”的方式（完全限定名）调用函数，
module1.foo()  # hello, world!
module2.foo()  # goodbye, world!
```
在导入模块时，还可以使用as关键字对模块进行别名，这样我们可以使用更为简短的完全限定名(就是取小名，就是import pandas as pd)调用更方便
- 但是，如果我们如果从两个不同的模块中导入了同名的函数，后面导入的函数会替换掉之前的导入，就像下面的代码，调用foo会输出goodbye, world!，因为我们先导入了module1的foo，后导入了module2的foo 。如果两个from...import...反过来写，那就是另外一番光景了。
```python
from module1 import foo
from module2 import foo

foo()  # goodbye, world!
```
如果想在上面的代码中同时使用来自两个模块的foo函数还是有办法的，大家可能已经猜到了，还是用as关键字对导入的函数进行别名，代码如下所示。
```python
from module1 import foo as f1
from module2 import foo as f2

f1()  # hello, world!
f2()  # goodbye, world!
```
---
## 异常处理（raise和try-except）
#### raise，报告错误给使用者（抛出异常）
#### try-except
- try:
  使用某个功能模块
  except:
  捕获异常,可以参考下面这个代码
```python
  import random
real = random.randint(1,100)
account = 0
list1 =[]
while True:
    guess = input('请输入你猜测的数字（范围是1到100）：')
    if guess == 'q':
        break
    try:
        guess = int(guess)
        if not(1<=guess<=100):
            print('输入错误，请重新输入1到100之间的数')
            continue
    except ValueError:
        print('输入无效，请重新输入或者按q退出')
        continue
    account += 1
    list1.append(guess)
    if real == guess:
        print('恭喜你猜对了')
        break
    elif real > guess:
        print('猜小了')
    else:
        print('猜大了')
print(f'一共猜测了{account}次')
print(f'你猜测的记录是{list1}')
```

## 高阶函数
- 使用函数作为另外一个函数的参数和返回值

# 字符串格式化
## 三代的演变
- 远古时代：C的风格，使用%占位符
- 工业时代：使用.format的方法
- 现代标准：f-string

## 一，字符串格式化（远古时代）
- 基本语法：使用%来连接字符串和变量元组：“string”%{values}
- 案例：
```python
'''字符串格式化远古时代'''
name = 'python'
do = '学习'
version = 3.13
print('欢迎来到name的do')  #欢迎来到name的do
print('欢迎来到 %s的%s'%(name,do))
print('欢迎来到 %s %f的%s'%(name,version,do))  #欢迎来到 python 3.130000的学习
print('欢迎来到 %s %.2f的%s'%(name,version,do))   #欢迎来到 python 3.13的学习
```



## 二，字符串格式化（.format工业时代的方法）
- 字符串格式化使用.format（）方法，用法如下

<模板字符串>.format(<逗号分隔的参数>)

## 槽
- 使用{}表示，例如

‘{}：计算机{}的CPU占用率为{}%.format('2018-10-10','c',10)’

不指定的情况下，槽中会被括号中的内容依次（按照对应的顺序）填充

‘{1}：计算机{2}的CPU占用率为{0}%.format('2018-10-10','c',10)’
- 这样在槽中就可以指定填充的内容
- 其他的信息可以看自己的git账号



























