# Generated by Django 4.2.4 on 2023-11-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GC', '0013_alter_solicituddereemplazo_educacion_requerida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='habilidades_pos',
            field=models.CharField(choices=[('programacion', 'programacion'), ('liderazgo', 'liderazgo')], default='programacion', max_length=50),
        ),
    ]