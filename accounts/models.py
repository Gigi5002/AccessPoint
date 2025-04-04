# accounts/models.py
from django.db import models


class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password_hash = models.CharField(max_length=255)  # Хэш пароля
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=(('client', 'Client'), ('moderator', 'Moderator')))
    status = models.CharField(
        max_length=20,
        choices=(('active', 'Active'), ('inactive', 'Inactive'), ('banned', 'Banned')),
        default='active'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Client(User):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        self.role = 'client'
        super().save(*args, **kwargs)


class Moderator(User):
    department = models.CharField(max_length=50)
    access_level = models.IntegerField(default=1)
    employee_id = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        self.role = 'moderator'
        super().save(*args, **kwargs)
