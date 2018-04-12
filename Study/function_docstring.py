# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
def print_max(x, y):
    '''
    打印两个书中的最大值面两个值都必须为整数.

    :param x:数1
    :param y:数2
    :return:maximum
    '''

    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(3, 6)
print(print_max.__doc__)
help(print_max)