# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# 实验urllib.reuest
import urllib.request
import urllib.parse

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
proxy_support = urllib.request.ProxyHandler({'http': 'localhost:9876'})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

url = "http://httpbin.org/post"
url_UInnovation = 'http://10.100.13.106/UInnovation/front/fontController/login.do'
data_UInnovation = bytes(urllib.parse.urlencode({'returnUrl': '',
                                                 'loginName': '9001@qq.com',
                                                 'password': '47ec2dd791e31e2ef2076caf64ed9b3d',
                                                 'passKey': ''}), encoding='utf8')
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# response_post = urllib.request.urlopen(url, data)
response_post = urllib.request.urlopen(url_UInnovation, data_UInnovation)
print(response_post.read().decode('utf-8'))
