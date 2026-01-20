from django.core.management import BaseCommand
from faker import Faker
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Creates new users"

    def handle(self, *args, **options):
        fake = Faker()
        User = get_user_model()
        create_users_list = []

        for i in range(10):
            unique_email = fake.unique.email()
            user = User(
                email=unique_email,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                bio=fake.text(),
                is_staff= False,
                is_superuser= False,
                is_active= True
            )
            user.set_password('admin')
            create_users_list.append(user)
        self.stdout.write("Add new users...")
        User.objects.bulk_create(create_users_list)

        self.stdout.write("users ware created!")


