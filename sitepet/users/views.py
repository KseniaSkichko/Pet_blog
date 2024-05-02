from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import LoginUserForm




class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}



#
#
# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('users:logout'))
