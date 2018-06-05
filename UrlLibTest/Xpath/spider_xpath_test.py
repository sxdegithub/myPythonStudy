# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# [Python3网络爬虫开发实战] 4.1-使用XPath
# From：https://cuiqingcai.com/5545.html

from lxml import etree

# # 补齐节点标签，生成etree对象，并转化为string
######################################################################
# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))
######################################################################

######################################################################
# # 和上面的一样，也可以直接对文件进行解析
# from lxml import etree
#
# html = etree.parse('.\\test.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result)
# # 6.子节点
# # 使用/与//
# # 定位到div节点,再获取div节点后的文本
# divPoint = html.xpath('//div/text()')
# print(divPoint)
#
# # 7.父节点
# # 定位到其他节点
# # 定位到父节点方法1
# item0Point = html.xpath("// a[ @ href = 'link5.html']/../@class")
# print(item0Point)
#
# # 定位到父节点方法2
# item1Point = html.xpath("//a[@href = 'link4.html']/parent::*/@class")
# print(item1Point)


# 9. 文本获取,上面6中有
# from lxml import etree
# html = etree.parse('.\\test.html',etree.HTMLParser())
# textPoint = html.xpath("//a[@href = 'link3.html']/text()")
# print(textPoint)
# print(type(textPoint))
#
#
# html1 = etree.parse('./test.html', etree.HTMLParser())
# # 这样定位返回的结果是一个列表，包含calss=‘item-0’的2个节点下的文本，以及li下换行符节点，一共三个节点
# result = html1.xpath('//li[@class="item-0"]//text()')
# print(result)
# # 打印结果：['first item', 'fifth item', '\r\n         ']
# # windows换行是\n\r,linux下是\n，mac os下是\r


# 10. 属性获取
# 获取节点中的属性值
from lxml import etree

html = etree.parse('.\\test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)

result1= html.xpath("//li[@class = 'item-0']/a/@href")
result2= html.xpath("//li[contains(@class,'item-0' ) and @id='item']/a/@href" )

print(result1)
print(result2)
######################################################################
