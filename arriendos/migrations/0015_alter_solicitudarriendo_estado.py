# Generated by Django 4.2 on 2024-05-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arriendos', '0014_remove_solicitudarriendo_aceptada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudarriendo',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('aceptada', 'Aceptada'), ('rechazada', 'Rechazada')], default='pendiente', max_length=20),
        ),
    ]