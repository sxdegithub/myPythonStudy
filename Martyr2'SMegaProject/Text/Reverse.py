# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx

# 字符串切片反转
sStr = 'zxcvbnmnmafhj'

print("切片反转：" + sStr[::-1])

# 内置reversed（）函数反转
sList = list(reversed(sStr))
print("内置reversed（）函数反转后的列表:\n\t{}".format(sList))
sStr = ''.join(list(reversed(sStr)))
print("内置reversed（）函数反转后字符串:\n\t{}".format(sStr))
