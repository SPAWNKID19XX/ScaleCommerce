from django.urls import path, include
from.views import UserRegistrationView

urlpatterns = [
    path('sign-up', UserRegistrationView.as_view(), name='sign-up'),
]
