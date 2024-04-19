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
    photo = models.ImageField(upload_to='photos/%d/%m/%Y',
                              default=None, blank=True, null=True, verbose_name='Файл')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=70, unique=True, db_index=True, verbose_name='slug')
    content = models.TextField(blank=True, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время последнего редактирования')
    publication = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Publiks.choices)),
                                      default=Publiks.PUBLISHED, verbose_name='Статус')
    typepost = models.ForeignKey('TypePost', on_delete=models.PROTECT,
                                 related_name='posts', verbose_name='Тип поста')
    tags = models.ManyToManyField('TagPosts', blank=False, null=False,
                                  related_name='tags', verbose_name='Теги')

    objects = models.Manager()
    publik = PublicationManager()

    def __str__(self):
        return self.title

 #   def get_absolute_url(self):



#Сортируем по времени публикации (свежие записи-время больше находятся выше)
    class Meta:
        verbose_name = 'Мир животных'
        verbose_name_plural = 'Мир животных'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]


#Модель описывает питомца
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
    byaka = models.CharField(blank=True, max_length=500, verbose_name='Что не любит?')
    favorite = models.CharField(blank=True, max_length=500, verbose_name='Что любит?')


    class Meta:
        verbose_name = 'Мой питомец'
        verbose_name_plural = 'Мои питомцы'


class TypePost(models.Model):
    name = models.CharField(max_length=70, db_index=True, verbose_name='Тип поста')
    slug = models.SlugField(max_length=70, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип поста'
        verbose_name_plural = 'Тип поста'


class TagPosts(models.Model):
    tag = models.CharField(max_length=30, db_index=True, verbose_name='Тег')
    slug = models.SlugField(max_length=70, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Тип поста'
        verbose_name_plural = 'Тип поста'



class Animal(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class UploadFields(models.Model):
    file = models.FileField(upload_to='upload_fiel')


