from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['action', 'model_name', 'user', 'object_repr', 'created_at']
    list_filter = ['action', 'model_name', 'created_at']
    search_fields = ['object_repr', 'user__email']
    date_hierarchy = 'created_at'
    readonly_fields = ['user', 'action', 'model_name', 'object_id', 'object_repr', 'details', 'ip_address', 'created_at']
