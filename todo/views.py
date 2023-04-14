from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, login, authenticate
from .forms import *


def index(request):
    context = {
        'title': 'Главная страница',
    }
    return render(request, 'todo/index.html', context=context)


def register(request):
    form = RegistrationUserForm()

    context = {
        'title': 'Регистрация',
        'form': form,
        'error': '',
    }

    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('personal_area')
        else:
            #  Вывод текста с ошибкой, если имя аккаунта занято и т.д.
            for field in form.errors:
                context['error'] = form.errors[field].as_text()
    return render(request, 'todo/register.html', context=context)


def loginuser(request):
    form = CustomAuthForm

    context = {
        'title': 'Авторизация',
        'form': form,
        'error': '',
    }

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('personal_area')
        else:
            context['error'] = 'Неверный логин или пароль'

    return render(request, 'todo/loginuser.html', context=context)


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def personal_area(request):
    context = {
        'title': 'Личный кабинет',
    }

    return render(request, 'todo/personal_area.html', context=context)
