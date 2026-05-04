from django.urls import path, include
from .views import send_email, test

app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("api/v1/", include("accounts.api.v1.urls")),
    path("send_email/", send_email, name="send_email"),
    path("test/", test, name="test"),
]
