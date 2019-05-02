from django import template

from news_models.models import Category

register = template.Library()


@register.inclusion_tag('tags/menu_tag.html')
def menu(style=False):
    return {"style": style}


@register.inclusion_tag('tags/category_tag.html')
def category_list():
    return {"list_category": Category.objects.all()}

