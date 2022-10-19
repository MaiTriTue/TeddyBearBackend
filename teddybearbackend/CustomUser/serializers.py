from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name',
                  'email', 'username', 'password', 'avatar']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])

        # user = User()
        # user.set_password(validated_data['password'])
        # user.first_name = validated_data['first_name']
        # user.last_name = validated_data['last_name']
        # user.email = validated_data['email']
        # user.username = validated_data['username']
        # user.avatar = validated_data['avatar']

        user.save()
        return user
