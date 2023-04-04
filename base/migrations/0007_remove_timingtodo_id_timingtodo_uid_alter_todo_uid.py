# Generated by Django 4.0.6 on 2023-04-04 17:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_todo_uid_timingtodo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timingtodo',
            name='id',
        ),
        migrations.AddField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('f9a3859b-19ee-4d54-a3bf-917b1a8e1345'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('f0eb9d8a-52c3-412e-beef-c03273e8ee83'), editable=False, primary_key=True, serialize=False),
        ),
    ]
