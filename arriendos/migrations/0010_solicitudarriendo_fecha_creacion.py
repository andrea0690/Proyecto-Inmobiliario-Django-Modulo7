# Generated by Django 4.2 on 2024-05-09 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('arriendos', '0009_tipoinmueble_alter_inmueble_tipo_de_inmueble'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudarriendo',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
