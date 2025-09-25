from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Post (models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey("accounts.Profile",on_delete=models.CASCADE)
    category = models.ForeignKey("Category",on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Category (models.Model):

    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name