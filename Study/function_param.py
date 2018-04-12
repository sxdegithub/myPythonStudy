# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
def print_max(a, b):
    if a > b:
        print(a, "大")
    elif a == b:
        print(a, "等于", b)
    else:
        print(b, "大")


print_max(1, 2)
print_max(2, 2)
print_max(3, 1)
