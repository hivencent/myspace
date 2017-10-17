#coding:utf-8

import unittest
import os
import time
from macaca import WebDriver
from macaca import Keys
from retrying import retry
from MacacaBase import *
from swith_context import *

desired_caps = {
    'platformName': 'android',
    'app': '/Users/jinlong/Desktop/app-automation-test/macaca/app-datebao-release.apk',
    }

server_url = {
    'hostname': 'localhost',
    'port': 3456
}



class MacacaTest(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriver(desired_caps, server_url)
        self.initDriver()

    def tearDown(self):
        self.driver.quit()

    @retry
    def initDriver(cls):
        print("Retry connecting server...")
        cls.driver.init()

    def test_datebao(self):

        """welcome pictures"""
        time.sleep(3)
        BasePage(self.driver).swipe_left(steps=0.1)
        BasePage(self.driver).swipe_left(steps=0.1)
        BasePage(self.driver).swipe_left(steps=0.1)
        self.driver.wait_for_element("class_name","android.widget.ImageView").click()

        """login"""
        self.driver.wait_for_element("id","com.datebao.datebaoapp:id/main_mine").click()        #我的
        self.driver.wait_for_element("id","com.datebao.datebaoapp:id/personal_title_txt").click()       #登录/注册
        self.driver.wait_for_element("id","com.datebao.datebaoapp:id/login_phonenum_content").send_keys("18910505634")      #手机号
        self.driver.wait_for_element("id","com.datebao.datebaoapp:id/login_pwd_content").send_keys("jinlong1990")           #密码
        self.driver.wait_for_element("id","com.datebao.datebaoapp:id/login_login").click()

        """find insurance and insurance detail"""
        self.driver.wait_for_element("id","com.datebao.datebaoapp:id/find_insurance").click()
        self.driver.wait_for_element('xpath','//*[@text="悦享守护百万医疗保险"]').click()

        driver = switch_to_webview(self.driver)
        print 'driver.context',driver.context
        driver.wait_for_element('xpath','//li[@data-id=545]').click()
        driver.wait_for_element('xpath',"//li[@data-value='无社保']").click()

        time.sleep(5)


if __name__ == "__main__":
    unittest.main()