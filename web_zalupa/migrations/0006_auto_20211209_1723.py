# Generated by Django 3.2.7 on 2021-12-09 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_zalupa', '0005_remove_servicedonatestatus_nameservice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicedonatestatus',
            old_name='namePlayer',
            new_name='name_player',
        ),
        migrations.RenameField(
            model_name='servicedonatestatus',
            old_name='serviceId',
            new_name='service_id',
        ),
        migrations.RenameField(
            model_name='servicedonatestatus',
            old_name='statusPay',
            new_name='status_pay',
        ),
    ]
