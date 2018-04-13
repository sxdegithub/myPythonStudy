# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
#######################################
# Numbers
# Find PI to the Nth Digit - Enter a number and have the program generate PI
# up to that many decimal places. Keep a limit to how far the program will go.
#######################################

# 采用级数
# π = 2 + 2/3 + 2/3*2/5 + 2/3*2/5*3/7 + ...
# 转自http://www.cppfans.com/articles/basecalc/c_pi_10000.asp


import math
import decimal

print(float("%.2f" % math.pi))


def find_pi():
    a = 1
    b = 3
    t = 1
    x = 0
    while t > 1e-15:
        t = t * a / b
        x += t
        a += 1
        b += 2
        print("Pi is :{}".format(2 * x + 2))


if __name__ == "__main__":
    find_pi()
