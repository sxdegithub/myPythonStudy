# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
from  pymongo import MongoClient
import pymongo

try:
    conn = MongoClient('192.168.88.168', 27017)
    db = conn.mydb
finally:
    pass
