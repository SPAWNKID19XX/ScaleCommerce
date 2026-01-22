from django.db.models import F, Sum, Count, Avg
from rest_framework import generics, permissions, request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .permitions import PutDeleteUpdateOrReadOnly
from .serializers import ProductSerializer

# Create your views here.
class ProductsAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.select_related("category", "seller").filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)

class ProductAPIRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related("category", "seller").filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = (PutDeleteUpdateOrReadOnly,)

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get("pk")
        Product.objects.filter(pk=product_id).update(count_viewed=F("count_viewed") + 1)
        return self.retrieve(request, *args, **kwargs)


class StatProductAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user

        queryset = Product.objects.get_queryset().filter(
            seller=user
        ).aggregate(
            total_views=Sum('count_viewed'),
            avg_views=Avg('count_viewed'),
            total_products=Count('id'),
            totat_sold=Sum(F('product__price') * F('product__quantity')),
        )

        print(queryset)

        return Response(queryset)
