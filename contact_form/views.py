from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.base import View

from .models import *
from .forms import ContactForm


class FormView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact_form/forms.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        # Redirect back to the same page if the data
        # was invalid
        else:
            return render(request, 'contact_form/forms.html', {'form': form})
        return redirect(request.path)


'''
def form_view(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, 'contact_form/forms.html', {'form': form})
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        # Redirect back to the same page if the data
        # was invalid
        #else:
            #return render(request, 'contact_form/forms.html', {'form':form})
        return redirect(request.path)
'''
#добавить в админке поля вывода мейл и даты, добавить фильтр чтобы можно было соортировать данные
#в модель добавить поле автозаполнения даты
# в самом view сделать if form not valid(высылать сообщиние при успешном или не успешой отправке формы