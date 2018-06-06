# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
import math
from operator import mod

# 取模
# age =20
# print(age >19 and age <33)
# print(-5 / 2)
#
# print(5 % 2)
# print(-5 % 2)
# print(5 % -2)
# print(-5 % -2)
#
# print(mod(5,2))
# print(mod(-5,2))
# print(mod(5,-2))
# print(mod(-5,-2))

# 切片，只能从前往后顺序切（一般情况下切片的下标，前面的下标小，后面的大），倒数第一个是下标-1
listTest = [0, 1, 2, 3, 4, 5, 6]
listTest_B = [7, 8]
print(listTest[0:2])
print(listTest[-2:])
print(listTest[-5:-1:2])

print(listTest[-1:])

# 反转
# listTest.reverse()
# print(listTest)

# 切片反转
# print(listTest[6:1:-1])
# print(listTest[::-1][0:5])

# 更新列表
# listTest[0]='a'
# print(listTest)

# 删除元素
# del listTest[0]
# print(listTest)

# 列表基本操作符
# 长度
print(len(listTest))
# 相加
print(listTest + listTest_B)
# 乘法
print(listTest * 2)
# 判断元素是否存在
print(2 in listTest)
# 迭代器遍历
print([x + 10 for x in listTest])

# for x in listTest:
#     print(x)


# 生成器a，这个只是还是不太懂，多学
a = (x for x in listTest)
print(a.__next__())
print(a.__next__())

# Python列表函数&方法
# 最大值
print(max(listTest))
# 最小值
print(min(listTest))
# 将元组转换为列表
tup = (1, 2, 3)
print(type(list(tup)), list(tup))
print(type(tup), tup)
print(type(tup)), str(tup)

# 其他方法
# 追加
listTest.append(999)
print(listTest)

# 统计某个元素出现的次数
listTest = [0, 1, 2, 3, 4, 5, 6]
print(listTest.count(2))

# 查看元素中某个值第一次出现的位置
listTest = [0, 1, 2, 3, 4, 5, 6]
print(listTest.index(2))

# 插入元素list.insert(index,obj)
listTest = [0, 1, 2, 3, 4, 5, 6]
print(listTest)
print(listTest.insert(2, 22))
print(listTest)

# 移除列表中的一个元素，并返回元素值
# list.pop([index=-1])
listTest = [0, 1, 2, 3, 4, 5, 6]
print(listTest.pop(1))
print(listTest)

# 移除列表中某个值的第一个匹配项
listTest = [0, 1, 2, 3, 4, 5, 6]
listTest.remove(6)
print(listTest)

# 反转
# list.reverse()
listTest = [0, 1, 2, 3, 4, 5, 6]
listTest.reverse()
print(listTest)

# 列表排序
# list.sort()这个方法会修改list本身

# 推荐使用sorted(list)方法
# 该方法对可迭代序列都生效
print('列表排序')
listTest = [0, 3, 1, 3, 4, 5, 6]
print('sorted(list)',sorted(listTest))
# https://blog.csdn.net/jb19900111/article/details/50649932
# 2）key参数/函数
print('key参数/函数',sorted("This is a test string from Andrew".split(), key=str.lower))
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']

# list.clear()，清空列表
listTest = [0, 1, 2, 3, 4, 5, 6]
listTest.clear()
print(listTest)
# list.copy()，复制
listTest = [0, 1, 2, 3, 4, 5, 6]
listTest_C =listTest.copy()
print(listTest_C)