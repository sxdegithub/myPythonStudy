# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# 只有那些位于参数列表末尾的参数才能被赋予默认参数值，
# 意即在函数的参数列表中拥有默认参数值的参数不能位于没有默认参数值的参数之前
def say(messages, times=1):
    print(messages * times)


say('hello')
say('hello', 4)
