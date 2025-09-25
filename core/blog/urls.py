from django.contrib import admin
from django.urls import path 
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    # path('cbv/', views.cbv.as_view(), name='cbv'),
    path('post/list/', views.postListView.as_view(), name='home'),
    path('post/detail/<int:pk>/', views.postDetailView.as_view(), name='post_detail'),
    path('post/create/', views.CreatePostView.as_view(), name='create'),
    path('post/<int:pk>/edit/', views.editPostView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='delete_post'),
]