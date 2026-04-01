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












### 线条的格式等还可以使用命行来控制
- color = 某个值来控制颜色 
- linestyle   线条风格
- marker    标记风格
- markerfacecolor   标记的颜色
- marksize    标记的尺寸

## pyplot的中文显示
- 正常如果直接输入中文是无法实现显示中文的，pyplot提供了其他的方式来实现中文的显示（两种方法）
### 一.使用rcParams修改字体来实现（全局字体的改变）
- matplotlib.rcParams 【'font.family'】 = 'SimHei'    黑体（【】应该是英文状态的列表符号）
- 接下来使用方式类似
1. 【'font.family'】 ---显示字体的名称
2. 【'font.style'】 ---字体的风格（italic是斜体）
3. 【'font.size'】 ---指定字体的大小或者是‘large’和‘x-small’

常见字体的名称
1. Kaiti   楷体
2. LiSu   隶书
3. FangSong  仿宋
4. YouYuan  幼圆
5. STSong   宋体

### 中文字体显示的方法二（局部字体的改变）---推荐
- 在有中文输入的地方增加一个属性
- fontproperties = 'LiSu'  -- 字体名称
- fontsize = 20  -- 字体大小

例子：plt.ylabel('纵轴：数据'，fontproperties = 'LiSu'，fontsize = 20)
```python
import matplotlib.pyplot as plt
plt.subplot(3,2,1)
plt.plot([3,1,4,5,2])
plt.ylabel('超级数字',fontproperties='LiSu')
plt.subplot(326)
plt.plot([3,1,4,5,2],[1,2,3,4,5],'r--')
plt.ylabel('中文排版',fontproperties='FangSong',fontsize=20)
plt.axis([-1,10,0,6])
plt.savefig('绘图区域练习.png',dpi=1000)
plt.show()
```
![中文显示练习](https://raw.githubusercontent.com/cheng-energy/energy-python/refs/heads/main/images/%E4%B8%AD%E6%96%87%E6%98%BE%E7%A4%BA%E7%9A%84%E7%BB%83%E4%B9%A0.png)













## 文本显示函数
### 常用函数
- plt.xlabel()
- plt.ylabel()
- plt.title()-------图形文本的整体标题
- plt.text()--------任意位置文本
- plt.annotate()----图形中增加带箭头的注解
- plt.annotate(s,xy=arow_crd,xytext=tet_crd,arrowprops=dict)
1. s----注解文字是什么
2. xy=arow_crd-----箭头位置
3. xytext=tet_crd------文本位置
4. arrowprops=dict-----字典类型定义箭头显示的一些属性
```python
import numpy as np
a = np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),)
plt.xlabel('横轴：时间',fontproperties='FangSong',fontsize=25,color='red')
plt.ylabel('纵轴：振幅',fontproperties='FangSong',fontsize=25,color='green')
plt.title('余弦波实例',fontproperties='LiSu',fontsize=30,color='blue')
plt.annotate(r'$\mu=100$',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.1,width=2))
plt.axis([-1,6,-2,2])
plt.grid(True)
plt.savefig('余弦波实例',dpi=1000)
plt.show()
# xy=(2,1)是箭头所在位置，xytext是文本所在位置，width是箭头宽度是2
# shrink=0.1 表示：箭头的起点（xytext 位置）和终点（xy 位置），都向箭头中心方向缩短「箭头总长度的 10%」
#还可以只控制箭头一端的缩短
arrowprops=dict(
    facecolor='black',
    width=2,
    shrinkA=0,    # 箭头尖端和目标点的距离（像素），设0就不缩尖端
    shrinkB=5     # 箭尾和文字的距离（像素），设5就只剪尾)
```
![](https://raw.githubusercontent.com/cheng-energy/energy-python/refs/heads/main/images/%E4%BD%99%E5%BC%A6%E6%B3%A2%E5%AE%9E%E4%BE%8B.png)















## pyplot的子绘图区域方法
- 前面虽然有绘图区域的介绍subplot，但是那个绘图区域是被规整划分的，无法做到随心所欲。例如绘制下方这个子绘图区域无法做到

![](https://raw.githubusercontent.com/cheng-energy/energy-python/refs/heads/main/images/%E8%AE%BE%E8%AE%A1%E5%AD%90%E7%BB%98%E5%9B%BE%E5%8C%BA%E5%9F%9F.png)






- 接下来介绍一个方法subplot2grid（GridSpace，CurSpec，colspan=1，rowspan=1）

理念：设定网格，选中网格，缺点选中行列区域数量，编号从0开始





















