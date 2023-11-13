# Generated by Django 4.2.4 on 2023-11-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GC', '0012_educacion_experiencia_idioma_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicituddereemplazo',
            name='educacion_requerida',
            field=models.CharField(choices=[('basica', 'basica'), ('Media', 'Media'), ('Superior', 'Superior')], default='basica', max_length=50),
        ),
        migrations.RemoveField(
            model_name='solicituddereemplazo',
            name='experiencia_requerida',
        ),
        migrations.RemoveField(
            model_name='solicituddereemplazo',
            name='habilidades_requeridas',
        ),
        migrations.AlterField(
            model_name='solicituddereemplazo',
            name='tipo_de_contrato',
            field=models.CharField(choices=[('Indefinido', 'Indefinido'), ('Temporal', 'Temporal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='solicituddereemplazo',
            name='tipo_de_trabajo',
            field=models.CharField(choices=[('Tiempo completo', 'Tiempo completo'), ('Medio tiempo', 'Medio tiempo'), ('Freelance', 'Freelance'), ('Reemplazo', 'Reemplazo')], max_length=50),
        ),
        migrations.AddField(
            model_name='solicituddereemplazo',
            name='experiencia_requerida',
            field=models.CharField(choices=[('asistente_ejecutivo', 'asistente_ejecutivo'), ('coordinador_proyecto', 'coordinador_proyecto'), ('gerente_de_seguridad', 'gerente_de_seguridad'), ('desarrollador_backend', 'desarrollador_backend'), ('desarrollador_frontend', 'desarrollador_frontend'), ('desarrollador_full_stack', 'desarrollador_full_stack'), ('especialista_en_recursos_humanos', 'especialista_en_recursos_humanos'), ('especialista_en_ventas', 'especialista_en_ventas'), ('especialista_en_soporte Técnico', 'especialista_en_soporte Técnico'), ('especialista_en_logística', 'especialista_en_logística'), ('analista_financiero', 'analista_financiero')], default='asistente_ejecutivo', max_length=50),
        ),
        migrations.AddField(
            model_name='solicituddereemplazo',
            name='habilidades_requeridas',
            field=models.CharField(choices=[('programacion', 'programacion'), ('liderazgo', 'liderazgo')], default='programacion', max_length=50),
        ),
    ]