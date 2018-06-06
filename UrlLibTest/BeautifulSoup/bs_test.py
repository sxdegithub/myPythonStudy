# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# BeautifulSoup测试
# 转自，https://cuiqingcai.com/5548.html
# from bs4 import BeautifulSoup
#
# soup0 = BeautifulSoup('<p>hahaha</p>', 'lxml')
# soup1 = BeautifulSoup('<p>hahaha</p>', 'html.parser')
# soup3 = BeautifulSoup('<p>hahaha</p>', 'xml')
# # soup2 = BeautifulSoup('<p>hahaha</p>', 'html5lib')
#
#
# print('soup0----------->',soup0.p.string)
# print('soup1----------->',soup1.p.string)
# print('soup3---------->',soup1.p.string)
# # print('soup2----------->',soup1.p.string)

# 5.节点选择
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print('type(soup.head)-------------->', type(soup.head))
# <class 'bs4.element.Tag'>   Tag类型有很多属性,例如string,name
print('soup.title.string-------------->', soup.title.string)
print('soup.title.name-------------->', soup.title.name)
print(soup.head)
print(soup.p)

# (1)获取名称
print('soup.title.name-------------->', soup.title.name)

# (2)获取属性
# 节点属性可能比较多,例如id,class等
print(soup.p.attrs)
print(soup.p.attrs['name'])
print("soup.p['name']----------------------->", soup.p['name'])

# (3)获取内容
print('soup.p.string---------------->', soup.p.string)

# 嵌套选择
print('soup.head.title.string------------>', soup.head.title.string)
