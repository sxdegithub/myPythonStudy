# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx

# https://cuiqingcai.com/5584.html
# [Python3网络爬虫开发实战] 5.3.1-MongoDB存储
from  pymongo import MongoClient
import pymongo

# student1 = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# student3 = {
#     'id': '2111',
#     'name': 'sx',
#     'age': 23,
#     'gender': 'male'
# }
#
# student3 = {"site":"www.runoob.com", "name":"菜鸟教程"}
# try:
#     client = pymongo.MongoClient('10.10.220.77', 27017)
#     db = client.test_db
#     collection = db.students
#     # 插入数据
#     result =collection.insert(student3)
#
# finally:
#     pass

# 6.查询数据
try:
    client = pymongo.MongoClient('10.10.220.77', 27017)
    db = client.test_db
    collection = db.students
    # result1 = collection.insert(student3)

    # result = collection.find_one({'name': 'Mike'})
    # print(result)
    # print(type(result))

    # find方法返回的是一个生成器对象
    for i in collection.find({'age': {'$lt': 21}}):
        print(i)
    for i in collection.find({'age': {'$gt': 21}}):
        print(i)

    for i in collection.find({'age': {'$lte': 21}}):
        print(i)

    # 7.计数
    print(collection.find().count())

    # 8.排序
    results = collection.find().sort('name', pymongo.ASCENDING)
    print([r['name'] for r in results])

    # 10.更新
    condition = {'name': 'sx'}
    student = collection.find_one(condition)
    student['age'] = 28
    result = collection.update_one(condition,{'$set':student})
    print(result)

finally:
    pass
