from decimal import Decimal
from shop.models import Order, Client, Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Update information about order"

    def add_arguments(self, parser):

        parser.add_argument('pk', type=int, help='Order ID')
        parser.add_argument('client', type=int, help='Client ID')
        parser.add_argument('product', nargs='*', type=int, help='List product ID')
        parser.add_argument('total_amount_order', type=str, help='Total amount order')

    def handle(self, *args, **kwargs):

        pk: int = kwargs.get('pk')
        client_id: int = kwargs.get('client')
        list_product_id: list = kwargs.get('product')
        total_amount_order: str = kwargs.get('total_amount_order')
        total_amount_order_price: Decimal = Decimal(total_amount_order)

        client = Client.objects.filter(pk=client_id).first()

        list_products: list = []

        for product_id in list_product_id:
            product = Product.objects.filter(pk=product_id).first()
            if product:
                list_products.append(product)

        order = Order.objects.filter(pk=pk).first()

        if order:

            order.client = client
            order.total_amount_order = total_amount_order_price

            order.product.clear()
            #order.product.set([])
            #for product in order.product.all():
            #    order.product.remove(product)

            for product in list_products:
                order.product.add(product)

            order.save()

        self.stdout.write(f'{order}')
