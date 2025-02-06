from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def list_task(request):
    tasks = Task.objects.all()
    return render(request, 'list_task.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_task')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def att_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list_task')
    else:
        form = TaskForm(instance=task)
    return render(request, 'att_task.html', {'form': form, 'task': task})


def del_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('list_task')
    return render(request, 'del_task.html', {'task': task})


def ver_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'ver_task.html', {'task': task})