# Generated by Django 3.2.3 on 2021-05-29 17:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('my_web', '0004_auto_20210515_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255, unique=True, verbose_name='Слово')),
                ('ano_mode', models.CharField(choices=[('yes', 'Да'), ('no', 'Нет')], default='yes', max_length=3, verbose_name='Анаграмма')),
            ],
            options={
                'verbose_name': 'Черное слово',
                'verbose_name_plural': 'Черные слова',
            },
        ),
        migrations.AlterField(
            model_name='aware_page',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 17, 14, 33, 423658, tzinfo=utc), verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='info',
            name='i_time_active',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 17, 14, 33, 262657, tzinfo=utc), verbose_name='Активно до'),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='st_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 29, 17, 14, 33, 424652, tzinfo=utc), verbose_name='Время обновления'),
        ),
    ]
