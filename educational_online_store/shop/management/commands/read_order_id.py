from shop.models import Order
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Read order by id"

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='ID order')

    def handle(self, *args, **kwargs):

        pk: int = kwargs.get('pk')

        order = Order.objects.filter(pk=pk).first()

        if order:
            text: str = str(order)
        else:
            text: str = 'Заказа с таким ID нет в базе данных'

        self.stdout.write(text)