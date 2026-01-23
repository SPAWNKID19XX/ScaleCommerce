from os import name

from django.urls import path, include
from .views import OrderViewSet, OrderReviewViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'list', OrderViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', OrderReviewViewSet.as_view(), name='order_details'),
]