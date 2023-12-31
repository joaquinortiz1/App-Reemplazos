# Generated by Django 4.2.4 on 2023-11-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GC', '0006_alter_curriculum_correo_electronico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True)),
                ('area_trabajo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('experiencia_laboral', models.TextField()),
                ('anios_experiencia', models.PositiveIntegerField()),
                ('educacion', models.TextField()),
                ('habilidades', models.TextField()),
                ('idiomas', models.TextField()),
            ],
        ),
    ]
