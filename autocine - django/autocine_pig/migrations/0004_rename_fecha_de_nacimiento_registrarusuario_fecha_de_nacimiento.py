# Generated by Django 4.2 on 2023-05-22 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autocine_pig', '0003_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrarusuario',
            old_name='fecha_De_Nacimiento',
            new_name='fecha_de_nacimiento',
        ),
    ]
