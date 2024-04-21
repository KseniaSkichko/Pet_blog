from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import NuwMaterialForm
from .models import Material, TagPosts



kart = [{'title': 'Карта','name_ur': 'map'},
        {'title': 'Аккаунт','name_ur': 'about'}]
# функция страницы со всеми публикациями
class MaterialHome(ListView):
    context_object_name = 'material'
    template_name = 'pet/materials.html'
    model = Material
    context = {
        'title': 'Интересное, полезное и смешное',
        'kart': kart,
        'type_sel': 1,
    }

    #def get_queryset(self):
      #  return Material.publik.all().select_related('typepost')





# разбивает на типы постов
class MaterialTypePost(ListView):
    template_name = 'pet/materials.html'
    context_object_name = 'material'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        typepost = context['material'][0].typepost
        context['title'] = typepost.name
        context['kart'] = kart
        context['type_sel'] = typepost.pk
        return context

    def get_queryset(self):
        return (Material.publik.
                filter(typepost__slug=self.kwargs['typepost_slug']).
                select_related('typepost'))




# разбивает по тегам
class MaterialTags(ListView):
    template_name = 'pet/materials.html'
    context_object_name = 'material'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tags = TagPosts.objects.get(slug=self.kwargs['tags_slug'])
        context['title'] = tags.tag
        context['kart'] = kart
        context['type_sel'] = None
        return context

    def get_queryset(self):
        return (Material.publik.filter
                (tag__slug=self.kwargs['tags_slug']).
                select_related('tag'))




# подробности и детали поста
class DetailMaterial(DetailView):
    model = Material
    template_name = 'pet/material/material_detail.html'
    slug_url_kwarg = 'material_slug'
    context_object_name = 'detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['detail'].title
        context['kart'] = kart
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Material.publik, slug=self.kwargs[self.slug_url_kwarg])




# создаём новый пост
class NuwMaterial(CreateView):
    form_class = NuwMaterialForm
    template_name = 'material/nuw_material'
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Новый пост',
        'kart': kart,
    }




# редактируем пост
class UpdateMaterial(UpdateView):
    model = Material
    template_name = 'material/nuw_material'
    fields = ['typepost', 'photo', 'title',
              'content', 'tags', 'publication']
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Редактирование',
        'kart': kart,
    }






# выдаём ошибку на несуществующую страницу
def page_does_not_exist(request, exception):
    return HttpResponseNotFound('<h1>Страница не существует</h1>')


