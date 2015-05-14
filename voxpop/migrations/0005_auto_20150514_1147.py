# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voxpop', '0004_review_tagline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='datetime',
            new_name='dt',
        ),
    ]
