# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
#   This my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), "things to purchase")

print('This items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice')
shoplist.append('rice')
print('My shopping lit is now', shoplist)

print('I will sort my list now')
shoplist.sort()

print('Soreted shopping list is', shoplist)

print('The first thing I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)
