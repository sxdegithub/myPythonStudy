# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
import string


def reverse(text):
    """将字符串翻转"""
    return text[::-1]


def is_palindrome(text):
   
    print(e for e in text if e.isalnum())
    # 去掉标点空格
    m = ''.join(e for e in text if e.isalnum())
    print(m)
    """是否是回文数"""
    return m == reverse(m)


something = input('请输入:')
if is_palindrome(something):
    print('是,这是个回文数')
else:
    print('不,这不是回文数')
