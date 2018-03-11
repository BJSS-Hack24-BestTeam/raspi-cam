import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='51.143.186.87',credentials=pika.PlainCredentials('hack24', 'hack24')))
channel = connection.channel()

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='hack24topic',queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,     queue=queue_name,     no_ack=True)

 
channel.start_consuming()