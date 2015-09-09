# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import pika
import sys

#定义连接
credentials = pika.PlainCredentials('gdqWeb', 'BigwinWeb')
parameters = pika.ConnectionParameters('192.168.1.96',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='test_queue',durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='test_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2, #设置消息持久化
                      ))

print "[x] Sent %r" % (message,)
connection.close()