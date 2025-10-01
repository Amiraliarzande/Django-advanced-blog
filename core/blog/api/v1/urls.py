from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api_v1'

router = DefaultRouter()

router.register('post-list', views.ApiPostViewSet, basename='post')
router.register('post-categories', views.ApiPostCategoryViewSet, basename='post-categories')

urlpatterns = router.urls
    


'''urlpatterns = [
    # path('v1/post-list/', views.ApiPostList, name='post-list'),
    # path('v1/post-list/', views.ApiPostList.as_view(), name='post-list'),
    # path('v1/post-list/<int:pk>/', views.ApiPostDetail, name='post-detail'),
    # path('v1/post-list/<int:pk>/', views.ApiPostDetail.as_view(), name='post-detail'),
    path('v1/post-list/', views.ApiPostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
    path('v1/post-list/<int:pk>/', views.ApiPostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),
]'''