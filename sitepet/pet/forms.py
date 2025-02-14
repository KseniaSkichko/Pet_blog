from django import forms
from django.core.exceptions import ValidationError
from .models import Element, Material, MyPet


# фформа-шаблон для создания нового поста
class NuwMaterialForm(forms.ModelForm):
    elem = forms.ModelChoiceField(queryset=Element.objects.all(),
                                  empty_label='Не выбрано', label='Категория')

    class Meta:
        model = Material
        fields = ['elem', 'title', 'slug', 'content', 'photo', 'publication']
        labels = {'slug': 'URL'}
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Длина превышает 50 символов")
        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')


class NuwMyPets(forms.ModelForm):
    class Meta:
        model = MyPet
        fields = ['name', 'animal', 'bread',
                  'photo', 'character', 'can',
                  'delicacy', 'foo', 'favorite']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),

        }


