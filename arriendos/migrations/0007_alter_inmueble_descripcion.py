# Generated by Django 4.2 on 2024-05-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arriendos', '0006_region_comuna_alter_inmueble_comuna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='descripcion',
            field=models.CharField(max_length=300),
        ),
    ]
