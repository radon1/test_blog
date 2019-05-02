from django import forms
from .models import ContactFormModel


class ContactForm(forms.ModelForm):
    '''Форма для комментариев'''
    class Meta:
        model = ContactFormModel
        fields = ('text', 'email', 'username')
        widgets = {

        }
