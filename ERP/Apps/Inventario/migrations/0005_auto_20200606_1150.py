# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-06 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0004_auto_20200606_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='rutas',
            field=models.ManyToManyField(blank=True, to='Inventario.Opciones_Rutas'),
        ),
    ]
