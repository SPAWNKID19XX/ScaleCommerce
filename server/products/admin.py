from django.contrib import admin
from .models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    fields = ('name', 'slug',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'seller', 'stock', 'is_active', 'price', 'description', 'created_at')
    fields = ('name', 'category', 'brand', 'seller', 'stock', 'price')
    readonly_fields = ('created_at',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

