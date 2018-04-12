# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

# Indexing or 'Subscription' operation
# 索引或下标(Subscription) 操作符
print('Item 0 is ', shoplist[0])
print('Item -1 is ', shoplist[-1])
print('Item -4 is ', shoplist[-4])

# slicing on a list
print('Item 1 to 3 is ', shoplist[1:5])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])
print('Item  to -1 is', shoplist[:-1])

print('步进为1', shoplist[::1])
print('步进为2', shoplist[::2])
print('步进为-2', shoplist[::-2])

# slicing on a string
print('characters 1 to 3 is ', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])

print('characters -1 to 1 is', name[-1:1])
print('characters start to end is ', name[:])
