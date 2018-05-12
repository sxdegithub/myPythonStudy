# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.PhantomJS()
# 打开百度首页
driver.get("https://www.baidu.com")

# 搜索sb
driver.find_element_by_id(u'kw').send_keys(u'sb')
driver.find_element_by_id(u'su').click()
# 打开新窗口
new_window = 'window.open("");'
driver.execute_script(new_window)
# # 切换到新的窗口
# handles = driver.window_handles
# driver.switch_to.window(handles[-1])
# print(handles[-1].title())
# # 关闭新窗口
# driver.execute_script('window.close();')
# # 切换第一个窗口
# driver.switch_to.window(handles[0])
# driver.find_element(By.ID, u'su').click()
# 获取页面title
# 点击“百度一下”按钮时候，title被ajax刷新了，打印出来的title还是“百度一下，你就知道”，
# 实际上title已经刷新成“sb_百度搜索”
# 问题： 如何才能获取最新的title？
driver.implicitly_wait(10)
# 强制等待
# time.sleep(20)
# 刷新
# driver.refresh()
page_title = driver.title
# 等待10
driver.implicitly_wait(10)
page_title_by_xpath = driver.find_element_by_xpath('/html/head/title').text
element_title = driver.find_element_by_xpath('/html/head/title')
print(element_title)
# page_title_by_xpath = driver.find_element_by_tag_name('title').text
# page_title_by_xpath = driver.find_element_by_xpath('//title').text
js_title = 'document.title'
get_title_by_js = driver.execute_script(js_title)
print('page_title_by_xpath的值:{}'.format(page_title_by_xpath))
print('get_title_by_js的值：{}'.format(get_title_by_js))
print(page_title)

# assert "W3School" in driver.title
