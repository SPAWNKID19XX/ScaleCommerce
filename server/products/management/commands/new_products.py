from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from products.models import Category, Product
from faker import Faker
import faker_commerce
from django.contrib.auth import get_user_model
import random


class Command(BaseCommand):
    help = "Creates new products"
    faker = Faker(faker_commerce.Provider)

    def handle(self, *args, **options):
        self.stdout.write("Products creating...")
        all_users = get_user_model().objects.all()
        products_list = []

        for product in range(500):
            product = Product(
                name=self.faker.word(),
                brand=self.faker.word(),
                price=random.randint(100, 10000)/100,
                description=self.faker.sentence(),
                category=random.choice(Category.objects.all()),
                seller=random.choice(all_users),
                stock=random.randint(10, 100),
                is_active=True
            )
            products_list.append(product)

        Product.objects.bulk_create(products_list)
        self.stdout.write("Categories ware created!")


