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
        driver = self.driver

        #先滑动欢迎图
        time.sleep(5)
        # print '欢迎页contexts',self.driver.contexts
        BasePage(self.driver).swipe_left(steps=0.2)
        BasePage(self.driver).swipe_left(steps=0.2)
        BasePage(self.driver).swipe_left(steps=0.2)
        driver.wait_for_element("class_name","android.widget.ImageView").click()
        driver.wait_for_element("id","com.datebao.datebaoapp:id/find_insurance").click()
        driver.wait_for_element('xpath','//*[@text="悦享守护百万医疗保险"]').click()

        driver = switch_to_webview(driver)
        print 'driver.context',driver.context
        driver.wait_for_element('xpath','//li[@data-id=545]').click()
        driver.wait_for_element('xpath',"//li[@data-value='无社保']").click()

        time.sleep(5)
        pass


if __name__ == "__main__":
    unittest.main()