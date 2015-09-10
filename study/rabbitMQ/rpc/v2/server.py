# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import time
from rpyc import Service
from rpyc.utils.server import ThreadedServer
class TimeService(Service):
    def exposed_sum(self,a,b):
        print a,b
        return a+b

s=ThreadedServer(TimeService,port=12233,auto_register=False)
s.start()