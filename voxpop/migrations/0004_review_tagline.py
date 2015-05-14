# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voxpop', '0003_review_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='tagline',
            field=models.CharField(default='hello world', max_length=128),
            preserve_default=False,
        ),
    ]
