from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from ...models import User  # Assuming User model is imported from appropriate location

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('email', 'password', 'password1')

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if password != attrs.get('password1'):
            raise serializers.ValidationError({"detail": "Passwords do not match."})
        
        try:
            validate_password(password)

        except serializers.ValidationError as e:

            raise serializers.ValidationError({"detail": e.messages})

        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password1')
        user = User.objects.create_user(**validated_data)
        return user


        

    