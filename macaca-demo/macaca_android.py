#coding:utf-8

import unittest
import os
import time
from macaca import WebDriver
from macaca import Keys
from retrying import retry

desired_caps = {
    'platformName': 'android',
    'app': '/Users/jinlong/Desktop/app-automation-test/macaca/app-datebao-debug.apk',
    'package': 'com.datebao.datebaoapp',
    'activity': 'com.datebao.datebaoapp.SparkActivity',
    'autoAcceptAlerts': 'true'
    }



def switch_to_webview(driver):
    contexts = driver.contexts
    print 'contexts',contexts
    driver.context = contexts[-1]
    return driver

def switch_to_native(driver):
    contexts = driver.contexts
    print 'contexts',contexts
    driver.context = contexts[0]
    return driver

def _get_element_size(element):
    rect = element.rect

    x_center = rect['x'] + rect['width'] / 2
    y_center = rect['y'] + rect['height'] / 2
    x_left = rect['x']
    y_up = rect['y']
    x_right = rect['x'] + rect['width']
    y_down = rect['y'] + rect['height']

    return x_left, y_up, x_center, y_center, x_right, y_down


class MacacaTest(unittest.TestCase):


    def setUp(self):
        server_url = {
            'hostname': '127.',
            'port': 3456
        }

        self.driver = WebDriver(desired_caps,)
        self.driver.init()
        # cls.initDriver()


    def test_01_login(self):
        print 'init after context:',self.driver.contexts


        """
        小米手机权限弹出：2次

        """
        #权限
        # allow_bt = self.driver.element('xpath','//*[@resource-id="android:id/button1"]')        #xiaomi element
        # allow_bt.click()
        # time.sleep(2)
        # self.driver.element('id','android:id/button1').click()              #通过resource-id查找

        #启动页
        time.sleep(5)           #确认权限后，会有一个页面跳到欢迎页的动作
        # welcome_pager_ele = self.driver.element('xpath','//*[@resource-id="com.datebao.datebaoapp:id/welcome_pager"]/android.widget.ImageView[1]')
        # self.driver.element('id','com.datebao.datebaoapp:id/welcome_pager')
        # x_left, y_up, x_center, y_center, x_right, y_down = _get_element_size(welcome_pager_ele)
        # print x_left, y_up, x_center, y_center, x_right, y_down

        # switch_to_webview(self.driver)
        # 不指定元素滑动
        y = self.driver.get_window_size()['height']
        x = self.driver.get_window_size()['width']
        print "x y",x,y
        fromX = 1 * x
        fromY = 0.5 * y
        toX = 0.25 * x
        toY = 0.5 * y

        print 'fromX fromY toX toY',fromX,fromY,toX,toY
        time.sleep(3)
        print self.driver.contexts
        switch_to_native(self.driver).touch('drag', {'fromX': fromX, 'fromY': fromY, 'toX': toX, 'toY': toY, 'steps': 1000})
        # allow_bt.touch('tap')

        # print 'self.driver.contexts',self.driver.contexts
        # switch_to_native(self.driver) \
        #     .wait_for_element_by_name(u'允许') \
        #     .click()


        time.sleep(5)



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MacacaTest)
    unittest.TextTestRunner(verbosity=1).run(suite)