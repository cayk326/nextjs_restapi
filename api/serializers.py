from rest_framework import serializers
from .models import Task, Post
from django.contrib.auth.models import User

# ユーザーモデル作成用シリアライザ
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# Postモデル用シリアライザー
class PostSerializer(serializers.ModelSerializer):
    # crated_atを変換しておく
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at')

# Taskモデル用シリアライザー
class TaskSerializer(serializers.ModelSerializer):
    # crated_atを変換しておく
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at')