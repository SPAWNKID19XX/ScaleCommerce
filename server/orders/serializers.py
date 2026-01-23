from itertools import product

from django.db import transaction
from rest_framework import serializers

from .models import Order, OrderItem
from products.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'quantity', 'price')
        read_only_fields = ('id', 'order', 'product', 'quantity', 'price')


class OrderSerializer(serializers.ModelSerializer):
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    order_items=OrderItemSerializer(many=True,read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'user', 'order_items',"total_amount", 'status')

    def create(self, validated_data):
        order_items = validated_data.pop('order_items')
        total = 0
        order_item_to_create = []


        order_quantity = {item['product'].id : item['quantity'] for item in order_items}
        products = Product.objects.filter(id__in=order_quantity.keys()).select_for_update()

        with transaction.atomic():
            order = Order.objects.create(user=self.context['request'].user, total_amount=0)
            for product in products:
                if product.stock < order_quantity[product.id]:
                    raise serializers.ValidationError("We can't add more items than we have")

                total += product.price*order_quantity[product.id]
                product.stock -= order_quantity[product.id]
                order_item_to_create.append(
                    OrderItem(
                        order=order,
                        product=product,
                        quantity=order_quantity[product.id],
                        price=product.price
                    )
                )
            order.total_amount = total
            order.save()
            Product.objects.bulk_update(products, ['stock'])
            OrderItem.objects.bulk_create(order_item_to_create)