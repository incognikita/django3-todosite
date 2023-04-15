from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .models import ToDo
from .forms import *


def index(request):
    context = {
        'title': 'Главная страница',
        'todos': ''
    }

    # Вывод заметок, созданных конкретным пользователем
    if request.user.is_authenticated:
        current_todos = ToDo.objects.filter(user=request.user)
        context['todos'] = current_todos
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


def create_todo(request):
    form = TodoForm

    context = {
        'title': 'Заметки',
        'form': form,
        'error': ''
    }

    if request.method == 'POST':
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('index')
        except ValueError:
            context['error'] = 'Переданы неверные данные'
            return render(request, 'todo/create_todo.html', context=context)
    return render(request, 'todo/create_todo.html', context=context)
