

from django.db import models
from django.template.defaulttags import now
from django.urls import reverse, reverse_lazy
from django.utils import timezone


class PublicationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(publication=Material.Publiks.PUBLISHED)


class Material(models.Model):
    class Publiks(models.IntegerChoices):
        PRIVAT = 0, 'Приватно'
        PUBLISHED = 1, 'Опубликовано'
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',
                              default=None, blank=True, null=True, verbose_name='Файл')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=70, unique=True, db_index=True, verbose_name='slug')
    content = models.TextField(blank=True, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время последнего редактирования')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name='Теги')
    elem = models.ForeignKey('Element', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    publication = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Publiks.choices)),
                                      default=Publiks.PUBLISHED, verbose_name='Статус')

    objects = models.Manager()
    publik = PublicationManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мир животных'
        verbose_name_plural = 'Мир животных'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
         return reverse('post', kwargs={'post_slug': self.slug})


class Element(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категирия'

    def get_absolute_url(self):
        return reverse('element', kwargs={'elem_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=30, db_index=True, verbose_name='Тег')
    slug = models.SlugField(max_length=30, db_index=True, unique=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class UploadFieles(models.Model):
    file = models.FileField(upload_to='upload_model')



class MyPet(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, verbose_name='Имя') #Имя
    animal = models.OneToOneField('Animal', on_delete=models.PROTECT,
                                  null=False,
                                  blank=False, related_name='animal',
                                  max_length=50, verbose_name='Вид питомца')
    bread = models.CharField(null=True, blank=True, max_length=50, verbose_name='Порода')     #Порода
    photo = models.ImageField(upload_to='users/%d/%m/%Y', blank=True,
                              null=True, verbose_name='Фотография')
    happy_birth = models.DateTimeField(null=True, blank=True,
                                       verbose_name='Дата рождения')
    character = models.CharField(blank=False, null=False, max_length=500, verbose_name='Характер')
    can = models.CharField(blank=False, null=False, max_length=500, verbose_name='Что умеет?')
    delicacy = models.CharField(blank=False, null=False, max_length=500, verbose_name='Любимая еда')
    foo = models.CharField(blank=True, max_length=500, verbose_name='Что не любит?')
    favorite = models.CharField(blank=True, max_length=500, verbose_name='Что любит?')
    slug = models.SlugField(max_length=30, db_index=True, unique=True)



    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Мой питомец'
        verbose_name_plural = 'Мои питомцы'
        # ordering = ['-time_create']
        # indexes = [
        #     models.Index(fields=['-time_create'])
        # ]




class Animal(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Животное')
    slug = models.SlugField(max_length=30, db_index=True, unique=True)
    def __str__(self):
        return self.name

