from django.urls import path
from .. import views

urlpatterns = [
    path("", views.profileApiView.as_view(), name="profile"),
]
