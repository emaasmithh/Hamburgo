# Generated by Django 5.0.4 on 2024-07-19 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_entrada2_otroproducto2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.bebida')),
            ],
        ),
    ]
