# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# 百度搜索页面page,继承自Page类

from PageObject.base import Page
from  selenium.webdriver.common.by import By


class SearchPage(Page):

    # 定位器

    # 搜索输入框
    search_input = (By.ID, u'kw')
    # 百度一下按钮
    search_button = (By.ID, 'su')

    #
    def __init__(self, selenium_driver, base_url=u'https://www.baidu.com/'):
        Page.__init__(self, selenium_driver, base_url)

    # 打开百度
    def goto_baidu_homepage(self):
        print(u"打开百度首页", self.base_url)
        self.open(self.base_url)

    # 搜索框
    def input_serch_text(self, text):
        self.input_text(self.search_input, text)

    # 点击搜索按钮
    def click_search_btn(self):
        self.click(self.search_button)

