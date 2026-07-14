from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from functools import wraps


def editor_required(view_func):
    @wraps(view_func)
    def _wrapper_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.shortcuts import redirect
            return redirect('users:login')
        if not (request.user.is_editor() or request.user.is_admin_it() or request.user.is_superuser):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapper_view


def admin_it_required(view_func):
    @wraps(view_func)
    def _wrapper_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.shortcuts import redirect
            return redirect('users:login')
        if not (request.user.is_admin_it() or request.user.is_superuser):
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapper_view


class EditorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_editor() or user.is_admin_it() or user.is_superuser


class AdminITRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_admin_it() or user.is_superuser
