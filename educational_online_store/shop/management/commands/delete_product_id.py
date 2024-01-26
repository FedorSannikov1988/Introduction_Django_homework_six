from shop.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Delete product by id"

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **kwargs):

        pk: int = kwargs.get('pk')

        product = \
            Product.objects.filter(pk=pk).first()

        self.stdout.write(f'{product}')

        if product:
            product.delete()

