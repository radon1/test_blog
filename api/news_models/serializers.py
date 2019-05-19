from rest_framework import serializers

from news_models.models import Category, Post, Tag


class CategorySerializer(serializers.ModelSerializer):
    """Сериализация категорий"""
    class Meta:
        model = Category
        fields = ("name", "slug")


class TagSerializer(serializers.ModelSerializer):
    """Сериализация тегов"""
    class Meta:
        model = Tag
        fields = ("title", "slug")


class PostSerializer(serializers.ModelSerializer):
    """Сериализация постов"""
    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ("title", 'short_text', 'category', 'tags', 'created', 'publish')
