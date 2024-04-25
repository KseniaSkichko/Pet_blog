from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import UploadFileForm, NuwMaterialForm, NuwMyPets
from .models import Material, TagPost, UploadFieles

elems_db = [{'id': 1, 'name': 'Статьи'},
            {'id': 2, 'name': 'Смешное'},
            {'id': 3, 'name': 'Милое'},
            {'id': 4, 'name': 'Коммиксы'},]

top = [{'title': 'Мои питомцы', 'url_name': 'mypet'},
       {'title': 'Карта', 'url_name': 'maps'},
       {'title': 'Меню', 'url_name': 'menu'}]


class MaterialHome(ListView):
    context_object_name = 'posts'
    template_name = 'pet/materials.html'
    extra_context = {
        'title': 'Интересное, полезное и смешное',
        'top': top,
        'elem_selected': 0,
    }

    def get_queryset(self):
        return Material.publik.all().select_related('elem')


class MyPetView(ListView):
    context_object_name = 'mypets'
    template_name = 'pet/mypet_list.html'
    extra_context = {
        'title': 'Мои питомцы',
        'top': top,
    }




def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFieles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    context = {
        'title': 'Карта',
        'top': top,
        'form': form
    }
    return render(request, 'pet/about.html', context=context)


class NuwMaterial(CreateView):
    form_class = NuwMaterialForm
    template_name = 'pet/nuw_post.html'
    extra_context = {
        'title': 'Создать запись',
        'top': top,
    }

class NuwMyPet(CreateView):
    form_class = NuwMyPets
    template_name = 'pet/nuw_pet.html'
    extra_context = {
       'title': 'Создать питомца',
        'top': top,
    }


class DetailMaterial(DetailView):
    template_name = 'pet/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        context['top'] = top
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Material.publik,
                                 slug=self.kwargs[self.slug_url_kwarg])


class UpdateMaterial(UpdateView):
    model = Material
    template_name = 'material/nuw_post.html'
    fields = ['elem', 'title',
              'content', 'photo', 'tag', 'publication']
    success_url = reverse_lazy('guests')
    extra_context = {
        'title': 'Редактирование',
        'top': top,
    }


def account(request):
    return HttpResponse('Это Я')




def maps(request):
    return HttpResponse('Карта')


def menu(request):
    return HttpResponse('Меню')


class MaterialElement(ListView):
    template_name = 'pet/materials.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return (Material.publik.
                filter(elem__slug=self.kwargs['elem_slug']).
                select_related('elem'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        elem = context['posts'][0].elem
        context['title'] = 'Категория - ' + elem.name
        context['top'] = top
        context['elem_selected'] = elem.pk
        return context




class MaterialTags(ListView):
    template_name = 'pet/materials.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        context['title'] = 'Тег: ' + tag.tag
        context['top'] = top
        context['elem_selected'] = None
        return context

    def get_queryset(self):
        return (Material.publik.filter
                (tags__slug=self.kwargs['tag_slug']).
                select_related('elem'))


def page_does_not_exist(request, exception):
     return HttpResponseNotFound('<h1>Страница не существует</h1>')
