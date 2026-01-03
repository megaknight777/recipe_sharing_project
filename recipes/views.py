from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm # Стандартная форма регистрации
from django.contrib import messages
from django.contrib.auth import logout

def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes})

def register(request):
    if request.method == 'POST':
        # Если пользователь нажал кнопку "Зарегистрироваться"
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Сохраняем нового пользователя в БД
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт для {username}!')
            return redirect('home') # Перенаправляем на главную
    else:
        # Если пользователь просто открыл страницу
        form = UserCreationForm()
    
    return render(request, 'recipes/register.html', {'form': form})

def logout_view(request):
    logout(request) # Стандартная команда Django "Выйти"
    return redirect('home') # Перенаправляем на главную