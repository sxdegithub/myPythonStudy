# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# ab是地址(Address)簿(Book)的缩写

ab = {
    'Swaroop': 'Swaroop@swaroop.com',
    'Larry': 'larry@wall.org',
    'sx': 'sx@chinabluedon.cn',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

print(len(ab))
# 删除键值对
del ab['sx']
print(len(ab))

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print("{}'s address is{}".format(name, address))

# 添加一对键值对
ab['hz'] = 'hh@china.cn'
print(len(ab))
print(ab)

print('打印ab字典中的所有键值对:',ab.items())
for name, address in ab.items():
    print("{}'s address is {}".format(name, address))

if 'hz' in ab:
    print("\nhz's address is", ab['hz'])

