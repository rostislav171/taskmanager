from django import forms
from .models import TodoList, Entry


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['task_name']
        labels = {'task_name': ''}


class EntryForm(forms.ModelForm):
    priority_ch = forms.ChoiceField(choices=(("high", "High"), ("medium", "Medium"), ("low", "Low")))

    class Meta:
        model = Entry
        fields = {}
        labels = {}
