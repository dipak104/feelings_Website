# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-10 18:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('thoughts', '0003_auto_20170709_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thought',
            name='recorded_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 10, 18, 6, 31, 887423, tzinfo=utc), editable=False),
        ),
    ]
