# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('task', models.CharField(max_length=250)),
                ('progress', models.IntegerField(default=0)),
                ('deadline', models.DateField(default=datetime.datetime.now)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['task'],
            },
        ),
    ]
