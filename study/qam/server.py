__author__ = 'jinlong'
from qam.qam_server import QAMServer
qam_server = QAMServer(hostname='192.168.1.96',
                       port=5672,
                       username='gdqWeb',
                       password='BigwinWeb',
                       vhost='/',
                       server_id='testqamjinlong')

def adder_function(x,y):
    return x+y

print 'adder_function name >>',adder_function.__name__
qam_server.register_function(adder_function,'add')

qam_server.serve()