# Generated by Django 5.1.2 on 2024-10-23 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0014_tipodocumento_usuariosga_numero_empleado_procesos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='archivo',
            field=models.FileField(upload_to='filesPDF/Cursos/'),
        ),
    ]
