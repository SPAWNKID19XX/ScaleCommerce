from django.urls import path, include
from .views import UserRegistrationView, UsersViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,

)

urlpatterns = [
    path('/', UsersViewSet.as_view({"get": "list"})),
    path('sign-up/', UserRegistrationView.as_view(), name='sign-up'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
