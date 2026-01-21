from rest_framework import serializers

from .models import Category, Product
from ..users.serializers import UserShortSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Category.objects.all(),
        many=False,
        source='category'
    )
    seller = UserShortSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'brand', 'price','description', 'category', 'seller', 'stock','is_active', 'created_at')
        read_only_fields = ('id', 'category','seller','created_at')