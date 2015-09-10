# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import rpyc

c=rpyc.connect('localhost',12233)
print c.root.sum(1,2)
c.close()