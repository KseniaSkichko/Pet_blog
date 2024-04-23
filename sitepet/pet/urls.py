from django.urls import path
from .views import (
    MaterialHome, MaterialElement,
    about, mypet, account, maps, menu,
    MaterialTags, DetailMaterial,
    NuwMaterial, UpdateMaterial
)


urlpatterns = [
    path('', MaterialHome.as_view(), name='guests'),
    path('about/', about, name='about'),
    path('account/', account, name='account'),
    path('maps/', maps, name='maps'),
    path('menu/', menu, name='menu'),
    path('mypet/', mypet, name='mypet'),
    path('updat/<slug:slug>/', UpdateMaterial.as_view(), name='updat'),
    path('nuw/', NuwMaterial.as_view(), name='nuw'),
    path('post/<slug:post_slug>/', DetailMaterial.as_view(), name='post'),
    path('element/<slug:elem_slug>/', MaterialElement.as_view(), name='element'),
    path('tag/<slug:tag_slug>/', MaterialTags.as_view(), name='tag'),
]
