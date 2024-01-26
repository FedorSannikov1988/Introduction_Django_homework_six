from shop.models import Order
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Delete all orders"

    def handle(self, *args, **kwargs):

        orders = Order.objects.all()

        if orders:
            for order in orders:
                self.stdout.write(str(order))
                order.delete()
        else:
            text: str = 'Заказов нет в базе данных'
            self.stdout.write(text)
