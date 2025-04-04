# accounts/serializers.py
from rest_framework import serializers
from .models import Client
import re


class ClientRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['login', 'password_hash', 'email', 'first_name', 'last_name', 'phone']

    def validate_password_hash(self, value):
        errors = []

        # Проверки пароля
        if len(value) < 8:
            errors.append("Password must be at least 8 characters long")
        if not re.search(r'[A-Z]', value):
            errors.append("Password must contain at least one uppercase letter")
        if not re.search(r'[a-z]', value):
            errors.append("Password must contain at least one lowercase letter")
        if not re.search(r'\d', value):
            errors.append("Password must contain at least one digit")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            errors.append("Password must contain at least one special character")

        if errors:
            raise serializers.ValidationError(errors)
        return value  # В реальном проекте хэшировать пароль здесь или в view