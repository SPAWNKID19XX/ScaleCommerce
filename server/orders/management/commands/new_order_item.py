from django.core.management import BaseCommand
from products.models import Category, Product
from orders.models import Order, OrderItem
from faker import Faker
import faker_commerce
from django.contrib.auth import get_user_model
import random


class Command(BaseCommand):
    help = "Creates new order Item"

    def handle(self, *args, **options):
        self.stdout.write("Products creating...")
        all_orders =list(Order.objects.all())
        all_products = list(Product.objects.all())
        order_item = []
        orders_update = []

        for order in all_orders:
            order_total = 0

            for obj in range(random.randint(1,10)):
                product = random.choice(all_products)
                price_product = product.price
                quantity = random.randint(1,10)
                order_total += quantity * price_product

                new_order_item = OrderItem(
                    order=order,
                    quantity = quantity,
                    product = product,
                    price=price_product,
                )

                order_item.append(new_order_item)

            order.total_amount = order_total
            orders_update.append(order)

        OrderItem.objects.bulk_create(order_item)
        Order.objects.bulk_update(orders_update, ["total_amount"])

        self.stdout.write("order items ware created!")


