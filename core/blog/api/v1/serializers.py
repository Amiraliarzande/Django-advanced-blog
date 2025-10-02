from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=200)
#     author = serializers.CharField(max_length=100)

class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name']


class PostSerializer(serializers.ModelSerializer):

    snippet_content = serializers.CharField(source='snippet_api_content', read_only=True)
    absolute_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title','category', 'author', 'content','snippet_content','status' ,'created_at', 'updated_at','published_at','absolute_url']
        read_only_fields = ['author']

    def get_absolute_url(self, obj):
        # Generate absolute URL for the post
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        # Customize representation based on presence of 'pk' in URL kwargs
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            # If 'pk' is present, remove 'snippet_content' and 'absolute_url'
            rep.pop('snippet_content')
            rep.pop('absolute_url')
        else:
            # If 'pk' is not present, remove 'content'
            rep.pop('content')

        rep['category'] = PostCreateSerializer(instance.category, context={'request': request}).data # Serialize category field
        return rep
    def create(self, validated_data):
        # Automatically set the author to the current user
        validated_data['author'] = Profile.objects.get(user__id=self.context.get('request').user.id)
        return super().create(validated_data)
    