from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import UploadFileForm, NuwMaterialForm, NuwMyPets
from .models import Material, UploadFieles, MyPet

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

    def get_queryset(self):
        return MyPet.objects.all().select_related()



@login_required
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


class NuwMaterial(LoginRequiredMixin, CreateView):
    form_class = NuwMaterialForm
    template_name = 'pet/nuw_post.html'
    extra_context = {
        'title': 'Создать запись',
        'top': top,
    }

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class NuwMyPet(LoginRequiredMixin, CreateView):
    form_class = NuwMyPets
    template_name = 'pet/nuw_pet.html'
    extra_context = {
        'title': 'Создать питомца',
        'top': top,
    }


class DetailMaterial(DetailView):
    model = Material
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
    template_name = 'pet/nuw_post.html'
    fields = ['elem', 'title',
              'content', 'photo', 'publication']
    success_url = reverse_lazy('guests')
    extra_context = {
        'title': 'Редактирование',
        'top': top,
    }

class UpdateMyPet(UpdateView):
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'mypet'
    model = Material
    template_name = 'pet/nuw_pet.html'
    fields = [
        'name', 'animal', 'bread',
        'photo', 'character', 'can',
        'delicacy', 'foo', 'favorite'
    ]
    success_url = reverse_lazy('mypet')
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




def page_does_not_exist(request, exception):
     return HttpResponseNotFound('<h1>Страница не существует</h1>')
