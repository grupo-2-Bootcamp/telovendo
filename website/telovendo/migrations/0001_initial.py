# Generated by Django 4.2.1 on 2023-06-09 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioProveedoresDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(max_length=50)),
                ('razon_social', models.CharField(max_length=50)),
                ('rut', models.CharField(max_length=12)),
                ('giro', models.CharField(max_length=30)),
                ('contacto', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('comuna', models.CharField(max_length=20)),
                ('categoria', models.CharField(max_length=30)),
                ('productos', models.CharField(max_length=1000)),
            ],
        ),
    ]
