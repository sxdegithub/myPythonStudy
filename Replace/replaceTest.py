# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx

"""
str_a="AAAAABBBBBCCCCCC"
str_b = str_a.replace('A','D',2)
print(str_a)
print(str_b)

#test line
#test line 2

"""

#
# import re
# a ='hello world'
# strinfo = re.compile('world')
# b = strinfo.sub('python',a)
# print(b)


# 去空格及特殊符号
# s = '  ,sdsdsd #@, '
# print(s.strip().lstrip(',s').rstrip(','))

# 比较字符串
# strcmp(sStr1,sStr2)
# import operator
# sStr1 = 'strchr'
# sStr2 = 'strch'
# print(operator.eq(sStr1, sStr2))

# 扫描字符串是否包含指定的字符
# strspn(sStr1,sStr2)
# sStr1 = '12345678'
# sStr2 = '456'
# #sStr1 and chars both in sStr1 and
# print(sStr1 and sStr2)
# print(len(sStr1 and sStr2))

# 追加指定长度
# strncat(sStr1,sStr2,n)
# sStr1 = '12345'
# sStr2 = 'abcdef'
# n = 3
# sStr1 += sStr2[0:n]
# print(sStr1)

# 字符串指定长度比较
# strncmp(sStr1,sStr2,n)
# import operator
# sStr1 = '12345'
# sStr2 = '123bc'
# n = 3
#
# print(operator.eq(sStr1[0:n],sStr2[0:n]))


# 复制指定长度的字符
# strncpy(sStr1,sStr2,n)
# sStr1 = ''
# sStr2 = '12345'
# n = 3
# sStr1 = sStr2[0:n]
# print(sStr1)

# 扫描字符串
# strpbrk(sStr1,sStr2)
# sStr1 = 'cekjgdklab'
# sStr2 = 'gka'
# nPos = -1
# for c in sStr1:
#     # print(c)
#     if c in sStr2:
#         nPos = sStr1.index(c)
#         print(nPos)
#         continue
# # 输入2,4,2,8    2个2都是index(k)的结果
# #  print(nPos)

# 翻转字符串
# 后面的数字为步进，-1时候，字符串倒序输出
# strrev(sStr1)
# sStr1 = 'abcdefg'
sStr1 = '你是谁'
sStr2 = sStr1[::-1]
# sStr3 = sStr1[::]
# sStr4 = sStr1[::2]
# sStr5 = sStr1[1::-1]
# sStr6 = sStr1[1::]
#
print(sStr2)
# print(sStr3)
# print(sStr4)
# print(sStr5)
# print(sStr6)



# 分割字符串
# strtok(sStr1,sStr2)
# sStr1 = 'ab,cde,fgh,ijk'
# sStr2 = ','
# sStr1 = sStr1[sStr1.find(sStr2) + 1:]
# print(sStr1)
#
# # 或者
# s = 'ab,cde,fgh,ijk'
# print(s.split(','))

# 连接字符串
# delimiter = ','
# mylist = ['Brazil', 'Russia', 'India', 'China']
# print(delimiter.join(mylist))

# 只显示字母与数字
# def OnlyCharNum(s):
#     s2 = s.lower()
#     fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
#     for c in s2:
#         if not c in fomart:
#             s = s.replace(c, '')
#     return s
#
# print(OnlyCharNum("a000 aa-b"))
