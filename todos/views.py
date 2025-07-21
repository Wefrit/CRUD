from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import date
from .models import Todo


class TodoListView(ListView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_create")

    # função para retornar quantas tarefas foram feitas
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total"] = Todo.objects.count()
        context["finalizadas"] = Todo.objects.filter(finished_at__isnull=False).count()
        context["faltam"] = context["total"] - context["finalizadas"]
        return context


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    template_name = "todos/todo_update.html"


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def post(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        if todo.finished_at:
            todo.finished_at = None
        else:
            todo.finished_at = date.today()
        todo.save()
        return redirect("todo_list")
