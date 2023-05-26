# Generated by Django 4.2 on 2023-05-25 22:38

from django.db import migrations, models
import django.db.models.deletion


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
        migrations.CreateModel(
            name='Valor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=128, verbose_name='Valor')),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autocine_pig.pelicula')),
            ],
        ),
    ]
