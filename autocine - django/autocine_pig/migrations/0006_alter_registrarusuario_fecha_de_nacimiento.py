# Generated by Django 4.2 on 2023-05-27 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autocine_pig', '0005_pelicula_complejo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrarusuario',
            name='fecha_de_nacimiento',
            field=models.DateField(default='1900-01-01', verbose_name='Fecha_de_Nacimiento'),
        ),
    ]
