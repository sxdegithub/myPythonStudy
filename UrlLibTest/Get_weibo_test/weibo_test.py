# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx

from requests import Request, Session
import json
import pymongo
from pyquery import PyQuery as pq


#
# def getPage(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
#     }
#     proxies = {'http': '127.0.0.1:1080',
#                'https': '127.0.0.1:1080'}
#     session = Session()
#     reponse = session.get(url, headers=headers, proxies=proxies)
#     print(reponse.json())



# 采用打开文本模拟get到的数据
def function_get_page(url):
    with open('cqc_weibo_response', 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(data)
        return data


def function_parse_data(data):
    if data:
        items = data.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            dic = {}
            dic['id'] = item.get('id')
            dic['text'] = item.get('text')
            # dic['text'] = pq(item.get('text')).text()

            dic['reposts_count'] = item.get('reposts_count')
            dic['attitudes_count'] = item.get('attitudes_count')
            # 返回生成器对象
            yield dic


# 将采集的数据插入到mongo
def function_save_data_to_Mongo(dics):
    db_client = pymongo.MongoClient('10.10.220.77', port=27017)
    my_db = db_client.test_db
    my_colection = my_db.WeiBo

    for dic in dics:
        my_colection.insert(dic)


if __name__ == '__main__':
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=2830678474&containerid=1076032830678474&page=2'
    data = function_get_page(url)
    dics = function_parse_data(data)
    # print(type(dic))
    # for i in dic:
    #     print(i)
    function_save_data_to_Mongo(dics)
