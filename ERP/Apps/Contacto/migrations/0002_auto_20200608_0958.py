# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-08 13:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compania',
            options={'verbose_name': 'Compañia', 'verbose_name_plural': 'Compañias'},
        ),
        migrations.AlterModelOptions(
            name='individual',
            options={'verbose_name': 'Individual', 'verbose_name_plural': 'Individual'},
        ),
        migrations.AlterModelOptions(
            name='titulo',
            options={'verbose_name': 'Titulo', 'verbose_name_plural': 'Titulos'},
        ),
        migrations.RemoveField(
            model_name='compania',
            name='tipo_contacto_choice',
        ),
    ]
