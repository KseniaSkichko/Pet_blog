from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


elems_db = [{'id': 1, 'name': 'Статьи'},
            {'id': 2, 'name': 'Смешное'},
            {'id': 3, 'name': 'Милое'},
            {'id': 4, 'name': 'Коммиксы'},]

top = [{'title':'Это Я', 'url_name': 'account'},
       {'title':'Мои питомцы', 'url_name': 'mypet'},
       {'title':'Карта', 'url_name': 'maps'},
       {'title':'Меню', 'url_name': 'menu'}]

pet = [
    {'id': 1, 'name': 'Mila', 'description': 'smal, clever, happy', 'age': '1', 'is_pablik': True},
    {'id': 2, 'name': 'Tosha', 'description': 'average, clever, elderly', 'age': '10', 'is_pablik': False},
]
def index(request):
    context = {'title': 'Интересное и полезное',
               'top': top,
               'posts': pet,
               'elem_selected': 0,
               }
    return render(request, 'pet/index.html', context)


def about(request):
    context = {
               'title': 'Карта/помощь',
               'top': top,
              }
    return render(request, 'pet/about.html', context)


def see_post(request, post_id):
    return HttpResponse(f'Отображение поста: {post_id}')


def account(request):
    return HttpResponse('Это Я')


def mypet(request):
    return HttpResponse('Мои питомцы')

def maps(request):
    return HttpResponse('Карта')


def menu(request):
    return HttpResponse('Меню')

def see_element(request, elem_id):
    context = {'title': 'Просмотр по элементам',
               'top': top,
               'posts': pet,
               'elem_selected': elem_id,
               }
    return render(request, 'pet/index.html', context)


def page_does_not_exist(request, exception):
     return HttpResponseNotFound('<h1>Страница не существует</h1>')
































# from django.http import HttpResponseNotFound
# from django.shortcuts import get_object_or_404
# from django.urls import reverse_lazy
# from django.views.generic import ListView, DetailView, CreateView, UpdateView
#
# from .forms import NuwMaterialForm
# from .models import Material, TagPosts
#
#
#
# kart = [{'title': 'Карта','name_ur': 'map'},
#         {'title': 'Аккаунт','name_ur': 'about'}]
# # функция страницы со всеми публикациями
# class MaterialHome(ListView):
#     context_object_name = 'material'
#     template_name = 'pet/materials.html'
#     model = Material
#     context = {
#         'title': 'Интересное, полезное и смешное',
#         'kart': kart,
#         'type_sel': 1,
#     }
#
#     def get_queryset(self):
#         return Material.publik.all().select_related('typepost')
#
#
#
#
#
# # разбивает на типы постов
# class MaterialTypePost(ListView):
#     template_name = 'pet/materials.html'
#     context_object_name = 'material'
#     allow_empty = False
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         typepost = context['material'][0].typepost
#         context['title'] = typepost.name
#         context['kart'] = kart
#         context['type_sel'] = typepost.pk
#         return context
#
#     def get_queryset(self):
#         return (Material.publik.
#                 filter(typepost__slug=self.kwargs['typepost_slug']).
#                 select_related('typepost'))
#
#
#
#
# # разбивает по тегам
# class MaterialTags(ListView):
#     template_name = 'pet/materials.html'
#     context_object_name = 'material'
#     allow_empty = False
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         tags = TagPosts.objects.get(slug=self.kwargs['tags_slug'])
#         context['title'] = tags.tag
#         context['kart'] = kart
#         context['type_sel'] = None
#         return context
#
#     def get_queryset(self):
#         return (Material.publik.filter
#                 (tag__slug=self.kwargs['tags_slug']).
#                 select_related('tag'))
#
#
#
#
# # подробности и детали поста
# class DetailMaterial(DetailView):
#     model = Material
#     template_name = 'pet/detail/material_detail.html'
#     slug_url_kwarg = 'detail_slug'
#     context_object_name = 'detail'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = context['detail'].title
#         context['kart'] = kart
#         return context
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(Material.publik, slug=self.kwargs[self.slug_url_kwarg])
#
#
#
#
# # создаём новый пост
# class NuwMaterial(CreateView):
#     form_class = NuwMaterialForm
#     template_name = 'material/nuw_material'
#     success_url = reverse_lazy('home')
#     extra_context = {
#         'title': 'Новый пост',
#         'kart': kart,
#     }
#
#
#
#
# # редактируем пост
# class UpdateMaterial(UpdateView):
#     model = Material
#     template_name = 'material/nuw_material'
#     fields = ['typepost', 'photo', 'title',
#               'content', 'tags', 'publication']
#     success_url = reverse_lazy('home')
#     extra_context = {
#         'title': 'Редактирование',
#         'kart': kart,
#     }
#
#
#
#
#
#
# # выдаём ошибку на несуществующую страницу
# def page_does_not_exist(request, exception):
#     return HttpResponseNotFound('<h1>Страница не существует</h1>')
#
#
