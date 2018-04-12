# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
import sys
import re

input_args = sys.argv
print(sys.argv)

with open(input_args[1], 'r+', encoding='utf-8') as f:
    d = f.read()
    tt = re.sub('A', 'B', d)
    f.seek(0, 0)
    f.write(tt)
