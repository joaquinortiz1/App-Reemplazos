# Generated by Django 4.2.4 on 2023-11-04 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trabajos', '0003_remove_solicituddetrabajo_codigo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicituddetrabajo',
            name='codigo',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
