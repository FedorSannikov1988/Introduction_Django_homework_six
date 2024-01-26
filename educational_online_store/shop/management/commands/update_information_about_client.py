from shop.models import Client
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Update information about client"

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Name fake client')
        parser.add_argument('email', type=str, help='Email fake client')
        parser.add_argument('phone_number', type=str, help='Phone number fake client')
        parser.add_argument('address', type=str, help='Address fake client')

    def handle(self, *args, **kwargs):

        pk: int = kwargs.get('pk')
        name: str = kwargs.get('name')
        email: str = kwargs.get('email')
        phone_number: str = kwargs.get('phone_number')
        address: str = kwargs.get('address')

        client = Client.objects.filter(pk=pk).first()

        if client:
            client.name = name
            client.email = email
            client.phone_number = phone_number
            client.address = address
            client.save()

        self.stdout.write(f'{client}')
