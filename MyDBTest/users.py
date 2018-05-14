# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx

# user对象序列化
class Users:
    def __init__(self, username, userid, shopid, url):
        self.username = username
        self.userid = userid
        self.url = url
        self.shopid = shopid

    def GetUsersInfo(self):
        print(U'姓名:%s' % (self.username).decode('utf-8'))  # 将utf-8转成Unicode输出，避免错误
        print(U'userid:%s' % (self.userid).decode('utf-8'))
        print(U'url:%s' % (self.url).decode('utf-8'))
        print(U'邮件:%s' % (self.shopid).decode('utf-)8'))

    def getUserName(self):
        return self.username

    def getUserId(self):
        return self.userid

    def getShopId(self):
        return self.shopid

    def getUrl(self):
        return self.url

    def SetName(self, username):
        self.username = username

    def SetUserid(self, userid):
        self.userid = userid

    def SetUrl(self, Url):
        self.url = Url

    def SetShopid(self, shopid):
        self.mail = shopid
