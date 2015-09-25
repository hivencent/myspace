# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import pika
import sys
import uuid

class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.96',5672,'/',pika.PlainCredentials('gdqWeb', 'BigwinWeb')))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)     #为回复（replies）声明独享的回调队列
        self.callback_queue = result.method.queue
        print 'callback_queue >>',self.callback_queue
        self.channel.basic_consume(self.on_response,no_ack=True,
                                   queue=self.callback_queue)   #订阅这个回调队列，以便接收RPC的响应

    def on_response(self,ch,method,props,body):
        if self.corr_id == props.correlation_id:
            self.response = body
            print 'on_response corr_id',self.corr_id

    def call(self,n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        print 'call corr_id >>',self.corr_id
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body = str(n))

        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()
print " [x] Requesting fib(30)"
response = fibonacci_rpc.call(30)
print " [.] Got %r" % (response,)
