"""
RabbitMQ command listening server for EV3 robot bodies.
"""

import pika
import json


class CommandRelay(object):
    def __init__(self, request_processor, queue='robot'):
        credentials = pika.PlainCredentials('robot', 'xyz')
        parameters = pika.ConnectionParameters('10.0.1.5', 5672, '/robot', credentials)
        self._queue = queue
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self._queue)
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(self.on_request, queue=self._queue)
        self.request_processor = request_processor

    def start_listening(self):
        self.channel.start_consuming()
        print("Awaiting command messages over RabbitMQ.")

    def on_request(self, channel, delivery_method, msg_properties, msg_body):
        print('received: {}'.format(msg_body))
        json_msg = json.loads(msg_body)
        self.request_processor.process_request(json_msg)
