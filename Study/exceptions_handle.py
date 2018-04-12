# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx

try:
    text = input('Enter something-->')
except EOFError:
    print('Here is a EOFError')
except KeyboardInterrupt:
    print('You Cancelled the operation')
else:
    print('You entered {}'.format(text))
