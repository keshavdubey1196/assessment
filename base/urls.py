# from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"todo-api", views.TodoApi, basename="todo")

urlpatterns = []

urlpatterns += router.urls
