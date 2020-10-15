# Generated by Django 2.2.16 on 2020-10-15 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Contacto', '0006_compania_tipo_contacto_choice'),
        ('Inventario', '0016_reglasestrategiatraslado'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaqueteEntrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_paquete', models.CharField(max_length=255)),
                ('transportista', models.CharField(choices=[('1', 'Sin transportista')], default='1', max_length=255)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ancho', models.DecimalField(decimal_places=2, max_digits=10)),
                ('longitud', models.DecimalField(decimal_places=2, max_digits=10)),
                ('peso_maximo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('codigo_barras', models.CharField(blank=True, max_length=255, null=True)),
                ('codigo_paquete', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Paquete de Entrega',
                'verbose_name_plural': 'Paquetes de Entrega',
            },
        ),
        migrations.CreateModel(
            name='ReglasAbastecimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_minima', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad_maxima', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidad_multi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Producto')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Ubicaciones')),
                ('udm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Unidades_Medida')),
            ],
            options={
                'verbose_name': 'Regla de Abastecimiento',
                'verbose_name_plural': 'Reglas de Abastecimiento',
            },
        ),
        migrations.CreateModel(
            name='EmpaquetadoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empaquetado', models.CharField(max_length=255)),
                ('cantidad_contenida', models.DecimalField(decimal_places=2, max_digits=10)),
                ('codigo_barras', models.CharField(blank=True, max_length=255, null=True)),
                ('compania', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Contacto.Compania')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Producto')),
            ],
            options={
                'verbose_name': 'Empaquetado de Producto',
                'verbose_name_plural': 'Empaquetados de Productos',
            },
        ),
    ]
