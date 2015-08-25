# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import pika
import random

credentials = pika.PlainCredentials('gdqWeb', 'BigwinWeb')
parameters = pika.ConnectionParameters('192.168.1.96',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# channel.queue_declare(queue='hello1') #创建消息队列名称
channel.queue_declare(queue='hello1')

number = random.randint(1,1000)
body = 'hello world:%s' % number
channel.basic_publish(exchange='',routing_key='hello1',body=body)
print " [x] Sent %s" % body
connection.close()
