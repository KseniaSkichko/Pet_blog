from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import MyPet, Material


class MaterialHome(ListView):
    context_object_name = 'material'
    template_name = 'pet/materials.html'

    def get_queryset(self):
        return (Material.publication.all().
                select_related('typepost'))


class MaterialTypePost(ListView):
    template_name = 'pet/materials.html'
    context_object_name = 'material'
    allow_empty = False

    def get_queryset(self):
        return (Material.publication.filter
                (typepost__slug=self.kwargs['typepost_slag']).
                select_related('typepost'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        typepost = context['material'][0].typepost
        context['typepost_selected'] = typepost.pk
        return context


class MaterialTags(ListView):
    template_name = 'pet/materials.html'
    context_object_name = 'material'
    allow_empty = False

    def get_queryset(self):
        return (Material.publication.filter
                (tag__slug=self.kwargs['tag_slag']).
                select_related('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = context['material'][0].typepost
        context['tags_selected'] = tags.pk
        return context


def page_does_not_exist(request, exception):
    return HttpResponseNotFound('<h1>Страница не существует</h1>')
