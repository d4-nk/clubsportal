# Generated by Django 2.1.2 on 2018-12-12 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0015_auto_20181212_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onpollclub',
            name='release_date',
            field=models.TimeField(default=datetime.datetime(2018, 12, 12, 12, 49, 14, 746016)),
        ),
    ]
