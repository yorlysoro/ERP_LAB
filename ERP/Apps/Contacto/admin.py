from django.contrib import admin

# Register your models here.

from .models import Compania, Titulo, Individual

admin.site.register(Compania)
admin.site.register(Titulo)
admin.site.register(Individual)