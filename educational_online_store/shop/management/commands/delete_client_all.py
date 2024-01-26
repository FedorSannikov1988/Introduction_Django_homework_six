from shop.models import Client
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Delete all сlients"

    def handle(self, *args, **kwargs):

        clients = Client.objects.all()

        if clients:
            for client in clients:
                self.stdout.write(str(client))
                client.delete()
        else:
            text: str = 'Клиентов нет в базе данных'
            self.stdout.write(text)
