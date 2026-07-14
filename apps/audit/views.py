from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AuditLog
from django.db.models import Q


@login_required
def audit_list(request):
    query = request.GET.get('q', '')
    action = request.GET.get('action', '')

    logs = AuditLog.objects.select_related('user').all()

    if query:
        logs = logs.filter(
            Q(object_repr__icontains=query) |
            Q(user__email__icontains=query) |
            Q(model_name__icontains=query)
        )
    if action:
        logs = logs.filter(action=action)

    context = {
        'logs': logs,
        'query': query,
        'selected_action': action,
        'action_choices': AuditLog.Action.choices,
    }
    return render(request, 'audit/audit_list.html', context)
