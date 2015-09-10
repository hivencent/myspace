# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import rpyc

c=rpyc.connect('localhost',22)
print c.root.sum(1,2)
c.close()