from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-input'}
                               ))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-input'}
                               ))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
                                   attrs={'class': 'form-input'}
                               ))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}
    ))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}
    ))

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'E-mail',
            'password1': 'Пароль',
            'password2': 'Повторите пароль'
        }


        def clean_email(self):
            em = self.cleaned_data['email']
            if get_user_model().objects.filter(email=em).exists():
                raise forms.ValidationError('Такое email уже существует')
            return em

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(
                                   attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(
                                   attrs={'class': 'form-input'}))


    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }