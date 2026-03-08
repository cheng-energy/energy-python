# 面向对象编程
### 定义一个类描述数字时钟，提供走字和显示时间的功能。
```python
'''定义一个类描述数字时钟，提供走字和显示时间的功能。'''
import time
#先创建一个类
class newtime:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def run(self):
        #走字
        self.second +=1
        if self.second == 60:
            self.second = 0
            self.minute+=1
            if self.minute == 60:
                self.minute = 0
                self.hour+=1
                if self.hour == 24:
                    self.hour = 0
                    self.minute = 0
                    self.second = 0
    def show(self):
        print(f'记录的时间长度为{self.hour}时{self.minute}分{self.second}秒')
# 创建时钟对象
clock = newtime(23, 59, 58)
while True:
    # 给时钟对象发消息读取时间
    clock.show()
    # 休眠2秒钟
    time.sleep(2)
    # 给时钟对象发消息使其走字
    clock.run()
```
编写时出现的问题
- 英语单词问题，minute总是写成mintue，其实就是变量命名的问题，额，最好还是不用拼音命名
- 对于面向对象编程不熟悉，比如循环部分`if self.hour == 24:`，总是会打成hour == 34，感觉就是自己头脑中对于各部分发要填写的结构不清楚，多写就好
- 还有就是类创建完成以后不知道做什么，依旧是不够熟练的问题
- clock.show之前写的是print（clock.show），因为show函数已经有print，之前的写法是无意义的嵌套，导致打印出的部分出现None就是print() 函数会打印「括号内表达式的返回值」，而你的 show() 方法没有显式返回值（就是没有写return），Python 会默认返回 None，如果说在定义show函数的最后增加了return就不会返回None而是输出return后面跟着的内容，如果return后面是1，就会打印1，如果将定义函数时那个格式化的字符串print(f'记录的时间长度为{self.hour}时{self.minute}分{self.second}秒')去掉print，把字符串部分赋值给B，return B 就会返回那个时间
- 之前循环部分代码如下
```python
 if self.second == 60:
            self.second == 0
            self.minute+=1
            if self.minute == 60:
                self.minute = 0
                self.hour+=1
                if self.hour == 24:
                    self.hour = 0
                    self.minute = 0
                    self.second = 0
  ```
第二行self.second重新赋值的时候使用了==，导致秒数到 60 后无法重置为 0，分钟也不会正常累加。这就是大问题，解释如下
## ==是比较运算符并不会改变变量的值，他是用来进行布尔运算，判断左右两侧是否相等
- 没有限制初始化时分秒的值，用户调用对象时可以输入一些非法值，例如60秒25小时等
- 显示不规范，时钟显示应该是两位数补零（比如 8 时 9 分 5 秒应显示为 08:09:05），而不是直接显示原始数字。  好像这个问题我意识到也不会操作，这是字符串格式化的内容，这个非常有必要多多补充一些
- 



















