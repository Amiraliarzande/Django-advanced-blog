from django.urls import path, include
from . import views

app_name = 'api_v1'

urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.CustomAuthToken.as_view(), name='login'),
]