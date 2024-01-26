from shop.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Read product by id"

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='ID product')

    def handle(self, *args, **kwargs):

        pk: int = kwargs.get('pk')

        product = Product.objects.filter(pk=pk).first()

        if product:
            text: str = str(product)
        else:
            text: str = 'Продукта с таким ID нет в базе данных'

        self.stdout.write(text)