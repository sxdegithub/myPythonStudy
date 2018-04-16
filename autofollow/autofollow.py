# 获取某个用户的关注列表
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# selenium中的actionchains的方法
from selenium.webdriver.common.action_chains import ActionChains
import time


class Shopee:
    def __init__(self):
        self.driver = webdriver.Chrome()  # chrome浏览器驱动
        self.driver.implicitly_wait(10)  # 设置隐性等待时间，等待页面加载完成才会进行下一步，最多等待10秒
        self.driver.set_window_size(1920, 1080)  # 用phantomjs必须有这行
        self.wait = WebDriverWait(self.driver, 15)
        # self.uid_login = ''  # 登录后会赋予登录用户的id值
        pass

    # 获取该页面可关注列表
    def get_follow_lis_unf(self, url):
        url = 'https://shopee.com.my/shop/52738962/followers/'
        self.driver.get(url)

        # # 语言选择弹窗,可以关闭,前面选过就不用选了
        # if self.is_element_exist('language-container'):
        #     close_select_language = self.driver.find_element_by_class_name('ic_selectlanguage_close')
        #     close_select_language.click()
        #     # choose_chinese = self.driver.find_elements_by_class_name('language-option')
        #     # choose_chinese[2].click()
        # 翻页i次
        # https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python


        SCROLL_PAUSE_TIME = 2
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        print("last_height:{}".format(last_height))
        i = 0
        while i < 2:
            # Scroll down to bottom

            a_list = self.driver.find_elements_by_xpath('//span')
            print('a_list:{}'.format(len(a_list)))
            if len(a_list) > 0:
                self.driver.execute_script("arguments[0].scrollIntoView(false);", a_list[0])
                a_list[0].click()
                # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, u'关注'))).click()
            a_list.clear()
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            print("new_height:{}".format(new_height))

            # for i in a_list:
            #     if i.is_displayed():
            #         i.click()

            if new_height == last_height:
                break
            last_height = new_height
            i += 1

        # a_list = self.driver.find_elements_by_xpath('//*[@id ='shop-followers']/ul/li[2]/div[2]/span')
        # a_list = self.driver.find_elements_by_class_name('btn-follow')
        # a_list = self.driver.find_elements_by_css_selector(
        # 'shop-followers>ul>li:nth-child(2)>div.btn-follow.follow.L14>span')

        # for i in a_list:
        #     print(i)
        # # 返回未关注用户列表
        return a_list

    # 关注j个用户
    def follow_unf(self, unf_list):
        NUM = 1
        j = 0
        if NUM > len(unf_list):
            NUM = len(unf_list)
        while j < NUM:
            for i in unf_list:
                i.click()
                # i.send_keys(Keys.ENTER)
                j += 1

    # 该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
    def is_element_exist(self, element):
        flag = True
        try:
            self.driver.find_elements_by_class_name(element)
            return flag
        except NoSuchElementException as e:
            print(e)
            flag = False
            return flag

    # 登录
    def login_shopee(self, username, password):
        self.driver.get('https://shopee.com.my/')

        # 语言选择弹窗,不能关闭,选中文
        if self.is_element_exist('language-selection'):
            # 选择中文
            # 浮层无法点击解决
            # 参考 http: // blog.sina.com.cn / s / blog_53f023270101o8c1.html
            s = self.driver.find_element_by_xpath("//*[@id ='main']/div/div/div[2]/div[1]/ div/div[3]/button[3]")
            s.send_keys(Keys.ENTER)
            # choose_zn = self.driver.find_elements_by_class_name('shopee-button-outline')
            # print(choose_zn[2])
            # ActionChains(self.driver).move_to_element(choose_zn[2]).perform()
            # # choose_zn[2].sendKeys(Keys.ENTER)
            # choose_zn[2].click()
            print('打印调试代码')

            # self.driver.implicitly_wait(1000)
            time.sleep(5)

            # login_btn = self.driver.find_elements_by_class_name('navbar__link-text--medium')[1]
            # login_btn.click()
            # username_input = self.driver.find_elements_by_class_name('input-with-status__input')[0]
            # password_input = self.driver.find_elements_by_class_name('input-with-status__input')[1]
            # username_input.send_keys(id)
            # password_input.send_keys(password)
            self.driver.find_element_by_xpath(
                "//div[@id='main']/div/div/div[2]/div[1]/div/div[1]/div/ul[2]/li[5]").click()

            self.driver.find_element_by_xpath(
                "//*[@id='main']/div/div/div[2]/div[1]/span/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div[2]/div/input") \
                .send_keys(username)
            self.driver.find_element_by_xpath(
                "//*[@id='main']/div/div/div[2]/div[1]/span/div/div[1]/div/div[2]/div[1]/div/div/div[1]/div[3]/div/input") \
                .send_keys(password)
            self.driver.find_element_by_css_selector(
                "div.auth-form-submit-cancel > button.shopee-button-solid.shopee-button-solid--primary").click()

            time.sleep(2)

if __name__ == '__main__':
    op = Shopee()
    op.login_shopee('123123@qq.com', '123')
    unfollow_user_list = op.get_follow_lis_unf('1')
    # op.follow_unf(unfollow_user_list)
