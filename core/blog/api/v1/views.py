from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ViewSet , ModelViewSet

from .serializers import PostSerializer,PostCreateSerializer
from ...models import Post , Category
from django.shortcuts import get_object_or_404

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

"""
ApiPostList APIView

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

"""

"""
ApiPostList using GenericAPIView and mixins
class ApiPostList (GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    ''' API view to handle GET and POST requests for Post list '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get (self, request, *args, **kwargs):
        ''' Handle GET request to retrieve list of posts '''
        return self.list(request, *args, **kwargs)


    def post (self, request, *args, **kwargs):
        ''' Handle POST request to create a new post '''
        return self.create(request, *args, **kwargs)

"""

"""
ApiPostList using ListAPIView and ListCreateAPIView

class ApiPostList(ListAPIView,ListCreateAPIView):
    ''' API view to handle GET requests for Post list '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
"""


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

"""
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
"""

"""
class ApiPostDetail (GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    ''' API view to handle GET, PUT, DELETE requests for a single Post '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    

    def get (self, request, *args, **kwargs):
        ''' Handle GET request to retrieve a specific post '''
        return self.retrieve(request, *args, **kwargs)
    
    def put (self, request, *args, **kwargs):
        ''' Handle PUT request to update a specific post '''
        return self.update(request, *args, **kwargs)
    
    def delete (self, request, *args, **kwargs):
        ''' Handle DELETE request to delete a specific post '''
        return self.destroy(request, *args, **kwargs)
"""

"""
ApiPostDetail using RetrieveUpdateDestroyAPIView

class ApiPostDetail (RetrieveUpdateDestroyAPIView):
    ''' API view to handle GET, PUT, DELETE requests for a single Post '''
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
"""

"""
class ApiPostViewSet(ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        ''' Handle GET request to retrieve list of posts '''
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        ''' Handle POST request to create a new post '''
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        ''' Handle GET request to retrieve a specific post '''
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def update(self, request, pk=None):
        ''' Handle PUT request to update a specific post '''
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        ''' Handle DELETE request to delete a specific post '''
        post = get_object_or_404(Post, id=pk, status=True)
        post.delete()
        return Response({"data": "Post deleted successfully"}, status=204)
"""

class ApiPostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

class ApiPostCategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostCreateSerializer
    queryset = Category.objects.all()