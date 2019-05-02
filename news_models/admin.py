from django.contrib import admin

from .models import Post, Comment, Category, Tag


class CommentInlines(admin.StackedInline):
    """Инлайн"""
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Админка статей"""
    list_display = ("id", "title", "category", "count", "created", "publish")
    list_display_links = ("title",)
    list_filter = ("category", "tags")
    search_fields = ("title", "count")
    inlines = [CommentInlines]
    list_editable = ("count",)
    prepopulated_fields = ({"slug": ("title",)})
    # fieldsets = (
    #     (None, {
    #         'fields': ('title', 'short_text', 'text', 'slug')
    #     }),
    #     ('Advanced options', {
    #         'classes': ('collapse',),
    #         'fields': ('category', 'tags'),
    #     }),
    #     ('test', {
    #         "fields": ("count",),
    #     })
    # )
    readonly_fields = ("count", )


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "date")


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = ({"slug": ("title",)})


admin.site.register(Category)
#admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.site_header = "Rado Admin"
admin.site.site_title = "Rado Admin Portal"
admin.site.index_title = "Welcome to Rado Researcher Portal"
