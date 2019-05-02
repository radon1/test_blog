from django.contrib import admin
from .models import ContactFormModel


class ContactFormAdmin(admin.ModelAdmin):
    """Контакты"""
    list_display = ("username", "email", "date")
    readonly_fields = ("username", "date", )

admin.site.register(ContactFormModel, ContactFormAdmin)

