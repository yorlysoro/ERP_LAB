# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-08 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0007_recepcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recepcion',
            options={'verbose_name': 'Recepcion', 'verbose_name_plural': 'Recepciones'},
        ),
        migrations.AlterField(
            model_name='recepcion',
            name='fecha_programada',
            field=models.DateTimeField(),
        ),
    ]
