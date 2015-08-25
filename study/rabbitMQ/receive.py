# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import pika

credentials = pika.PlainCredentials('gdqWeb', 'BigwinWeb')
parameters = pika.ConnectionParameters('192.168.1.96',5672,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)


channel.basic_consume(callback,queue='client.sync.queue',no_ack=True)
channel.start_consuming()