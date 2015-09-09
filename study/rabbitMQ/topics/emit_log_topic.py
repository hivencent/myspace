# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import pika
import sys

#主题交换机
#定义连接
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.96',5672,'/',pika.PlainCredentials('gdqWeb', 'BigwinWeb')))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)

print " [x] Sent %r:%r" % (routing_key, message)
connection.close()
