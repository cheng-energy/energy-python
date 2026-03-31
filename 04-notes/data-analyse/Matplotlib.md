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
![演示生成图](https://github.com/cheng-energy/energy-python/blob/main/images/plot.png)
