from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    todo_title = models.CharField(max_length=200)
    todo_description = models.TextField()
    is_done = models.BooleanField(default=False, editable=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.todo_title

    class Meta:
        ordering = [
            "-created_at",
        ]


class TimingTodo(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    timing = models.DateField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.todo.todo_title}, {self.timing}"
