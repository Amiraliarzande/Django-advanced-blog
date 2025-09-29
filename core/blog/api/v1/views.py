from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post

@api_view()
def apiOverview(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)