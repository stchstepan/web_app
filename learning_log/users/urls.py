"""Определяет схемы URL для пользователей"""

from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
    #Включить URL авторизации по умолчанию
    path('', include('django.contrib.auth.urls')), #дефолтное включение 
    #для Django, чтобы работала аутентификация.
    #При использовании данного включения, используется функция представления
    #для login Django по умолчанию, но шаблон все равно должен быть
    #предоставлен. 
    #Аутентификационные представления по умолчанию ищут шаблоны в каталоге
    #с именем registration. В данном проекте, данный каталог находится по 
    #пути learning_log/users/templates/registration.
    path('register/', views.register, name='register'),

]