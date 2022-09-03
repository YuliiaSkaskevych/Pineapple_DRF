from .models import Post, Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'heading', 'text', 'create']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'post', 'publish']
