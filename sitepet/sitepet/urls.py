from django.conf.urls.static import static

from pet.views import page_does_not_exist
from sitepet import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
# путь к администратору
    path('admin/', admin.site.urls),

# начало всех записей
    path('pet/', include('pet.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]

handler404 = page_does_not_exist

# добавляем статику
if settings.DEBUG:
    urlpatterns += (static(settings.MEDIA_URL,
                           document_root=settings.MEDIA_ROOT))

#
# # редактируем панель администрирования
admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Всё о животных и не только'
