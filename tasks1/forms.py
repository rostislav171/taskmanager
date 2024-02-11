from django import forms
from .models import TodoList, Entry


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['task_name']
        labels = {'task_name': ''}


class EntryForm(forms.ModelForm):

    class Meta:

        model = Entry
        fields = ['description', 'deadline', 'status', 'priority']
        labels = {'description': 'Описание', 'deadline': 'Дедлайн', 'status': 'Статус', 'priority': 'Приоритет'}
        widgets = {'description': forms.Textarea(attrs={'cols': 80}), 'deadline': forms.DateInput(attrs={'type': 'date'})}
