# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voxpop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='salary',
            field=models.IntegerField(null=True),
        ),
    ]
