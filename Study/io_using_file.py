# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
poem = '''
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''

# 使用编辑模式打开一个文件
filePath = r'E:\python\helloWorld'
fileName = 'poem.txt'
print(filePath + '\\' + fileName)
with open(filePath + fileName, 'w') as f:
    f.write(poem)
    # f.close()

with open(filePath + fileName, 'r') as f:
    while True:
        line = f.readline()
        # 零长度指示符EOF
        if len(line) == 0:
            break
        print(line)
    # 不用手动关
    # f.close()
