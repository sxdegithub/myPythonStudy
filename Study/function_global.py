# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx

x = 50


def func():
    # 使用了global关键字后,改变的是全局变量x
    global x

    print("X is ", x)
    x = 2
    print("Changed global x to", x)


func()

print("Value of x is ", x)
