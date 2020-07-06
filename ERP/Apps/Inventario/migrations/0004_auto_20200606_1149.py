# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-06 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0003_auto_20200606_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opciones_Rutas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mto_obtener_bajo_pedido', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='rutas',
        ),
        migrations.AddField(
            model_name='producto',
            name='rutas',
            field=models.ManyToManyField(blank=True, null=True, to='Inventario.Opciones_Rutas'),
        ),
    ]
