import pika
import sys
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

# message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message = {"a":"aditya"}
channel.basic_publish(exchange='logs', routing_key='', body=json.dumps(message))
print(" [x] Sent %r" % message)
connection.close()