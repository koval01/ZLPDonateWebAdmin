# Generated by Django 3.2.7 on 2021-12-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_zalupa', '0010_alter_servicedonatestatus_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedonatestatus',
            name='success_code_pay',
            field=models.CharField(default=0, max_length=64, verbose_name='Код успеха'),
        ),
    ]
