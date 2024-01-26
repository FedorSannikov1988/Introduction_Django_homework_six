from decimal import Decimal
from shop.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Update information about product"

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('name', type=str, help='Name product')
        parser.add_argument('description', type=str, help='Description product')
        parser.add_argument('price', type=str, help='Price product')
        parser.add_argument('quantity', type=int, help='Quantity product')

    def handle(self, *args, **kwargs):

        pk: int = kwargs.get('pk')
        name: str = kwargs.get('name')
        description: str = kwargs.get('description')
        price: str = kwargs.get('price')
        decimal_price: Decimal = Decimal(price)
        quantity: int = kwargs.get('quantity')

        product = Product.objects.filter(pk=pk).first()

        if product:
            product.name = name
            product.description = description
            product.price = decimal_price
            product.quantity = quantity
            product.save()

        self.stdout.write(f'{product}')
