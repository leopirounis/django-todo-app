from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Task
from .forms import TaskForm

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('/')

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed  # Toggle complete
    task.save()
    return redirect('/')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('/')