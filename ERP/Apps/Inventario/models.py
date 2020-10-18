#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright 2020 yorlysoro <yorlysoro@gmail.com>
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
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
from django.db import models
from Apps.Contacto.models import Individual, Compania
from .constantes import *
# Create your models here.


class Almacen(models.Model):
    almacen = models.CharField(max_length=255)
    nombre_corto = models.CharField(max_length=10)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    albaranes_entrada = models.CharField(
        max_length=255,
        choices=ALBARANES_ENTRADA,
        default='1')
    envios_salientes = models.CharField(
        max_length=255,
        choices=ENVIOS_SALIENTES,
        default='1')
    comprar_para_resurtir = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Almacen"
        verbose_name_plural = "Almacenes"

    def __str__(self):
        return self.almacen


class Secuencia_Referencia(models.Model):
    nombre = models.CharField(max_length=255)
    implementacion = models.CharField(
        max_length=255,
        choices=IMPLEMENTACIONES,
        default='Sd')
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


class Ubicaciones(models.Model):
    nombre_ubicacion = models.CharField(max_length=255)
    ubicacion_padre = models.ForeignKey(
        'self', null=True,
        blank=True,
        on_delete=models.SET_NULL)
    tipo_ubicacion = models.CharField(
        max_length=255,
        choices=TIPO_UBICACION_CHOICES, default='Up')
    ubicacion_chatarra = models.BooleanField(default=False)
    ubicacion_devolucion = models.BooleanField(default=False)
    nota = models.TextField(null=True, blank=True)
    estrategia_retirada = models.CharField(
        max_length=255,
        null=True,
        blank=True, choices=LOGISTICA_CHOICES)

    class Meta:
        verbose_name = "Ubicacion"
        verbose_name_plural = "Ubicaciones"

    def __str__(self):
        return self.nombre_ubicacion


class Tipo_Operacion(models.Model):
    tipo_de_operacion = models.CharField(max_length=255)
    tipo_de_operacion_choice = models.CharField(
        max_length=255,
        choices=TIPO_OPERACION_CHOICES,
        blank=True, null=True)
    secuencia_referencia = models.ForeignKey(
        Secuencia_Referencia,
        null=True, blank=True,
        on_delete=models.SET_NULL)
    mostrar_op_detalladas = models.BooleanField(default=False)
    codigo = models.CharField(max_length=10)
    to_devoluciones_recibo = models.ForeignKey(
        'self',
        blank=True, null=True,
        on_delete=models.SET_NULL)
    precompletar_op_detalladas_recibo = models.BooleanField(default=True)
    ubicacion_origen = models.ForeignKey(
        Ubicaciones,
        blank=True, null=True,
        related_name='ubicacion_origen_ubicaciones',
        on_delete=models.SET_NULL)
    ubicacion_destino = models.ForeignKey(
        Ubicaciones, blank=True,
        null=True,
        related_name='ubicacion_destino_ubicaciones',
        on_delete=models.SET_NULL)
    crear_nuevo_lote_serie = models.BooleanField(default=False)
    utilizar_existentes_lote_seria = models.BooleanField(default=False)
    mover_paquetes_completos = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Tipo de Operacion"
        verbose_name_plural = "Tipos de Operaciones"

    def __str__(self):
        return self.tipo_de_operacion


class Categoria_Producto(models.Model):
    nombre_categoria = models.CharField(max_length=255)
    categoria_padre = models.ForeignKey(
        'self', null=True,
        blank=True,
        on_delete=models.SET_NULL)
    logistica = models.CharField(
        max_length=255,
        null=True, blank=True,
        choices=LOGISTICA_CHOICES)

    class Meta:
        verbose_name = "Categoria de Producto"
        verbose_name_plural = "Categorias de Productos"

    def __str__(self):
        return self.nombre_categoria


class Opciones_Rutas(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Categoria_Unidades(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Categoria de Medida"
        verbose_name_plural = "Categorias de Medidas"

    def __str__(self):
        return self.nombre


class Unidades_Medida(models.Model):
    unidad_de_medida = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria_Unidades, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255,
                            choices=TIPO_UNIDAD_MEDIDA,
                            default='1')
    ratio = models.FloatField()
    activo = models.BooleanField(default=True)
    precision_redondeo = models.FloatField()

    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"

    def __str__(self):
        return self.unidad_de_medida


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=255)
    vender = models.BooleanField(default=True)
    comprar = models.BooleanField(default=True)
    tipo_producto = models.CharField(max_length=255,
                                     choices=TIPO_PRODUCTO_CHOICES,
                                     default='Al')
    referencia_interna = models.CharField(max_length=255,
                                          null=True,
                                          blank=True)
    codigo_barras = models.CharField(max_length=255, null=True, blank=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    coste = models.DecimalField(max_digits=10, decimal_places=2)
    notas_internas = models.TextField(null=True, blank=True)
    rutas = models.ManyToManyField(Opciones_Rutas, blank=True)
    plazo_entrega_cliente = models.PositiveIntegerField(default=0)
    ubicacion_produccion = models.ForeignKey(
        Ubicaciones,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='ubicacion_produccion')
    ubicacion_inventario = models.ForeignKey(
        Ubicaciones,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='ubicacion_inventario')
    peso = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    volumen = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    responsable = models.ForeignKey(
        Individual,
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    descripcion_pedido_entrega = models.TextField(null=True, blank=True)
    descripcion_recepciones = models.TextField(null=True, blank=True)
    foto = models.ImageField(
        upload_to='fotos/producto/',
        null=True,
        blank=True)
    categoria = models.ForeignKey(
        Categoria_Producto,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    udm_venta = models.ForeignKey(
        Unidades_Medida,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='udm_venta')
    udm_compra = models.ForeignKey(
        Unidades_Medida,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='udm_compra')

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre_producto


class Recepcion(models.Model):
    recibir = models.ForeignKey(
        Individual,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    tipo_operacion = models.ForeignKey(
        Tipo_Operacion,
        on_delete=models.CASCADE)
    fecha_programada = models.DateTimeField()
    documento_origen = models.CharField(max_length=255, null=True, blank=True)
    producto = models.ManyToManyField(Producto, blank=True)
    nota = models.TextField(null=True, blank=True)
    responsable = models.ForeignKey(
        Individual,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='responsable_recepcion')
    estado = models.CharField(
        max_length=255,
        choices=ESTADO_RECEPCION,
        default='Bor')

    class Meta:
        verbose_name = "Recepcion"
        verbose_name_plural = "Recepciones"

    def __str__(self):
        return self.id


class Rutas(models.Model):
    ruta = models.CharField(max_length=255)
    compania = models.ForeignKey(
        Compania,
        null=True, blank=True,
        on_delete=models.SET_NULL)
    categoria_producto = models.BooleanField(default=False)
    productos = models.BooleanField(default=True)
    almacenes = models.BooleanField(default=False)
    linea_pedido_ventas = models.BooleanField(default=False)
    reglas = models.ManyToManyField(
        'Reglas',
        blank=True,
        related_name='rutas_reglas')

    class Meta:
        verbose_name = "Ruta"
        verbose_name_plural = "Rutas"

    def __str__(self):
        return self.ruta


class Reglas(models.Model):
    nombre = models.CharField(max_length=255)
    accion = models.CharField(
        max_length=255,
        choices=ACCIONES_REGLAS,
        default='1')
    tipo_operacion = models.ForeignKey(
        Tipo_Operacion,
        blank=True, null=True,
        on_delete=models.SET_NULL, related_name='operacion_regla')
    ubicacion_origen = models.ForeignKey(
        Ubicaciones,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='ubicacion_reglas_origen')
    ubicacion_destino = models.ForeignKey(
        Ubicaciones,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name='ubicacion_reglas_destino')
    movimiento_automatico = models.CharField(
        max_length=255,
        choices=MA_CHOICES, default='1')
    metodo_suministro = models.CharField(
        max_length=255,
        choices=MS_CHOICES,
        default='1')
    ruta = models.ForeignKey(
        Rutas,
        blank=True, null=True,
        on_delete=models.SET_NULL,
        related_name='reglas_rutas')
    compania = models.ForeignKey(
        Compania,
        blank=True, null=True,
        on_delete=models.SET_NULL)
    plazo_entrega = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Regla"
        verbose_name_plural = "Reglas"

    def __str__(self):
        return self.nombre


class ReglasEstrategiaTraslado(models.Model):
    producto = models.ForeignKey(
        Producto,
        null=True, blank=True,
        on_delete=models.SET_NULL)
    categoria = models.ForeignKey(
        Categoria_Producto,
        null=True, blank=True,
        on_delete=models.SET_NULL)
    entrada = models.ForeignKey(
        Ubicaciones,
        on_delete=models.CASCADE,
        related_name='RET_Ubicaciones_E')
    salida = models.ForeignKey(
        Ubicaciones,
        on_delete=models.CASCADE,
        related_name='RET_Ubicaciones_S')
    compania = models.ForeignKey(Compania, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Regla de Estrategia de Traslado"
        verbose_name_plural = "Reglas de Estrategias de Traslados"

    def __str__(self):
        return self.producto.nombre


class ReglasAbastecimiento(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicaciones, on_delete=models.CASCADE)
    cantidad_minima = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_maxima = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_multi = models.DecimalField(max_digits=10, decimal_places=2)
    udm = models.ForeignKey(Unidades_Medida, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Regla de Abastecimiento"
        verbose_name_plural = "Reglas de Abastecimiento"

    def __str__(self):
        return self.producto.nombre


class EmpaquetadoProducto(models.Model):
    empaquetado = models.CharField(max_length=255)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_contenida = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_barras = models.CharField(max_length=255, null=True, blank=True)
    compania = models.ForeignKey(
        Compania,
        null=True, blank=True,
        on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Empaquetado de Producto"
        verbose_name_plural = "Empaquetados de Productos"

    def __str__(self):
        return self.empaquetado


class PaqueteEntrega(models.Model):
    tipo_paquete = models.CharField(max_length=255)
    transportista = models.CharField(
        max_length=255,
        choices=TRANSPORTISTA_LIST,
        default='1')
    altura = models.DecimalField(max_digits=10, decimal_places=2)
    ancho = models.DecimalField(max_digits=10, decimal_places=2)
    longitud = models.DecimalField(max_digits=10, decimal_places=2)
    peso_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_barras = models.CharField(max_length=255, null=True, blank=True)
    codigo_paquete = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "Paquete de Entrega"
        verbose_name_plural = "Paquetes de Entrega"

    def __str__(self):
        return self.tipo_paquete
