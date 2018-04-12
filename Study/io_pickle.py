# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
import io
import pickle

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['apple', 'mango', 'carrot']
# write to the file
f = open(shoplistfile, 'wb')
# dunmp the object to the file
pickle.dump(shoplist, f)
f.close()

# destroy the shoplist
del shoplist

# read back from the storage
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)

ff = io.open('abc.txt', 'wt', encoding='utf-8')
ff.write(u'Imagine non-English language here,我不是英语')
ff.close()

text = io.open('abc.txt', encoding='utf-8').read()
print(text)
