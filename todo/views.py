from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Todo
from .forms import TodoForm

# Create your views here.

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todo/todo_list.html", {"todos": todos})


def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("todo:todo_list"))
    else:
        form = TodoForm()
    return render(request, "todo/todo_form.html", {"form": form})


def update_todo(request, pk):
    todo_obj = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        form = TodoForm(instance=todo_obj, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("todo:retreive_todo", args=[pk,]))
    else:
        form = TodoForm(instance=todo_obj)
    return render(request, "todo/todo_form.html", {"form": form, "object": todo_obj})


def retreive_todo(request, pk):
    todo_obj = get_object_or_404(Todo, pk=pk)
    return render(request, "todo/todo_detail.html", {"todo": todo_obj})


def delete_todo(request, pk):
    todo_obj = get_object_or_404(Todo, pk=pk)
    todo_obj.delete()
    return redirect(reverse("todo:todo_list"))

