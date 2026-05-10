from . import views
from rest_framework.routers import DefaultRouter

app_name = "api_v1"

router = DefaultRouter()

router.register("post-list", views.ApiPostViewSet, basename="post")
router.register(
    "post-categories", views.ApiPostCategoryViewSet, basename="post-categories"
)

urlpatterns = router.urls
