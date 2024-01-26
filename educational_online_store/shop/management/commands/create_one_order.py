from decimal import Decimal
from shop.models import Order, Client, Product
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create one order"

    def add_arguments(self, parser):

        parser.add_argument('client', type=int, help='ID client')
        #parser.add_argument('product', type=int, help='ID product')
        parser.add_argument('product', nargs='*', type=int, help='List product ID')
        parser.add_argument('total_amount_order', type=str, help='Total amount order')

    def handle(self, *args, **kwargs):

        client_id: int = kwargs.get('client')
        list_product_id: list = kwargs.get('product')
        total_amount_order: str = kwargs.get('total_amount_order')
        total_amount_order_price: Decimal = Decimal(total_amount_order)

        client = \
            Client.objects.filter(pk=client_id).first()

        list_products: list = []

        for product_id in list_product_id:

            product = Product.objects.filter(pk=product_id).first()

            if product:
                list_products.append(product)

        text = None

        if client and list_products:

            new_order = Order(client=client,
                              total_amount_order=
                              total_amount_order_price)
            new_order.save()
            #new_order.product.add(product)
            #new_order.product.set([product])

            for product in list_products:
                new_order.product.add(product)

            text = new_order

        self.stdout.write(str(text))
