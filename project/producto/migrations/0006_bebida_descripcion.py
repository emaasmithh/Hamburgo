# Generated by Django 5.0.4 on 2024-07-19 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_bebida2'),
    ]

    operations = [
        migrations.AddField(
            model_name='bebida',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
