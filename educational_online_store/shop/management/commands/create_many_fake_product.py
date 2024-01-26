import random
from shop.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create many fake product"

    def add_arguments(self, parser):

        parser.add_argument('quantity', type=int, help='Quantity fake products')

    def handle(self, *args, **kwargs):

        quantity: int = kwargs.get('quantity')

        for i in range(quantity):
            one_product = \
                Product(name=f'name_{i}',
                        description=f'description_fake_product_name_{i}',
                        price=i*random.randint(1, 10),
                        quantity=i+random.randint(1, 10))

            self.stdout.write(str(one_product))

            one_product.save()

