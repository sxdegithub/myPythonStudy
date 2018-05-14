# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: sx
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from  selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait


# '''
# # 跳入frame
# frame = driver.find_element_by_xpath("//iframe[@name='i']")
# frame = driver.find_element_by_xpath("//iframe[@name='i']")
# driver.switch_to.frame(frame)
#
# select = Select(driver.find_element_by_xpath("//select"))
#
# audi = select.select_by_value("audi")
#
# driver.implicitly_wait(2)
# select.select_by_index(1)
# driver.implicitly_wait(2)
# select.select_by_visible_text("Opel")
# all_selecte_options = select.all_selected_options
# options = select.options
#
# print(all_selecte_options)
# print(options)
#
#
# print(frame)
# print(select)
#
# # 跳出frame
# driver.switch_to.default_content()
# '''

# 拖拽


# 鼠标拖拽，在这个网页里面没有生效，不知道为什么 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
###################################################################
# source = driver.find_element_by_xpath("//a[contains(@href,'/index.html')]")
# target = driver.find_element_by_id("TestCode")
# 
# # target_1 = driver.find_element_by_id("bt")
# action_chains = ActionChains(driver)
# action_chains.drag_and_drop(source, target).perform()
# 
# target = driver.find_element_by_id("TestCode")
# taget = driver.find_element('By.ID',"TestCode")
# print(source.get_attribute("title"))
# print(target.text)
###################################################################
# 鼠标拖拽，在这个网页里面没有生效，不知道为什么 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑



# select = Select(driver.find_element_by_id("ss"))
# cookie = driver.get_cookie("__utma")
# print(type(cookie))
# driver.add_cookie(cookie)
# select.select_by_value()
# print(driver.page_source)


# ###################################################################
# 输入文字，点击按钮提交
# textArea = driver.find_element_by_id("TestCode")
# textArea.send_keys("啊啊啊啊")
#
# submit_btn = driver.find_element_by_xpath("//input[@value='提交代码']")
#
#
# # submit_btn.submit()
# submit_btn.click()
# ###################################################################


# ###################################################################
# # 打开新标签，切换标签
# js_open_new_window = "window.open('https://www.baidu.com')"
# driver.execute_script(js_open_new_window)
# handles = driver.window_handles
#
# sleep(2)
# driver.switch_to.window(handles[0])
# sleep(2)
# driver.switch_to.window(handles[1])
#
# print(driver.current_window_handle)
# print(handles)
#
# # driver.switch_to.window()
# ###################################################################


# ###################################################################
# # 对话框
# js_open_new_window = "window.open('http://www.w3school.com.cn/tiy/t.asp?f=hdom_alert')"
# driver.execute_script(js_open_new_window)
# handles = driver.window_handles
# driver.switch_to.window(handles[1])
# frame = driver.find_element_by_name("i")
# driver.switch_to.frame(frame)
# driver.implicitly_wait(2)
# open_alert=driver.find_element_by_xpath("//input[@value='显示消息框' and @type='button']")
# # open_alert=driver.find_element_by_xpath("/html/body/input")
# open_alert.click()
#
# # alert = driver.switch_to_alert()
# alert = driver.switch_to.alert
# print(alert.text)
#
# alert.accept()
# # alert.dismiss()
# ###################################################################


# ###################################################################
# # 前进后退
# driver.back()
# sleep(2)
# driver.forward()
# ###################################################################


###################################################################
# 显示等待
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#     )
# finally:
#     driver.quit()
###################################################################

# driver.switch_to.default_content()



