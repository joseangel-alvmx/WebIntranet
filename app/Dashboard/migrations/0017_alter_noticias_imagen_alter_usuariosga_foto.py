# Generated by Django 5.1.2 on 2024-10-24 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0016_ubicaciones_latitud_ubicaciones_longitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='imagen',
            field=models.ImageField(upload_to='FotosNoticia/'),
        ),
        migrations.AlterField(
            model_name='usuariosga',
            name='foto',
            field=models.ImageField(upload_to='FotosPlantilla/'),
        ),
    ]