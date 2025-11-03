from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated   
from accounts.models import User


from .serializers import RegistrationSerializer, CustomAuthTokenSerializer, ChangePasswordSerializer


class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "email": serializer.validated_data.get("email"),
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
class ChangePassword(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
            obj = self.request.user
            return obj
    
    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            
            if not self.object.check_password(serializer.validated_data.get("old_password")):

                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.validated_data.get("new_password1"))
            self.object.save()

            return Response({"details": "Password updated successfully"})       