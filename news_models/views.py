from datetime import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View

from .models import Post, Comment, Category, Tag
from .forms import CommentForm


class ListNewsView(ListView):
    model = Post
    queryset = Post.objects.filter(publish__lte=datetime.now())
    context_object_name = "news"
    template_name = "news_models/post-list.html"

    def get_queryset(self):
        if self.kwargs.get("category", None) is not None:
            self.queryset = Post.objects.filter(category__slug=self.kwargs.get("category"), publish__lte=datetime.now())
        elif self.kwargs.get("tag", None) is not None:
            self.queryset = Post.objects.filter(tags__slug=self.kwargs.get("tag"), publish__lte=datetime.now())
        return self.queryset


# class ListNewsCategory(View):
#     """Список статей"""
#     def get(self, request, category):
#         posts = Post.objects.filter(category__slug=category, publish__lte=datetime.now())
#         return render(request, 'news_models/post-list.html', {"news": posts})


# class ListNewsTag(View):
#     """Список тегов"""
#     def get(self, request, tag):
#         posts = Post.objects.filter(tags__slug=tag, publish__lte=datetime.now())
#         return render(request, 'news_models/post-list.html', {"news": posts})

#
# class ListNews(View):
#     """Список статей"""
#     def get(self, request):
#         posts = Post.objects.filter(publish__lte=datetime.now())
#         # return HttpResponse(posts)
#         return render(request, 'news_models/post-list.html', {"news": posts})


class Categories(ListView):
    """Список категорий"""
    model = Category
    context_object_name = "categories"
    template_name = "news_models/category-list.html"


class PostDetailView(DetailView, CreateView):
    model = Post
    context_object_name = "new"
    template_name = 'news_models/post-detail.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new"].count += 1
        context["new"].save()
        context["comments"] = Comment.objects.filter(post_id=context["new"].id)
        context["form"] = CommentForm()
        return context

    def form_valid(self, form):
        form.instance.post = Post.objects.get(slug=self.kwargs.get("slug"))
        form.save()
        return super().form_valid(form)



# class PostDetail(View):
#     """Вывод полной статьи"""
#     def get(self, request, category, slug):
#         # try:
#         #     post = Post.objects.get(id=pk)
#         # except Post.DoesNotExist:
#         #     raise Http404
#         post = get_object_or_404(Post, slug=slug)
#         post.count += 1
#         post.save()
#         comments = Comment.objects.filter(post_id=post.id)
#         form = CommentForm()
#         # for comment in post.comment_set.all():
#         #     print(comment)
#         return render(request, 'news_models/post-detail.html', {"new": post, "comments": comments, "form": form})
#
#     def post(self, request, category, slug):
#         # text = request.POST.get("text")
#         # Comment.objects.create(text=text, post_id=pk)
#         # print(text)
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.post = Post.objects.get(slug=slug)
#             form.save()
#         return redirect(request.path)


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