# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# 这是一个字符串对象
name = 'Swaroop'

if name.startswith('Swar'):
    print('Yes,the string starts with Swar')
if name.startswith(('a', 's')):
    print("yes there is a 'S'")
if 'a' in name:
    print("Yes ,the string contains character 'a'")
if name.find('war') != -1:
    print("Yes,it contains the string 'war'")

delimiter = '_*_'
mylist = ['brazil', 'Russia', 'India', 'China']
print(mylist)
print(delimiter.join(mylist))
