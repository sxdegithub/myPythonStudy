# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# 转自https://www.oschina.net/translate/computing-pi-with-python

# import sys
# import math


# def main(argv):
#     if len(argv) != 1:
#         sys.exit('Usage: calc_pi.py，请输入一个数字参数')
#
#     print('\nComputing Pi v.01\n')
#     a = 1.0
#     b = 1.0 / math.sqrt(2)
#     t = 1.0 / 4.0
#     p = 1.0
#
#     # print("打印int(sys.argv[1]):{}：".format(int(sys.argv[1])))
#     # print("打印rang（int(sys.argv[1])）:{}：".format(range(int(sys.argv[1]))))
#     # for i in range(2,5):
#     #     print(i)
#
#     for i in range(int(sys.argv[1])):
#         print("打印i：{}".format(i))
#         at = (a + b) / 2
#         bt = math.sqrt(a * b)
#         tt = t - p * (a - at) ** 2
#         pt = 2 * p
#
#         a = at;b=bt;t = tt;p = pt
#
#         my_pi = (a + b) ** 2 / (4 * t)
#         accuracy = 100 * (math.pi - my_pi) / my_pi
#
#         print("Pi is approximately: " + str(my_pi))
#         print("Accuracy with math.pi: " + str(accuracy))
#
# if __name__ == "__main__":
#         main(sys.argv[1:])


import sys
import math
from decimal import Decimal

print(Decimal(10))


def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1) ** k) * (
            Decimal(math.factorial(6 * k)) / ((math.factorial(k) ** 3) * (math.factorial(3 * k))) * (
                13591409 + 545140134 * k) / (
                640320 ** (3 * k)))
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi ** (-1)
    return pi


if __name__ == "__main__":
    chudnovsky(sys.argv[1])
