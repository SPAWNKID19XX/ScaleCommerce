from django.db.models import F
from rest_framework import generics, permissions
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


