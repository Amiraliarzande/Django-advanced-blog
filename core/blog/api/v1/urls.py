from django.urls import path , include
from . import views

app_name = 'api_v1'

urlpatterns = [
    path('v1/post-list/', views.ApiPostList, name='post-list'),
    path('v1/post-list/<int:pk>/', views.ApiPostDetail, name='post-detail'),
]