from django.shortcuts import render
from rest_framework import viewsets
from hitcount.views import HitCountDetailView
from .models import Post, UserProfile, Comment, Category
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, UserProfileSerializer
# Create your views here.


class PostViewSet(viewsets.ModelViewSet, HitCountDetailView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    count_hit = True


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
