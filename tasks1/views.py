from django.shortcuts import render, redirect
from .models import TodoList
from .forms import TodoForm, EntryForm
# Create your views here.


def index(request):
    """Домашняя страница приложения Task"""
    return render(request, 'tasks1/index.html')


def tasks(request):
    """Выводит список задач"""
    tasks = TodoList.objects.order_by('task_name')
    context = {'tasks': tasks}
    return render(request, 'tasks1/tasks.html', context)


def task(request, task_id):
    """Выводит одну задачу и ее подзадачи."""
    task = TodoList.objects.get(id=task_id)
    entries = task.entry_set.order_by('deadline')
    context = {'task': task, 'entries': entries}
    return render(request, 'tasks1/task.html', context)


def new_task(request):
    """Определяет новую задачу."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TodoForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TodoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks1:tasks')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'tasks1/new_task.html', context)


def new_entry(request, task_id):
    """Добавляет новую запись по конкретной задаче."""
    task = TodoList.objects.get(id=task_id)
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = EntryForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.task = task
            new_entry.save()
            return redirect('tasks1:task', task_id=task_id)
    # Вывести пустую или недействительную форму.
    context = {'task': task, 'form': form}
    return render(request, 'tasks1/new_entry.html', context)
