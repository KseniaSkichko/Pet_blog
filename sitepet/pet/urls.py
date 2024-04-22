from django.conf.urls.static import static
from sitepet import settings
from django.contrib import admin
from django.urls import path, include
from .views import (index, about, see_post,
                    account, maps, mypet, menu, see_element)



urlpatterns = [
    path('', index, name='guests'),
    path('about/', about, name='about'),
    path('account/', account, name='account'),
    path('maps/', maps, name='maps'),
    path('menu/', menu, name='menu'),
    path('mypet/', mypet, name='mypet'),
    path('post/<int:post_id>/', see_post, name='post'),
    path('element/<int:elem_id>/', see_element, name='element'),
]














# from django.urls import path
# from .views import (MaterialHome, MaterialTypePost,
#                     MaterialTags, DetailMaterial,
#                     NuwMaterial, UpdateMaterial)
#
# urlpatterns = [
# # все публикации (от всех)
#     path('material/', MaterialHome.as_view(), name='material'),
#
# # на форму для создания новой публикации (сылка на неё на личной страничке с животными)
#     path('nuw/', NuwMaterial.as_view(), name='nuw'),
#
# # изменить пост (на страничке с деталями поста)
#
# # подробная информация поста
#     path('detail/<slug:detail_slug>/', DetailMaterial.as_view(), name='detail'),
#     path('update/<slug:slug>/', UpdateMaterial.as_view(), name='update'),
#
# # разбивает по разным типам
#     path('typepost/<slug:typepost_slug>/', MaterialTypePost.as_view, name='type'),
#
# # разбивает по тегам
#     path('tags/<slug:tags_slug>/', MaterialTags.as_view(), name='tag'),
# ]
#
