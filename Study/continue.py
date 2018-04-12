# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
while True:
    s = input("随便输入点什么:")
    if s == "quit":
        break
    if len(s)<3:
        print("你太短了")
        continue
    print("输入其他长度")

