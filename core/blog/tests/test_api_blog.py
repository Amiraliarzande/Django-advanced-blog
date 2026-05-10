from rest_framework.test import APIClient
from django.urls import reverse
import pytest
from datetime import datetime
from accounts.models import User


@pytest.fixture
def cuman_user():
    user = User.objects.create_user(email="amirali@gmail.com", password="Amirali@1384")
    user.is_active = True
    user.save()
    return user


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.mark.django_db
class TestApiBlog:
    def test_api_blog_response_200(self, client):
        url = reverse("blog:api_v1:post-list")
        response = client.get(url)
        assert response.status_code == 200

    def test_api_blog_post_response_401(self, client):
        url = reverse("blog:api_v1:post-list")
        data = {
            "status": True,
            "content": "dsbkjs",
            "published_at": datetime.now(),
            "title": "ksdksdnk",
        }
        response = client.post(url, data)
        assert response.status_code == 401

    def test_api_blog_post_response_201(self, cuman_user, client):
        url = reverse("blog:api_v1:post-list")
        data = {
            "status": True,
            "content": "dsbkjs",
            "published_at": datetime.now(),
            "title": "ksdksdnk",
        }
        user = cuman_user
        client.force_authenticate(user=user)
        response = client.post(url, data)
        assert response.status_code == 201
