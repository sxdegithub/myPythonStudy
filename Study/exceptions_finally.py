# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
import sys
import time

f = None
try:
    f = open(r'E:\python\helloWorldpoem.txt')
    # 常用读文件风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        # print('length of line is {}'.format(len(line)))
        # sys.stdout.flush()
        print('Press ctrl+c now')
        # 为了确保能运行一段时间
        time.sleep(1)
except IOError:
    print('Could not find file poem.txt')
except KeyboardInterrupt:
    print('!!You cancelled the reading from the file')
finally:
    if f:
        # f.__exit__()
        f.close()
    print('(Cleaning up:closed the file)')
