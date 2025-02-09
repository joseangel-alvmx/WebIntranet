# Generated by Django 5.1.2 on 2024-10-11 18:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('descrpcion', models.TextField(blank=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_termino', models.DateField(null=True)),
                ('importante', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=10)),
                ('codigo_sucursal', models.CharField(max_length=10, null=True)),
                ('telefono', models.CharField(max_length=10, null=True)),
                ('extension', models.CharField(max_length=10, null=True)),
                ('nombre_tiular', models.CharField(max_length=50, null=True)),
                ('ap_paterno', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('direccion', models.CharField(max_length=200)),
                ('tipo_cedis', models.CharField(max_length=10, null=True)),
                ('coordenadas', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VacanteAct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacante', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_termino', models.DateField(null=True)),
                ('estatus', models.BooleanField(default=False)),
                ('sueldo', models.CharField(max_length=100, null=True)),
                ('respon', models.TextField(blank=True)),
                ('departamento', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VacanteActivas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacante', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_termino', models.DateField(null=True)),
                ('estatus', models.BooleanField(default=False)),
                ('sueldo', models.CharField(max_length=100, null=True)),
                ('respon', models.TextField(blank=True)),
                ('departamento', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vacantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacante', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_termino', models.DateField(null=True)),
                ('estatus', models.BooleanField(default=False)),
                ('sueldo', models.CharField(max_length=100, null=True)),
                ('respon', models.TextField(blank=True)),
                ('departamento', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
