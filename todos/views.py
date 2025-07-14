from django.shortcuts import render


def todo_list(request):
    nome = "Lista de Tarefas"
    lista = ["Tarefa 1", "Tarefa 2", "Tarefa 3"]
    return render(request, "todos/todo_list.html", {"nome": nome, "lista": lista})
