from django.core.management import BaseCommand
from products.models import Category
from orders.models import Order, StatusOrder
from django.contrib.auth import get_user_model
import random


class Command(BaseCommand):
    help = "Creates new orders"


    def handle(self, *args, **options):
        self.stdout.write("Orders creating...")
        orders_list = []
        all_users = get_user_model().objects.all()
        all_statuses = StatusOrder.values
        print(all_statuses)

        for order in range(5000):
            order = Order(
                user=random.choice(all_users),
                status=random.choice(all_statuses),
            )
            orders_list.append(order)

        Order.objects.bulk_create(orders_list)

        self.stdout.write("Categories ware created!")


