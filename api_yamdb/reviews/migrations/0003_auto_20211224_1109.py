# Generated by Django 2.2.16 on 2021-12-24 08:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20211224_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 24, 8, 9, 10, 979422, tzinfo=utc), verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 24, 8, 9, 10, 979422, tzinfo=utc), verbose_name='Дата публикации'),
        ),
    ]
