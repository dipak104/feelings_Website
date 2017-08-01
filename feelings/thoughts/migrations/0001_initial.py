# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-06 20:42
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recorded_at', models.DateTimeField(default=datetime.datetime(2017, 7, 6, 20, 42, 35, 303867, tzinfo=utc), editable=False)),
                ('condition', models.IntegerField(choices=[(0, 'Joy'), (5, 'Passionate'), (10, 'Happy'), (15, 'Optimistic'), (20, 'Content'), (25, 'Bored'), (26, 'Tired'), (27, 'Hungry'), (30, 'Pessimistic'), (35, 'Frustated'), (40, 'Overwhelmed'), (45, 'Dissapointed'), (50, 'Worried'), (55, 'Angry'), (60, 'Jealous'), (65, 'Insecure'), (70, 'Guilty'), (75, 'Fear'), (80, 'Grief'), (85, 'Despair')])),
                ('notes', models.TextField(blank=True, default='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thoughts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
