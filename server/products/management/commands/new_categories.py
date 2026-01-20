from django.core.management import BaseCommand
from products.models import Category


class Command(BaseCommand):
    help = "Creates new categories"
    PRODUCT_CATEGORIES = (
        "electronics",
        "computers",
        "smartphones",
        "accessories",
        "home_appliances",
        "furniture",
        "clothing",
        "shoes",
        "beauty_health",
        "sports",
        "toys",
        "automotive",
        "tools",
        "office_supplies",
        "food_beverages",
        "books",
        "pet_supplies",
        "garden",
        "construction",
        "services",
    )


    def handle(self, *args, **options):
        self.stdout.write("Categories creating...")
        categories_list = []

        for category in self.PRODUCT_CATEGORIES:
            category = Category(
                name=category,
                slug=category,
            )
            categories_list.append(category)

        Category.objects.bulk_create(categories_list)

        self.stdout.write("Categories ware created!")


