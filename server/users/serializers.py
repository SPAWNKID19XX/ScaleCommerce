from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password




class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ["id","password", "email", "first_name", "last_name", "bio"]

    def validate_password(self,value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            **validated_data
        )
        return user