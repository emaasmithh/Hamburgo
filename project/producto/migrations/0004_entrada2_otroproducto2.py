# Generated by Django 5.0.4 on 2024-07-19 18:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_bebida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.entrada')),
            ],
        ),
        migrations.CreateModel(
            name='OtroProducto2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.otroproducto')),
            ],
        ),
    ]
