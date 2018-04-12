# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
def powersum(power, *args):
    """return the sum of each argument raised to the specified power"""
    total = 0
    for i in args:
        total += pow(i, power)
    print(total)
    return total


powersum(2, 3, 4)
