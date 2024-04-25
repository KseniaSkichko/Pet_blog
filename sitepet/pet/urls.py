from django.urls import path
from .views import (
    MaterialHome, MaterialElement,
    about, account, maps, menu,
    MaterialTags, DetailMaterial,
    NuwMaterial, UpdateMaterial, NuwMyPet, MyPetView, UpdateMyPet
)


urlpatterns = [
    path('', MaterialHome.as_view(), name='guests'),
    path('about/', about, name='about'),
    path('account/', account, name='account'),
    path('maps/', maps, name='maps'),
    path('menu/', menu, name='menu'),
    path('mypet/', MyPetView.as_view(), name='mypet'),
    path('updatmat/<slug:slug>/', UpdateMaterial.as_view(), name='updat'),
    path('updatpet/<slug:slug>/', UpdateMyPet.as_view(), name='updatpet'),
    path('nuw/', NuwMaterial.as_view(),name='nuw'),
    path('post/<slug:post_slug>/', DetailMaterial.as_view(), name='post'),
    path('element/<slug:elem_slug>/', MaterialElement.as_view(), name='element'),
    path('tag/<slug:tag_slug>/', MaterialTags.as_view(), name='tag'),
    path('nuwpet/', NuwMyPet.as_view(), name='nuwpet'),
]
