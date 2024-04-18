from django.db import models



class Material(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    publication = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class MyPet(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    bread = models.CharField(null=True, blank=True, max_length=50)
    photo = models.ImageField(upload_to='users/%d/%m/%Y', blank=True, null=True, verbose_name='Фотография')
    happy_birth = models.DateTimeField(null=True, blank=True, verbose_name='Дата рождения')
    character = models.CharField(blank=False, null=False, max_length=500)
    can = models.CharField(blank=False, null=False, max_length=500)
    delicacy = models.CharField(blank=False, null=False, max_length=500)
    byaka = models.CharField(blank=True, max_length=500)
    favorite = models.CharField(blank=True, max_length=500)

