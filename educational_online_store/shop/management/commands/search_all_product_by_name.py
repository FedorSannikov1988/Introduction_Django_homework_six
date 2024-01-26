from shop.models import Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Search all product by name"

    def add_arguments(self, parser):

        parser.add_argument('name', type=str, help='Name product')
        parser.add_argument('order_grading', type=str, help='Order grading product')
        parser.add_argument('number_results', type=int, help='Number output results')

    def handle(self, *args, **kwargs):

        name: str = kwargs.get('name')
        order_grading: str = kwargs.get('order_grading')
        number_results: int = kwargs.get('number_results')

        param_sort: str = '-date_and_time_additions_product'

        if order_grading == 'True':
            param_sort = 'date_and_time_additions_product'

        products = \
            Product.objects.filter(name=name).order_by(param_sort).all()

        if products:
            for product in products[:number_results]:
                self.stdout.write(str(product))
        else:
            text: str = 'Продуктов с таким названием нет в базе данных'
            self.stdout.write(str(text))
