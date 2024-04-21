from django.urls import path
from .views import (MaterialHome, MaterialTypePost,
                    MaterialTags, DetailMaterial,
                    NuwMaterial, UpdateMaterial)

urlpatterns = [
# все публикации (от всех)
    path('material/', MaterialHome.as_view(), name='material'),

# на форму для создания новой публикации (сылка на неё на личной страничке с животными)
    path('nuw/', NuwMaterial.as_view(), name='nuw'),

# изменить пост (на страничке с деталями поста)
    path('update/<slug:slug>/', UpdateMaterial.as_view(), name='update'),

# подробная информация поста
    path('material/<slug:material_slug>/', DetailMaterial.as_view(), name='detail'),

# разбивает по разным типам
    path('typepost/<slug:typepost_slug>/', MaterialTypePost.as_view, name='type'),

# разбивает по тегам
    path('tags/<slug:tags_slug>/', MaterialTags.as_view(), name='tag'),
]

