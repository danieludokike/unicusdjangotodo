from django.urls import path
from .views import todo_view, update_todo_view, delete_todo_view, add_todo_view

app_name = "todoapp"
urlpatterns = [
    path("", todo_view, name="todo_view"),
    path("add-todo/", add_todo_view, name="add_todo_view"),
    path("update-todo/<int:todo_id>/", update_todo_view,  name="update_todo_view"),
    path("delete-todo/<int:todo_id>/", delete_todo_view,  name="delete_todo_view")
    
]
