# Generated by Django 2.2.16 on 2020-10-15 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Contacto', '0006_compania_tipo_contacto_choice'),
        ('Inventario', '0015_auto_20201015_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReglasEstrategiaTraslado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventario.Categoria_Producto')),
                ('compania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contacto.Compania')),
                ('entrada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RET_Ubicaciones_E', to='Inventario.Ubicaciones')),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Inventario.Producto')),
                ('salida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RET_Ubicaciones_S', to='Inventario.Ubicaciones')),
            ],
            options={
                'verbose_name': 'Regla de Estrategia de Traslado',
                'verbose_name_plural': 'Reglas de Estrategias de Traslados',
            },
        ),
    ]
