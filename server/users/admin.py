from django.contrib import admin
from .models import CustomUser
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "username", "first_name", "last_name"]
    field = ["__all__"]
admin.site.register(CustomUser, UserAdmin)