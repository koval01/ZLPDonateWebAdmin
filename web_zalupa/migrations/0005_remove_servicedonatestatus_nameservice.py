# Generated by Django 3.2.7 on 2021-12-09 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_zalupa', '0004_remove_servicedonatestatus_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicedonatestatus',
            name='nameService',
        ),
    ]
