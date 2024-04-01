from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Проверка работы</h2>")


def about(request):
    return HttpResponse("<h4>Страница по нас </h4>")