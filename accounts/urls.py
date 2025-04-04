# accounts/urls.py
from django.urls import path
from .views import ClientRegistrationView

urlpatterns = [
    path('register/client/', ClientRegistrationView.as_view(), name='client_register'),
]
