# Generated by Django 5.1.2 on 2024-11-06 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0025_vacantes_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacanteactivas',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Dashboard.empresas'),
        ),
    ]
