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
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
TIPO_CONTACTO_CHOICE = (
    ('Ind', 'Individual'),
    ('Comp', 'Compañia'),)

TIPO_DIRECCION_CHOICE = (
    ('con', 'Contacto'),
    ('fact', 'Direccion de Factura'),
    ('ent', 'Direccion de Entrega'),
    ('otr', 'Otra Direccion'),
    ('priv', 'Direccion Privada'),)


class Sector(models.Model):
    nombre = models.CharField(max_length=40)
    nombre_completo = models.CharField(max_length=255, null=True, blank=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectores"

    def __str__(self):
        return self.nombre


class Compania(models.Model):
    tipo_contacto_choice = models.CharField(
        max_length=255, choices=TIPO_CONTACTO_CHOICE, default='Ind')
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    rif = models.CharField(max_length=30, null=True, blank=True)
    telefono = models.CharField(max_length=8, null=True, blank=True)
    movil = models.CharField(max_length=8, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    pagina = models.URLField(null=True, blank=True)
    foto = models.ImageField(
        upload_to='fotos/contacto/', null=True, blank=True)
    sector = models.ForeignKey(
        Sector, null=True, blank=True, on_delete=models.SET_NULL)
    nota_interna = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Compañia"
        verbose_name_plural = "Compañias"

    def __str__(self):
        return self.nombre


class Titulo(models.Model):
    titulo = models.CharField(max_length=255)
    abreviatura = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = "Titulo"
        verbose_name_plural = "Titulos"

    def __str__(self):
        return self.titulo


class Individual(Compania):
    cedula = models.CharField(max_length=8, null=True, blank=True)
    tipo_direccion = models.CharField(
        max_length=255, null=True, blank=True, choices=TIPO_DIRECCION_CHOICE)
    puesto_trabajo = models.CharField(max_length=30, null=True, blank=True)
    titulo = models.ForeignKey(
        Titulo, blank=True, null=True, on_delete=models.SET_NULL)
    compania = models.ForeignKey(
        Compania, blank=True, null=True,
        on_delete=models.SET_NULL, related_name='relacion_compania')

    class Meta:
        verbose_name = "Individual"
        verbose_name_plural = "Individual"

    def __str__(self):
        if self.compania:
            return self.compania.nombre + ' ' + self.nombre
        else:
            return self.nombre


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Compania.objects.create(usuario=instance)
