from django.shortcuts import render
from .models import Task
# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    tasksDict = list(Task.objects.values())
    print("Tareas en la base de datos:", tasks)
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'tasksDict': tasksDict})