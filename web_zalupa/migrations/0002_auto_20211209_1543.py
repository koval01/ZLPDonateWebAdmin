# Generated by Django 3.2.7 on 2021-12-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_zalupa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedonate',
            name='command',
            field=models.TextField(default='/say Hello &player&!', verbose_name='Команда'),
        ),
        migrations.AlterField(
            model_name='servicedonatestatus',
            name='namePlayer',
            field=models.CharField(default='lomaka', max_length=255, verbose_name='Игрок'),
        ),
    ]
