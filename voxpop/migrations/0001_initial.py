# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=128)),
                ('salary', models.IntegerField()),
                ('pros', models.CharField(max_length=300)),
                ('cons', models.CharField(max_length=300)),
                ('estagio', models.CharField(max_length=300)),
                ('firm', models.ForeignKey(to='voxpop.Firm')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
