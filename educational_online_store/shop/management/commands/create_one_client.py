from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from shop.models import Client, for_phone_number_validation


class Command(BaseCommand):
    help = "Create one client"

    def add_arguments(self, parser):

        parser.add_argument('name', type=str, help='Name client')
        parser.add_argument('email', type=str, help='Email client')
        parser.add_argument('phone_number', type=str, help='Phone number client')
        parser.add_argument('address', type=str, help='Address client')

    def handle(self, *args, **kwargs):

        name: str = kwargs.get('name')
        email: str = kwargs.get('email')
        phone_number: str = kwargs.get('phone_number')
        address: str = kwargs.get('address')

        try:
            for_phone_number_validation(phone_number)
        except ValidationError as error:
            self.stderr.write(str(error))
            return

        client = Client(name=name,
                        email=email,
                        phone_number=
                        phone_number,
                        address=address)

        self.stdout.write(str(client))

        client.save()
