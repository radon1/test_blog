from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.base import View

from .models import Post, Comment, Category, Tag
from .forms import CommentForm


class ListNewsCategory(View):
    """Список статей"""
    def get(self, request, category):
        posts = Post.objects.filter(category__slug=category, publish__lte=datetime.now())
        return render(request, 'news_models/post-list.html', {"news": posts})


class ListNewsTag(View):
    """Список тегов"""
    def get(self, request, tag):
        posts = Post.objects.filter(tags__slug=tag, publish__lte=datetime.now())
        return render(request, 'news_models/post-list.html', {"news": posts})


class ListNews(View):
    """Список статей"""
    def get(self, request):
        posts = Post.objects.filter(publish__lte=datetime.now())
        # return HttpResponse(posts)
        return render(request, 'news_models/post-list.html', {"news": posts})


class Categories(ListView):
    """Список категорий"""
    model = Category
    context_object_name = "categories"
    template_name = "news_models/category-list.html"



class PostDetail(View):
    """Вывод полной статьи"""
    def get(self, request, category, slug):
        # try:
        #     post = Post.objects.get(id=pk)
        # except Post.DoesNotExist:
        #     raise Http404
        post = get_object_or_404(Post, slug=slug)
        post.count += 1
        post.save()
        comments = Comment.objects.filter(post_id=post.id)
        form = CommentForm()
        # for comment in post.comment_set.all():
        #     print(comment)
        return render(request, 'news_models/post-detail.html', {"new": post, "comments": comments, "form": form})

    def post(self, request, category, slug):
        # text = request.POST.get("text")
        # Comment.objects.create(text=text, post_id=pk)
        # print(text)
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=slug)
            form.save()
        return redirect(request.path)


class Search(View):
    """Поиск"""
    def get(self, request):
        title = request.GET.get("search_name")
        if Post.objects.filter(title__icontains=title).exists():
            title = Post.objects.filter(title__icontains=title)
        else:
            title = Post.objects.filter(category__name__icontains=title) | Post.objects.filter(tags__title__icontains=title)
        return render(request, 'news_models/post-list.html', {'news': title.distinct()})


#написать template_tag который бы выводил меню в header.html
#https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/ смотри здесь
## Here, register is a django.template.Library instance, as before
#@register.inclusion_tag('results.html')
#def show_results(poll):
#   ...
# register.simple_tag(lambda x: x - 1, name='minusone')
#
# @register.simple_tag(name='minustwo')
# def some_function(value):
#     return value - 2





# def list_post(request):
#     if request.method == "GET":
#         pass