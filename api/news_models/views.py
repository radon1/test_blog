from rest_framework import permissions, generics

from news_models.models import Category, Post, Tag
from .serializers import CategorySerializer, PostSerializer


class CategoryList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

