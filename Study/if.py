# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
number = 23
guess = int(input("请输入整数:"))

if guess == number:
    print("你真是棒棒的！")
elif guess < number:
    print("辣鸡，猜小了！")

else:
    print("辣鸡，猜大了！")

print('done!')
