from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render


def pets_post(request, post_id):
    return HttpResponse(f'')


def page_does_not_exist(request, exception):
    return HttpResponseNotFound('<h1>Страница не существует</h1>')
