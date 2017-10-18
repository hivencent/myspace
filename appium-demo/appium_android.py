# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from appium import webdriver
from selenium.webdriver.common.by import By
import unittest, time
import os
from AppiumBase import *
from SeleniumBase import *

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)


class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='7.0'
        # desired_caps['platformVersion']='6.0.1'
        desired_caps['deviceName']='XiaoMi'       #这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['appPackage'] = 'com.datebao.datebaoapp'
        # desired_caps['recreateChromeDriverSessions'] = 'True'
        desired_caps['unicodeKeyboard'] = "True"
        desired_caps['resetKeyboard'] = "True"
        desired_caps['app'] = PATH('/Users/jinlong/Desktop/app-automation-test/macaca/app-datebao-release.apk')    #被测试的App在电脑上的位置

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(15)


    def test_login(self):

        """boot page"""
        time.sleep(3)
        for i in range(1,4,1):
            time.sleep(0.5)
            AppiumBase(self.driver).swipLeft(t=500)
        self.driver.find_element(By.CLASS_NAME,"android.widget.ImageView").click()      #内置API

        """login"""
        self.driver.find_element(By.ID,"com.datebao.datebaoapp:id/main_mine").click()
        self.driver.find_element(By.ID,"com.datebao.datebaoapp:id/personal_title_txt").click()
        self.driver.find_element(By.ID,"com.datebao.datebaoapp:id/login_phonenum_content").send_keys("18910505634")
        self.driver.find_element(By.ID,"com.datebao.datebaoapp:id/login_pwd_content").send_keys("jinlong1990")
        self.driver.find_element(By.ID,"com.datebao.datebaoapp:id/login_login").click()

        """find insurance"""
        self.driver.find_element_by_id("com.datebao.datebaoapp:id/find_insurance").click()
        self.driver.find_element_by_xpath('//*[@text="悦享守护百万医疗保险"]').click()
        time.sleep(2)

        """config insurance detail"""
        print 'detail contexts',self.driver.contexts
        self.driver.switch_to.context("WEBVIEW_com.datebao.datebaoapp")
        NewWebDriverUtil(self.driver).click((By.XPATH,"//li[@data-id=545]"))
        NewWebDriverUtil(self.driver).click((By.XPATH,"//li[@data-value='无社保']"))
        print self.driver.page_source

        time.sleep(5)





    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=1).run(suite)