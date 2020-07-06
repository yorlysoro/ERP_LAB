# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-06-04 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('almacen', models.CharField(max_length=255)),
                ('nombre_corto', models.CharField(max_length=10)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria_Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=255)),
                ('logistica', models.CharField(blank=True, choices=[('nulo', ''), ('FIFO', 'First In First Out (FIFO)'), ('LIFO', 'Last In First Out (LIFO)')], default='nulo', max_length=255, null=True)),
                ('categoria_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventario.Categoria_Producto')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=255)),
                ('vender', models.BooleanField(default=True)),
                ('comprar', models.BooleanField(default=True)),
                ('tipo_producto', models.CharField(choices=[('Co', 'Consumible'), ('Se', 'Servicio'), ('Al', 'Almacenable')], default='Al', max_length=255)),
                ('referencia_interna', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo_barras', models.CharField(blank=True, max_length=255, null=True)),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coste', models.DecimalField(decimal_places=2, max_digits=10)),
                ('notas_internas', models.TextField(blank=True, null=True)),
                ('rutas', models.CharField(choices=[('MTO', 'Obtener Bajo Pedido (MTO)')], default='MTO', max_length=255)),
                ('plazo_entrega_cliente', models.PositiveIntegerField(default=0)),
                ('peso', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('volumen', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('responsable', models.CharField(blank=True, max_length=255, null=True)),
                ('descripcion_pedido_entrega', models.TextField(blank=True, null=True)),
                ('descripcion_recepciones', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Secuencia_Referencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('implementacion', models.CharField(choices=[('Sd', 'Estandar'), ('Sh', 'Sin Hueco')], default='Sd', max_length=255)),
                ('codigo_secuencia', models.CharField(blank=True, max_length=10, null=True)),
                ('prefijo', models.CharField(blank=True, max_length=255, null=True)),
                ('sufijo', models.CharField(blank=True, max_length=255, null=True)),
                ('ultilizar_subsec_date_range', models.BooleanField(default=False)),
                ('tamano_secuencia', models.PositiveIntegerField(default=0)),
                ('paso', models.PositiveIntegerField(default=1)),
                ('proximo_numero', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Operacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_operacion', models.CharField(max_length=255)),
                ('tipo_de_operacion_choice', models.CharField(choices=[('nulo', ''), ('En', 'Envio'), ('Re', 'Recibo'), ('Ti', 'Transferencia Interna')], default='nulo', max_length=255)),
                ('mostrar_op_detalladas', models.BooleanField(default=False)),
                ('codigo', models.CharField(max_length=10)),
                ('precompletar_op_detalladas_recibo', models.BooleanField(default=True)),
                ('secuencia_referencia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventario.Secuencia_Referencia')),
                ('to_devoluciones_recibo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventario.Tipo_Operacion')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ubicacion', models.CharField(max_length=255)),
                ('tipo_ubicacion', models.CharField(choices=[('Up', 'Ubicacion de Proveedor'), ('V', 'Vista'), ('Ui', 'Ubicacion Interna'), ('Uc', 'Ubicacion del Cliente'), ('Pi', 'Perdida de Inventario'), ('Pr', 'Produccion'), ('Ut', 'Ubicacion de Transito')], default='Up', max_length=255)),
                ('ubicacion_chatarra', models.BooleanField(default=False)),
                ('ubicacion_devolucion', models.BooleanField(default=False)),
                ('nota', models.TextField(blank=True, null=True)),
                ('ubicacion_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventario.Ubicaciones')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='ubicacion_inventario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ubicacion_inventario', to='Inventario.Ubicaciones'),
        ),
        migrations.AddField(
            model_name='producto',
            name='ubicacion_produccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ubicacion_produccion', to='Inventario.Ubicaciones'),
        ),
    ]
