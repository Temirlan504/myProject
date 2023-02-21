from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("<int:task_id>/delete/", views.delete, name="delete"),
    path('<int:pk>/update/', views.UpdateTaskView.as_view(), name="update")
]