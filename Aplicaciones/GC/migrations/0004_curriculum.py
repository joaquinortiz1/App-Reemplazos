# Generated by Django 4.2.4 on 2023-11-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GC', '0003_usuario_contrasena_usuario_rut'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('area_trabajo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('experiencia_laboral', models.TextField()),
                ('anios_experiencia', models.PositiveIntegerField()),
                ('educacion', models.TextField()),
                ('habilidades', models.TextField()),
                ('idiomas', models.TextField()),
                ('curriculum_adjunto', models.FileField(upload_to='curriculums/')),
            ],
        ),
    ]
