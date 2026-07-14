from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        EDITOR = 'editor', 'Editor (Tim IT)'
        VIEWER = 'viewer', 'Viewer (Manager ke atas)'
        ADMIN_IT = 'admin_it', 'Admin IT'

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.EDITOR)
    phone = models.CharField(max_length=20, blank=True)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"

    def is_editor(self):
        return self.role == self.Role.EDITOR

    def is_viewer(self):
        return self.role == self.Role.VIEWER

    def is_admin_it(self):
        return self.role == self.Role.ADMIN_IT or self.is_superuser
