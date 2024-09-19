from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'bio']
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            bio=validated_data.get('bio', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user


class CustomUserSerializer(serializers.ModelSerializer):
    following = serializers.StringRelatedField(many=True, read_only=True)
    followers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'following', 'followers']
