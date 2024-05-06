from django.contrib.auth import login
from django.urls import path
from .views import (
    MaterialHome, MaterialElement,
    about, account, maps, menu,
    DetailMaterial, NuwMaterial,
    UpdateMaterial, NuwMyPet,
    MyPetView, UpdateMyPet
)


urlpatterns = [
    path('login/', login, name='login'),
    path('', MaterialHome.as_view(), name='guests'),
    path('about/', about, name='about'),
    path('account/', account, name='account'),
    path('maps/', maps, name='maps'),
    path('menu/', menu, name='menu'),
    path('mypet/', MyPetView.as_view(), name='mypet'),
    path('updatmat/<slug:slug>/', UpdateMaterial.as_view(), name='updatmat'),
    path('updatpet/<slug:updatpet_slug>/', UpdateMyPet.as_view(), name='updatpet'),
    path('nuw/', NuwMaterial.as_view(),name='nuw'),
    path('post/<slug:post_slug>/', DetailMaterial.as_view(), name='post'),
    path('element/<slug:elem_slug>/', MaterialElement.as_view(), name='element'),
    path('nuwpet/', NuwMyPet.as_view(), name='nuwpet'),
]
