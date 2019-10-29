from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


# 회원가입 시리얼라이저
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'phone', 'privateKey', 'address']

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user


# 접속 중인 유저 시리얼라이저
class UserSerializer(serializers.ModelSerializer):
    private_key = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'address', 'private_key']


class PrivateKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['private_key']
