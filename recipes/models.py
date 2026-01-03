from django.db import models
from django.contrib.auth.models import User  # Импортируем стандартного пользователя

class Recipe(models.Model):
    # Связь с автором (если удалить юзера, удалятся и его рецепты)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Текстовые поля
    title = models.CharField(max_length=200)  # Название рецепта
    description = models.TextField()          # Полное описание
    ingredients = models.TextField(help_text="Каждый ингредиент с новой строки") 
    instructions = models.TextField()         # Как готовить
    
    # Время и даты
    cooking_time = models.IntegerField(help_text="Время в минутах")
    created_at = models.DateTimeField(auto_now_add=True) # Автоматически ставить время создания

    def __str__(self):
        return self.title