# Generated by Django 5.1.2 on 2024-10-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0017_alter_noticias_imagen_alter_usuariosga_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventariosoporte',
            name='responsiva',
            field=models.FileField(upload_to='Media/filesPDF/Responsivas_Soporte/'),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='imagen',
            field=models.ImageField(upload_to='Media/FotosNoticia/'),
        ),
        migrations.AlterField(
            model_name='usuariosga',
            name='foto',
            field=models.ImageField(upload_to='Media/FotosPlantilla/'),
        ),
    ]