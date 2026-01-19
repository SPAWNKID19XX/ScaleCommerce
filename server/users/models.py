from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email, password=None, **extra_fields):
        if not email: raise ValueError('Users must have an email address, and it should be unique')

        email = self.normalize_email(email).lower()
        user = self.model(email=email, **extra_fields)

        if password:
            user.set_password(password)
        else:
            raise ValueError('Users must have a password.')

        user.save(using=self._db)
        return user

    def create_superuser(self,email, password = None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if (
            (extra_fields.get('is_staff') is not True) or
            (extra_fields.get('is_superuser') is not True) or
            (extra_fields.get('is_active') is not True)
        ):
            raise ValueError('Superuser must have is_staff=True and is_superuser=True')
        user = self.create_user(email, password, **extra_fields)
        return user



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    username = None
    bio = models.TextField(blank=True, null=True)
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
