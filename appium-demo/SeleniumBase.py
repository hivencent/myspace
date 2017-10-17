# -*- coding: utf-8 -*-
__author__ = 'jinlong'
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait         #等待某个条件出发后再继续执行代码
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class NewWebDriverUtil(object):
    """
    新版webdriver二次封装
    """

    def __init__(self,driver):
        self.driver = driver
        self.wait = NewWaitUtil(self.driver)

    def search_element(self, loc):
        # self.wait.wait_until_presence(loc)
        return self.driver.find_element(*loc)

    def clear_keys(self, loc):
        self.search_element(loc).clear()

    def input_text(self,loc, value):
        # self.wait.wait_until_visibility(loc)
        self.clear_keys(loc)
        time.sleep(0.5)
        self.search_element(loc).send_keys(value)

    def click(self, loc):
        self.wait.wait_until_clickable(loc)
        self.search_element(loc).click()

    def get_text(self,loc):
        return self.search_element(loc).text

    def is_element_present(self,loc):
        #元素是否存在
        self.driver.implicitly_wait(1)
        try:
            self.search_element(loc)
        except NoSuchElementException, e:
            return False
        return True

    def is_element_visibility(self,loc):
        #元素是否显示
        try:
            the_element = EC.visibility_of_element_located(loc)
            assert the_element(self.driver)
            flag = True
        except Exception, e:
            flag = False
        return flag

    def is_alert_present(self):
        """
        是否有alert
        :param driver:
        :return:
        """
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException, e:
            return False
        return True

class NewWaitUtil(object):
    """
    新版等待方法
    """

    def __init__(self,driver):
        self.time_out = 5
        self.driver = driver

    # 等待某元素可点击
    def wait_until_clickable(self, loc,time_out = 5):
        WebDriverWait(self.driver, time_out).until(
            EC.element_to_be_clickable(loc)
        )

    # 等待某元素显示,切高宽大于0
    def wait_until_visibility(self, loc):
        WebDriverWait(self.driver, self.time_out).until(
            EC.visibility_of_element_located(loc)
        )


    # 等待某元素不显示
    def wait_until_not_visibility(self, loc):
        WebDriverWait(self.driver, self.time_out).until_not(
            EC.visibility_of_element_located(loc)
        )

    # 等待一个元素存在，并不意味着元素是可见的
    def wait_until_presence(self, loc):
        WebDriverWait(self.driver, self.time_out).until(
            EC.presence_of_element_located(loc)
        )

    # 等待一个元素不存在 如渐变的JS弹出框
    def wait_until_not_presence(self, loc):
        WebDriverWait(self.driver, 5).until_not(
            EC.presence_of_element_located(loc)
        )