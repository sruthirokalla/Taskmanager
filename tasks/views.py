from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm  # Make sure this form exists for creating/updating tasks

# Home page or task list view (requires login)
@login_required
def task_list(request):
    tasks = Task.objects.all()  # Display all tasks
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Add a new task
@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new task to the database
            messages.success(request, 'Task added successfully!')
            return redirect('task_list')  # Redirect to task list view
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

# Edit an existing task
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Fetch task by ID
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Save the updated task to the database
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')  # Redirect to task list view
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

# Delete a task
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Fetch task by ID
    task.delete()  # Delete the task
    messages.success(request, 'Task deleted successfully!')
    return redirect('task_list')  # Redirect to task list view

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in after registration
            messages.success(request, 'Registration successful!')
            return redirect('task_list')  # Redirect to task list view
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

# User login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()  # Authenticate user
            login(request, user)  # Log the user in
            messages.success(request, 'Login successful!')
            return redirect('task_list')  # Redirect to task list view
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})

# User logout view
@login_required
def user_logout(request):
    logout(request)  # Log the user out
    messages.success(request, 'Logout successful!')
    return redirect('user_login')  # Redirect to login page

