# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx

# [Python3网络爬虫开发实战] 5.1.3-CSV文件存储
# https://cuiqingcai.com/5571.html

# 1. 写入
#
# import csv
#
# with open('_csv_data.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',',
#                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     writer.writerow(['Spam'] * 5 + [',Beans'])
#     writer.writerow(['xxxx'] * 6)
#     writer.writerow(['dddd'] * 6)
#
# # 下面是爬虫常用的
# # 但是一般情况下，爬虫爬取的都是结构化数据，我们一般会用字典来表示。在csv库中也提供了字典的写入方式，示例如下：
# with open('_csv_data_dic.csv', 'a',newline='') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     # 写入行头
#     writer.writeheader()
#     writer.writerow({'id': 1, 'name': 'sx', 'age': 22})


# 2. 读取
import csv

with open('_csv_data_dic.csv','r',newline='',encoding='utf-8' ) as csvfile:
    reader = csv.reader(csvfile)
    for read in reader:
        print(read)

# import pandas as pd
