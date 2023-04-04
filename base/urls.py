# from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r"todo-api", views.TodoApi, basename="todo")

urlpatterns = [
    path("todo/", views.TodoView.as_view()),
]

urlpatterns += router.urls
