# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
class Person():
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello,my name is', self.name)

p = Person('sx')
p.say_hi()

