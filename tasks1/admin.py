from django.contrib import admin
from .models import TodoList, Entry

# Register your models here.
admin.site.register(TodoList)
admin.site.register(Entry)
