# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# BeautifulSoup测试
# 转自，https://cuiqingcai.com/5548.html
from bs4 import BeautifulSoup

soup0 = BeautifulSoup('<p>hahaha</p>', 'lxml')
soup1 = BeautifulSoup('<p>hahaha</p>', 'html.parser')
soup3 = BeautifulSoup('<p>hahaha</p>', 'xml')
# soup2 = BeautifulSoup('<p>hahaha</p>', 'html5lib')


print('soup0----------->',soup0.p.string)
print('soup1----------->',soup1.p.string)
print('soup3---------->',soup1.p.string)
# print('soup2----------->',soup1.p.string)


