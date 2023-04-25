from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('APPS.base.urls')),
    # path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
    # path('secret/defender/', include('defender.urls')), # defender admin
]
