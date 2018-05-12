# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
import time
from selenium import webdriver
from PageObject.baiduSearchPage import SearchPage
import unittest


class TestSearchPage(unittest.TestCase):
    # class TestSearchPage():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def testSearch(self):
        driver = self.driver
        url = u'https://www.baidu.com/'
        # 搜索文本
        text = 'sb'
        assert_title = u'sb_百度搜索'
        search_Page = SearchPage(driver, url)
        # 打开百度首页
        search_Page.goto_baidu_homepage()
        # 输入关键词
        search_Page.input_serch_text(text)
        # time.sleep(5)

        # 点击搜索
        search_Page.click_search_btn()

        driver.implicitly_wait(10)
        title = search_Page.get_title()
        print(title)
        driver.implicitly_wait(10)
        time.sleep(2)
        # 验证标题
        driver.refresh()
        self.assertEqual(title, assert_title)

        print(search_Page.get_title())

        def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
    # a = TestSearchPage()
    # a.testSearch()
