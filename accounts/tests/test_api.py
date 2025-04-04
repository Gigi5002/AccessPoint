import pytest
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_registration():
    client = APIClient()
    url = reverse('register')
    data = {
        "username": "testuser",
        "password": "testpass123",
        "email": "test@example.com"
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201