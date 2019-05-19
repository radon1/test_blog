

from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('Категория', max_length=100)
    slug = models.SlugField('Url', max_length=100, default='')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_list')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Tag(models.Model):
    '''Класс Тегов статей'''
    title = models.CharField('Тег', max_length=50)
    slug = models.SlugField("Url", max_length=55)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


class Post(models.Model):
    """Статья"""
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Изображение", upload_to="post/", null=True, blank=True)
    short_text = models.TextField("Превью", default='')
    text = models.TextField("Текст статьи")
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, null=True)
    slug = models.SlugField('Url', max_length=100, default='', unique=True)
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    count = models.IntegerField(verbose_name='Просмотры', default=0)
    created = models.DateTimeField("Дата создания", auto_now_add=True, null=True)
    publish = models.DateTimeField("Опубликовать", default=timezone.now)
    #позволяет видеть в админке название статьи

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_list_category', kwargs={"category": self.category.slug})

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    """Модель комментариев"""
    post = models.ForeignKey(Post, verbose_name="Статья", on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    date = models.DateTimeField("Дата", auto_now_add=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"category": self.post.category.slug, "slug": self.post.slug})

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


#создать модель тегов и завязать посты с помощью manytomany
#учет количества просмотров на странице(int поле)
