from django.urls import path

from .views import *


urlpatterns = [
    path('news/', ListNews.as_view(), name="new"),
    path('category/', Categories.as_view(), name="category_list"),
    path('search/', Search.as_view(), name="search"),
    path('tag/<slug:tag>/', ListNewsTag.as_view(), name="tag_detail"),
    path('<slug:category>/', ListNewsCategory.as_view(), name="post_list_category"),
    path('<slug:category>/<slug:slug>/', PostDetail.as_view(), name="post_detail"),

]