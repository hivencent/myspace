# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import os
# print os.name
# print os.uname()
# print os.environ['PATH'] == os.getenv('PATH')        #环境变量
# print os.path.abspath('.')          #当前路径
# print os.path.join('/home/','jinlong')          #合并路径
# print os.path.split('/home/jinlong/test.log')     #拆分路径
# print os.path.splitext('/home/jinlong/test.log')            #得到文件拓展名

#序列化
try:
    import cPickle
except ImportError:
    import pickle
d = {"a":"1","b":"2"}
f = open(os.path.join(os.path.abspath('.'),'test.log'),'wb')
# f = open(os.path.join(os.path.abspath('.'),'test.log'),'rb')
g = cPickle.load(f)
f.close()
print g

# f = open('/Users/jinlong/Desktop/wanglibao_test/TestCase/API/TestCase_API.py')
#
# u = f.read().decode('utf-8')
# print u