from django.contrib import admin
from django.urls import path, include
from pet.views import page_does_not_exist


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pet.urls')),
]


handler404 = page_does_not_exist()