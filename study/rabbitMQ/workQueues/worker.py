# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import pika
import time

#定义连接
credentials = pika.PlainCredentials('gdqWeb', 'BigwinWeb')
parameters = pika.ConnectionParameters('192.168.1.96',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='test_queue',durable=True)
# print '[*] Waiting for message. To exit press CTRL+C'

def callback(ch,method,properties,body):
    print "[x] Received %r" % (body,)
    time.sleep(body.count('.'))

    print "[x] Done"
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)     #再同一时刻，不要发送超过1条消息给一个工作者（worker）,直到它已经处理了上一条消息并且作出了响应
channel.basic_consume(callback,queue='test_queue')
channel.start_consuming()