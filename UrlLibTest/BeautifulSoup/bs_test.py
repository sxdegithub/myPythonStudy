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
# from bs4 import BeautifulSoup
#
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html, 'lxml')
# print(soup.title)
# print('type(soup.head)-------------->', type(soup.head))
# # <class 'bs4.element.Tag'>   Tag类型有很多属性,例如string,name
# print('soup.title.string-------------->', soup.title.string)
# print('soup.title.name-------------->', soup.title.name)
# print(soup.head)
# print(soup.p)
#
# # (1)获取名称
# print('soup.title.name-------------->', soup.title.name)
#
# # (2)获取属性
# # 节点属性可能比较多,例如id,class等
# print(soup.p.attrs)
# print(soup.p.attrs['name'])
# print("soup.p['name']----------------------->", soup.p['name'])
#
# # (3)获取内容
# print('soup.p.string---------------->', soup.p.string)
#
# # 嵌套选择
# print('soup.head.title.string------------>', soup.head.title.string)

# 关联选择
"""
 在做选择的时候，有时候不能做到一步就选到想要的节点元素，
 需要先选中某一个节点元素，然后以它为基准再选择它的子节点、父节点、兄弟节点等，这里就来介绍如何选择这些节点元素
"""
# (1)子节点和子孙节点
# from bs4 import BeautifulSoup
#
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>
#             none
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
#
# soup= BeautifulSoup(html,'lxml')
# # 直接获取节点的内容,contents属性得到的结果是直接子节点的列表
# print(soup.p.contents)
# print(len(soup.p.contents))
# for it in soup.p.contents:
#     print('------------->',it)


# # xpath，父子节点【child，parent】、祖先后代【descendants，ancestor】，beatifulsoup对应的【child，parent】、【children，parents】
# 调用children属性得到和contents属性一样的结果，都是直系子节点

# from  bs4 import BeautifulSoup

# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>
#             none
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html, 'lxml')
# print(soup.p.children)

# for i, child in enumerate(soup.p.children):
#     print('{}---------->{}'.format(i, child))

# 使用descendants属性，获取所有子孙节点
# for i, child in enumerate(soup.p.descendants):
#     print('{}---------->{}'.format(i, child))

# (2)父节点和祖先节点
# print(soup.p.parent)
# 所有祖先，
# print(soup.p.parents)
# for i, parent in enumerate(soup.p.parents):
#      print('{}---------->{}'.format(i, parent))
#

# (3)兄弟节点
# from  bs4 import BeautifulSoup
#
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1"><span>Elsie</span></a>
#             noneprev
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html, 'lxml')
#
# # sibling(s)表示多个同级节点
# # 上一个同级节点
# print('next sibling---------->',soup.a.next_sibling)
# # 下一个同级节点
# print('Prev sibling---------->',soup.a.prev_sibling)

# （4）提取信息,获取文本使用.string，获取属性使用.[属性名]
# from  bs4 import BeautifulSoup
#
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">555<span>Elsie</span></a>
#             noneprev
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
#
# soup = BeautifulSoup(html, 'lxml')
# print("soup.p['class']------------>", soup.p['class'])
# print('soup.a.next_sibling.string------------->',soup.a.next_sibling.string)
#
# # print输出：
#
# """
# soup.p['class']------------> ['story']
# soup.a.next_sibling.string------------->
#             noneprev
# """


# 6. 方法选择器
# 列如find（）和findall（）

# (1)NAME，根据节点的名字来查询
# from  bs4 import BeautifulSoup
#
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element2">Foo</li>
#             <li class="element3">Bar</li>
#             <li class="element4">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element5">123</li>
#             <li class="element6">456</li>
#         </ul>
#     </div>
# </div>
# '''
#
# soup = BeautifulSoup(html, 'lxml')
# print("len(soup.find_all(name='ul'))-------->", len(soup.find_all(name='ul')))
# print("soup.find_all(name='ul')--------------->", soup.find_all(name='ul'))
# # # print输出：
# """
# len(soup.find_all(name='ul'))--------> 2
# soup.find(name='ul')---------------> [<ul class="list" id="list-1">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>, <ul class="list list-small" id="list-2">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# </ul>]
# """
#
# # find()直接会找第一个
#
# print("type(soup.find(name='ul'))--------------->", type(soup.find(name='ul')))
# print("soup.find(name='ul')--------------->", soup.find(name='ul'))
# # # print输出：
# """
# type(soup.find(name='ul'))---------------> <class 'bs4.element.Tag'>
# soup.find(name='ul')---------------> <ul class="list" id="list-1">
# <li class="element">Foo</li>
# <li class="element">Bar</li>
# <li class="element">Jay</li>
# </ul>
#
#
# """
#
# # 都是bs4.element.Tag类型，可嵌套
#
# for ul in soup.find_all(name='ul'):
#     for li in ul.find_all(name='li'):
#
#         print(li.string)
#         print(li['class'])
#
# # 输出：
# """
#
# Foo
# ['element2']
# Bar
# ['element3']
# Jay
# ['element4']
# 123
# ['element5']
# 456
# ['element6']
#
# """


# (2)attrs,通过节点属性

# from  bs4 import BeautifulSoup
#
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element2">Foo</li>
#             <li class="element3">Bar</li>
#             <li class="element4">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element5">123</li>
#             <li class="element6">456</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# # 传入的attrs属性是一个字典
# print(soup.find(attrs={'class': 'list', 'id': 'list-2'}))
# # 输出：
# """
# <ul class="list list-small" id="list-2">
# <li class="element5">123</li>
# <li class="element6">456</li>
# </ul>
#
# """


# (3)text
# 匹配文本节点

# from bs4 import BeautifulSoup
# import re
#
# html = '''
# <div class="panel">
#     <div class="panel-body">
#         <a>Hello, this is a link
#         </a>
#         <a>Hello, this is a link, too</a>
#     </div>
# </div>
# '''
# # find_all()会返回所有匹配的节点
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text=re.compile('link')))



# 还有find()默认匹配第一个
# from bs4 import BeautifulSoup
# import re
#
# html = '''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find(name='ul'))
# print(type(soup.find(name='ul')))
# print(soup.find(class_='element'))

"""
find_parents()和find_parent()：前者返回所有祖先节点，后者返回直接父节点。
find_next_siblings()和find_next_sibling()：前者返回后面所有的兄弟节点，后者返回后面第一个兄弟节点。
find_previous_siblings()和find_previous_sibling()：前者返回前面所有的兄弟节点，后者返回前面第一个兄弟节点。
find_all_next()和find_next()：前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点。
find_all_previous()和find_previous()：前者返回节点后所有符合条件的节点，后者返回第一个符合条件的节点。

"""

# 7.CSS选择器
#  只要调用select(),传入相应的css选择器即可
from bs4 import BeautifulSoup

html = """
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element1">Bar</li>
        </ul>
    </div>
</div>

"""

soup = BeautifulSoup(html, 'lxml')
# print(soup.select('.panel-body'))
# print(soup.select('ul'))
print(soup.select('#list-2 .element'))
print(soup.select('ul')[1])
