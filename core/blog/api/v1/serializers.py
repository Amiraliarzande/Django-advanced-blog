from rest_framework import serializers
from ...models import Post, Category

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=200)
#     author = serializers.CharField(max_length=100)

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'content', 'created_at', 'updated_at', 'status','published_at']

class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name']