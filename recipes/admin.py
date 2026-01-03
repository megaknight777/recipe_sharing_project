from django.contrib import admin
from .models import Recipe  # Импортируем нашу модель Рецепта

# Говорим админке: "Управляй и этим тоже"
admin.site.register(Recipe)