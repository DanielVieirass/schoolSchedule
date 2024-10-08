# Generated by Django 5.0.2 on 2024-10-01 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_materias_course_professor_coordenador_and_more'),
        ('materias', '0001_initial'),
        ('professors', '0003_remove_professor_cursos_professor_materias'),
        ('turmas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='materias',
            field=models.ManyToManyField(blank=True, to='materias.materia'),
        ),
        migrations.AlterField(
            model_name='course',
            name='professor_coordenador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='professors.professor'),
        ),
        migrations.AlterField(
            model_name='course',
            name='turmas',
            field=models.ManyToManyField(blank=True, to='turmas.turma'),
        ),
    ]
