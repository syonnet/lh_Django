# Generated by Django 5.0.2 on 2024-02-12 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0003_curso_delete_alumno'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='cursos/'),
        ),
    ]