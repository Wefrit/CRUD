from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo


class TodoListView(ListView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_create")


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    template_name = "todos/todo_update.html"
