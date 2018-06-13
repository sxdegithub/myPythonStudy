# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx

# 插入序列化数据
# ##################################################################################################
import pymysql
from pymysql import MySQLError

from UrlLibTest.MyDBTest.users import Users

tables = 'users'
user = Users('sx', 123456, 123456789, 'http://baidu.com')
user_2 = Users('sxsx', 123456, 123456789, 'http://youku.com')
# 用户存储列表
userList = [user]
userList.append(user_2)
# userList.append(user)

db = pymysql.connect(host='localhost', user='root', password='', port=3306, db='shopee')
cursor = db.cursor()

for user in userList:
    userid = user.getUserId()
    username = user.getUserName()
    shopid = user.getShopId()
    url = user.getUrl()

    userDataTemp = {
        'id':None,
        'user_id': user.getUserId(),
        'user_name': user.getUserName(),
        'shop_id': user.getShopId(),
        'url': user.getUrl()
    }

    values = ','.join(['%s'] * len(userDataTemp))
    keys = ', '.join(userDataTemp.keys())
    print('userDataTemp.keys(): %s ' % userDataTemp.keys())

    sql_incert = "INSERT INTO {tables} ({keys})VALUES ({values})".format(tables=tables, keys=keys, values=values)
    print( sql_incert)
    try:
        cursor.execute(sql_incert,tuple(userDataTemp.values()))
        print("userDataTemp.values():%s" % userDataTemp.values())
        db.commit()
    except MySQLError as e:
        print(e)
        db.rollback()

