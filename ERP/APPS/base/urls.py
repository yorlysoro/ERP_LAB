from django.urls import path
from APPS.base.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]