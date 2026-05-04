from django.urls import path, include
from .. import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("jwt/create/", jwt_views.TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", jwt_views.TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", jwt_views.TokenVerifyView.as_view(), name="jwt_verify"),
    path("registration/", views.RegistrationView.as_view(), name="registration"),
    path("login/", views.CustomAuthToken.as_view(), name="login"),
    path("logout/", views.LogoutTokenApiView.as_view(), name="logout"),
    path("change_password/", views.ChangePassword.as_view(), name="change_password"),
]
