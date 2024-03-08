from django.conf import settings
from django.core.management.base import BaseCommand
from app.utils.consumer import RabbitMQConsumer

class Command(BaseCommand):
    def handle(self, *args, **options):
        connection_params = dict(
            host=settings.EDA_BROKER_HOST,
            port=settings.EDA_BROKER_PORT,
            userid=settings.EDA_BROKER_USER,
            password=settings.EDA_BROKER_PASSWORD,
            virtual_host=settings.EDA_VIRTUAL_HOST,
        )
        consumer = RabbitMQConsumer()
        consumer.start_consuming(connection_params, "prototype_queue")
