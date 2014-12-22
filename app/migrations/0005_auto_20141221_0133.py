# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20141220_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitte',
            name='relevancy',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twitte',
            name='sentiment',
            field=models.CharField(default='none', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twitte',
            name='stock',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
