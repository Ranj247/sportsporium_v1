# Generated by Django 3.2.9 on 2021-12-08 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211203_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='has_sizes',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
