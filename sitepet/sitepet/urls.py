from django.conf.urls.static import static
from sitepet import settings
from django.contrib import admin
from django.urls import path, include
from pet.views import page_does_not_exist


urlpatterns = [
# путь к администратору
    path('admin/', admin.site.urls),

# начало всех записей
    path('pet/', include('pet.urls')),
]

# добавляем статику
if settings.DEBUG:
    urlpatterns += (static(settings.MEDIA_URL,
                           documenr_root=settings.MEDIA_ROOT))

# ошибка
handler404 = page_does_not_exist

# редактируем панель администрирования
admin.site.site_header = 'Панель администрирования'
admin.site.index_title = 'Всё о животных и не только'
