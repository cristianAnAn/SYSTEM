# Generated by Django 5.0.6 on 2024-08-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0008_alter_asignar_actividad_calificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignar_actividad',
            name='calificacion',
            field=models.BooleanField(null=True),
        ),
    ]
