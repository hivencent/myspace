# -*- coding: utf-8 -*-
__author__ = 'jinlong'

import unittest
import os
import time
from macaca import WebDriver
from macaca import Keys
from retrying import retry
from MacacaBase import *
from macaca_android import *
from swith_context import *

desired_caps = {
    'platformName': 'Android',
    'browserName': 'Chrome',
    # 'browserName': 'electron'
    # 'app': 'com.android.chrome'
}

server_url = {
    'hostname': 'localhost',
    'port': 3456
}

class MacacaTest(unittest.TestCase):

    def setUp(self):
        self.driver = WebDriver(desired_caps, server_url)
        self.driver.init()


    def test_get_url(self):
        self.driver.get("https://m.datebao.com")

        """Login"""
        #WEBVIEW
        switch_to_webview(self.driver).wait_for_element("id","icenterFooter").click()
        switch_to_webview(self.driver).wait_for_element("link text","登录").click()
        switch_to_webview(self.driver).wait_for_element("xpath","//li[@tab='prReg']").click()
        self.driver.wait_for_element("class name",'name').send_keys("18910505634")
        self.driver.wait_for_element("name",'password').send_keys("jinlong1990")
        time.sleep(1)
        self.driver.wait_for_element('class name','loginBtn').click()

        time.sleep(3)
        switch_to_webview(self.driver).wait_for_element('id','ilistFooter').click()        #点击保险
        switch_to_webview(self.driver).wait_for_element('xpath',"//li[@data-tab='jiankang']").click()

        self.driver.context = self.driver.contexts[0]
        print u'滑动前：self.driver.context',self.driver.context
        time.sleep(3)

        BasePage(self.driver).swipe_up(steps=0.05)
        time.sleep(1)
        BasePage(self.driver).swipe_up(steps=0.05)
        switch_to_webview(self.driver).wait_for_element('xpath',"//div[@class='tab tab1']//a[@href='https://m.datebao.com/product/show/543']").click()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
