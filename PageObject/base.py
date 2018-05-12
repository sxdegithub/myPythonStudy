# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
# 用于封装基础Page类
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException


class Page(object):
    # 页面基础类，用于所有页面继承

    base_url = 'http://'

    def __init__(self, selenium_driver, base_url, ):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    # 使用title断言进入的页面是否正确
    def on_page(self, pagetile):
        return pagetile in self.driver.title

    # # 使用单下划线开头的方法，在使用import导入时候，不会导入，作为类的私有方法
    # def _open(self, url):
    #     self.driver.get(url)
    #     self.driver.maximize_window()
    #     # 校验打开窗口标题是否正确
    #     # assert self.on_page(pagetitle), u"打开开页面失败 %s" % url

    # 调用_open进行打开
    def open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    # 重写元素定位方法
    # 传入多个参数，比如：传入（'By.ID'，'value'）
    def find_element(self, *loc):
        try:
            # 显示等待
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except WebDriverException as e:
            print("元素不存在:%s", e)

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to.frame(loc)

    # 重写js执行方法
    def script(self, jscript):
        return self.driver.execute_script(jscript)

    # def send_keys(self,loc,value,clear_first=True,click_first=True):
    #     try:
    #         # 不是很理解这句
    #         loc = getattr(self,'_%s'%loc)
    #         if click_first:
    #             self.find_element(*loc).click()
    #         if clear_first:
    #             self.find_element(*loc).clear()
    #             self.find_element(*loc).send_keys(value)
    # 重写click
    def click(self, loc):
        self.find_element(*loc).click()

    # 重写sendkeys
    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def get_title(self):
        return self.driver.title
