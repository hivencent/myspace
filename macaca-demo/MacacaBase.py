# -*- coding: utf-8 -*-

import os
import time

from xml.etree.ElementTree import ElementTree

from macaca import WebDriverException



class BasePage(object):

    def __init__(self,driver):
        self.driver = driver

    def _get_window_size(self):
        window = self.driver.get_window_size()
        y = window['height']
        x = window['width']

        return x, y

    @staticmethod
    def _get_element_size(element):
        rect = element.rect

        x_center = rect['x'] + rect['width'] / 2
        y_center = rect['y'] + rect['height'] / 2
        x_left = rect['x']
        y_up = rect['y']
        x_right = rect['x'] + rect['width']
        y_down = rect['y'] + rect['height']

        return x_left, y_up, x_center, y_center, x_right, y_down

    def _swipe(self, fromX, fromY, toX, toY, steps):
        print "fromX, fromY, toX, toY",fromX, fromY, toX, toY

        self.driver.touch('drag', {'fromX': fromX, 'fromY': fromY, 'toX': toX, 'toY': toY, 'duration': steps})

    def swipe_up(self, element=None, steps=0.05):
        """
        swipe up
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            x, y = self._get_window_size()
            print "_get_window_size",x,y
            fromX = 0.5*x
            fromY = 0.75*y
            toX = 0.5*x
            toY = 0.25*y

        self._swipe(fromX, fromY, toX, toY, steps)


    def swipe_left(self, element=None, steps=10):
        """
        swipe left
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_left
            toY = y_center
        else:
            x, y = self._get_window_size()
            fromX = 0.5*x
            fromY = 0.5*y
            toX = 0.15*x
            toY = 0.5*y

        self._swipe(fromX, fromY, toX, toY, steps)

