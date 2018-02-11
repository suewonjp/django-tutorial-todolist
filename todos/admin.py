from django.contrib import admin

from .models import Todo, Category

admin.site.register(Todo)
admin.site.register(Category)

