# Generated by Django 3.2.9 on 2021-12-07 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='original_bag',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
