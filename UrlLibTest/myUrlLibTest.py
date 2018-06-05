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
# import http.cookiejar
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
# # 代理handler
# myProxyHandler = urllib.request.ProxyHandler({'http': 'localhost:9876', 'https': 'localhost:9876'})
# # 处理cookie的handler
# # 还可以保存cookie到文件这时CookieJar就需要换成MozillaCookieJar
# cookieFile = u'.\cookie.txt'
# # cookie = http.cookiejar.CookieJar(cookieFile)
# cookie = http.cookiejar.MozillaCookieJar(cookieFile)
# myCookieHandler = urllib.request.HTTPCookieProcessor(cookie)
# # 构建opener
# opener = urllib.request.build_opener(myCookieHandler, myProxyHandler)
#
# reponse = opener.open(request)
# # 保存cookie
# cookie.save()
# # 打印cookie的值
# print(type(cookie))
# tempCookie = ''
#
# # 这是手动将cookie添加到headers里面
# for item in cookie:
#     tempCookie += item.name + '=' + item.value + ';'
#     print(item.name + '=' + item.value)
# cookieHeaders = {'Cookie': tempCookie}
# print('cookieHeaders:%s' % cookieHeaders)
# # cookieHeaders ={'Cookie':''}
#
# # 使用获取的cookie去访问后面的内容
# urlMemberCenter = "http://10.100.13.106/UInnovation/front/portalController/actNewsIndex.do?index=3"
# # resWithCookie = urllib.request.Request(urlMemberCenter, headers=cookieHeaders, method='GET')
# # 这是使用自动方式，用cookie.load()方法去加载cookie
# cookie.load(cookieFile, ignore_discard=True, ignore_expires=True)
# myCookieHandler = urllib.request.HTTPCookieProcessor(cookie)
# # 加和不加加cookiehandler是不一样的
# # opener = urllib.request.build_opener(myCookieHandler, myProxyHandler)
# opener = urllib.request.build_opener(myProxyHandler)
# opener.open(urlMemberCenter)
#
#



# HTTPCookieProcessor处理Cookie#####################################################################################################




# error异常处理
# URLError异常类
# URLError异常类##################################################################################################
# from urllib import error, request
#
# try:
#     # 打开一个不存在的页面
#     response = request.urlopen('http://baid.com/dwdds')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers, sep='\n')
# except error.URLError as e:
#     print(e.reason)
# URLError异常类 ##################################################################################################




# [Python3网络爬虫开发实战] 3.1.3-解析链接
# ##################################################################################################
# https://cuiqingcai.com/5508.html
# 1.urlparse()
# from  urllib.parse import urlparse
# result  = urlparse('http://172.16.8.2:38080/redmine/projects/bd-clouddesktop-v1-0/issues?set_filter=1')
# print(type(result),result)
# # 9.quote() 将中文参数转化为URL编码
# from  urllib.parse import quote,unquote
# keyword = '哈哈'
# url ='https://www.baidu.com.com/s'+quote(keyword)
# print(url)
# # 10.unquote()方法，进行url解码
# urlDecode ='https://www.baidu.com.com/s%E5%93%88%E5%93%88'
# print(unquote(urlDecode))
# ##################################################################################################



# # [Python3网络爬虫开发实战] 3.1.4-分析Robots协议
# # https://cuiqingcai.com/5511.html
# # 3.robotparser
# from urllib import robotparser
#
# url = 'http://www.jianshu.com/robots.txt'
# rp = robotparser.RobotFileParser()
# rp.set_url(url)
# print(rp.can_fetch('*', 'http://www.jianshu.com/'))
# print(rp.disallow_all)


# [Python3网络爬虫开发实战] 3.2.1-request基本用法
# # https://cuiqingcai.com/5517.html
'''
上一节中，我们了解了urllib的基本用法，但是其中确实有不方便的地方，比如处理网页验证和Cookies时，需要写Opener和Handler来处理。
为了更加方便地实现这些操作，就有了更为强大的库requests，有了它，Cookies、登录验证、代理设置等操作都不是事儿。

'''
import requests

# r = requests.get('https://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(r.text)
# print(type(r.text))
#
# print(type(r.cookies))
# print(r.cookies)
# data = {
#     'name':'gg',
#     'age':222
# }
# rr = requests.get('http://httpbin.org/get',params = data)
# print(rr.text)
# print(rr.json())

# url = "https://www.v2ex.com/api/nodes/show.json
# querystring = {"name":"python"}
# headers = {'Cache-Control': 'no-cache'}
# response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)
# import re
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
# }
#
# url = "https://www.v2ex.com/api/nodes/show.json"
# querystring = {"name": "python"}
# # response = requests.request("GET", url, headers=headers, params=querystring)
# # 知乎问题
# response = requests.get("https://www.zhihu.com/explore", headers=headers)
# # pattern = re.compile('这里讨论各种 (.*?) 语言编程话题，也包括 Django，Tornado 等框架的讨论。这里是一个能够帮助你解决实际问题的地方。', re.S)
# # print(re.findall(pattern,response.text))
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, response.text)
# print(titles)


# # github图标
# iconUrl = "https://github.com/favicon.ico"
# picUrl = "https://assets-cdn.github.com/images/modules/site/home-illo-team.svg"
# # r = requests.get(iconUrl)
# r = requests.get(picUrl)
# # print(r.text)
# # print(r.content)
# icoFile = u'.\\favicon.ico'
# picFile = u'.\\pic.ico'
# with open(picFile,'wb') as f:
#     f.write(r.content)
# # with open(icoFile,'wb') as f:
# #     f.write(r.content)

# # 4. POST请求

# import requests
# url = 'http://httpbin.org/post'
# data = {
#     'name':'ssxsx',
#     'age':12
# }
# r = requests.post(url,data)
# print(r.text)

# # 5. 响应

# import requests
#
# url = 'https://www.baidu.com'
# r = requests.get(url=url)
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.cookies), r.cookies)
# print(type(r.url), r.url)
# print(type(r.history), r.history)




# [Python3网络爬虫开发实战] 3.2.2- requests高级用法
# ###########################################################################################
# https://cuiqingcai.com/5523.html
# 1.文件上传
# import requests
#
# url = 'http://httpbin.org/post'
# files = {
#     'file': open('.\\favicon.ico', 'rb')
# }
# r = requests.post(url, files=files)
# print(r.text)

# 2.cookies
# import requests
#
# r = requests.get('https://www.baidu.com')
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)
# str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
# print((str.split(' ', 1))

#
# url = ''
# import requests
# # 手动复制浏览器cookie
# headers = {
#     'Cookie': 'JSESSIONID=c02dffac-d6e3-40b4-aac0-26a5168403dd; rememberMe=MfxWgfvKisGVweztL44YNcFZlSHAu8BdGhU/N5qbu6usDT9aEMvctHP8AC/6c6JykhKA7T+m3aOyO7x93HsoexD02DKkmEfmaTfERwqyV+RFq4Xw17YovkhTbo482FhyZ+4zunFYB4zaKv0DZI99gHwLZPeeJ9rAiupxQO9lrCpVRm0DR5HqP/i6zRpa/heQvaLO6wkpnUfjlSMX7FCnfTn2B7OhoPyc+q1cctumEtrmFRbG3J+2bSCvEkmwApIrgxtzo/ex2mUtKSQPgIIPCUtAyHfiMHlzLhViYBC3i9MSotNHYDOFgTBPi9ca9JUOr/wdYzqvGsqT+FDG7FsJo/QBRZarfinVRTHrOiTWPc7Qs7tvQo4KOERwGwP26S0dRUf6CQIasN1WBA1xnqz5tmBhcgbLWgO+n79ou8A01rqNodjqGmaXpUJJf9YNJNO7ZpwS8j9niO8K7fOHlf+/EqSTrmQhKIuQMfKdMQ+gu0bVXZK7QVpl5MlOWE1h0VRAfgTmZ+s9eZee1He/Xf67cLI+ELItvXIrGTuhWCJDb0BKjPb2blzKgFnY46gVh8nPVzE2Yvzkv4gBdWS2il9lSLrw9uVZtGvRr5UAWCJYabbYQ8lNhIBjG/gIrcwe1qODjUrUXkoq0BVQVV5b0BtUfGROPPBlrvVCkAM827WExCQSo2/8+V6d+XmzuU9vl2iput2soXSjRij6loVGsV7KLAjGrbu80YxNkxgxlWw7yD7B6BdkcTwAnA0AB2OfrzeIOiJJUegeegVfjZj7tRL2mnZhpEI09k5nka0dn6B/aC54wz6iVoDmmIU3NqH+jjayQEDVnv+YknBLNjpY1Q3TqV18BzCt9AHWcYxYT/p5UVNITjMZc2RN6e2eyPmb0J/BOQ7PdYfJqEwTv2qVLdc537Z/C9bpBCrXM49vfgfonp2INyifjExnyNIOQ/K8EGIpcUSYhqDx099ONWHQ0Gq1HUezfQnatzuNqowOLBekHfcbpR+tDSaZrStqNxAsbZH+MNFyYrw3BdgPtX3yRwsaNr3yOodaHbvfBIRkrdhsEBYA8AI3DhPvAWA3QfAPK7wHorYCDe8IcBtt3Ei5FPeKbwPfbCI2RXSRFdYcYfbhDlk8eXd2kz+hZYPZyJHFSX9KHh691y6h5b0m61tRd0mxqa0Eth0aDpjaeeBcmtDvc4Cw93oz+8/aGQd/4VBPeJQtB6++vgBJONwVjXnQ5RWXeutichdnfHXkR9n4Xiq7/2/03PgqHzPhYhuh8FxKtkzGtXzZn0iCzUTAgHxLGA95kgrvCf28GP93/ICsKGbH0V2cYnbQE96lYkD63ZZluopKnaxL6SYwbh7FF1opEAPmTJJh9LZGHddJBTpg7avQBzwFeSkWUVKYWtndMukGcYjoven5eLZxvHQq/YPdWTjjcos3MrZ3QLThrM+QGQbzZ6YRlLr8nGPx3zuQaT2ftq4k'
# }
# r = requests.get('http://10.100.13.106/UInnovation/',headers=headers)
# print(r.text)



# 使用RequestCookieJar,去添加
# import requests
#
# url = 'http://10.100.13.106/UInnovation/'
#
# cookie = 'JSESSIONID=0664e6b8-ca37-45bf-b15b-d0233f020804; rememberMe=YgWg2ILT2UaKhK4a6mmei7Hf7Sa2trhrmZxh0mCtos2ENzxYo6NcWRfbDlOKOS4TNUbEAx/1ZUEZATV3O4pztDuSz0wXlaabOk61221HL3xTNmfToLfrkru4/43+j9vKxx5kjIdz7yDPVbYdt+46hWPkwZQiEy+SE4fmmPceQW4Cdl9APZVNy/z8VzSISj+sTBVfzprTvDN0Qq3vKvFXzPBkBn/2mk0pSaFEd9eXFOkFp0HaaCkt1mcSTPqv+q5kaAcvWgoR9rMjHnfVIG8ExGumYi/961jNLv1AF5ubT433KLricyqccjdkmMyEiyujvsaO7luCv8hZKWklcTCM12qXQzvEhJiAzxUY5eFeyfBTE6e3S+Duwis1a1Oi3iGKhOYqtReTpvM50rVj3ZZBcKhpKy/yHTcQN4oP3D0msnwpIkXKJQ36IFELKnJffIwbUo6gFz62csn1ozMhjJEQaPAAD6nUriStHZQUuJg4EOaq9bMfqIXui7o2nKQU126BIqO3pLXn8P0lAxEcGfF2GvBK4pubTv3Ns0k3rBv5Ts/CcR9E5rb/pAk2k6dkxj2t4gwY4lly7fOLL3CXYb5jZSJT3UAJGSwN2fUV+2RgempkD81osvD7jbJLK8Ap26WZ4piHIHOf/fzgrxGbP7YY7nCBY6Ez/P0M11PIM+VX8hLLaX8u3rv1h+1iwfS4DS4svjtP6Yp9hf0FAnIbtux6YIRS0TES+z62z92sA6D9qz5k2Ur+FByD/vbIwRP1kh+nMred1g5UaNC+xjWqvUXZUlTB9A/LppoZ6FJec1TXvwj+Rb0YC1WrWb485lpGxXG2EUhdLc3gIBkuCcH1GEsOrK67tIoDsUONN/o83ZkJYFMaMzCgaH6ypkq7yNarZ+cPuYH80JXF6mnYr3iVbDT+KvAzE2z3LzNxVYZDzE5g1T4ea7JIclvcSTkK5msOm1SKwqz0CIUtaVxj5GrhlG33ZeC3Pbt+hIfSytLDHKIlId80ncoDgM4nN6fJYjS6DV2KTk1BqpECuomJNGvg7bmePnxfpmS2qVMD6IK25FWg7ho6x5izC9Knku3Jt1hF62sg1Cy1htWkRNKF4Tjmeuu2VxQchb/HGvV0FamndobJ2Bk1OxrAzXH3WhrE6jBvLI6rGp+6yJ9bsOvuy5Uca2b2w3wsZEwrCzkQvBAcupjYOvEdnK9QP/xpxWaUEQgQCZZTOpT7ziLmpiYr7EPtabjMWocXUIunmuII1o+qfvzHCRud6iRlPKTYD/IYR6gyUdso8CiutpEqe7SlKNS2donaZ5S5VPyTFMRlyTZoKNRWUJIQzv0A0znHTZJXsmKVFI/knIWwxhc4lH9+bi4MVIPdBGGP0IsSSCqYx/uZ2hcXs4AG2iJ5su8W8Vh3rq+n5turyDsq2SjX9xYZBOTi5wE6YMhzxoWgNKPhQhFcmKFmWFgumpBRVhQZT/4hInORfTRK'
# jar = requests.cookies.RequestsCookieJar()
# for cookie in cookie.split(';'):
#     key, value = cookie.split('=', 1)
#     jar.set(key, value)
# r = requests.get(url,cookies=jar)
#
# print(r.text)
# print(r.cookies.items())



# # 3. 会话维持
# import requests
#
# session = requests.session()
# session.get('http://httpbin.org/cookies/set/number/123456789')
# r =session.get('http://httpbin.org/cookies')
# print(r.text)

# 4. SSL证书验证
# import requests
# # 忽略证书异常，怎么添加证书还没弄过
# from requests.packages import urllib3
# urllib3.disable_warnings
#
# urllib3.disable_warnings()
# url = 'https://www.12306.cn'
# r = requests.get(url, verify=False)
#
# print(r.status_code)



# 5. 代理设置
# import requests
#
# # 使用本地的charles代理
# proxies_http = {
#     'http': '127.0.0.1:9876',
#     'https': '127.0.0.1:9876'
#
# }
# proxies = {
#     'http': 'socks5://127.0.0.1:1080'
#     # 'https': 'socks5://127.0.0.1:1080'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
# }
# url = 'https://www.google.com.hk'
# r=requests.get(url, proxies=proxies, headers=headers, verify=False)
# print(r.text)

# # 6.超时设置
# import requests
# import time
# url = 'https://www.baidu.com'
# timeNow = time.time()
# r = requests.get(url, timeout=0.01)
# print(r.t)
# timeNow = time.time()-timeNow
# print(timeNow)
# print(r.status_code)
# print(timeNow)

#
# # 7.身份认证
# import requests
# from requests.auth import HTTPBasicAuth
#
# url = 'http://192.168.88.3'
# # r = requests.get(url,auth =HTTPBasicAuth('sxdeadmin','sx6226728'))
# # print(r.status_code)
# # 简单写法
# rr = requests.get(url, auth=('sxdeadmin', 'sx6226728'))
# print(rr.status_code)
# # OAuth1认证
# # https://requests-oauthlib.readthedocs.org/
#


# 8.Prepared Request
# # 类似于urllib里面的request对象
# from requests import Request, Session
#
# url = 'http://httpbin.org/post'
# data = {'name': 'sx'}
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
# }
# s = Session()
# request = Request('POST', url=url, data=data, headers=headers)
# prepared = s.prepare_request(request)
# r= s.send(prepared)
# print(r.text)




# [Python3网络爬虫开发实战] 3.3-正则表达式
# 1.实例引入
# 2.match()方法

# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello\s\d\d\d\s(\d{4})\s\w{10}',content)
# print(type(result))
# print(result.group(0))
# print(result.group(1))
# print(type(result.group()))
# print(result.span(0))
# print(result.span(1))

# # 通用匹配
# # 贪婪与非贪婪
# import  re
#
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$',content)
# result1 = re.match('^He.*(\d+).*Demo$',content)
# print(result)
# print(result.group())
#
# # 非贪婪模式下，.*？会尽可能少匹配，后面的\d+只匹配到123
# print(result.group(1))
# # 贪婪模式下，.*会尽可能多匹配，导致后面的\d+只匹配到一个数7
# print(result1.group(1))
#
# print(result.span())



# 修饰符re.S，使.匹配包括换行
# import re
#
# content = '''Hello
# 1234567 World_This
# is a Regex Demo
# '''
# result = re.match('^He.*?(\d+).*?Demo$', content,re.S)
# print(result.group(1))

# 转义
# import re
#
# content = '(百度)www.baidu.com'
# result = re.match('\(百度\)www\.baidu\.com', content)
# print(result)


# 3. search()
# match()方法是从字符串开头进行匹配，开头不匹配就报错了
# search()可以任意位置
import re

# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# result = re.search('Hello.*Demo', content)
#
# html = '''<div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>
#         </li>
#         <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#         <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#         <li data-view="5">
#             <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
#         </li>
#     </ul>
# </div>'''

# pattern = '<li.*?active.*?singer="(.*?)">(.*?)</a>'
#
# result = re.search(pattern, html, re.S)
# print(result.group(1))
# print(result.group(2))
# print(result.group(0))
# print(result)


# 4. findall()
# 该方法会搜索整个字符串，然后返回匹配正则表达式的所有内容。
# patternall = '<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>'
# resultAll = re.findall(patternall, html, re.S)
# print(resultAll)


# 5. sub()
# 修改文本

# import re
#
# content = 'sdsc5sdsd15ds8dwd54d'
# content = re.sub('\d', '', content, 2, re.S)
# print(content)


# 6. compile()
# 这个方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用
# import re
#
# content1 = '2016-12-15 12:00'
# content2 = '2016-12-17 12:55'
# content3 = '2016-12-22 13:21'
# pattern = re.compile('\d{2}:\d{2}')
# result1 = pattern.sub('', content1)
# result2 = pattern.sub('', content2)
# result3 = pattern.sub('', content3)
# # 等同于
# #       = re.sub(pattern,'',content1)
# print(result1)
# print(result2)
# print(result3)

# [Python3网络爬虫开发实战] 3.4-抓取猫眼电影排行
# https://cuiqingcai.com/5534.html
import re
import requests
import urllib.error

import json
import requests
from requests.exceptions import RequestException
import re
import time
import random


def get_one_page(url):
    proxies = {
        'http': 'http://127.0.0.1:9876',
        'https': 'https://127.0.0.1:9876'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    try:
        response = requests.get(url, proxies=proxies, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(0, 3):
        t = random.randint(3, 4)
        main(offset=i * 10)
        time.sleep(t)
