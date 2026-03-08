# python的语法3
## 函数部分
### 函数的定义
```python
def 函数名称（函数参数）
    函数体代码
    return <返回值>
```
案例
```python
# 计算n的阶乘
def fact(n):
    s = 1
    for i in range(1,n+1):
        s *= 1
    return s
```
定义中的参数n计算占位符
### 函数的使用和调用过程
- 调用时给出实际参数，使用实际参数替换定义中的占位参数，调用后就会得到返回值
案例
```python
# 计算n的阶乘
def fact(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s
a = fact(10)
print(a)
```












