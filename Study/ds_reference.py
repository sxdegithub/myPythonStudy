# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx

print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist只是指向同一对象的另一种名字
mylist = shoplist

# 使用mylist删除apple
# 打印shoplist完整内容后删除索引0
# 制作副本的时候必须使用切片操作,这样副本内容才不会影响引用的对象
mylist2 = shoplist[:]
print('完整的shoplist切片内容:', shoplist[:])
del shoplist[0]
print('删除索0后的shoplist is', shoplist)
print('mylist is', mylist)
print('副本mylist2 is', mylist2)
