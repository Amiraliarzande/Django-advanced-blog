from django.contrib import admin
from django.urls import path 
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('fbv/', views.fbv, name='fbv'),
    path('cbv/', views.cbv.as_view(), name='cbv'),
    
]