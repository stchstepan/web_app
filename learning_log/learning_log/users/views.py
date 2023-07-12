from django.shortcuts import render, redirect
from django.contrib.auth import login #импортируем функцию login для выполнения входа
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Регестрирует нового пользователя"""
    if request.method != 'POST': #Если не содержится регистрационных
        #данных (то есть функция не отвечает на запрос POST), то 
        #создается экземпляр класса UserCreationForm.
        #Данный класс создает форму для регистрации.
        #Выводит пустую форму регистрации
        form = UserCreationForm()
    else: #Если же функция содержит запрос POST, то создается экземпляр
        #UserCreationForm, основанный на отправленных данных.
        #Обработка заполненной формы
        form = UserCreationForm(data=request.POST)

        if form.is_valid(): #идет проверка на правильность отправляемых
            #данных, а именно: имя пользователя содержит только разрешенные
            #символы, пароли совпадают, пользователь не пытается вставить 
            #вредоностный код.
            new_user = form.save()
            #Выполнение входа и перенаправление на домашнюю страницу
            login(request, new_user)
            return redirect('learning_logs:index')
    
    #Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'registration/register.html', context)