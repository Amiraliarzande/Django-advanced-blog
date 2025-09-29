from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404

@api_view()
def apiOverview(request, pk):
    post = get_object_or_404(Post, id=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)