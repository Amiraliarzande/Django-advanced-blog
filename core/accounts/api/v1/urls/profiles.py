from django.urls import path, include
from .. import views

urlpatterns = [
    path("", views.profileApiView.as_view(), name="profile"),
]
