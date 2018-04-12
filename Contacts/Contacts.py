# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx

# 存储文件位置
contactsFile = r"E:\python\helloWorld\Contacts\contactsFile.dat"

# 用来存联系人列表
contactsList = []
with open(contactsFile, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        # print(line)
        content = line.strip('\r\n')
        if content is not None:
            contactsList.append(content)
    pass
# 调试
# print(contactsList)
# 用来存单个联系人
contactsDic = {}
# 输入姓名
set_nameInfo = input("请输入姓名:")
# 输入手机号

set_phoneInfo = input("请输入手机号:")
# 将姓名和手机号存入
contactsDic = {set_nameInfo: set_phoneInfo}
# 联系人存入列表
contactsList.append(contactsDic)
# 打开文件,把列表写入
# print(contactsList)
print(len(contactsList))
with open(contactsFile, 'w', encoding='utf-8', newline='\n') as f:
    if contactsList is not None:
        for i in contactsList:
            f.write(str(i) + '\n')
print(contactsList)

# 清空列表
contactsList.clear()

# 读取列表中的联系人,进行查询
with open(contactsFile, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        # print(line)
        content = line.strip('\r\n')
        if content is not None:
            contactsList.append(content)

# 输入姓名
get_nameInfo = input("请输入姓名:")
# 打印信息
print(contactsList[get_nameInfo])
