from rest_framework.permissions import BasePermission

class MyIsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_authenticated and obj.user_id == request.user.id