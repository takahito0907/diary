# Generated by Django 3.0.3 on 2020-03-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0006_auto_20200323_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='photo',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
