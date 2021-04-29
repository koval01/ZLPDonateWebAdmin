# Generated by Django 3.2 on 2021-04-29 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_web', '0024_auto_20210422_2052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info',
            options={'verbose_name': 'Рекламная запись', 'verbose_name_plural': 'Рекламные записи'},
        ),
        migrations.AlterField(
            model_name='aware_page',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 19, 41, 11, 964721), verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='info',
            name='i_text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='info',
            name='i_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 19, 41, 11, 693444), verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='st_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 29, 19, 41, 11, 965721), verbose_name='Время обновления'),
        ),
    ]
