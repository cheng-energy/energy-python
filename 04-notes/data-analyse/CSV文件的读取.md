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
```python
import numpy as np
a = np.arange(100).reshape(5,20)
np.savetxt('a.csv',a,fmt='%d',delimiter=',')
c = np.loadtxt('a.csv',dtype=np.int64,delimiter=',')
c
```

## 局限性
- 只能有效读取一维和二维数据

# 多维数据的读取
## .tofile和.fromfile
- a.tofile（frame,sep,format='%s'
1. frame:文件，字符串
2. sep:数据分割字符串，如果是空串，写入文件是二进制
3. format:写入数据的格式
```python
a = np.arange(60).reshape(12,5)
a.tofile('b.dat',format='%d')  #没有指定sep，这个文件是一个二进制的文件，文本编译器看不懂
#不过二进制文件占据内存更小，可以做为储存备份数据的一种方式
```
这样写入的数据没有任何的维度信息，他只是把数据逐一列出写入文件
- np.fromfile(drame,dtype=float,count=-1,sep='')
1. dtype是读取数据的格式
2. count是读入元素的个数，默认是-1，-1就是读入所有的元素
```python
a = np.arange(60).reshape(12,5)
a.tofile('b.dat',format='%d',sep=',')
c = np.fromfile('b.dat',dtype=np.float64,sep=',').reshape(12,5)
c
```
使用这种方式读取数据必须知道原本数据读入文件时的维度信息，这样才能还原数据

写入方式	读取方式	是否匹配	结果
tofile(sep=' ', format='%d')（文本）	fromfile(sep='', dtype=np.float64)（二进制）	❌ 不匹配	乱码

tofile()（二进制）	fromfile(dtype=np.int64, sep='')（二进制）	✅ 匹配	正常

tofile(sep=' ', format='%d')（文本）	fromfile(dtype=np.int64, sep=' ')（文本）	✅ 匹配	正常






























