from django.contrib import admin
from .models import OrderItem,Order
# Register your models here.
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity',)
    fields = ('order', 'product', 'price', 'quantity',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','status','total_amount','created_at', 'updated_at')
    fields = ('user','status','total_amount')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
