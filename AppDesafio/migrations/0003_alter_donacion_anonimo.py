# Generated by Django 4.0.4 on 2022-05-10 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDesafio', '0002_rename_nombre_donacion_anonimo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='anonimo',
            field=models.CharField(max_length=30),
        ),
    ]
