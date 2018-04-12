# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# version:3.0
# 在文件名中添加注释

import os
import time
import sys

# 1.需要备份的文件与目录被指定放在一个列表中.
# 例如在Windows下:
# source= ['"C:\\Download"','"D:\\code"']

source = ['F:\\F\\BackUpSource', 'F:\\F\\BackUpSource1']
# 必须在字符串中使用双引号

# 2.备份文件必须存储在一个主备份目录
# 指定备份目录
# target = 'E:\\BackUp'
# 3.备份文件要被压缩
# 4.压缩文件名使用当前时期与时间

target_dir = 'F:\\F\\BackUpTest'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
# 文件存储的名称
# targetName = target_dir + os.sep + now + '.zip'

# 为压缩文件添加注释
comment = input('添加注释语:')
# 检查评论输入
if len(comment) == 0:
    targetName = target_dir + os.sep + now + '.zip'
else:
    # 将注释语句添加进文件名
    targetName = target_dir + os.sep + now + '_' +\
                 comment.replace(' ', '_') + '.zip'
# 如果文件目录不存在则创建目录
if not os.path.exists(today):
    os.mkdir(today)

# 5.运行zip命令将文件打包成zip格式
zip_command = 'zip -r {0}  {1}'.format(targetName, ' '.join(source))

# 列表转换字符串
# print('列表转换字符串:' + ' '.join(source))
# Systype = sys.getfilesystemencoding()
# print('类型为:', Systype)

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Zip file successful backup to', targetName)
else:
    print('Backup FAILED')
# os.system("ls")
