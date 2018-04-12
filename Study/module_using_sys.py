# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
import sys
from math import sqrt

print("The command line arguments are:")
for i in sys.argv:
    print(i)
# 运行的脚本module_using_sys.py总是位于参数中的第一位
# 所以共有4个参数
print(sys.argv.__len__())
print("\n\nThe PYTHONPATH is ", sys.path, "\n")
j = 1
for i in sys.path:
    print(i, j)

print('Square root of 16 is:{0:.2f}'.format(sqrt(25)))
