# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from appium import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import os
from selenium.webdriver.common.by import By

PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)
)


"""
实例：
appium通过手机端Web浏览器进行自动化
"""

def wait_alter(seconds):
        count = 0
        while (count <= time):
            ncount = seconds - count
            time.sleep(1)
            print u'等待%s秒，剩余%s秒' % (seconds,ncount)
            count += 1
        return True


class AppiumUsageDemo(unittest.TestCase):

    def setUp(self):
        desired_caps={}
        # desired_caps['device'] = 'android'
        desired_caps['platformName']='Android'
        desired_caps['browserName']='Chrome'
        desired_caps['version']='7.0'
        # desired_caps['appPackage'] = 'com.datebao.datebaoapp'
        desired_caps['deviceName']='XiaoMi'       #这是测试机的型号，可以查看手机的关于本机选项获得

        # desired_caps['app'] = '/Users/jinlong/Desktop/app-automation-test/macaca/app-datebao-release.apk'    #被测试的App在电脑上的位置

        #如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
        #desired_caps['appPackage']='com.subject.zhongchou'
        #desired_caps['appActivity']='.ZhongChou'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(15)

    def scroll_to_element(self,driver,element):
        """
        滚动元素到最上方
        :param driver:
        :param element:
        :return:
        """
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def test_login(self):
        print self.driver.contexts
        self.driver.get('https://m.datebao.com/')
        """
        1. 客服元素滚动到最上方
        2. 点击客服icon
        """
        ele = self.driver.find_element(By.XPATH,'//*[@id="newHeaderBox"]/a')
        self.scroll_to_element(self.driver,ele)
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="newHeaderBox"]/a').click()
        self.driver.switch_to.context('CHROMIUM')           #切换到CHROMIUM
        time.sleep(10)

        # #切换到WEBVIEW模式
        # driver.switch_to.context('WEBVIEW')
        # print self.driver.contexts
        #
        #
        # # print self.driver.page_source     #打印页面元素
        #
        # #判断页面是否有对话框
        # # time.sleep(10)
        # driver.implicitly_wait(15)
        # head = driver.find_element_by_class_name('popup-head').text
        # print head
        # button = driver.find_element_by_class_name('popup-buttons')
        # button_text = button.text
        # print button_text
        # #点击确定button
        # button.click()
        # time.sleep(1)
        # #获取当前的activity
        # print '取当前的activity',driver.current_activity
        # # print driver.find_element_by_class_name('loading').get_attribute()
        # #用CSS获取input指定类型的标签
        #
        # text = driver.find_element_by_css_selector('input[type=text]')
        # if text.get_attribute('placeholder') == u'用户名':
        #     text.send_keys('13298764321')
        #
        # password = driver.find_element_by_css_selector('input[type=password]')
        # if password.get_attribute('placeholder') == u'密码':
        #     password.send_keys('123qwe')
        #
        # driver.find_element_by_xpath('/html/body/div[3]/div[2]/ion-modal-view/ion-content/div[4]/button').click()
        #
        #
        # time.sleep(5)
        #

        # self.driver.tap([(64, 822), (174, 936)], 500).start_client()
        # self.driver.tap([(64,822,174990)])


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumUsageDemo)
    unittest.TextTestRunner(verbosity=1).run(suite)