from .models import AuditLog


class AuditLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response


def log_audit(user, action, model_name, object_id=None, object_repr='', details=None, request=None):
    if not user or not user.is_authenticated:
        return
    AuditLog.objects.create(
        user=user,
        action=action,
        model_name=model_name,
        object_id=object_id,
        object_repr=object_repr,
        details=details,
        ip_address=request.META.get('REMOTE_ADDR') if request else None,
    )
