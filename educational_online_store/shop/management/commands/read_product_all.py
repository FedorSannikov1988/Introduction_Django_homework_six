from shop.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Read all product"

    def handle(self, *args, **kwargs):

        products = Product.objects.all()

        if products:
            for product in products:
                self.stdout.write(str(product))
        else:
            text: str = 'Продуктов нет в базе данных'
            self.stdout.write(text)