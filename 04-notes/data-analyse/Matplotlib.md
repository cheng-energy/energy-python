# Matplotlib库的介绍
- Matplotlib是python可视化分析的优秀库，内部可视化模块分成了很多类
- 直接使用.pyplot这个命令字库就可以使用所有可视化的类
```pythonimport matplotlib.pyplot as plt
plt.plot([3,1,4,5,2])    #plt.plot如果传入的是一维数组的话会被直接做为y轴数据处理
plt.ylabel('some numbers')  # 注意如果想显示中文需要额外操作，后续介绍
plt.savefig('plot.png',dpi=1000) # 这个是保存生成的图片，单引号里面是文件名字，dpi是指一英寸空间有多少个像素点
plt.show()
```
生成的图片如下
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




































