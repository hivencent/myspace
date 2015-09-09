# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import pika
import sys

#定义连接
credentials = pika.PlainCredentials('gdqWeb', 'BigwinWeb')
parameters = pika.ConnectionParameters('192.168.1.96',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or 'info:Hello World!'
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print "[x] Sent %r" % (message,)
connection.close()