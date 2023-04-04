# Generated by Django 4.0.6 on 2023-04-04 12:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_todo_options_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('db5080dd-912e-40a8-bbe1-ab84fec4e21a'), editable=False, primary_key=True, serialize=False),
        ),
    ]
