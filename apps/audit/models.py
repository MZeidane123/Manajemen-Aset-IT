from django.db import models
from django.conf import settings


class AuditLog(models.Model):
    class Action(models.TextChoices):
        CREATE = 'create', 'Membuat'
        UPDATE = 'update', 'Mengubah'
        DELETE = 'delete', 'Menghapus'
        LOCK = 'lock', 'Mengunci'
        EXPORT = 'export', 'Export Data'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=20, choices=Action.choices)
    model_name = models.CharField(max_length=100)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    object_repr = models.CharField(max_length=200, blank=True)
    details = models.JSONField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'audit_logs'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['model_name']),
            models.Index(fields=['action']),
            models.Index(fields=['-created_at']),
        ]

    def __str__(self):
        return f"{self.get_action_display()} {self.model_name} oleh {self.user}" if self.user else f"{self.get_action_display()} {self.model_name}"
