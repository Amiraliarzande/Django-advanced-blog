from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

'''
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def ApiPostList(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''  
class ApiPostList (APIView):
    ''' API view to handle GET and POST requests for Post list '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    def get (self, request):
        ''' Handle GET request to retrieve list of posts '''
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post (self, request):
        ''' Handle POST request to create a new post '''
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


'''
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def ApiPostDetail(request, pk):

    post = get_object_or_404(Post, id=pk, status=True)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        post.delete()
        return Response({"data": "Post deleted successfully"}, status=204)
'''

class ApiPostDetail (APIView):
    ''' API view to handle GET, PUT, DELETE requests for a single Post '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get (self, request, pk):
        ''' Handle GET request to retrieve a specific post '''
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put (self, request, pk):
        ''' Handle PUT request to update a specific post '''
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete (self, request, pk):
        ''' Handle DELETE request to delete a specific post '''
        post = get_object_or_404(Post, id=pk, status=True)
        post.delete()
        return Response({"data": "Post deleted successfully"}, status=204)