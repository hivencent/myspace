# -*- coding: utf-8 -*-
__author__ = 'jinlong'
from wsgiref.simple_server import make_server
from helloworld import *

httpd = make_server('',8000,application)
print 'Serving HTTP on port 8000...'
httpd.serve_forever()           #监听server
print httpd.base_environ