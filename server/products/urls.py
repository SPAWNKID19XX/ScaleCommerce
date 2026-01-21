from django.urls import path, include
from .views import ProductsAPIView,ProductAPIRetrieve
from rest_framework import routers

urlpatterns = [
    path('', ProductsAPIView.as_view(), name='products-list'),
    path('<int:pk>/', ProductAPIRetrieve.as_view(), name='products-detail'),
]
