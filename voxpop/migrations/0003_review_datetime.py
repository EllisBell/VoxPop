# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('voxpop', '0002_auto_20150413_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='datetime',
            field=models.DateTimeField(default=datetime.date(2015, 5, 14), auto_now_add=True),
            preserve_default=False,
        ),
    ]
