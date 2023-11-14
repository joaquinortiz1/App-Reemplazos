# Generated by Django 4.2.4 on 2023-11-14 00:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('GC', '0015_rename_habilidades_pos_usuario_habilidades_usuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postulacion',
            old_name='solicitud_reemplazo',
            new_name='solicitud',
        ),
        migrations.RemoveField(
            model_name='postulacion',
            name='puntaje',
        ),
        migrations.RemoveField(
            model_name='postulacion',
            name='usuario',
        ),
        migrations.AddField(
            model_name='postulacion',
            name='curriculum',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='GC.cv'),
        ),
        migrations.AddField(
            model_name='postulacion',
            name='fecha_postulacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]