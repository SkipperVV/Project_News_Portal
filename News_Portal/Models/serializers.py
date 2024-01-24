from .models import Post, Comment, Author
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
   class Meta:
       model = Post
       fields = ['url', 'id', 'author', 'title', 'text', ]


class CommentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Comment
       fields = ['url', 'id', 'post', 'text', ]


class AuthorSerializer(serializers.ModelSerializer):
   class Meta:
       model = Author
       fields = ['url', 'id', 'user', 'is_active', 'rating',]