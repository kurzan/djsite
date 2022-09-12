from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts})

def about(request):
    return render(request, 'women/about.html')


def categories(requests, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(requests, year):
    if int(year) > 2020:
        return redirect('/')

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(requests, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
