# Generated by Django 4.0.4 on 2022-05-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppDesafio', '0005_alter_donacion_anonimo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donacion',
            name='anonimo',
        ),
        migrations.AddField(
            model_name='donacion',
            name='nota_donacion',
            field=models.CharField(default='', max_length=30),
        ),
    ]
