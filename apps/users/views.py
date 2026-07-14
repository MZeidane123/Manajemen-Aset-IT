from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, UserCreateForm, UserEditForm
from .models import User
from .decorators import admin_it_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)
            messages.success(request, f'Selamat datang, {user.get_full_name() or user.email}!')
            return redirect('dashboard:index')
        messages.error(request, 'Email atau password salah.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('users:login')


@login_required
def profile_view(request):
    return render(request, 'users/profile.html')


@login_required
@admin_it_required
def user_list(request):
    users = User.objects.all().order_by('-date_joined')
    return render(request, 'users/user_list.html', {'users': users})


@login_required
@admin_it_required
def user_create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User berhasil dibuat.')
            return redirect('users:user_list')
        messages.error(request, 'Periksa kembali form.')
    else:
        form = UserCreateForm()
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Tambah User'})


@login_required
@admin_it_required
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User berhasil diupdate.')
            return redirect('users:user_list')
        messages.error(request, 'Periksa kembali form.')
    else:
        form = UserEditForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Edit User'})


@login_required
@admin_it_required
def user_toggle_active(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user == request.user:
        messages.error(request, 'Tidak bisa menonaktifkan akun sendiri.')
        return redirect('users:user_list')
    user.is_active = not user.is_active
    user.save()
    status = 'diaktifkan' if user.is_active else 'dinonaktifkan'
    messages.success(request, f'User {user.email} {status}.')
    return redirect('users:user_list')


@login_required
@admin_it_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user == request.user:
        messages.error(request, 'Tidak bisa menghapus akun sendiri.')
        return redirect('users:user_list')
    if request.method == 'POST':
        email = user.email
        user.delete()
        messages.success(request, f'User {email} berhasil dihapus.')
        return redirect('users:user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})
