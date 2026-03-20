# 遍历循环（for <循环变量> in <遍历结构> 然后下一行缩进加语句块）
- 从遍历结构中取出数据赋值给循环变量然后用循环变量执行语句块（循环变量可有可无）
## 计数循环（N次和特定次）
N次计数循环如下：
```
for i in range(N):
    <语句块>
遍历的数字应该是：
0，1，2，3，4，......，N-1
```
这个是指执行语句块N次

特定次计数循环：

```
for i in range (N,M,K)
    <语句块>
范围从N到M（左闭右开区间），步长是K
```

## 字符串的遍历循环
```
#字符串的遍历循环并且以逗号分开
for i in "python":
    print(i,end=",")
```
## 列表的遍历循环
- 遍历结构是列表

## 文件的遍历循环
```
for i in fi
    print(i)
```
所谓的fi就是文件标识符
- 如果在python中以字符串形式打开一个文件，就有一个标识符，上面代码会逐行打印文件中的内容

## 还可对元组，列表，字典等进行遍历循环

## 无线循环（while循环）
- while <条件>：

      <语句块>
只要条件成立，语句块就会一直被执行


## 循环控制的保留字（break和continue）
- break：打破本层循环，继续执行后续代码块
- continue： 结束本次循环，继续下一次的循环

代码案例：
```python
a = 3
while a > 0:
    a -=1
    print(a)   #while循环
```
```python
#%%
s = 'python'
for i in s:
    if i =='h':
        continue
    print(i,end=',')         #p y t o n
```
使用遍历循环，如果i==h的时候，执行continue跳过这次循环进行下一次的循环。
```python
s = 'python'
while True:
    for i in s:
        if i =='h':
            break
        print(i,end=',')      # p y t p y t p y t ......p y t 
```
上面的代码，当i遍历s使得i的值是h的时候，break终止这一次的for循环（打破了这次的for循环，不在执行print函数，之后while循环继续循环）

循环的高级操作（与else的搭配）
- 就是在for循环和while循环后面加一个else语句，只有循环没有执行break时else后面的语句才会被执行。类似于使用try-except捕获异常时，在最后增加else语句，如果没有发生异常，则会奖励性执行else语句
```python
for i in 'python':
    if i =='h':
        continue
    print(i)
else:
    print('正常退出')
```



















