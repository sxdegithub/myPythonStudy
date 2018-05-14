# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
import pymysql
from  pymysql import MySQLError

# https://cuiqingcai.com/5578.html
# 连接数据库，创建表
##################################################################################################
# db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='sqlstudy')
# cursor = db.cursor()
# sql = 'CREATE TABLE IF NOT EXISTS spider_two(id VARCHAR(100) NOT NULL,name VARCHAR(100) NOT NULL,age INT NOT NULL,' \
#       'PRIMARY KEY(id))'
# cursor.execute(sql)
# cursor.close()
# db.close()
##################################################################################################

# # 连接数据库，插入数据
# id = 1
# name = 'sx'
# age = 17
# value = (id, name, age)
# db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='sqlstudy')
# cursor = db.cursor()
# sql = 'INSERT INTO spider_two(id,name,age) values (%s, %s, %s)'
# try:
#     cursor.execute(sql, value)
#     db.commit()
# except MySQLError as e:
#     db.rollback()
#     print(e)
# cursor.close()
# db.close()


# 连接数据库，插入数据,优化
# id = 1
# name = 'sx'
# age = 17
# data = {'id': 1,
#         'name': 'sx',
#         'age': 18
#         }

# 插入数据
# table = 'spider_two'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
# db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='sqlstudy')
# cursor = db.cursor()
# sql = 'INSERT INTO {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values)
# try:
#     cursor.execute(sql, tuple(data.values()))
#     db.commit()
# except MySQLError as e:
#     db.rollback()
#     print(e)
# cursor.close()
# db.close()

# print(sql)

#
# print(tuple(data.values()))
# print(values)

# # 更新数据
# sql_update = "UPDATE spider_two  SET age =%s WHERE name = %s "
# try:
#     cursor.execute(sql_update,(25,'sx'))
#     db.commit()
# except:
#     db.rollback()
# cursor.close()
# db.close()
# print(sql_update)


# 插入数据，如果id重复就更新数据
# ##################################################################################################
# data = {
#     'id': 1,
#     'name': 'sx',
#     'age': '27'
# }
# table = 'spider_two'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
#
# sql = 'INSERT INTO {table} ({keys})VALUES({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys, values=values)
# update=','.join(['{key}=%s'.format(key=key) for key in data])
# sql+=update
#
# db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='sqlstudy')
# cursor = db.cursor()
# try:
#     cursor.execute(sql,tuple(data.values())*2)
#     db.commit()
# except MySQLError as e:
#     print(e)
#     db.rollback()
# cursor.close()
# db.close()
# print(sql)
# ##################################################################################################


# 删除数据
# ##################################################################################################
# table = 'spider_two'
# condition = 'age > 20'
#
# db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='sqlstudy')
# cursor = db.cursor()
# sql_delete = 'DELETE FROM {table} WHERE {condition}'.format(table=table,condition=condition)
# try:
#     cursor.execute(sql_delete)
#     db.commit()
# except MySQLError as e:
#     print(e)
#     db.rollback()
# cursor.close()
# db.close()
# ##################################################################################################

# 查询数据
db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='sqlstudy')
cursor = db.cursor()
sql_select = 'SELECT * FROM spider_two WHERE age>2'
# try:
#     cursor.execute(sql_select)
#     print("count:", cursor.rowcount)
#     one = cursor.fetchone()
#     print("one:", one)
#     results = cursor.fetchall()
#     print("Results:", results)
#     print("Result Type:", type(results))
#     for row in results:
#         print(row)
# except MySQLError as e:
#     print(e)

# 使用fetchone偏移，随取随用
try:
    cursor.execute(sql_select)
    print('Count:',cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:',row)
        row = cursor.fetchone()
except MySQLError as e:
    print(e)