# Generated by Django 5.0.2 on 2024-02-09 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=144)),
                ('apellido', models.CharField(max_length=144)),
                ('cedula', models.CharField(max_length=144)),
                ('telefono', models.CharField(max_length=144)),
                ('correo', models.EmailField(max_length=144)),
                ('observaciones', models.CharField(max_length=144)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=144)),
                ('email', models.EmailField(max_length=144)),
                ('tipo', models.CharField(choices=[('User', 'User'), ('Admin', 'Admin')], max_length=15)),
                ('password', models.CharField(max_length=144)),
                ('telefono', models.CharField(max_length=144)),
            ],
        ),
        migrations.CreateModel(
            name='P_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=144)),
                ('apellido', models.CharField(max_length=144)),
                ('telefono', models.CharField(max_length=144)),
                ('correo', models.EmailField(max_length=144)),
                ('observaciones', models.CharField(max_length=144)),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad_disponible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=144)),
                ('fecha_ingreso', models.DateField()),
                ('fecha_caducidad', models.DateField()),
                ('tipo', models.CharField(choices=[('Casa', 'Casa'), ('Terreno', 'Terreno')], max_length=15)),
                ('ubicacion', models.CharField(max_length=144)),
                ('descripcion', models.TextField(max_length=500)),
                ('tipo_comision', models.DecimalField(decimal_places=2, max_digits=65)),
                ('precio_comercial', models.DecimalField(decimal_places=2, max_digits=65)),
                ('precio_crea', models.DecimalField(decimal_places=2, max_digits=65)),
                ('precio_minimo', models.DecimalField(decimal_places=2, max_digits=65)),
                ('convenio', models.CharField(choices=[('En Convenio', 'En Convenio'), ('Sin Convenio', 'Sin Convenio')], max_length=20)),
                ('proceso', models.CharField(choices=[('Proceso de Venta', 'Proceso de Venta'), ('Vendida', 'Vendida')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad_posible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=144)),
                ('fecha_registro', models.DateField()),
                ('ubicacion', models.CharField(max_length=144)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=65)),
                ('tipo', models.CharField(choices=[('Casa', 'Casa'), ('Terreno', 'Terreno')], max_length=15)),
                ('descripcion', models.TextField(max_length=500)),
                ('precio_avaluo', models.DecimalField(decimal_places=2, max_digits=65)),
            ],
        ),
    ]
