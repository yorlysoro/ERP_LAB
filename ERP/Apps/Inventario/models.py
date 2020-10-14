#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  
#  Copyright 2020 yorlysoro <yorlysoro@gmail.com>
#  
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#  
#  
from django.db import models
from Apps.Contacto.models import Individual
# Create your models here.
class Almacen(models.Model):
	almacen = models.CharField(max_length=255)
	nombre_corto = models.CharField(max_length=10)
	direccion = models.CharField(max_length=255, blank=True, null=True)

	class Meta:
		verbose_name = "Almacen"
		verbose_name_plural = "Almacenes"

	def __str__(self):
		return self.almacen

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

	class Meta:
		verbose_name = "Secuencia de Referencia"
		verbose_name_plural = "Secuencias de Referencia"

	def __str__(self):
		return self.nombre

class Tipo_Operacion(models.Model):
	TIPO_OPERACION_CHOICES = ( 
		('En' , 'Envio'), 
		('Re' , 'Recibo'), 
		('Ti' , 'Transferencia Interna'),
		)
	tipo_de_operacion = models.CharField(max_length=255)
	tipo_de_operacion_choice = models.CharField(max_length=255, choices=TIPO_OPERACION_CHOICES, blank=True, null=True)
	secuencia_referencia = models.ForeignKey(Secuencia_Referencia, null=True, blank=True, on_delete=models.SET_NULL)
	mostrar_op_detalladas = models.BooleanField(default=False)
	codigo = models.CharField(max_length=10)
	to_devoluciones_recibo = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
	precompletar_op_detalladas_recibo = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Tipo de Operacion"
		verbose_name_plural = "Tipos de Operaciones"

	def __str__(self):
		return self.tipo_de_operacion

class Categoria_Producto(models.Model):
	LOGISTICA_CHOICES = ( 
	('FIFO' , 'First In First Out (FIFO)'), 
	('LIFO' , 'Last In First Out (LIFO)'),
	)
	nombre_categoria = models.CharField(max_length=255)
	categoria_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
	logistica = models.CharField(max_length=255, null=True, blank=True, choices=LOGISTICA_CHOICES)

	class Meta:
		verbose_name = "Categoria de Producto"
		verbose_name_plural = "Categorias de Productos"

	def __str__(self):
		return self.nombre_categoria

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
	class Meta:
		verbose_name = "Ubicacion"
		verbose_name_plural = "Ubicaciones"

	def __str__(self):
		return self.nombre_ubicacion
class Opciones_Rutas(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre

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
	rutas = models.ManyToManyField(Opciones_Rutas, blank=True)
	plazo_entrega_cliente = models.PositiveIntegerField(default=0)
	ubicacion_produccion = models.ForeignKey(Ubicaciones, null=True, blank=True, on_delete=models.SET_NULL, related_name='ubicacion_produccion')
	ubicacion_inventario = models.ForeignKey(Ubicaciones, null=True, blank=True, on_delete=models.SET_NULL, related_name='ubicacion_inventario')
	peso = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
	volumen = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
	responsable = models.CharField(max_length=255, null=True, blank=True)
	descripcion_pedido_entrega = models.TextField(null=True, blank=True)
	descripcion_recepciones = models.TextField(null=True, blank=True)
	foto = models.ImageField(upload_to='fotos/producto/', null=True, blank=True)
	categoria = models.ForeignKey(Categoria_Producto, null=True, blank=True, on_delete=models.SET_NULL)
	class Meta:
		verbose_name = "Producto"
		verbose_name_plural = "Productos"

	def __str__(self):
		return self.nombre_producto

class Recepcion(models.Model):
	recibir = models.ForeignKey(Individual, null=True, blank=True, on_delete=models.SET_NULL)
	tipo_operacion = models.ForeignKey(Tipo_Operacion, on_delete=models.CASCADE)
	fecha_programada = models.DateTimeField()
	documento_origen = models.CharField(max_length=255, null=True, blank=True)
	producto = models.ManyToManyField(Producto, blank=True)

	class Meta:
		verbose_name = "Recepcion"
		verbose_name_plural = "Recepciones"
	def __str__(self):
		return self.id