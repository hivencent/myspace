# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from appium import webdriver
from selenium.webdriver.common.by import By
import unittest
import os
from SeleniumBase import *
from AppiumBase import *



PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)


"""
实例：
appium通过手机端Web浏览器进行自动化
"""

class H5Elements(object):

    def __init__(self):
        self.mine = (By.ID, "icenterFooter")
        self.login_link = (By.LINK_TEXT, "登录")
        self.login_tab = (By.XPATH, "//li[@tab='prReg']")
        self.login_name = (By.CLASS_NAME, "name")
        self.login_pwd = (By.NAME, "password")
        self.login_button = (By.CLASS_NAME, "loginBtn")

        self.insurance_footer = (By.ID,"ilistFooter")
        self.insurance_tab_jiankang = (By.XPATH,"//li[@data-tab='jiankang']")


class AppiumUsageDemo(unittest.TestCase):

    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['browserName']='Chrome'
        desired_caps['version']='7.0'
        desired_caps['deviceName']='XiaoMi'

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(15)


        self.webdriver = NewWebDriverUtil(self.driver)
        self.wait = NewWaitUtil(self.driver)
        self.elements = H5Elements()

    def _scroll_to_element(self,driver,element):
        """
        滚动元素到最上方
        :param driver:
        :param element:
        :return:
        """
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def test_datebao(self):
        print self.driver.contexts
        self.driver.get('https://m.datebao.com/')

        """登录"""
        self.webdriver.click(self.elements.mine)
        self.webdriver.click(self.elements.login_link)
        self.webdriver.click(self.elements.login_tab)
        self.webdriver.input_text(self.elements.login_name,"18910505634")
        self.webdriver.input_text(self.elements.login_pwd,"jinlong1990")
        self.webdriver.click(self.elements.login_button)

        """保险footer"""
        self.webdriver.click(self.elements.insurance_footer)
        self.webdriver.click(self.elements.insurance_tab_jiankang)

        '''
        """向下滑动查找元素方式一：_scroll_to_element"""
        product_element_543 = self.webdriver.search_element((By.XPATH,"//div[@class='tab tab1']//a[@href='https://m.datebao.com/product/show/543']"))
        self._scroll_to_element(self.driver,product_element_543)
        print "第一次滚动 product_element_543"
        time.sleep(2)
        product_element_198 = self.webdriver.search_element((By.XPATH,"//div[@class='tab tab1']//a[@href='https://m.datebao.com/product/show/198']"))
        self._scroll_to_element(self.driver,product_element_198)
        print "第二次滚动 product_element_198"
        time.sleep(2)
        product_element_8 = self.webdriver.search_element((By.XPATH,"//div[@class='tab tab1']//a[@href='https://m.datebao.com/product/show/8']"))
        self._scroll_to_element(self.driver,product_element_8)
        print "第三次滚动 product_element_8"
        '''

        """向下滑动查找元素方式二："""
        #切换NATIVE
        self.driver.switch_to.context("NATIVE_APP")
        for i in range(1,2,1):
            time.sleep(i)
            AppiumBase(self.driver).swipeUp(t=800)
            print "第%s次滑动完成" % i

        """进入产品详情页"""
        #切换WEBVIEW
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.webdriver.click((By.XPATH,"//div[@class='tab tab1']//a[@href='https://m.datebao.com/product/show/543']"))
        self.webdriver.click((By.XPATH,"//li[@data-id=545]"))
        self.webdriver.click((By.XPATH,"//li[@data-value='无社保']"))

        time.sleep(5)



    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumUsageDemo)
    unittest.TextTestRunner(verbosity=1).run(suite)