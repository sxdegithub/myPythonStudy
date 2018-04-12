# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
import  math
number = 23
running = True
inputNum = True
guess = ''
while running:
    while inputNum:
        temp = input('输入一个整数：')
        if temp.isdigit():
            guess = int(temp)
            inputNum = False

    if guess == number:
        print('猜对了啊')
        running = False

    elif guess < number:
        print('猜小了!')

    else:
        print('猜大了!')

    inputNum = True
print('done')
