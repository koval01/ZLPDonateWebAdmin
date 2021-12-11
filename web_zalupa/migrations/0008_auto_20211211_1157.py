# Generated by Django 3.2.7 on 2021-12-11 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_zalupa', '0007_systemsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicedonate',
            name='name',
            field=models.CharField(default='Строитель', max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='servicedonate',
            name='type',
            field=models.CharField(choices=[('prefix', 'Префикс'), ('rank', 'Привилегия'), ('other', 'Другое')], default='prefix', max_length=16, verbose_name='Тип'),
        ),
    ]
