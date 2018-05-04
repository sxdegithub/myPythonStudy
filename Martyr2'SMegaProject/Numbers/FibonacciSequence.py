# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
import time


# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 递归效率，函数调用导致效率低
def Fib(n):
    # n=n-1
    if n < 2:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # def fib_i(a, b, n):
    # if n == 3:
    #     return a + b
    # else:
    #     return fib_i(b, a + b, n - 1)


def fib_i(n):
    Fib = []
    n=n+1
    for i in range(n):
        Fib.append(i)
        print(Fib[i])
    # print(Fib[0])

    for i in range(2, n):
        Fib[i] = Fib[i - 1] + Fib[i - 2]
        print(Fib[i])
    return Fib[n - 1]


n = int(input("输入整数："))
if n <= 0:
    print("请输入正整数")
else:
    startime = time.time()
    print("输出迭代fib_i:%s" % fib_i(n))
    endtime = time.time()
    time_take = endtime - startime
    print("计算耗时:%s" % time_take)

    startime = time.time()
    print("输出递归Fib:%s" % Fib(n))
    endtime = time.time()
    time_take = endtime - startime
    print("计算耗时:%s" % time_take)
