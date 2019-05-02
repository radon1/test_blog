from django.urls import path

from .views import *


urlpatterns = [
    path('', FormView.as_view(), name="contact_form"),
]