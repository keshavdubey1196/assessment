from django.urls import path
from . import views

urlpatterns = [
    path("api/home/", views.home, name="home-view"),
    path("api/post-todo/", views.post_todo, name="post-todo"),
    path("api/get-todo/", views.get_todos, name="get-todo"),
]
