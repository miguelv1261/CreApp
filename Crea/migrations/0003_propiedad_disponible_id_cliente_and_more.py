# Generated by Django 5.0.2 on 2024-02-09 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crea', '0002_propiedad_posible_id_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad_disponible',
            name='id_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pk', to='Crea.cliente'),
        ),
        migrations.AlterField(
            model_name='propiedad_disponible',
            name='tipo_comision',
            field=models.CharField(choices=[('Fijo', 'Fijo'), ('Porcentaje', 'Porcentaje')], max_length=15),
        ),
    ]
