from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard:index')
    return redirect('users:login')

urlpatterns = [
    path('', root_redirect, name='root'),
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.users.urls')),
    path('core/', include('apps.core.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
    path('audit/', include('apps.audit.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
