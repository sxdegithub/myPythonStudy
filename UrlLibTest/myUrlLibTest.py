# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# 实验urllib.reuest
import urllib.request
import urllib.parse
import urllib.error
import socket

# urllib说明:
# urllib.request 用于打开和读取URL,
# urllib.error 用于处理前面request引起的异常,
# urllib.parse 用于解析URL,
# urllib.robotparser用于解析robots.txt文件





# urllib.reuest
###########################################################################
# help(urllib.request.urlopen)
# Help on function urlopen in module urllib.request:
# urlopen(url, data=None, timeout=<object object at 0x000002C11551F0C0>, *, cafile=None, capath=None, cadefault=False, context=None)

# 基本get方法
# response = urllib.request.urlopen("http://10.100.13.106/UInnovation/")
# # 网页源码
# # print(response.read().decode("utf-8"))
# print(type(response))
# # http.client.HTTPResonse对象的基本方法与属性
# # status,响应状态码
# print("响应状态码：%s" % response.status)
# # 响应头headers与header
# print("响应头：%s" % response.getheaders())
# print("响应头cookie：%s" % response.getheader('Set-Cookie'))
# print(type(response.getheader('Set-Cookie')))
# print(response.getheader('Set-Cookie').split(';'))
#
# print(response.readinto())


# post方法
# 还需要用到parse库
# data参数是可选的。如果要添加该参数，并且如果它是字节流编码格式的内容，即bytes类型，则需要通过bytes()方法转化。另外，如果传递了这个参数，则它的请求方式就不再是GET方式，而是POST方式。



# 使用代理，方便抓包
# 下面这个可能没有请求头，导致有问题
##########################################################################################
# proxy_support = urllib.request.ProxyHandler({'http': 'localhost:9876'})
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)
#
# url = "http://httpbin.org/post"
# url_UInnovation = 'http://10.100.13.106/UInnovation/front/fontController/login.do'
# data_UInnovation = bytes(urllib.parse.urlencode({'returnUrl': '',
#                                                  'loginName': '9001@qq.com',
#                                                  'password': '47ec2dd791e31e2ef2076caf64ed9b3d',
#                                                  'passKey': ''}), encoding='utf8')
# # data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# # response_post = urllib.request.urlopen(url, data)
# response_post = urllib.request.urlopen(url_UInnovation, data_UInnovation)
# print(response_post.read().decode('utf-8'))
##########################################################################################


# timeout 参数
# #########################################################################################
# 使用代理，很奇怪，使用代理了会导致下面运行失败
# proxy_support = urllib.request.ProxyHandler({'http': 'localhost:9876'})
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)
#
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print(e)
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')
#     print(type(socket.timeout))
#     print(type(e.reason))
#
#     print(e.reason)
#     print(socket.timeout)
# #########################################################################################


# urllib.request.Request
# 先构建一个Request对象，然后通过urlopen来发送出去
# Request的init方法，，__init__(self,url,data=None,headers={},origin_req_host=None,unverifiable=False, method=None)
# 这样可以方便的添加headers
'''
第一个参数url用于请求URL，这是必传参数，其他都是可选参数。
第二个参数data如果要传，必须传bytes（字节流）类型的。如果它是字典，可以先用urllib.parse模块里的urlencode()编码。
第三个参数headers是一个字典，它就是请求头，我们可以在构造请求时通过headers参数直接构造，也可以通过调用请求实例的add_header()方法添加。
添加请求头最常用的用法就是通过修改User-Agent来伪装浏览器，默认的User-Agent是Python-urllib，我们可以通过修改它来伪装浏览器。比如要伪装火狐浏览器，你可以把它设置为
'''

# request = urllib.request.Request('http://python.org', headers={
#     'User-Agent': 'mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
# response = urllib.request.urlopen(request)
# # print(response.read().decode('utf-8'))
# print('request.headers: %s' % request.headers)
# print(response.geturl())
# # print(response.info())
# print(response.getcode())
# print(response.getheader('Date'))




# 1.重定向
# 2.代理handler
# 3.携带cookie
# nfasnfdnfadaufifa
#######################################################################################################
# # 使用urllib.request.Requst构造登录http://10.100.13.106/UInnovation/front/fontController/login.do
# # 用上代理方便看亲请求
# # 不知道原因，登录失败了，后面再处理，可能涉及到请求重定向了
#
#
# # 全局代理模式
# # proxy_support = urllib.request.ProxyHandler({'http': 'localhost:9876'})
# # proxy_opener = urllib.request.build_opener(proxy_support)
# # urllib.request.install_opener(proxy_opener)
#
# url = 'http://10.100.13.106/UInnovation/front/fontController/login.do'
# dictData = {
#     'returnUrl': '',
#     'loginName': '9001@qq.com',
#     'password': '47ec2dd791e31e2ef2076caf64ed9b3d',
#     'passKey': ''}
# headers = {'Content-Type': 'application/x-www-form-urlencoded',
#            'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
#            'Host': '10.100.13.106'
#
#            }
#
# # data必须是字节流,还要用urllib.parse.urlencode编码
# data = bytes(urllib.parse.urlencode(dictData), encoding='utf8')
# request = urllib.request.Request(url, data=data, headers=headers,
#                                  method='POST')
#
#
# # response_redirect = urllib.request.HTTPRedirectHandler.redirect_request(request)
# #
# # response = urllib.request.urlopen(request)
# # print(response.read().decode('utf-8'))
# # print(response.geturl())
#
#
# # 定义一个自己的头类, 继承HTTPRedirectHandler，拒绝重定向
# # 重写 http_error_302, 直接返回 fp(reponse);
# class MyRedirectHandler(urllib.request.HTTPRedirectHandler):
#     def http_error_302(self, req, fp, code, msg, hdrs):
#         return fp
#
#
# # 安装重定向handler
# myRedirectHandler = MyRedirectHandler()
# # 安装代理handler
# myProxySupportHandler = urllib.request.ProxyHandler({'http': 'localhost:9876'})
#
# opener = urllib.request.build_opener(myRedirectHandler, myProxySupportHandler)
# # opener.add_handler(myHandler)
#
# # 安装代理handler
# proxy_support = urllib.request.ProxyHandler({'http': 'localhost:9876'})
#
# res = opener.open(request)
#
# print(res.getcode())
# print(res.getheader('Set-Cookie'))
# #
# # 使用上面获得的cookie去访问urlMemberCenter页面,这样就登录成功了
# # 另外还有HTTPCookieProcessor可以直接处理cookie
# # 参见下面的  HTTPCookieProcessor处理Cookie
# urlMemberCenter = "http://10.100.13.106/UInnovation/front/memberController/myCollection.do?leftIndex=member_center"
# reqWithCookie = urllib.request.Request(urlMemberCenter, headers={'Cookie': res.getheader('Set-Cookie')}, method='GET')
# openerWithCookie = urllib.request.build_opener(myProxySupportHandler)
# responseWithCookie = openerWithCookie.open(reqWithCookie)
# print(responseWithCookie.read().decode('utf-8'))
######################################################################################################
# nfasnfdnfadaufifa




# 打开带验证的网页，例如路由器的弹出登录窗
# ######################################################################################################
# # 使用HTTPBasicAuthHandler
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
#
# myProxyHandler = urllib.request.ProxyHandler({'http': 'localhost:9876'})
# routerUserName = 'sxdeadmin'
# routerPassWord = 'sx6226728'
# routerUrl = 'http://192.168.88.3'
# # 创建对象，添加url密码
# myP = HTTPPasswordMgrWithDefaultRealm()
# myP.add_password(None, routerUrl, routerUserName, routerPassWord)
# # 使用HTTPBasicAuthHandler处理
# myHTTPBasicAuthHandler = HTTPBasicAuthHandler(myP)
# # 添加opener
# myOpener = urllib.request.build_opener(myHTTPBasicAuthHandler, myProxyHandler)
# try:
#
#     response = myOpener.open(routerUrl)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print(e.reason)
######################################################################################################


# HTTPCookieProcessor处理Cookie
# HTTPCookieProcessor处理Cookie#####################################################################################################
import http.cookiejar

url = 'http://10.100.13.106/UInnovation/front/fontController/login.do'
dictData = {
    'returnUrl': '',
    'loginName': '9001@qq.com',
    'password': '47ec2dd791e31e2ef2076caf64ed9b3d',
    'passKey': ''}
headers = {'Content-Type': 'application/x-www-form-urlencoded',
           'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11',
           'Host': '10.100.13.106'

           }

# data必须是字节流,还要用urllib.parse.urlencode编码
data = bytes(urllib.parse.urlencode(dictData), encoding='utf8')
request = urllib.request.Request(url, data=data, headers=headers,
                                 method='POST')

# 代理handler
myProxyHandler = urllib.request.ProxyHandler({'http': 'localhost:9876', 'https': 'localhost:9876'})
# 处理cookie的handler
# 还可以保存cookie到文件这时CookieJar就需要换成MozillaCookieJar
cookieFile = u'.\cookie.txt'
# cookie = http.cookiejar.CookieJar(cookieFile)
cookie = http.cookiejar.MozillaCookieJar(cookieFile)
myCookieHandler = urllib.request.HTTPCookieProcessor(cookie)
# 构建opener
opener = urllib.request.build_opener(myCookieHandler, myProxyHandler)

reponse = opener.open(request)
# 保存cookie
cookie.save()
# 打印cookie的值
print(type(cookie))
tempCookie = ''

# 这是手动将cookie添加到headers里面
for item in cookie:
    tempCookie += item.name + '=' + item.value + ';'
    print(item.name + '=' + item.value)
cookieHeaders = {'Cookie': tempCookie}
print('cookieHeaders:%s' % cookieHeaders)
# cookieHeaders ={'Cookie':''}

# 使用获取的cookie去访问后面的内容
urlMemberCenter = "http://10.100.13.106/UInnovation/front/portalController/actNewsIndex.do?index=3"
# resWithCookie = urllib.request.Request(urlMemberCenter, headers=cookieHeaders, method='GET')
# 这是使用自动方式，用cookie.load()方法去加载cookie
cookie.load(cookieFile, ignore_discard=True, ignore_expires=True)
myCookieHandler = urllib.request.HTTPCookieProcessor(cookie)
# 加和不加加cookiehandler是不一样的
# opener = urllib.request.build_opener(myCookieHandler, myProxyHandler)
opener = urllib.request.build_opener(myProxyHandler)
opener.open(urlMemberCenter)





# HTTPCookieProcessor处理Cookie#####################################################################################################
