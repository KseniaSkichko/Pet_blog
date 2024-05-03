from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Material, Element, MyPet


# работа с постами из админа
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_filter = ('publication', 'elem__name')
    fields = [
        'title', 'slug', 'content', 'photo_post', 'photo',
        'elem', 'publication'
    ]
    list_display = (
        'title', 'content', 'photo_post','photo',
        'elem', 'publication', 'kol_simbol'
    )
    search_fields = ('title__startwith', 'elem__name')
    list_display_links = ('title',)
    ordering = ['-time_create', 'title']
    list_editable = ('publication',)
    list_per_page = 7
    readonly_fields = ['photo_post']
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    @admin.display(description='Фотография')
    def photo_post(self, material: Material):
        if material.photo:
            return mark_safe(f'<img src="{material.photo.url}" width=100>')
        return 'Без фотографии'

    @admin.display(description='Размер')
    def kol_simbol(self, material: Material):
        return f'{len(material.content)} символов'

    # возможность в ленте админа делать опубликованной
    @admin.action(description='Опубликовать')
    def publik_set(self, request, queryset):
        count = queryset.update(publication=Material.Publiks.PUBLISHED)
        self.message_user(request, f'Опубликовади {count} записей')

    # возможность в ленте админа делать приватной
    @admin.action(description='Сделать приватным')
    def private_set(self, request, queryset):
        count = queryset.update(publication=Material.Publiks.PRIVAT)
        self.message_user(request, f'Сделали приватными {count} записей')


@admin.register(Element)
class ElementAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',
    )
    list_display_links = ('id', 'name',)



@admin.register(MyPet)
class MyPetAdmin(admin.ModelAdmin):
    fields = ['photo_mypet', 'photo', 'name', 'animal', 'happy_birth', 'slug',
              'bread', 'character',
              'can', 'delicacy', 'foo', 'favorite']
    list_display = (
        'photo_mypet', 'name', 'bread',  'happy_birth', 'slug'
    )
    list_display_links = ('name',)
    readonly_fields = ['photo_mypet']

    # добавили возможность видеть статику в админе
    @admin.display(description='Фотография')
    def photo_mypet(self, mypet: MyPet):
        if mypet.photo:
            return mark_safe(f'<img src="{mypet.photo.url}" width=100>')
        return 'Без фото'



