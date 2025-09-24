from django.contrib import admin
from django.urls import path 
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    # path('cbv/', views.cbv.as_view(), name='cbv'),
    path('list/', views.postListView.as_view(), name='home'),
    path('detail/<int:pk>/', views.postDetailView.as_view(), name='post_detail'),
    path('add/', views.addPostView.as_view(), name='add_post'),
]