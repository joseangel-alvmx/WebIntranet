# Generated by Django 5.1.2 on 2024-10-17 17:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0005_alter_solicitudempleo_curriculum'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Puestos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto', models.CharField(max_length=100, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='UsuariosGA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=80)),
                ('ap_paterno', models.CharField(max_length=80)),
                ('sucursal', models.CharField(max_length=80)),
                ('ap_materno', models.CharField(max_length=80)),
                ('correo', models.CharField(max_length=100)),
                ('extension', models.CharField(max_length=5)),
                ('fecha_nacimiento', models.DateTimeField(auto_now_add=True)),
                ('fecha_ingreso', models.DateField(null=True)),
                ('rfc', models.CharField(max_length=13)),
                ('foto', models.ImageField(upload_to='FotosPlantilla')),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.departamentos')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.empresas')),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.puestos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
