# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# 关键字参数

def func(a, b, c=10):
    print("a is", a, "and b is ", b, "and c is", c)
    # print("a is"+a+"and b is ")


func(3, 7)
func(25, 1, c=1)
func(11, 10, c=11)
