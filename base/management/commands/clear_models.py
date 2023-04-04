from django.core.management import BaseCommand
from base.models import Todo


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Todo.objects.all().delete()
