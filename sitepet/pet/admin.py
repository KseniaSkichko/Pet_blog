from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Material, MyPet, TypePost




@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    fields = ['photo_post', 'title', 'slag', 'content',
        'typepost', 'tags', 'publication']
    list_display = (
        'photo_post', 'title', 'content',
        'typepost', 'publication','kol_simbol'
    )
    readonly_fields = ['photo_post']
    filter_horizontal = ['tags']
    list_filter = ('publication', 'typepost__name', 'tags__tag')
    search_fields = ('title', 'typepost__name')
    list_display_links = ('title',)
    ordering = ['-time_create', 'title']
    list_editable = ('publication',)
    list_per_page = 10
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True

    @admin.action(description='Опубликовать')
    def publik_set(self, request, queryset):
        count = queryset.update(publication=Material.Publiks.PUBLISHED)
        self.message_user(request, f'Опубликовади {count} записей')

    @admin.action(description='Сделать приватным')
    def private_set(self, request, queryset):
        count = queryset.update(publication=Material.Publiks.PRIVAT)
        self.message_user(request, f'Сделали приватными {count} записей')

    @admin.display(description='Размер')
    def kol_simbol(self, material: Material):
        return f'{len(material.content)} символов'

    @admin.display(description='Файл')
    def photo_post(self, material: Material):
        if material.photo:
            return mark_safe(f'<img src="{material.photo.url}" width=100>')
        return 'Без файла'

@admin.register(MyPet)
class MyPetAdmin(admin.ModelAdmin):
    fields = ['photo_mypet', 'name', 'animal',
              'bread', 'happy_birth', 'character',
              'can', 'delicacy', 'byaka', 'favorite']
    list_display = (
        'photo_mypet', 'name', 'bread',
        'happy_birth'
    )
    list_display_links = ('name',)
    readonly_fields = ['photo_mypet']


    @admin.display(description='Фотография')
    def photo_mypet(self, mypet: MyPet):
        if mypet.photo:
            return mark_safe(f'<img src="{mypet.photo.url}" width=100>')
        return 'Без фото'


@admin.register(TypePost)
class TypePostsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',
    )
    list_display_links = ('id', 'name')


# admin.site.register(MyPet, MyPetAdmin)
# admin.site.register(TypePost, TypePostAdmin)
# admin.site.register(TagPosts)
