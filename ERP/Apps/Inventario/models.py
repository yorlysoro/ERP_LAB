from django.db import models

# Create your models here.
class Almacen(models.Model):
	almacen = models.CharField(max_length=255)
	nombre_corto = models.CharField(max_length=10)
	direccion = models.CharField(max_length=255, blank=True, null=True)

class Secuencia_Referencia(models.Model):
	IMPLEMENTACIONES = (
		('Sd' ,'Estandar'), 
		('Sh', 'Sin Hueco'),
		)
	nombre = models.CharField(max_length=255)
	implementacion = models.CharField(max_length=255, choices=IMPLEMENTACIONES, default='Sd')
	codigo_secuencia = models.CharField(max_length=10, null=True, blank=True)
	prefijo = models.CharField(max_length=255, null=True, blank=True)
	sufijo = models.CharField(max_length=255, null=True, blank=True)
	ultilizar_subsec_date_range = models.BooleanField(default=False)
	tamano_secuencia = models.PositiveIntegerField(default=0)
	paso = models.PositiveIntegerField(default=1)
	proximo_numero = models.PositiveIntegerField(default=0)

class Tipo_Operacion(models.Model):
	TIPO_OPERACION_CHOICES = (
		('nulo', ''), 
		('En' , 'Envio'), 
		('Re' , 'Recibo'), 
		('Ti' , 'Transferencia Interna'),
		)
	tipo_de_operacion = models.CharField(max_length=255)
	tipo_de_operacion_choice = models.CharField(max_length=255, choices=TIPO_OPERACION_CHOICES, default='nulo')
	secuencia_referencia = models.ForeignKey(Secuencia_Referencia, null=True, blank=True, on_delete=models.SET_NULL)
	mostrar_op_detalladas = models.BooleanField(default=False)
	codigo = models.CharField(max_length=10)
	to_devoluciones_recibo = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
	precompletar_op_detalladas_recibo = models.BooleanField(default=True)

class Categoria_Producto(models.Model):
	LOGISTICA_CHOICES = (
	('nulo' , ''), 
	('FIFO' , 'First In First Out (FIFO)'), 
	('LIFO' , 'Last In First Out (LIFO)'),
	)
	nombre_categoria = models.CharField(max_length=255)
	categoria_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
	logistica = models.CharField(max_length=255, null=True, blank=True, choices=LOGISTICA_CHOICES, default='nulo')

class Ubicaciones(models.Model):
	nombre_ubicacion = models.CharField(max_length=255)
	ubicacion_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
	TIPO_UBICACION_CHOICES = ( 
		('Up' , 'Ubicacion de Proveedor'), 
		('V' , 'Vista'), 
		('Ui' , 'Ubicacion Interna'), 
		('Uc' , 'Ubicacion del Cliente'), 
		('Pi' , 'Perdida de Inventario'), 
		('Pr' , 'Produccion'), 
		('Ut' , 'Ubicacion de Transito'),
		)
	tipo_ubicacion = models.CharField(max_length=255, choices=TIPO_UBICACION_CHOICES, default='Up')
	ubicacion_chatarra = models.BooleanField(default=False)
	ubicacion_devolucion = models.BooleanField(default=False)
	nota = models.TextField(null=True, blank=True)

class Producto(models.Model):
	nombre_producto = models.CharField(max_length=255)
	vender = models.BooleanField(default=True)
	comprar = models.BooleanField(default=True)
	TIPO_PRODUCTO_CHOICES = (
		('Co' , 'Consumible'), 
		('Se' , 'Servicio'), 
		('Al' , 'Almacenable'),
		)
	tipo_producto = models.CharField(max_length=255, choices=TIPO_PRODUCTO_CHOICES, default='Al')
	referencia_interna = models.CharField(max_length=255, null=True, blank=True)
	codigo_barras = models.CharField(max_length=255, null=True, blank=True)
	precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
	coste = models.DecimalField(max_digits=10, decimal_places=2)
	notas_internas = models.TextField(null=True, blank=True)
	RUTAS_CHOICES = (
		('MTO' , 'Obtener Bajo Pedido (MTO)'),
		)
	rutas = models.CharField(max_length=255, choices=RUTAS_CHOICES, default='MTO')
	plazo_entrega_cliente = models.PositiveIntegerField(default=0)
	ubicacion_produccion = models.ForeignKey(Ubicaciones, null=True, blank=True, on_delete=models.SET_NULL, related_name='ubicacion_produccion')
	ubicacion_inventario = models.ForeignKey(Ubicaciones, null=True, blank=True, on_delete=models.SET_NULL, related_name='ubicacion_inventario')
	peso = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
	volumen = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
	responsable = models.CharField(max_length=255, null=True, blank=True)
	descripcion_pedido_entrega = models.TextField(null=True, blank=True)
	descripcion_recepciones = models.TextField(null=True, blank=True)
