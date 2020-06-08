from django.contrib import admin

# Register your models here.

from .models import Compania, Titulo, Individual, Sector

class IndividualAdmin(admin.ModelAdmin):
	exclude = ['sector']

admin.site.register(Compania)
admin.site.register(Titulo)
admin.site.register(Individual, IndividualAdmin)
admin.site.register(Sector)