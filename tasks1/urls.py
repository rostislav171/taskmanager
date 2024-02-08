"""Определяет схемы URL для tasks1"""

from django.urls import path
from . import views

app_name = 'tasks1'
urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/', views.task, name='task'),
    path('new_task/', views.new_task, name='new_task'),
    path('new_entry/<int:task_id>/', views.new_entry, name='new_entry'),
]