from django.db import models, transaction
from django.conf import settings
from django.db.models import Sum


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    count_viewed = models.PositiveIntegerField(default=0)

    def save(self,*args, **kwargs):
        with transaction.atomic():
            self_id = self.pk

            if self_id:
                old_price = Product.objects.get(pk=self_id).price
                new_price = self.price

                if new_price != old_price:
                    HistoryPrice.objects.create(product=self, old_price=old_price, new_price=new_price)

            super().save(*args, **kwargs)


    def __str__(self):
        return self.category.name + " - " + self.name

class HistoryPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='history_price')
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)
