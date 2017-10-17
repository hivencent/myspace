import unittest
import os
import time
from macaca import WebDriver
from macaca import Keys
from retrying import retry
from MacacaBase import *

def switch_to_webview(driver):
    contexts = driver.contexts
    driver.context = contexts[-1]
    return driver

def switch_to_native(driver):
    contexts = driver.contexts
    # print 'native contexts:',contexts

    driver.context = contexts[0]
    return driver