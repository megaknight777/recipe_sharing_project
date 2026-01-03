from django.db import models
from django.contrib.auth.models import User

# 1. Новая модель Категории
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # 2. Новая связь с Категорией
    # null=True означает, что поле может быть пустым (нужно для старых рецептов)
    # on_delete=models.PROTECT запрещает удалять категорию, если к ней привязаны рецепты
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Категория")

    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField(help_text="Каждый ингредиент с новой строки")
    instructions = models.TextField()
    
    cooking_time = models.IntegerField(help_text="Время в минутах")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title