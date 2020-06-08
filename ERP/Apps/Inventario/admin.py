from django.contrib import admin
from django.db import models
from django import forms
from .models import (
	Almacen, Secuencia_Referencia, Tipo_Operacion, Categoria_Producto, Ubicaciones, 
	Producto, Opciones_Rutas, Recepcion)
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple },
    }

admin.site.register(Almacen)
admin.site.register(Secuencia_Referencia)
admin.site.register(Tipo_Operacion)
admin.site.register(Categoria_Producto)
admin.site.register(Ubicaciones)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Recepcion)
