# Generated by Django 4.1.3 on 2022-11-21 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0012_productos_tipo2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='precio_entrada',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True, verbose_name='Valor entrada'),
        ),
    ]
