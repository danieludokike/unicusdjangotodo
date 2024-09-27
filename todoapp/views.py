from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Todo


def todo_view(request):        
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, "index.html", context)


def add_todo_view(request):
    if request.method == "POST":
        name = request.POST.get("item")
        if name:
            todo = Todo()
            todo.name = name
            todo.save()
            messages.error(request, f"Successfully added {name}.")
            return redirect("todoapp:todo_view")
        else:
            messages.error(request, "Please enter an item name")
    return render(request, "add_todo.html")


def update_todo_view(request, todo_id):
    item_to_update = Todo.objects.get(id=todo_id)
    if request.method == "POST":
        todo_name = request.POST.get("item")
        
        item_to_update.name = todo_name
        item_to_update.save()
        
        messages.info(request, "Item updated successful")
        return redirect("todoapp:todo_view")
    context = {"item_to_update": item_to_update}
    return render(request, "update_todo.html", context)


def delete_todo_view(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    
    messages.info(request, "Item was deleted successfully!")
    return redirect("todoapp:todo_view")
        