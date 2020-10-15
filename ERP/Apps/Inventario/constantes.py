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
LOGISTICA_CHOICES = ( 
('FIFO' , 'First In First Out (FIFO)'), 
('LIFO' , 'Last In First Out (LIFO)'),
)
ESTADO_RECEPCION = (
	('Bor', 'Borrador'),
	('Esp', 'En Espera'),
	('Rea', 'Realizado'),
	)
TIPO_UBICACION_CHOICES = ( 
		('Up' , 'Ubicacion de Proveedor'), 
		('V' , 'Vista'), 
		('Ui' , 'Ubicacion Interna'), 
		('Uc' , 'Ubicacion del Cliente'), 
		('Pi' , 'Perdida de Inventario'), 
		('Pr' , 'Produccion'), 
		('Ut' , 'Ubicacion de Transito'),
		)

IMPLEMENTACIONES = (
	('Sd' ,'Estandar'), 
	('Sh', 'Sin Hueco'),
)

TIPO_OPERACION_CHOICES = ( 
		('En' , 'Envio'), 
		('Re' , 'Recibo'), 
		('Ti' , 'Transferencia Interna'),
		)

TIPO_PRODUCTO_CHOICES = (
		('Co' , 'Consumible'), 
		('Se' , 'Servicio'), 
		('Al' , 'Almacenable'),
		)

TIPO_UNIDAD_MEDIDA = (
	('1', 'Mas grande que la unidad de medida de referencia'),
	('2', 'Unidad de medida de referencia para esta categoria'),
	('3', 'Mas pequeña que la unidad de medida de referencia'),
	)

ALBARANES_ENTRADA = (
	('1', 'Recibir bienes directamente (1 paso)'),
	('2', 'Recibir bienes en la ubicación de entrada y luego llevar a existencias (2 pasos)'),
	('3', 'Recibir bienes en la ubicación de entrada, transferir a ubicación de control de calidad, y luego llevar a existencias (3 pasos)'),
	)

ENVIOS_SALIENTES = (
	('1', 'Entregar bienes directamente (1 paso)' ),
	('2', 'Enviar bienes a ubicación de salida y entregar (2 pasos)'),
	('3', 'Empaquetar, transferir bienes a ubicación de salida, y enviar (3 pasos)'),
	)

ACCIONES_REGLAS = (
	('1', 'Obtener desde'),
	('2', 'Empujar A'),
	('3', 'Jalar & Empujar'),
	('4', 'Comprar'),
	)

MA_CHOICES = (
	('1', 'Operacion Manual'),
	('2', 'Automatico paso no añadido'),
	)

MS_CHOICES = (
	('1', 'Obtene del Stock'),
	('2', 'Activa otra regla'),
	('3', 'Tomar de almacen, si no esta disponible, active otra regla'),
	)

TRANSPORTISTA_LIST = (
	('1', 'Sin transportista'),
	)
