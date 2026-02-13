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
- 上面的代码[random.randrange(60, 101) for _ in range(3)] 可以产生由3个随机整数构成的列表，我们把这段代码又放在了另一个列表生成式中作为列表的元素，这样的元素一共生成5个，最终得到了一个嵌套列表。
