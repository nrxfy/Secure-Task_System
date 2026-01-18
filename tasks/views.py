from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Task, AuditLog
from .forms import RegisterForm, TaskForm,ProfileForm
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def profile_edit(request):
    user = request.user

    if request.method == 'POST':
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')

    return render(request, 'tasks/profile_edit.html', {
        'user': user
    })

@staff_member_required
def audit_log_view(request):
    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'tasks/audit_logs.html', {'logs': logs})


# --- Requirement 2: Role-Based Access Control (RBAC) ---
def is_admin(user):
    return user.is_staff # Admin check

# --- Requirement 1: User Registration ---
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! You can now login.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# --- Requirement 3: Secure CRUD (Task Management) ---
@login_required
def task_list(request):
    # SECURITY FIX: Filter by owner to prevent IDOR
    tasks = Task.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user # Set current user as owner
            task.save()
            # Log the action
            AuditLog.objects.create(user=request.user, action=f"Created task: {task.title}")
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_update(request, pk):
    # SECURITY FIX: owner=request.user ensures user can't edit others' tasks
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    # SECURITY FIX: owner=request.user ensures user can't delete others' tasks
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        AuditLog.objects.create(user=request.user, action=f"Deleted task: {task.title}")
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# --- Requirement 4: User Profile ---
@login_required
def profile_view(request):
    return render(request, 'tasks/profile.html', {'user': request.user})

# --- Requirement 5: Audit Log (Admin Only) ---
@user_passes_test(is_admin)
def audit_log_view(request):
    logs = AuditLog.objects.all().order_by('-timestamp')
    return render(request, 'tasks/audit_logs.html', {'logs': logs})