import pika
import json
import time

credentials = pika.PlainCredentials('robot', 'xyz')
parameters = pika.ConnectionParameters('localhost', 5672, '/robot', credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='robot')

drive_forward_command = {
    'command_name': 'drive',
    'args': {}
}

drive_backward_command = {
    'command_name': 'drive',
    'args': {'reverse': True}
}

channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(drive_forward_command))
print("Sent drive forward command")

time.sleep(3)

channel.basic_publish(exchange='', routing_key='hello', body=json.dumps(drive_backward_command))
print("Sent drive backward command")

connection.close()
