# Generated by Django 3.2.7 on 2021-12-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_zalupa', '0009_servicedonatestatus_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedonatestatus',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='Время'),
        ),
    ]
