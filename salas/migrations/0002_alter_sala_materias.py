# Generated by Django 5.1.1 on 2024-10-02 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materias', '0002_alter_materia_horario'),
        ('salas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='materias',
            field=models.ManyToManyField(blank=True, to='materias.materia'),
        ),
    ]
