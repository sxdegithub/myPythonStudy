# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo are', len(new_zoo))

print('Number of animals in new_zoo is', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[len(new_zoo) - 1][len(new_zoo) - 1])
print('Number of animals in the new zoo are', len(new_zoo) - 1 + len(new_zoo[2]))

# 只有唯一一个元素的元组,在第一个元素后面必须加一个逗号
# ex:
singleItemTuple = (3,)
print(singleItemTuple[0])
print(len(singleItemTuple))
