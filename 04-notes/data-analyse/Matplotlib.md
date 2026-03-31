# Matplotlib库的介绍
- Matplotlib是python可视化分析的优秀库，内部可视化模块分成了很多类
- 直接使用.pyplot这个命令字库就可以使用所有可视化的类
```pythonimport matplotlib.pyplot as plt
plt.plot([3,1,4,5,2])    #plt.plot如果传入的是一维数组的话会被直接做为y轴数据处理
plt.ylabel('some numbers')  # 注意如果想显示中文需要额外操作，后续介绍
plt.savefig('plot.png',dpi=1000) # 这个是保存生成的图片，单引号里面是文件名字，dpi是指一英寸空间有多少个像素点
plt.show()
```

![演示生成图](https://github.com/cheng-energy/energy-python/blob/main/images/plot.png?raw=true)


















- 如果输入的是两个列表，
```python
import matplotlib.pyplot as plt
plt.plot([3,1,4,5,2],[1,2,3,4,5],'r--')  #默认是第一个数据是x轴第二个是y轴
plt.ylabel('some numbers')
plt.axis([-1,10,0,6])  #意思是x轴从-1到10，y轴从0到6。axis的具体参数后面学习
plt.savefig('plot.png',dpi=1000)
plt.show()
```
![给出两个列表的示例](https://raw.githubusercontent.com/cheng-energy/energy-python/refs/heads/main/images/plot1.png)




















- pypiot的绘图区域，使用plt.subplot(nrows,ncols,plt_number)
- nrows是横行有几个部分，ncols是纵向有几列，plt_number是当前绘图区域是几行
- 接下来尝试把上面两个图放在一个画布的不同绘图区域，例如划分6个区域把两个图片放在1和6子区域上
```python
plt.subplot(3,2,1)
plt.plot([3,1,4,5,2])    
plt.ylabel('some numbers')  
plt.subplot(326)   #中间的逗号是可以省略的
plt.plot([3,1,4,5,2],[1,2,3,4,5],'r--')
plt.ylabel('some numbers')
plt.axis([-1,10,0,6])
plt.savefig('绘图区域练习.png',dpi=1000)
plt.show()
```
![绘图区域小练习](https://raw.githubusercontent.com/cheng-energy/energy-python/refs/heads/main/images/%E7%BB%98%E5%9B%BE%E5%8C%BA%E5%9F%9F%E7%BB%83%E4%B9%A0.png)















## pyplot的plot函数
- plt.plot(x,y,'format-string',**kwargs)
1. x和y是列表或者数组
2. format—string是控制曲线格式的字符串
3. **kwsrgs是同时绘制多条曲线（重复上面参数），注意每条曲线的x是不可以忽略的
4. 若是绘制一条曲线可以忽略x轴参数

### format-string
#### 字体颜色
- 'b'---蓝色
- 'g'---绿色
- 'r'---红色
- 'c'---青绿色
- 'm'---洋红色
- 'y'---黄色
- 'k'---黑色
- 'w'---白色
- '#008000'---RGB某个颜色色
- '0.8'---灰度之字符串

如果不主动选择颜色，系统会自动为曲线选择不同的颜色
#### 线条样式
- 'r'---实线
- '--'---破折线
- '-.'---点画线
- ' '---无线条（中间是空格）
- ':'---虚线
#### 数据点的标记字符
![标记字符](https://raw.githubusercontent.com/cheng-energy/energy-python/refs/heads/main/images/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202026-03-31%20215120.png)













