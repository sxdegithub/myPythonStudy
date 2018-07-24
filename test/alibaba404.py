# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 判断阿里巴巴页面是否404

import requests
from requests.exceptions import RequestException


def get_one_page(url):
    proxies = {
        'http': 'http://127.0.0.1:9876',
        'https': 'https://127.0.0.1:9876'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    try:
        # https访问经常需要添加cerify=False来忽略证书异常
        # allow_redirects 禁止重定向
        response = requests.get(url, proxies=proxies, headers=headers, verify=False, allow_redirects=False)
        if response.status_code == 404:
            print('page 404')
            print(response.text)
        if response.status_code == 200:
            print('page 200')
        if response.status_code == 302:
            print('page 302')
        return None
    except RequestException:
        return None


if __name__ == '__main__':
    url = 'https://detail.1688.com/offer/5550539912885.html'
    get_one_page(url)
