__author__ = 'jinlong'
from qam.qam_proxy import QAMProxy, QAMMethodNotFoundException, QAMException

qam_proxy = QAMProxy(hostname='192.168.1.96',
                      port=5672,
                      username='gdqWeb',
                      password='BigwinWeb',
                      vhost='/',
                      server_id='testqamjinlong',
                      client_id='qamproxy')

result = qam_proxy.add(2,3)
result1 = qam_proxy.echo_title('')
print result
print result1

qam_proxy.close()

