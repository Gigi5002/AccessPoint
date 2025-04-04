import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_successful_client_registration():
    client = APIClient()
    url = reverse('client_register')
    data = {
        "login": "john_doe",
        "password_hash": "Passw0rd!",
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "phone": "+1234567890"
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert "token" in response.data


@pytest.mark.django_db
def test_failed_client_registration():
    client = APIClient()
    url = reverse('client_register')
    data = {
        "login": "john_doe",
        "password_hash": "pass",
        "email": "john@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "phone": "+1234567890"
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert "errors" in response.data
    assert len(response.data["errors"]) > 0