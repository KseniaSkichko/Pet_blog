from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    photo = models.ImageField(blank=True, upload_to="users/%d/%m/%Y", null=True, verbose_name="Фотография")
    happy_birth = models.DateTimeField(null=True, blank=True, verbose_name="Дата рождения")
