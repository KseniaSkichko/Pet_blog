from django.db import models


#Проверяем опубликовано или приватно
class PublicationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(publication=Material.Publiks.PRIVAT)

#Модель описывает публикации(контент
class Material(models.Model):
    class Publiks(models.IntegerChoices):
        PRIVAT = 0, 'Приватно'
        PUBLISHED = 1, 'Опубликовано'
    title = models.CharField(max_length=255)    #название
    slug = models.SlugField(max_length=70, unique=True, db_index=True)   #слаг (запись сверху, в поле поиска
    content = models.TextField(blank=True)     #текс записи (описания)
    time_create = models.DateTimeField(auto_now_add=True)     #время создания
    time_update = models.DateTimeField(auto_now=True)       #время обновления
    publication = models.BooleanField(choices=Publiks.choices,
                                      default=Publiks.PUBLISHED)   #приватно или нет
    typepost = models.ForeignKey('TypePost', on_delete=models.PROTECT,
                                 related_name='posts')   #тип поста
    tags = models.ManyToManyField('TagPosts', blank=False, null=False,
                                  related_name='tags')

    objects = models.Manager()
    publik = PublicationManager()

    def __str__(self):
        return self.title


#Сортируем по времени публикации (свежие записи-время больше находятся выше)
    def Meta():
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]


#Модель описывает питомца
class MyPet(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50) #Имя
    animal = models.OneToOneField('Animal', on_delete=models.PROTECT,
                                  null=False,
                                  blank=False, related_name='animal',
                                  max_length=50)
    bread = models.CharField(null=True, blank=True, max_length=50)     #Порода
    photo = models.ImageField(upload_to='users/%d/%m/%Y', blank=True,
                              null=True, verbose_name='Фотография')
    happy_birth = models.DateTimeField(null=True, blank=True,
                                       verbose_name='Дата рождения')
    character = models.CharField(blank=False, null=False, max_length=500)
    can = models.CharField(blank=False, null=False, max_length=500)
    delicacy = models.CharField(blank=False, null=False, max_length=500)
    byaka = models.CharField(blank=True, max_length=500)
    favorite = models.CharField(blank=True, max_length=500)


class TypePost(models.Model):
    name = models.CharField(max_length=70, db_index=True)
    slug = models.SlugField(max_length=70, unique=True, db_index=True)

    def __str__(self):
        return self.name


class TagPosts(models.Model):
    tag = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=70, unique=True, db_index=True)

    def __str__(self):
        return self.tag


class Animal(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

