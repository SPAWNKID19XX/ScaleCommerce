from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import UserRegistrationSerializer, CustomUserViewSetSerializer


# Create your views here.
class UserRegistrationView(viewsets.generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class UsersViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserViewSetSerializer
    permission_classes = [permissions.IsAdminUser]

