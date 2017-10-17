# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from appium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest, time, re
import os

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)


def wait_alter(seconds):
        count = 0
        while (count <= time):
            ncount = seconds - count
            time.sleep(1)
            print u'等待%s秒，剩余%s秒' % (seconds,ncount)
            count += 1
        return True


class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        # desired_caps['device'] = 'android'
        desired_caps['platformName']='Android'
        # desired_caps['platformVersion']='7.0'
        desired_caps['platformVersion']='6.0.1'
        desired_caps['deviceName']='XiaoMi'       #这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['appPackage'] = 'com.datebao.datebaoapp'
        desired_caps['recreateChromeDriverSessions'] = 'True'
        # desired_caps['androidProcess'] = 'com.tencent.mm:tools'

        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'

        desired_caps['app'] = PATH('/Users/jinlong/Desktop/app-automation-test/macaca/app-datebao-release.apk')    #被测试的App在电脑上的位置

        #如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
        #desired_caps['appPackage']='com.subject.zhongchou'
        #desired_caps['appActivity']='.ZhongChou'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(15)

    # 获得机器屏幕大小x,y
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipeUp(self,t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self,t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        # print "fromx,fromy,tox,toy",x1,y1,x2,y1
        self.driver.swipe(x1, y1, x2, y1, t)


    def test_login(self):

        driver = self.driver
        time.sleep(3)
        print '启动成功 ',driver.contexts
        # driver.switch_to.context('WEBVIEW_com.android.quicksearchbox')

        print '进入欢迎页 ',driver.contexts
        # ←滑动
        self.swipLeft(800)
        # time.sleep(1)
        self.swipLeft(800)
        # time.sleep(1)
        self.swipLeft(800)
        # time.sleep(1)
        driver.find_element_by_class_name('android.widget.ImageView').click()
        # print 'driver.current_context',driver.current_context

        print "点击找保险："
        driver.find_element_by_id("com.datebao.datebaoapp:id/find_insurance").click()
        driver.find_element_by_xpath('//*[@text="悦享守护百万医疗保险"]').click()

        #切换到产品详情webview
        print '进入产品详情webview ',driver.contexts
        driver.switch_to.context("NATIVE_APP")
        driver.switch_to.context("WEBVIEW_com.datebao.datebaoapp")
        print '在详情页切换webview模式：',driver.current_context
        # print driver.page_source
        driver.find_element(By.XPATH,"//li[@data-id=545]").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//li[@data-value='无社保']").click()
        time.sleep(5)



    # def is_element_present(self, how, what):
    #     try: self.driver.find_element(by=how, value=what)
    #     except NoSuchElementException, e: return False
    #     return True



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=1).run(suite)