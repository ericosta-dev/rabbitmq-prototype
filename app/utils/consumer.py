import amqp

class RabbitMQConsumer:
    def start_consuming(self, connection_params, queue_name):
        with amqp.Connection(**connection_params) as c:
            ch = c.channel()
            def on_message(message):
                print('Received message (delivery tag: {}): {}'.format(message.delivery_tag, message.body))
            ch.basic_consume(queue=queue_name, callback=on_message, no_ack=True)
            while True:
                c.drain_events()