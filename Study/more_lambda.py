# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
# key值选定特定对象来作为排序基础
# 这里选定了ponts列表中的y的值
# i是对points列表进行遍历
points.sort(key=lambda i: i['y'])
print(points)

# 列表中元祖,lambda实验2
points_list = [('sx12', 12, 'male'), ('sx18', 18, 'male'), ('sx10', 10, 'male')]
points_list.sort(key=lambda i: i[1])
print(points_list)
