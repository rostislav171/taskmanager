from django.db import models

# Create your models here.


class TodoList(models.Model):
    """Задача пользователя"""
    task_name = models.CharField(max_length=200)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.task_name


class Entry(models.Model):
    """Описание задачи"""
    task = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    description = models.TextField()
    deadline = models.DateField()
    status = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=(("high", "High"), ("medium", "Medium"), ("low", "Low")))
    
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f"{self.task}"
    