# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: sx

class ShortInputException(Exception):
    """用户自己定义的异常类"""

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = input('Enter something:')
    if len(text) < 3:
        # 自己引发异常
        raise ShortInputException(len(text), 3)
except EOFError:
    print('Why did you do an EOF on me?')
# except ShortInputException as ex:
#     print(('ShortInputException:The input was {0} \
#     long ,excepted at least {1}').format(ex.length, ex.atleast))

except ShortInputException:
    print('ShortInputException!')
else:
    print('No Exception was raised!')
