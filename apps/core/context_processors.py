from .models import Asset


def expiring_assets(request):
    if not request.user.is_authenticated:
        return {}
    return {
        'expiring_soon_count': Asset.objects.expiring_soon().count(),
        'expired_count': Asset.objects.expired().count(),
    }
