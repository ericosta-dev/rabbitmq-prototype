import amqp
import json
from app.models import Messages

class RabbitMQConsumer:
    def persist_message(self, message):
        msg_body = json.loads(message.body)
        Messages.objects.create(body=msg_body)
        print(f"Message persisted: {msg_body}")

    def start_consuming(self, connection_params, queue_name):
        with amqp.Connection(**connection_params) as c:
            ch = c.channel()
            ch.basic_consume(
                queue=queue_name,
                callback=self.persist_message,
                no_ack=True)
            while True:
                c.drain_events()