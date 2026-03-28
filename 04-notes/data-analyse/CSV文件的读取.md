# CSV文件的操作
## 向文件中写入CSV格式的数据
- np.savetxt(frame,array,fmt='%.18e',delimiter=None)
1. frame---文件，字符串或者产生器的名字，还可以是.gz和.bz2的压缩文件名字
2. array是指要存入文件的数组
3. fmt是指存入的数据的格式，默认是%.18e科学计数法的形式（表示和C语言类似）
4. delimiter是指数据之间分隔采用什么分隔，None是用空格分隔。但是CSV文件一般是用逗号分隔
```python
import numpy as np
a = np.arange(100).reshape(5,20)
np.savetxt('a.csv',a,fmt='%d',delimiter=',')  
```
产生器（yield）：处理超大文件和数据流，生成无限序列（如计数器，倒计时），节省内存提升性能

## 读取CSV文件
- np.loadtxt(frame,dtype=np.float,delimiter=None,unpack=False)
1. frame---指定读入文件的来源，可以是压缩文件
2. dtype---指定读入文件的类型（默认是浮点数），获取整数时最好写np.int64
3. delimiter---分隔字符串
4. unpack---默认是False如果是True读入的属性将写入不同的变量

## 局限性
- 只能有效读取一维和二维数据





