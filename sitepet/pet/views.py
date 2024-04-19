from django.http import HttpResponseNotFound, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import NuwMaterialForm
from .models import Material, TagPosts, MyPet


# функция страницы со всеми публикациями
class MaterialHome(ListView):
    context_object_name = 'material'
    template_name = 'pet/materials.html'

    def get_queryset(self):
        return (Material.publication.all().
                select_related('typepost'))




# разбивает на типы постов
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




# разбивает по тегам
class MaterialTags(ListView):
    template_name = 'pet/materials.html'
    context_object_name = 'material'
    allow_empty = False

    def get_queryset(self):
        return (Material.publication.filter
                (tag__slug=self.kwargs['tag_slag']).
                select_related('tag'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = TagPosts.objects.get(slug=self.kwargs['tags_slag'])
        context['tags_selected'] = tags.pk
        return context




# подробности и детали поста
class DetailMaterial(DetailView):
    template_name = 'pet/material_detail.html'
    slug_url_kwarg = 'material_slug'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['detail'].title
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Material.publication, slug=self.kwargs[self.slug_url_kwarg])




# создаём новый пост
class NuwMaterial(CreateView):
    model = Material
    form_class = NuwMaterialForm
    template_name = 'material/create_material'
    success_url = reverse_lazy('home')




# редактируем пост
class UpdateMaterial(UpdateView):
    model = Material
    template_name = 'material/create_material'
    fields = ['typepost', 'title', 'slug', 'photo', 'content', 'tags', 'publication']




# выдаём ошибку на несуществующую страницу
def page_does_not_exist(request, exception):
    return HttpResponseNotFound('<h1>Страница не существует</h1>')


