# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import time

class AppiumBase():

    def __init__(self,driver):
        self.driver = driver

    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)


    def swipeUp(self, t):
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

    def wait_alter(self,seconds):
        count = 0
        while (count <= time):
            ncount = seconds - count
            time.sleep(1)
            print u'等待%s秒，剩余%s秒' % (seconds, ncount)
            count += 1
        return True