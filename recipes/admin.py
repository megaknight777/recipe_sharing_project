from django.contrib import admin
from .models import Recipe, Category  # Импортируем и Категорию

admin.site.register(Recipe)
admin.site.register(Category) # Регистрируем