from django.db import models
import uuid

# Create your models here.


class Todo(models.Model):
    uid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4(),
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
