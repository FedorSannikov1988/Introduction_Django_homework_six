from shop.models import Order
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Delete order by id"

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **kwargs):

        pk: int = kwargs.get('pk')

        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'{order}')

        if order:
            order.delete()
