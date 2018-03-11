from tornado import websocket, web, ioloop
import tornado
import logging
import os
import pika
import asyncio
from threading import Thread


clients = []

def consumer_callback(ch, method, properties, body):
    print (" [x] Received %r" % (body,))
    for itm in clients:
        itm.write_message(body)

def threaded_rmq():
    asyncio.set_event_loop(asyncio.new_event_loop())
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='51.143.186.87',credentials=pika.PlainCredentials('hack24', 'hack24')));
    print ('Connected:localhost')
    channel = connection.channel()
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='hack24topic',queue=queue_name)
    print ('Consumer ready, on my_queue')
    channel.basic_consume(consumer_callback, queue=queue_name,no_ack=True) 
    channel.start_consuming()




class SocketHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        logging.info('WebSocket opened')
        print('Websocket Opened')
        clients.append(self)

    def on_close(self):
        logging.info('WebSocket closed')
        clients.remove(self)


app = web.Application([
    (r'/ws', SocketHandler),
])


if __name__ == "__main__":
    thread = Thread(target = threaded_rmq)
    thread.start()

    app.listen(8889)

    tornado.ioloop.IOLoop.instance().start()