from django.contrib import admin
from .models import Almacen, Secuencia_Referencia, Tipo_Operacion, Categoria_Producto, Ubicaciones, Producto
# Register your models here.

admin.site.register(Almacen)
admin.site.register(Secuencia_Referencia)
admin.site.register(Tipo_Operacion)
admin.site.register(Categoria_Producto)
admin.site.register(Ubicaciones)
admin.site.register(Producto)
