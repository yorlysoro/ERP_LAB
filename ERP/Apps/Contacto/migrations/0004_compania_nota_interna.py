# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-08 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contacto', '0003_auto_20200608_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='compania',
            name='nota_interna',
            field=models.TextField(blank=True, null=True),
        ),
    ]
