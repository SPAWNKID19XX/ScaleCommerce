from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import UserRegistrationSerializer


# Create your views here.
class UserRegistrationView(viewsets.generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]