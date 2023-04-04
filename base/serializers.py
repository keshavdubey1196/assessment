from rest_framework import serializers
from .models import Todo, TimingTodo
import re
from django.template.defaultfilters import slugify


class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        # fields = "__all__"
        exclude = ["created_at", "updated_at"]

    # Method to return slug
    def get_slug(self, obj):
        return slugify(obj.todo_title)

    # Field specific validation
    def validate_todo_title(self, data):
        if data:
            todo_title = data
            regex = re.compile("[@_!#$%^&*()<>?/|}{~:\]")

            if len(todo_title) < 3:
                raise serializers.ValidationError("Title too short: char<3")

            if regex.search(todo_title):
                raise serializers.ValidationError(
                    "Invalid todo_title. Cannot contain special characters"
                )

        return data


class TimingTodoSerializer(serializers.ModelSerializer):
    # To get todo(foreign_key data), serialized accordingly
    todo = TodoSerializer()

    class Meta:
        model = TimingTodo
        exclude = ["created_at", "updated_at"]
        # depth = 1
