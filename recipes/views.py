from django.shortcuts import render
from .models import Recipe  # Импортируем нашу модель

def home(request):
    # 1. Спрашиваем у базы: "Дай все объекты рецептов"
    recipes = Recipe.objects.all()
    
    # 2. Отдаем эти рецепты в HTML-шаблон
    # 'recipes' (в кавычках) - это имя, по которому мы будем обращаться к списку в HTML
    return render(request, 'recipes/home.html', {'recipes': recipes})