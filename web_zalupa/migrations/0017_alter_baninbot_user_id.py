# Generated by Django 3.2.7 on 2021-12-13 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_zalupa', '0016_alter_baninbot_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baninbot',
            name='user_id',
            field=models.IntegerField(default=None, max_length=255, unique=True, verbose_name='ID пользователя'),
        ),
    ]