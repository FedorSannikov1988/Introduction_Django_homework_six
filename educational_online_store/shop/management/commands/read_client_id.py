from shop.models import Client
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Read client by id"

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='ID client')

    def handle(self, *args, **kwargs):

        pk: int = kwargs.get('pk')

        client = Client.objects.filter(pk=pk).first()

        if client:
            text: str = str(client)
        else:
            text: str = 'Клиента с таким ID нет в базе данных'

        self.stdout.write(text)