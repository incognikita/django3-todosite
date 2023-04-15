from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('login', loginuser, name='loginuser'),
    path('logoutuser', logoutuser, name='logoutuser'),
    path('personal_area', personal_area, name='personal_area'),
    path('create_todo', create_todo, name='create_todo'),
]